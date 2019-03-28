from selenium.webdriver.common.by import By


class SearchResults(object):
    def __init__(self, driver):
        self.driver = driver
        self.article = self.driver.find_element(By.TAG_NAME, 'article')
        self.search_field = self.driver.find_element(By.ID, 's')
        self.search_button = self.driver.find_element(By.ID, 'searchsubmit')

    def search_text(self, search_string):
        self.search_field.clear()
        self.search_field.send_keys(search_string)

    def article_title_contains(self, text):
        return self.driver.find_element(By.PARTIAL_LINK_TEXT, '{0}'.format(text)).text

    def click_link_with_title(self, text):
        self.driver.find_element(By.LINK_TEXT, '{0}'.format(text)).click()

    def submit(self):
        return self.search_button.click()


class Article(object):

    def __init__(self, driver):
        self.driver = driver
        self.title = self.driver.title
