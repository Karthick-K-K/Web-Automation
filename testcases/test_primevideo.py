import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import pytest

from pagesobjects.homespage import Homiepage

from utility.basicsutils import BaseClass



# @pytest.mark.usefixtures("setup")

class Test_SignInOut(BaseClass):

    @pytest.mark.smoke
    def test_signin(self):
        wait = WebDriverWait(self.driver, 10)

        # driver.find_element(By.XPATH, "//button[@aria-label='Profile, Settings, and Account']").click()

        action = ActionChains(self.driver)
        Hmepage = Homiepage(self.driver)
        # menu = self.driver.find_element(By.XPATH, "//button[@aria-label='Profile, Settings, and Account']")
        menu = Hmepage.menuOp()
        action.move_to_element(menu).perform()

        # item = self.driver.find_element(By.XPATH, "//span[text()='Sign In']")
        item = Hmepage.signin_item()
        action.move_to_element(item).click().perform()
        time.sleep(3)

        # self.driver.find_element(By.NAME, "email").send_keys("karthick.krishnasetty@ovyo.com")
        Hmepage.enter_email_id().send_keys("karthick.krishnasetty@ovyo.com")

        # self.driver.find_element(By.ID, "continue").click()
        Hmepage.click_cntn().click()
        time.sleep(2)

        # self.driver.find_element(By.NAME, "password").send_keys("kk@may23")
        Hmepage.enter_password().send_keys("kk@may23")

        # self.driver.find_element(By.ID, "signInSubmit").click()
        Hmepage.click_submit().click()
        time.sleep(3)

        # action = ActionChains(self.driver)
        # menu1 = self.driver.find_element(By.XPATH, "//button[@aria-label='Profile, Settings, and Account']")
        menu1 = Hmepage.menuOp()
        action.move_to_element(menu1).perform()
        print("sign in done successfully")

        # wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//span[text()='Sign Out']")))
        # item1 = self.driver.find_element(By.XPATH, "//span[text()='Sign out']")
        item1 = Hmepage.signout_item()
        action.move_to_element(item1).click().perform()
        print("sign out done successfully")
        
        time.sleep(2)
