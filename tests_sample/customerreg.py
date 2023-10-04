from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


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

print(color.BOLD+"Launching the website.."+color.END)
driver.get("https://parabank.parasoft.com/parabank/index.htm")

print(color.BOLD+"Starting registration process.."+color.END)
driver.find_element(By.XPATH, "//a[normalize-space()='Register']").click()

username = "first3"
password = "Welcome@123"
print(color.BOLD+"Enter personal information.."+color.END)
driver.find_element(By.ID, "customer.firstName").send_keys("first")
driver.find_element(By.ID, "customer.lastName").send_keys("last")
driver.find_element(By.ID, "customer.address.street").send_keys("Begur")
driver.find_element(By.ID, "customer.address.city").send_keys("Bengaluru")
driver.find_element(By.ID, "customer.address.state").send_keys("Karnataka")
driver.find_element(By.ID, "customer.address.zipCode").send_keys("56895")
driver.find_element(By.ID, "customer.phoneNumber").send_keys("8548695697")
driver.find_element(By.ID, "customer.ssn").send_keys("4152635264")
driver.find_element(By.ID, "customer.username").send_keys(username)
driver.find_element(By.ID, "customer.password").send_keys(password)
driver.find_element(By.ID, "repeatedPassword").send_keys(password)
driver.find_element(By.XPATH, "//input[@value='Register']").click()

welcomenote = driver.find_element(By.CLASS_NAME, "title").text
print(welcomenote)

print(color.BOLD+"Registration successful.."+color.END)

driver.quit()




