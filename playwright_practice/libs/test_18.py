from playwright.sync_api import sync_playwright, Playwright


def test_run(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page.goto("https://playwright.dev/")
    page.get_by_role("link", name="GET STARTED").click()
    context.tracing.stop(path="trace18.zip")
    page.wait_for_timeout(5000)


with sync_playwright() as playwright:
    test_run(playwright)
