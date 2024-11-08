from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_service import BaseService
import config
import logging
import time

class ProcessBSM(BaseService):
  def processar(self, name): 
    logging.info(f"Processando BSM para {name}")
    try:
      self.driver.get(config.URL_BSM)
      input_element = self.wait.until(EC.presence_of_element_located((By.NAME, "acusado")))
      input_element.send_keys(name)
      self.driver.execute_script("window.scrollBy(0, 500);")
      time.sleep(1)

      link = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[value='Pesquisar']")))
      link.click()

      self.wait.until(lambda d: d.execute_script('return document.readyState') == 'complete')
      time.sleep(2)

      return self.capture_screenshot()
      
    except Exception as e:
      logging.error(f"Error ao processar BSM para {name}: {e}")
      self.driver.quit()