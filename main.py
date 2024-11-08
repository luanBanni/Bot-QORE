import config_logging
from src.infra.web_driver import WebDriverManager
from src.data.transform import transformPDF
from src.services.process_anbima import ProcessAnbima
from src.services.process_bcb import ProcessBCB
from src.services.process_bsm import ProcessBSM
from src.services.process_cvm import ProcessCVM
from src.services.process_cvm_pas import ProcessCVMPAS
from src.services.process_cvm_irregular import ProcessCVMIrregular
from src.services.process_jus_brasil import ProcessJusBrasil
import config 
import logging
import pandas as pd
import time
from selenium.webdriver.support.ui import WebDriverWait
import os

def run_bots(name):
  logging.info(f"Começando o processo para {name}")

  driver_manager = WebDriverManager()
  driver = driver_manager.start_driver()
  wait = WebDriverWait(driver, config.TIMEOUT)

  try:
    services = [
      ProcessBCB(driver, wait),
      ProcessCVM(driver, wait),
      ProcessCVMIrregular(driver, wait),
      ProcessCVMPAS(driver, wait),
      ProcessBSM(driver, wait),
      ProcessAnbima(driver, wait),
      ProcessJusBrasil(driver_manager, wait),
    ]

    screenshots = []

    for service in services:
      screenshot = service.processar(name)
      if screenshot:
        if isinstance(screenshot, tuple):
          screenshots.extend(screenshot)
        else: 
          screenshots.append(screenshot)

    pdf_path = f"{config.PDF_OUTPUT_DIR}/dossie_{name.replace(' ', '_')}.pdf"
    transformPDF(screenshots, pdf_path)
    logging.info(f"PDF criado: {pdf_path}")

  except Exception as e:
    logging.error(f"Erro durante a execução para {name}: {e}")
  
  finally:
    driver_manager.quit_driver()

def run_bot_from_csv(csv_file):
  df = pd.read_csv(csv_file, delimiter=";", quotechar='"', skipinitialspace=True, on_bad_lines='warn', low_memory=False)

  tempo = time.time()
  for index, row in df.iterrows():
    name = row["NOME_COMPLETO"]
    logging.info(f"Rodando com o usuário: {index + 1} {name}")
    run_bots(name)
  tempofinal = time.time()

  logging.info(f"tempo: {tempofinal - tempo}")

def monitor_folder(folder_path):
  try:
    while True:
      csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
      if csv_files:
        for csv_file in csv_files:
          csv_file_path = os.path.join(folder_path, csv_file)
          logging.info(f"Arquivo encontrado, processando...")
          run_bot_from_csv(csv_file_path)
          os.remove(csv_file_path)
          logging.info(f"Arquivo {csv_file} processado e deletado com sucesso.")
                  
      else:
        logging.info("Nenhum arquivo CSV encontrado. Verificando novamente em 40 segundos")
      time.sleep(40)
      monitor_folder(config.CSV_FOLDER_PATH)
  except Exception as e:  
    print(e)
    time.sleep(10)

if __name__ == "__main__":
    config_logging.config_logging()
    monitor_folder(config.CSV_FOLDER_PATH)