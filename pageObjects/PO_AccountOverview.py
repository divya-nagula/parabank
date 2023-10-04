from selenium.webdriver.common.by import By


class AccountOverview:
    def __init__(self, driver):
        self.driver = driver

    pageTitle = (By.XPATH, "//div[@id='rightPanel']/div/div/h1")
    accountNo = (By.XPATH, "//*[@id='accountTable']/tbody/tr[1]/td[1]/a")
    logout = (By.XPATH, "//*[@id='leftPanel']/ul/li[8]/a")
    note = (By.XPATH, "//*[@id='leftPanel']/p")

    def getPageTitle(self):
        return self.driver.find_element(*AccountOverview.pageTitle)

    def getAccountNo(self):
        return self.driver.find_element(*AccountOverview.accountNo)

    def Logout(self):
        return self.driver.find_element(*AccountOverview.logout)

    def getNote(self):
        return self.driver.find_element(*AccountOverview.note)