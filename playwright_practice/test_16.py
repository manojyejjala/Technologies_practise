from playwright.sync_api import sync_playwright, Playwright


def test_run(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page.goto('http://139.59.79.118/')
    page.get_by_role("link", name="Status").click()
    page.get_by_role("link", name="Next").click()
    page.get_by_role("link", name="Stat").click()
    page.get_by_role("link", name="Home").click()
    page.wait_for_timeout(5000)
    context.tracing.stop(path='trace16.zip')


with sync_playwright() as playwright:
    test_run(playwright)
