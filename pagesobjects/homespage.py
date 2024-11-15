from selenium.webdriver.common.by import By


class Homiepage:

    menubutton = (By.XPATH, "//button[@aria-label='Profile, Settings, and Account']")

    signin_opt = (By.XPATH, "//span[text()='Sign In']")

    email_id_value = (By.NAME, "email")

    cntn_button = (By.ID, "continue")

    password = (By.NAME, "password")

    submit_cta = (By.ID, "signInSubmit")

    signout_opt = (By.XPATH, "//span[text()='Sign out']")

    def __init__(self, driver) -> None:
        self.driver = driver

    def menuOp(self):
        return self.driver.find_element(*Homiepage.menubutton)

    def signin_item(self):
        return self.driver.find_element(*Homiepage.signin_opt)

    def enter_email_id(self):
        return self.driver.find_element(*Homiepage.email_id_value)

    def click_cntn(self):
        return self.driver.find_element(*Homiepage.cntn_button)

    def enter_password(self):
        return self.driver.find_element(*Homiepage.password)

    def click_submit(self):
        return self.driver.find_element(*Homiepage.submit_cta)

    def signout_item(self):
        return self.driver.find_element(*Homiepage.signout_opt)