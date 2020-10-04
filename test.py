import unittest
from selenium import webdriver
import page


class PythonOrgSearch(unittest.TestCase):
    """A sample test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.python.org")

    def test_search_in_python_org(self):
        """
        Test python.org search features.
        Searches for the word 'pycon' then verified that some results show up.
        note that it does not look for any particular text in search results page.
        This test verifies that the results were not empty

        """

        # load the main page.
        # In this case the home page of python.org
        main_page = page.MainPage(self.driver)

        # Checks if the word "Python" is in title
        assert main_page.is_title_matches(), "python.org title doesn't match. "

        # Set the text of search textbox to "pycon"
        main_page.search_text_element = "py"
        main_page.click_go_button()
        search_result_page = page.SearchResultsPage(self.driver)

        # Verify that the results page is not empty
        assert search_result_page.is_results_found(), "No Result Found."

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    if __name__ == '__main__':
        unittest.main()


