from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_service import BaseService
import logging
import config
import time

class ProcessBCB(BaseService):
  def processar(self, name):
    logging.info(f"Processando BCB para {name}")
    try:
      self.driver.get(config.URL_BCB)
      input_element = self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "campoPesquisa")))
      input_element.send_keys(name)

      link = self.wait.until(EC.element_to_be_clickable((By.ID, "aBusca")))
      link.click()

      self.wait.until(lambda d: d.execute_script('return document.readyState') == 'complete')
      self.driver.execute_script('window.scrollBy(0, 100);')
      time.sleep(2)

      return self.capture_screenshot()

    except Exception as e:
      logging.error(f"Erro ao processar BCB para {name}: {e}")
      self.driver.quit()
      return None