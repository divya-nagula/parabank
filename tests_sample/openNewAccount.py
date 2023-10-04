from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
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

username = "first3"
password = "Welcome@123"

print(color.BOLD + "Launching the website.." + color.END)
driver.get("https://parabank.parasoft.com/parabank/index.htm")

print(color.BOLD + "Login Process is about to start.." + color.END)
print(color.BOLD + "\nLogging with Valid credentials" + color.END)
driver.find_element(By.NAME, "username").send_keys(username)
driver.find_element(By.NAME, "password").send_keys(password)
driver.find_element(By.XPATH, "//input[@value='Log In']").click()
# welcomeNote = driver.find_element(By.XPATH, "//p[@class='smallText']").text
# # assert "Welcome" in welcomeNote, "Some Error has occurred"
# print(welcomeNote)

print(color.BOLD + "Login Successful.." + color.END)
# wait = WebDriverWait(driver, 15)
# wait.until(expected_conditions.presence_of_element_located((By.XPATH, "///thead/tr/th[1]")))
# driver.find_element(By.XPATH, "//*[@id='accountTable']/tbody/tr/td[1]/a").click()
# print(accountNo)

print(color.BOLD + "Creating new account" + color.END)
driver.find_element(By.XPATH, "/html/body/div[1]/div[3]/div[1]/ul/li[1]/a").click()
accountType = Select(driver.find_element(By.XPATH, "//select[@id='type']"))
accountType.select_by_visible_text("CHECKING")
# depAmount = Select(driver.find_element(By.XPATH, "//*[@id='fromAccountId']"))
# depAmount.select_by_index(0)
driver.find_element(By.XPATH, "//input[@class='button']").click()
driver.implicitly_wait(10)
# successText = driver.find_element(By.XPATH, "//*[@id='rightPanel']/div/div/p[1]").text
# # assert "Congratulations" in successText
# print(successText)
title = driver.find_element(By.XPATH, "//*[@id='rightPanel']/div/div/h1").text
print(title)
driver.find_element(By.XPATH, "//a[@class='ng-binding']").click()

print(driver.find_element(By.XPATH, "//td[@id='accountId']").text)

driver.quit()
