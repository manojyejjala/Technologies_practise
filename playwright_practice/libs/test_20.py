from playwright.sync_api import sync_playwright

def test_run(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page.goto("")
    page.get_by_role("")