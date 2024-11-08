from selenium import webdriver

class WebDriverManager:
  def __init__(self):
    self.driver = None

  def start_driver(self):
    self.driver = webdriver.Chrome()
    self.driver.maximize_window()
    return self.driver

  def quit_driver(self):
    if self.driver:
      self.driver.quit()

