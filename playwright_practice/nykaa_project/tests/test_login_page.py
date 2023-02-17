from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.nykaa.com/")
    page.get_by_role("button", name="Google").click()
    page.get_by_role("textbox", name="Email or phone").click()
    page.get_by_role("textbox", name="Email or phone").fill("test.mail199302@gmail.com")
    page.get_by_role("textbox", name="Email or phone").press("Enter")
    page.get_by_role("checkbox", name="Show password").check()
    page.get_by_role("textbox", name="Enter your password").click()
    page.get_by_role("textbox", name="Enter your password").fill("test_mail93")
    page.get_by_role("textbox", name="Enter your password").press("Enter")
    page.goto("https://www.nykaa.com/?login=1")
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_run(playwright)
