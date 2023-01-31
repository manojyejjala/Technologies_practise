from playwright.sync_api import Playwright, sync_playwright


def test_run(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page = context.new_page()
    page.goto("https://www.w3schools.com/")
    page.get_by_role("link", name="Tutorials ").click()
    page.locator("#nav_tutorials").get_by_role("link", name="Learn HTML").click()
    page.get_by_role("link", name="HTML Introduction").click()
    page.get_by_role("link", name="HTML Editors").click()
    page.get_by_role("link", name="HTML Basic").click()
    page.get_by_role("link", name="HTML Elements").click()
    page.get_by_role("link", name="HTML Attributes").first.click()
    page.get_by_role("link", name="HTML Headings").click()
    page.get_by_role("link", name="HTML Paragraphs").click()
    page.get_by_role("link", name="HTML Styles").click()
    page.get_by_role("link", name="HTML Formatting").click()
    page.get_by_role("link", name="HTML Quotations").click()
    page.get_by_role("link", name="HTML Comments").click()
    page.get_by_title("CSS Tutorial").first.click()
    page.get_by_role("link", name="CSS Introduction").click()
    page.get_by_role("link", name="CSS Syntax").click()
    page.get_by_role("link", name="CSS Selectors").first.click()
    page.get_by_role("link", name="CSS How To").click()
    page.get_by_role("link", name="CSS Comments").click()
    page.locator("#topnav").get_by_role("link", name="SQL").click()
    page.get_by_title("Java Tutorial").click()
    page.get_by_title("Python Tutorial").click()
    page.get_by_role("link", name="Python Booleans").click()
    page.get_by_role("link", name="Python Variables").click()
    context.tracing.stop(path="trace12.zip")


with sync_playwright() as playwright:
    test_run(playwright)
