from playwright.sync_api import Playwright

def test_run(playwright: Playwright):
    try:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        page.goto("https://duckduckgo.com/")
        page.get_by_role("combobox").fill("playwright").press("Enter")
        page.press
        page.wait_for_timeout(5000)

    except Exception as e:
        print(e)
