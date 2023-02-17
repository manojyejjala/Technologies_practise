from playwright.sync_api import Playwright, sync_playwright


def test_case(page):
    portal = page.page
    settings = page.settings
    print(settings.name)
    assert 1
# def test_run(playwright: Playwright):
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     context.tracing.start(screenshots=True, snapshots=True, sources=True)
#     page = context.new_page()
#     page.goto("https://www.w3schools.com/")
#     page.get_by_placeholder("Search our tutorials, e.g. HTML").fill("HTML")
#     page.keyboard.press('Enter')
#     page.close()
#     context.tracing.stop(path="trace13.zip")


# with sync_playwright() as playwright:
#     test_run(playwright)
