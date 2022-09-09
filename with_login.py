from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time
import configparser

# variable
_url_path = "https://scanmevacuno.gob.cl/"
parser = configparser.ConfigParser()
parser.read('config.ini')


def without_login(url=_url_path):
  opt = Options()
  opt.add_argument("--disable-infobars")
  opt.add_argument("start-maximized")
  opt.add_argument("--disable-extensions")
  # Pass the argument 1 to allow and 2 to block
  opt.add_experimental_option("prefs", { \
      "profile.default_content_setting_values.media_stream_camera": 1,
    })
  driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=opt,)
  driver.get(_url_path)
  time.sleep(3)
  driver.find_element(By.CLASS_NAME,'color-purple').click()
  driver.find_element(By.CLASS_NAME,'dialog-button-bold').click()
  time.sleep(15)
  data = driver.find_element(By.CLASS_NAME,'identidad')
  driver.close()
  return {"data":data.text.split("\n")}
  

def with_login(url=_url_path):
  opt = Options()
  opt.add_argument("--disable-infobars")
  opt.add_argument("start-maximized")
  opt.add_argument("--disable-extensions")
  # Pass the argument 1 to allow and 2 to block
  opt.add_experimental_option("prefs", { \
      "profile.default_content_setting_values.media_stream_camera": 1,
    })
  driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),options=opt,)
  username = parser.get('scaper','username')
  password = parser.get('scaper','password')
  driver.get(_url_path)
  time.sleep(3)
  
  driver.find_element(By.CLASS_NAME,'texto').click()
  driver.find_element(By.ID,'uname').send_keys(username)
  time.sleep(2)
  driver.find_element(By.ID,'pword').send_keys(password)
  time.sleep(2)
  driver.find_element(By.ID,'login-submit').click()
  time.sleep(2)
  driver.find_element(By.CLASS_NAME,'color-purple').click()
  driver.find_element(By.CLASS_NAME,'dialog-button-bold').click()
  time.sleep(10)
  data = driver.find_element(By.CLASS_NAME,'identidad')
  driver.close()
  return {"data":data.text.split("\n")}

# print()
print(without_login())
