import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.PO_AccountOverview import AccountOverview
from pageObjects.PO_LoginPage import LoginPage
from pageObjects.PO_SignupPage import SignupPage
from testData.CustomerData import CustomerData
from utilities.BaseClass import BaseClass


class TestSignUp(BaseClass):

    def test_customerSignup(self, getData):
        # log = self.getLogger()
        login = LoginPage(self.driver)
        login.Register()
        print("Starting signup process..")
        signup = SignupPage(self.driver)
        signup.getFirstName().send_keys(getData["firstName"])
        signup.getLastName().send_keys(getData["lastName"])
        signup.getStreet().send_keys(getData["street"])
        signup.getCity().send_keys(getData["city"])
        signup.getState().send_keys(getData["state"])
        signup.getZip().send_keys(getData["zip"])
        signup.getPhone().send_keys(getData["phone"])
        signup.getSSN().send_keys(getData["SSN"])
        signup.getUsername().send_keys(getData["username"])
        signup.getPassword().send_keys(getData["password"])
        signup.getRepeatPassword().send_keys(getData["password"])
        signup.Register().click()
        print("Registration form submitted")
        note = signup.getWelcomeNote().text
        print(note)
        accOverview = AccountOverview(self.driver)
        accOverview.Logout().click()
        self.driver.refresh()

    def test_customerSignup_existingUsernameError(self, getData):
        # log = self.getLogger()
        login = LoginPage(self.driver)
        login.Register()
        print("Starting signup process..")
        signup = SignupPage(self.driver)
        signup.getFirstName().send_keys(getData["firstName"])
        signup.getLastName().send_keys(getData["lastName"])
        signup.getStreet().send_keys(getData["street"])
        signup.getCity().send_keys(getData["city"])
        signup.getState().send_keys(getData["state"])
        signup.getZip().send_keys(getData["zip"])
        signup.getPhone().send_keys(getData["phone"])
        signup.getSSN().send_keys(getData["SSN"])
        signup.getUsername().send_keys("first25")
        signup.getPassword().send_keys(getData["password"])
        signup.getRepeatPassword().send_keys(getData["password"])
        signup.Register().click()
        print("Registration form submitted")
        error1 = signup.getUsernameError().text
        assert "This username already exists." in error1
        print(error1)

        self.driver.refresh()

    def test_customerSignup_PasswordErrors(self, getData):
        # log = self.getLogger()
        login = LoginPage(self.driver)
        login.Register()
        print("Starting signup process..")
        signup = SignupPage(self.driver)
        signup.getFirstName().send_keys(getData["firstName"])
        signup.getLastName().send_keys(getData["lastName"])
        signup.getStreet().send_keys(getData["street"])
        signup.getCity().send_keys(getData["city"])
        signup.getState().send_keys(getData["state"])
        signup.getZip().send_keys(getData["zip"])
        signup.getPhone().send_keys(getData["phone"])
        signup.getSSN().send_keys(getData["SSN"])
        signup.getUsername().send_keys("first27")
        signup.getPassword().send_keys("")
        signup.getRepeatPassword().send_keys("")
        signup.Register().click()
        print("Registration form submitted")
        error2 = signup.getPasswordError().text
        assert "Password is required." in error2
        print(error2)
        error3 = signup.getRePasswordError().text
        assert "Password confirmation is required." in error3
        print(error3)
        signup.getPassword().send_keys("password")
        signup.getPassword().send_keys("password1")
        error4 = signup.getRePasswordError().text
        assert "Passwords did not match." in error4
        print(error4)

        self.driver.refresh()

    @pytest.fixture(params=CustomerData.getTestDataSignup("TC11"))
    def getData(self, request):
        return request.param
