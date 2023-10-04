from selenium.webdriver.common.by import By


class SignupPage:
    def __init__(self, driver):
        self.driver = driver

    fName = (By.ID, "customer.firstName")
    lName = (By.ID, "customer.lastName")
    street = (By.ID, "customer.address.street")
    city = (By.ID, "customer.address.city")
    state = (By.ID, "customer.address.state")
    zip = (By.ID, "customer.address.zipCode")
    phone = (By.ID, "customer.phoneNumber")
    ssn = (By.ID, "customer.ssn")
    username = (By.ID, "customer.username")
    password = (By.ID, "customer.password")
    rpassword = (By.ID, "repeatedPassword")
    register = (By.XPATH, "//input[@value='Register']")
    welcomeNote = (By.CLASS_NAME, "title")
    username_error = (By.ID, "customer.username.errors")
    password_error = (By.ID, "customer.password.errors")
    rpassword_error = (By.ID, "repeatedPassword.errors")

    def getFirstName(self):
        return self.driver.find_element(*SignupPage.fName)

    def getLastName(self):
        return self.driver.find_element(*SignupPage.lName)

    def getStreet(self):
        return self.driver.find_element(*SignupPage.street)

    def getCity(self):
        return self.driver.find_element(*SignupPage.city)

    def getState(self):
        return self.driver.find_element(*SignupPage.state)

    def getZip(self):
        return self.driver.find_element(*SignupPage.zip)

    def getPhone(self):
        return self.driver.find_element(*SignupPage.phone)

    def getSSN(self):
        return self.driver.find_element(*SignupPage.ssn)

    def getUsername(self):
        return self.driver.find_element(*SignupPage.username)

    def getPassword(self):
        return self.driver.find_element(*SignupPage.password)

    def getRepeatPassword(self):
        return self.driver.find_element(*SignupPage.rpassword)

    def Register(self):
        return self.driver.find_element(*SignupPage.register)

    def getWelcomeNote(self):
        return self.driver.find_element(*SignupPage.welcomeNote)

    def getUsernameError(self):
        return self.driver.find_element(*SignupPage.username_error)

    def getPasswordError(self):
        return self.driver.find_element(*SignupPage.password_error)

    def getRePasswordError(self):
        return self.driver.find_element(*SignupPage.rpassword_error)
