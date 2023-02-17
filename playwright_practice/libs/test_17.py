from playwright.sync_api import sync_playwright, Playwright


def test_run(playwright: Playwright):
    browser = playwright.chromium.launch()
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    page.goto("https://go.dev/")
    page.get_by_role("link", name='Learn').click()
    page.get_by_role("link", name='Packages').click()
    page.get_by_role("textbox").fill("log")
    page.keyboard.press("Enter")
    page.get_by_role("link", name="log(log)").click()
    page.get_by_role("link", name="go").click()
    context.tracing.stop(path="trace17.zip")
    page.wait_for_timeout(5000)


with sync_playwright() as playwright:
    test_run(playwright)
