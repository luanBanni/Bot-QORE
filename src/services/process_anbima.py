from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .base_service import BaseService
import config
import logging
import time

class ProcessAnbima(BaseService):
  def processar(self, name):
    logging.info(f"Processando Anbima para {name}")
    try:
      self.driver.get(config.URL_ANBIMA)
      input_element = self.wait.until(EC.visibility_of_element_located((By.ID, "filtroTermo")))
      input_element.send_keys(name)

      self.driver.execute_script("window.scrollBy(0, 400);")
      time.sleep(1)

      link = self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "btn-default")))
      link.click()

      self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul.biblioteca-docs.original")))
      time.sleep(3)

      screenshot_path6 = self.capture_screenshot()     

      cartaClick = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Carta de Recomendação")))
      time.sleep(2)
      cartaClick.click()

      div_element = self.wait.until(EC.presence_of_element_located((By.ID, "tab2")))
      input_element = div_element.find_element(By.CLASS_NAME, "form-control")
      link = div_element.find_element(By.CLASS_NAME, "btn-default")

      input_element.send_keys(name)
      time.sleep(2)     
      link.click()

      self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "ul.biblioteca-docs.original")))
      time.sleep(3)

      screenshot_path7 = self.capture_screenshot()  

      julgamentosClick = self.wait.until(EC.element_to_be_clickable((By.LINK_TEXT, "Julgamentos")))
      time.sleep(2)
      julgamentosClick.click()
      
      time.sleep(1)
      div_element = self.wait.until(EC.presence_of_element_located((By.ID, "tab3")))
      input_element = div_element.find_element(By.CLASS_NAME, "form-control")
      link = div_element.find_element(By.CLASS_NAME, "btn-default")

      input_element.send_keys(name)
      time.sleep(2) 
      link.click()
    
      self.wait.until(EC.presence_of_element_located((By.ID, "Form_4028B88156FAB9110156FBDC3DE812C3")))
      time.sleep(2)

      screenshot_path8 = self.capture_screenshot()

      self.driver.quit()

      return screenshot_path6, screenshot_path7, screenshot_path8

    except Exception as e:
      logging.error(f"Processando Anbima para o {name}: {e}")


