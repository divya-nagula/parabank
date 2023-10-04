import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.PO_AccountOverview import AccountOverview
from pageObjects.PO_LoginPage import LoginPage
from testData.CustomerData import CustomerData
from utilities.BaseClass import BaseClass


class TestLogin(BaseClass):

    def test_customerLogin(self, getData):
        login = LoginPage(self.driver)
        login.getUsername().send_keys(getData["username"])
        login.getPassword().send_keys(getData["password"])
        login.loginSubmit()
        accOverview = AccountOverview(self.driver)
        note = accOverview.getNote().text
        print(note)
        print("Login Successful")
        accOverview.Logout().click()
        self.driver.refresh()

    @pytest.fixture(params=CustomerData.getTestDataLogin("TC01"))
    def getData(self, request):
        return request.param
