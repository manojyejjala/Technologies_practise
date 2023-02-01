from playwright.sync_api import Page


class DuckDuckGoSearchPage:

    URL = "https://duckduckgo.com/"

    def __init__(self, page: Page) -> None:
        self.page = page
        self.search_button = page.locator('#search_button_homepage')
        self.search_input = page.locator('#search_form_input_homepage')

    def load(self) -> None:
        self.page.goto(self.URL)

    def search(self, phrase: str) -> None:
        self.search_input.fill(phrase)
        self.search_button.click()

    def test_basic_duckduckgo_search(page: Page) -> None:
        page.goto('https://duckduckgo.com/')
        page.locator('#search_from input_homepage').fill('panda')
        page.locator('#search_button_homepage').click()


# from pages.search import DuckDuckGoSearchPage

# def test_basic_duckduckgo_search(page: Page) -> None:
#     search_page = DuckDuckGoSearchPage(page)
#     search_page.load()
#     search_page.search('panda')
