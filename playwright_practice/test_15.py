from playwright.sync_api import sync_playwright, Playwright


def test_run(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page.goto("https://www.javatpoint.com/selenium-python")
    page.get_by_role("textbox", name="search").click().fill("selenium")
    page.get_by_role("button", name="search").click()
    page.wait_for_timeout(5000)
    context.tracing.stop(path='trace15.zip')


with sync_playwright() as playwright:
    test_run(playwright)
