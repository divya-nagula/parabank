from selenium.webdriver.common.by import By

from pageObjects.PO_AccountOverview import AccountOverview
from pageObjects.PO_SignupPage import SignupPage


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    username = (By.NAME, "username")
    password = (By.NAME, "password")
    loginButton = (By.XPATH, "//input[@value='Log In']")
    registerLink = (By.XPATH, "//a[normalize-space()='Register']")
    note = (By.XPATH, "//*[@id='leftPanel']/p")

    def getUsername(self):
        return self.driver.find_element(*LoginPage.username)

    def getPassword(self):
        return self.driver.find_element(*LoginPage.password)

    def loginSubmit(self):
        self.driver.find_element(*LoginPage.loginButton).click()
        accntoverview = AccountOverview(self.driver)
        return accntoverview

    def Register(self):
        self.driver.find_element(*LoginPage.registerLink).click()
        register = SignupPage(self.driver)
        return register
