from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
# chrome_options.add_extension("C:/Users/bittu.saishreyas/adblocker.crx")
chrome_options.add_argument("headless")  # comment it/remove when working with pytest
service_obj = Service("D:/selenium/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)
driver.maximize_window()

username = "first2"
password = "Welcome@123"

print(color.BOLD+"Launching the website.."+color.END)
driver.get("https://parabank.parasoft.com/parabank/index.htm")


print(color.BOLD+"Login Process is about to start.."+color.END)
# print(color.RED+"Login with Invalid credentials"+color.END)
# driver.find_element(By.NAME, "username").send_keys(username)
# driver.find_element(By.NAME, "password").send_keys(password+"hello")
# driver.find_element(By.XPATH, "//input[@value='Log In']").click()
# errortext1 = driver.find_element(By.XPATH, "//p[@class='error']").text
# print(errortext1)
# print(color.RED+"\nLogin with empty credentials"+color.END)
# driver.find_element(By.NAME, "username").send_keys(username)
# driver.find_element(By.XPATH, "//input[@value='Log In']").click()
# errortext2 = driver.find_element(By.XPATH, "//p[@class='error']").text
# print(errortext2)
print(color.GREEN+"\nLogin with Valid credentials"+color.END)
driver.find_element(By.NAME, "username").send_keys(username)
driver.find_element(By.NAME, "password").send_keys(password)
driver.find_element(By.XPATH, "//input[@value='Log In']").click()
# welcomeNote = driver.find_element(By.XPATH, "//p[@class='smallText']").text
# print(welcomeNote)
print(color.BOLD+"Login Successful.."+color.END)
# wait = WebDriverWait(driver, 10)
# wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='leftPanel']/ul/li[8]/a")))
# driver.find_element(By.XPATH, "//*[@id='leftPanel']/ul/li[8]/a").click()
# print(color.BOLD+"Logout Successful.."+color.END)
driver.quit()