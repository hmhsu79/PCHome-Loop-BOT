  
import sys
import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
import settings #data setting


if len(sys.argv) <= 2:
    print("Usage: %s productIdx cardIdx" % (sys.argv[0]))
    print("Note: Index start from 0")
    sys.exit(-1)

uidx = int(sys.argv[1])
cidx = int(sys.argv[2])
url = settings.url[uidx]

# can bypass account step 
options = webdriver.ChromeOptions()
options.add_argument(r"--user-data-dir=C:\\Users\\davidhs\\AppData\\Local\\Google\\ChromeUser")  # get --user-data-dir from chrome://version/

driver = webdriver.Chrome(executable_path='chromedriver.exe', chrome_options=options)
#driver = webdriver.Chrome(executable_path='chromedriver.exe')
driver.set_page_load_timeout(120)

isCartBtnClickable = False

driver.get(url)    
while isCartBtnClickable != True:
    #Refresh page
    driver.refresh()    
    # Cart
    WebDriverWait(driver, 20).until(
        expected_conditions.element_to_be_clickable((By.XPATH, "//li[@id='ButtonContainer']/button"))
    )
    
    driver.find_element_by_xpath("//li[@id='ButtonContainer']/button").click()
    time.sleep(0.2)
    try:
        isCartBtnClickable = True
        # Go to cart
        WebDriverWait(driver, 20).until(
            expected_conditions.element_to_be_clickable((By.ID, "ico_cart"))
        )
        driver.find_element_by_id('ico_cart').click()
    except Exception as e:
        print(e.__class__.__name__)
        print("Try reload page")
        isCartBtnClickable = False
        time.sleep(1)
        pass

time.sleep(1)
try:

    """
    # Login
    WebDriverWait(driver, 20).until(
        expected_conditions.presence_of_element_located((By.ID, 'loginAcc'))
    )
    elem = driver.find_element_by_id('loginAcc')
    elem.send_keys(settings.acc)
    elem = driver.find_element_by_id('loginPwd')
    elem.send_keys(settings.pwd)
    WebDriverWait(driver, 20).until(
        expected_conditions.element_to_be_clickable((By.ID, "btnLogin"))
    )
    driver.find_element_by_id('btnLogin').click()
    """
    """
    # Go to pay(pay once)
    WebDriverWait(driver, 20).until(
        expected_conditions.element_to_be_clickable((By.XPATH, "//li[@class='CC']/a[@class='ui-btn']"))
    )
    button = driver.find_element_by_xpath("//li[@class='CC']/a[@class='ui-btn']")
    driver.execute_script("arguments[0].click();", button)
    """

    time.sleep(0.2)
    # Go to pay(pay 24 month)
    WebDriverWait(driver, 20).until(
        expected_conditions.element_to_be_clickable((By.XPATH, "//li[@class='CI']/a[@class='ui-btn']"))
    )
    button = driver.find_element_by_xpath("//li[@class='CI']/a[@class='ui-btn']")
    driver.execute_script("arguments[0].click();", button)

    time.sleep(0.2)
    WebDriverWait(driver, 20).until(
        expected_conditions.element_to_be_clickable((By.XPATH, "//input[@data-periods='6']"))
    )
    button = driver.find_element_by_xpath("//input[@data-periods='6']")
    driver.execute_script("arguments[0].click();", button)

    select = Select(driver.find_element_by_name('multi_card_no_sel'))
    select.select_by_index(cidx)
 
    WebDriverWait(driver, 20).until(
        expected_conditions.element_to_be_clickable((By.XPATH, "//input[@name='multi_CVV2Num']"))
    )
    elem = driver.find_element_by_xpath("//input[@name='multi_CVV2Num']")
    elem.send_keys(settings.ccv[cidx])
    """
    # Check agree
    WebDriverWait(driver, 100).until(
        expected_conditions.element_to_be_clickable((By.XPATH, "//input[@name='chk_agree']"))
    )
    driver.find_element_by_xpath("//input[@name='chk_agree']").click()

    # Send PO
    WebDriverWait(driver, 20).until(
        expected_conditions.element_to_be_clickable((By.XPATH, "//a[@id='btnSubmit']"))
    )    
    button = driver.find_element_by_xpath("//a[@id='btnSubmit']")
    driver.execute_script("arguments[0].click();", button)
    """
except Exception as e:
    print(e.__class__.__name__)
    print("BOT leave")
