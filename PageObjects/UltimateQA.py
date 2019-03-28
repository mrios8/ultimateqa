from selenium.webdriver.common.by import By


class UlitmateQA(object):
    def __init__(self, driver):
        self.driver = driver
        self.big_elements = self.driver.find_element(By.LINK_TEXT, 'Big page with many elements')
        self.title = self.driver.title

        self.search_field = self.driver.find_element(By.ID, 's')
        self.search_button = self.driver.find_element(By.ID, 'searchsubmit')
        self.article = self.driver.find_element(By.TAG_NAME, 'article')
        self.first_article = self.driver.find_element(By.TAG_NAME, 'a')

    def search_text(self, search_text):
        self.search_field.clear()
        self.search_field.send_keys(search_text)

    def click_link_with_text(self, text):
        result_link = self.driver.find_element(By.PARTIAL_LINK_TEXT, '{0}'.format(text))
        result_link.click()
        print(result_link.getText())

    def submit(self):
        return self.search_button.click()

