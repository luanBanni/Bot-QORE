from .base_service import BaseService
import config
import logging
import time
from selenium.webdriver.support.ui import WebDriverWait

class ProcessJusBrasil(BaseService):
  def processar(self, name):
    logging.info(f"Processando JusBrasil para o {name}")
    driver = self.driver.start_driver()
    wait = WebDriverWait(driver, config.TIMEOUT)

    try:
      driver.get(f"{config.URL_JUS_BRASIL}?q={name.replace(' ', '+')}")

      wait.until(lambda d: d.execute_script('return document.readyState') == 'complete')
      time.sleep(1)

      return self.capture_screenshot()

    except Exception as e:
      logging.error(f"Error ao processar JusBrasil para {name}: {e}")
      return None