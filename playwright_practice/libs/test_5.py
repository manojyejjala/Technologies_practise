from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(page):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page.goto("https://www.apple.com/")
    page.get_by_role("navigation", name="Global").get_by_role("link", name="iPhone").click()
    page.get_by_role("button", name="Buy iPhone SE").click()
    page.get_by_role("img", name="iPhone 14 Pro—available in Deep Purple, Gold, Silver, and Space Black.").click()
    context.tracing.stop(path="trace.zip")
    

with sync_playwright() as playwright:
    test_run(playwright)
