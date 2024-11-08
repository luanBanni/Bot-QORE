from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_service import BaseService
import config
import logging
import time

class ProcessCVMPAS(BaseService):
  def processar(self, name):
    logging.info(f"Processando CVM PAS para {name}")
    try:
      self.driver.get(config.URL_CVM_PAS)
      iframe = self.wait.until(EC.presence_of_element_located((By.NAME, "Main")))
      self.driver.switch_to.frame(iframe)

      input_element = self.wait.until(EC.presence_of_element_located((By.NAME, "txtIndiciado")))
      input_element.send_keys(name)
        
      link = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[value='Procurar']")))
      time.sleep(1)
      link.click()
      
      time.sleep(1)

      return self.capture_screenshot()

    except Exception as e:
      logging.error(f"Error ao processar CVM PAS para {name}: {e}")
      