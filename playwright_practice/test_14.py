from playwright.sync_api import sync_playwright, Playwright


def test_run(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    page.goto("https://pypi.org/project/allure-pytest/")
    page.get_by_role('textbox').fill('allure')
    page.keyboard.press('Enter')
    page.get_by_role('generic')
    page.wait_for_timeout(10000)
    context.tracing.stop(path="trace14.zip")


with sync_playwright() as playwright:
    test_run(playwright)
