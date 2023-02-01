from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage
from playwright.sync_api import expect, Page


def test_basic_duckduckgo_search(page: Page) -> None:
    search_page = DuckDuckGoSearchPage(page)
    result_page = DuckDuckGoResultPage(page)

    search_page.load()
    search_page.search('panda')
    expect(result_page.search_input).to_have_value('panda')
    assert result_page.result_link_titles_contain_phrase('panda')
    expect(page).to_have_title('panda at DuckDuckGo')
