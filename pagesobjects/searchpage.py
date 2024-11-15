from selenium.webdriver.common.by import By


class SearchPage:

    search_icon = (By.XPATH, "(//button[@aria-label='Search Prime Video'])[1]")

    searchbox = (By.ID, "pv-search-nav")

    asset_name = (By.XPATH, "//a[text()='Vettaiyan']")

    def __init__(self, driver) -> None:
        self.driver = driver

    def click_search(self):
        return self.driver.find_element(*SearchPage.search_icon)

    def send_text(self):
        return self.driver.find_element(*SearchPage.searchbox)

    def sel_asset(self):
        return self.driver.find_element(*SearchPage.asset_name)