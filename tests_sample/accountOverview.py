from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from tabulate import tabulate


# account_no = ""
# balance = ""
# availAmt = ""


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
# wait = WebDriverWait(driver, 10)
# wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//p[@class='smallText']")))
# welcomeNote = driver.find_element(By.XPATH, "//p[@class='smallText']").text
# assert "Welcome" in welcomeNote, "Some Error has occurred"
# print(welcomeNote)
# assert "Account Overview" in driver.find_element(By.XPATH, "//h1[@class='title']").text
wait = WebDriverWait(driver, 10)
# wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//table[@id='accountTable']/thead")))
driver.implicitly_wait(10)
headers = driver.find_elements(By.XPATH, "//table[@id='accountTable']/thead/tr/th")
count = len(headers)
print("Table has", count, "headers")

headers_list = []
for i in headers:
    headers_value = i.text
    headers_list.append(headers_value)
wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//*[@id='accountTable']/tbody/tr")))
print("Header names are:", headers_list)

accounts = driver.find_elements(By.XPATH, "//*[@id='accountTable']/tbody")

accounts_dict = []
for j in accounts:
    accounts_data = j.find_elements(By.XPATH, "//*[@id='accountTable']/tbody/tr")
    noOfAccounts = len(accounts_data)-1
    print("The user has", noOfAccounts, "accounts")
    k = 0
    account_nos = j.find_elements(By.XPATH, "//*[@id='accountTable']/tbody/tr/td[1]")
    print(len(account_nos))
    balances = j.find_elements(By.XPATH, "//*[@id='accountTable']/tbody/tr/td[2]")
    print(len(balances))
    availAmounts = j.find_elements(By.XPATH, "//*[@id='accountTable']/tbody/tr/td[3]")
    print(len(availAmounts))
    while k < noOfAccounts:
        account_no = ""
        balance = ""
        availAmt = ""
        account_data = {}
        # account_nos = j.find_elements(By.XPATH, "//*[@id='accountTable']/tbody/tr/td[1]")
        for l in account_nos:
            account_no = l.text
            if "Total" not in account_no:
                account_data.update({"account_no": account_no})

                # balances = j.find_elements(By.XPATH, "//*[@id='accountTable']/tbody/tr/td[2]")
                for m in balances:
                    balance = m.text
                    account_data.update({"balance": balance})
                    # availAmounts = j.find_elements(By.XPATH, "//*[@id='accountTable']/tbody/tr/td[3]")
                    for n in availAmounts:
                        availAmt = n.text
                        account_data.update(({"available amount": availAmt}))
                k = k + 1

            else:
                break
            accounts_dict.append(account_data.copy())
print("Accounts:", accounts_dict)
print("headers:", headers_list)
table = tabulate(accounts_dict)
print(table)

driver.quit()