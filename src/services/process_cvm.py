from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_service import BaseService
import config
import logging
import time

class ProcessCVM(BaseService):
  def processar(self, name):
    logging.info(f"Processando CVM para {name}")
    try:
      self.driver.get(config.URL_CVM_PROCESSO)

      iframe = self.wait.until(EC.presence_of_element_located((By.NAME, "Main")))
      self.driver.switch_to.frame(iframe)


      input_element = self.wait.until(EC.presence_of_element_located((By.ID, "iReqInt")))
      input_element.send_keys(name)

      self.driver.execute_script("window.scrollBy(0, 200);")

      link = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[value='Procurar']")))
      time.sleep(1)
      link.click()

      self.wait.until(lambda d: d.execute_script('return document.readyState') == 'complete')

      return self.capture_screenshot()

    except Exception as e:
      logging.info(f"Processando CVM para {name}")
      self.driver.quit()
      return None