import pytest
# from playwright.sync_api import sync_playwright


# class Settings:
#     name = 'Parthiban'

# # @pytest.fixture
# # def page(request):
# #     class just:
# #         def __init__(self, page, request):
# #             self.page = page
# #             self.settings = request.config.settings
# #     with sync_playwright() as p:
# #         browser = p.chromium.launch(headless=False)
# #         page = browser.new_page()
# #         yield just(page, request)
# #         page.close()

# def pytest_configure(config):
#     print(config.getoption('--base-url'))
#     config.settings = Settings

@pytest.fixture
def credentials():
    return {"username": "test.mail199302@gmail.com", "password": "Test_mail93"}
