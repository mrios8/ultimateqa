import unittest
import datetime
from selenium import webdriver
from PageObjects.UltimateQA import UlitmateQA
from PageObjects.SearchResults import SearchResults
from PageObjects.SearchResults import Article




class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        print("Run started at :" + str(datetime.datetime.now()))
        print("Chrome Environment Set Up")
        print("-----------------------------------------------------------------------")
        self.driver.implicitly_wait(20)
        self.driver.maximize_window()

    def test_search(self):
        self.driver.get('https://www.ultimateqa.com/automation/')
        self.assertEqual('Automation Practice - Ultimate QA', UlitmateQA(self.driver).title)
        automation_practice_page = UlitmateQA(self.driver)

        # FIRST SEARCH TEST
        automation_practice_page.search_text('Automation')
        automation_practice_page.submit()
        search_results = SearchResults(self.driver)
        self.assertTrue(search_results.article.is_displayed())

        # SECOND SEARCH TEST
        search_results.search_text('Automation')
        search_results.submit()

        # SEARCH RESULTS
        search_results_2 = SearchResults(self.driver)
        self.assertTrue(search_results_2.article.is_displayed())
        article1 = search_results_2.article_title_contains('Practice')
        search_results_2.click_link_with_title(article1)

        # Article Page
        article_page = Article(self.driver)
        # Assert the title of the link you clicked is the same as the title of the article
        self.assertEqual(article1, article_page.title)

    def test_registration(self):
        pass

    def tearDown(self):
        if self.driver is not None:
            print("-----------------------------------------------------------------------")
            print("Test Environment Destroyed")
            print("Run Completed at :" + str(datetime.datetime.now()))
            self.driver.close()
            self.driver.quit()
if __name__ == '__main__':
    unittest.main()
