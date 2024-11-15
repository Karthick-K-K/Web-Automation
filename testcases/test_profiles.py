import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pagesobjects.homespage import Homiepage
from pagesobjects.profilespage import PageProfile

from utility.basicsutils import BaseClass



# @pytest.mark.usefixtures("setup")
class Test_Profiles(BaseClass):

    def test_profiles(self):
        wait = WebDriverWait(self.driver, 10)
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
        profilepage = PageProfile(self.driver)
        # item1 = self.driver.find_element(By.XPATH, "//span[text()='Manage profiles']")
        item1 = profilepage.click_profile()
        action.move_to_element(item1).click().perform()

        # avaiprofiles = self.driver.find_elements(By.CSS_SELECTOR, "button[type='submit']")
        avaiprofiles = profilepage.count_profiles()
        print(len(avaiprofiles))
        time.sleep(2)

        # driver.find_element(By.CLASS_NAME, "PxdfCI").click()
        # self.driver.find_element(By.XPATH, "//p[text()='Add new']").click()
        profilepage.click_addnew().click()
        time.sleep(2)

        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//a[text()='Create profile']")))
        # self.driver.find_element(By.XPATH, "//a[text()='Create profile']").click()
        profilepage.click_create().click()
        time.sleep(2)
        pname = "New2"
        # self.driver.find_element(By.NAME, "name").send_keys(pname)
        profilepage.txtbox_pname().send_keys(pname)

        wait.until(
            expected_conditions.presence_of_element_located((By.XPATH, "//button[text()='Save changes']"))).is_enabled()
        # savecta = profilepage.save_profile()
        # savecta.click()
        # savecta = self.driver.find_element(By.XPATH, "//button[text()='Save changes']")
        profilepage.save_profile().click()
        time.sleep(2)

        # avaiprofiles1 = self.driver.find_elements(By.XPATH, "//button[@type='submit']")
        avaiprofiles1 = profilepage.count_profiles()
        print(len(avaiprofiles1))
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//p[text()='Add new']")))
        assert len(avaiprofiles) != len(avaiprofiles1)

        if len(avaiprofiles) != len(avaiprofiles1):
            print('New profile has been created')
        else:
            print("New profile has not been created")
        time.sleep(2)

        # self.driver.find_element(By.CSS_SELECTOR, "button[data-automation-id='profiles-ww-edit']").click()
        profilepage.edit_profile().click()
        for i in avaiprofiles1:
            pname1 = i.find_element(By.XPATH, "div/p").text
            if pname1 == pname:
                i.find_element(By.XPATH, "p").click()
                break
        time.sleep(2)

        self.driver.execute_script("window.scrollTo(0,200);")
        # self.driver.find_element(By.XPATH, "//a[text()='Remove']").click()
        profilepage.click_remove().click()
        time.sleep(2)

        # self.driver.find_element(By.XPATH, "//button[text()='Remove profile']").click()
        profilepage.cnfm_remove().click()
        time.sleep(2)

        avaiprofiles2 = profilepage.count_profiles()
        if len(avaiprofiles) == len(avaiprofiles2):
            print('profile has been deleted')
        else:
            print("profile has not been deleted")
        time.sleep(2)
