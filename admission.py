from telethon.sessions import StringSession
from telethon import TelegramClient
from selenium import webdriver
import time
import os

api_id = os.environ.get("API_KEY")
api_hash = os.environ.get("API_HASH")
stringsession = os.environ.get("STRING")
client = TelegramClient(StringSession(stringsession),api_id,api_hash)

def message(capture):
    async def main():
        await client.send_message('me', capture)
        await client.send_message('me', '`Something changed on allduniv.ac.in !!`')

    with client:
        client.loop.run_until_complete(main())



chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-logging")
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("--no-sandbox")



while True:
    try:
        driver = webdriver.Chrome(executable_path="./chromedriver.exe", options=chrome_options)

        driver.get("https://www.allduniv.ac.in/admissions.php")

        driver.implicitly_wait(15)
        capture = driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div/div/h3").text
        if capture != "Admissions 2021 to be announced soon.":
            message(f"`{capture}`")

        driver.close()
        time.sleep(9000)

    except:
        pass