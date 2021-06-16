from selenium import webdriver
import os
from zeep import Client

def cline():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-logging")
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_argument("--no-sandbox")

    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)

    driver.maximize_window()
    driver.get("https://testcline.com/cccam_reseller_panel_free.php")
    element = driver.find_element_by_id("showb")
    driver.execute_script("arguments[0].setAttribute('style', 'display: block; background: white;')", element);
    element = driver.find_element_by_id("pin")
    element.screenshot("./sc/captcha.png")

    #now editing captcha images
    os.system("python3 captcha.py")

    #--------------------------------------------------------------
    LOGIN = os.environ.get("LOGIN_CAP")
    LICENSE = os.environ.get("LIC_KEY")
    client = Client('http://www.ocrwebservice.com/services/OCRWebService.asmx?WSDL')

    FilePath = "./sc/output.png"
    with open(FilePath, 'rb') as image_file:
        image_data = image_file.read()

    InputImage={
        'fileName': 'output.png',
        'fileData' : image_data,
        }
    ocrZones = {'OCRWSZone': [{'Top': 0, 'Left': 0, 'Height': 600, 'Width': 400, 'ZoneType': 0},
                              {'Top': 500, 'Left': 1000, 'Height': 150, 'Width': 400, 'ZoneType': 0}]}

    OCRSettings = {
        'ocrLanguages': 'ENGLISH',
        'outputDocumentFormat': 'DOC',
        'convertToBW': 'true',
        'getOCRText': 'true',
        'createOutputDocument': 'true',
        'multiPageDoc': 'true',
        'pageNumbers': 'allpages',
        'ocrZones': ocrZones,
        'ocrWords': 'false',
        'Reserved': '',

    }
    result = client.service.OCRWebServiceRecognize(user_name=LOGIN, license_code=LICENSE, OCRWSInputImage=InputImage, OCRWSSetting=OCRSettings)

    if result.errorMessage:
        #Error occurs during recognition
        print ("Recognition Error: " + result.errorMessage)
        exit()
    numbers = (result.ocrText.ArrayOfString[0].string[0])

    index0 = int(numbers.split("+")[0].strip(" "))
    index1 = int(numbers.split("+")[1].strip(" ="))
    final = (index0 + index1)

    #--------------------------------------------------------------

    driver.find_element_by_xpath("//input[@value='f2.kcccam.com']").click()
    driver.find_element_by_id("vehicle1").click()
    driver.find_element_by_class_name("cap").send_keys(final)
    driver.find_element_by_class_name("myButton").click()

    #--------------------------------------------------------------
    #now extracting data
    cline = driver.find_element_by_xpath('//*[@id="premium-table"]/thead/tr[1]/td[2]').get_attribute("innerText")
    driver.quit()

    return cline