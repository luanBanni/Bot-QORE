from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import logging
import pyautogui

class BaseService:
  def __init__(self, driver, wait):
    self.driver = driver
    self.wait = wait

  def capture_screenshot(self):
    screenshot = pyautogui.screenshot()
    return screenshot