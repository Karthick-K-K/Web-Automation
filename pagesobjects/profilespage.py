from selenium.webdriver.common.by import By


class PageProfile:


    profile_cta = (By.XPATH, "//span[text()='Manage profiles']")

    profiles_nums = (By.CSS_SELECTOR, "button[type='submit']")

    addnew_cta = (By.XPATH, "//p[text()='Add new']")

    create_cta = (By.XPATH, "//a[text()='Create profile']")

    pname_textbox = (By.NAME, "name")

    save_cta = (By.XPATH, "//button[text()='Save changes']")

    profile_edit = (By.CSS_SELECTOR, "button[data-automation-id='profiles-ww-edit']")

    remove_cta = (By.XPATH, "//a[text()='Remove']")

    remove_cnfm = (By.XPATH, "//button[text()='Remove profile']")

    def __init__(self, driver):
        self.driver = driver

    def click_profile(self):
        return self.driver.find_element(*PageProfile.profile_cta)

    def count_profiles(self):
        return self.driver.find_elements(*PageProfile.profiles_nums)

    def click_addnew(self):
        return self.driver.find_element(*PageProfile.addnew_cta)

    def click_create(self):
        return self.driver.find_element(*PageProfile.create_cta)

    def txtbox_pname(self):
        return self.driver.find_element(*PageProfile.pname_textbox)

    def save_profile(self):
        return self.driver.find_element(*PageProfile.save_cta)

    def edit_profile(self):
        return self.driver.find_element(*PageProfile.profile_edit)

    def click_remove(self):
        return self.driver.find_element(*PageProfile.remove_cta)

    def cnfm_remove(self):
        return self.driver.find_element(*PageProfile.remove_cnfm)