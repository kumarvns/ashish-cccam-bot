import time
from logging import exception

from selenium import webdriver
import os


chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-logging")
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("--no-sandbox")

driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)

driver.maximize_window()

try:
    video = driver.get("https://www.youtube.com/watch?v=HxMGkUxnbpk")
    time.sleep(120)

    video.sendkeys("k")
    time.sleep(120)
    driver.quit()
except:
    print("error!")