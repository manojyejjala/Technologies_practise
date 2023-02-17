from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.zomato.com/")
    page.locator("#navigation_cldrnusxz00002klmf1b3c0kb").get_by_text("Log in").click()
    with page.expect_popup() as page1_info:
        page.frame_locator("#auth-login-ui").get_by_role("button", name="Continue with Google").click()
    page.goto("https://accounts.google.com/o/oauth2/auth/oauthchooseaccount?redirect_uri=storagerelay%3A%2F%2Fhttps%2Faccounts.zomato.com%3Fid%3Dauth201253&response_type=permission%20id_token&scope=email%20profile%20openid&openid.realm&include_granted_scopes=true&client_id=442739719837.apps.googleusercontent.com&ss_domain=https%3A%2F%2Faccounts.zomato.com&prompt=select_account&fetch_basic_profile=true&gsiwebsdk=2&service=lso&o2v=1&flowName=GeneralOAuthFlow")
    # page1 = page1_info.value
    page.get_by_role("textbox", name="Email or phone").click()
    page.get_by_role("textbox", name="Email or phone").fill("test.mail199302@gmail.com")
    page.get_by_role("button", name="Next").click()
    page.get_by_role("textbox", name="Enter your password").click()
    page.get_by_role("checkbox", name="Show password").check()
    page.get_by_role("textbox", name="Enter your password").click()
    page.get_by_role("textbox", name="Enter your password").fill("test_mail93")
    page.get_by_role("button", name="Next").click()
    # page.close()
    page.goto("https://www.zomato.com/")
    page.get_by_text("location-filldown-trianglecurrent-locationDetect current locationUsing GPSplusAd").click()
    page.get_by_text("Add address").click()
    page.get_by_text("CHANGE").click()
    page.get_by_placeholder("Start typing to search").click()
    page.get_by_placeholder("Start typing to search").fill("asv chandilya")
    page.locator(".sc-gw20v4-1").first.click()
    page.get_by_role("button", name="Confirm And Proceed").click()
    page.locator("input[type=\"text\"]").nth(1).click()
    page.locator("input[type=\"text\"]").nth(1).fill("8th floor")
    page.locator("input[type=\"text\"]").nth(1).click()
    page.locator("input[type=\"text\"]").nth(1).fill("")
    page.locator("input[type=\"text\"]").nth(1).press("CapsLock")
    page.locator("input[type=\"text\"]").nth(1).fill("O")
    page.locator("input[type=\"text\"]").nth(1).press("CapsLock")
    page.locator("input[type=\"text\"]").nth(1).press("CapsLock")
    page.locator("input[type=\"text\"]").nth(1).fill("OMR R")
    page.locator("input[type=\"text\"]").nth(1).press("CapsLock")
    page.locator("input[type=\"text\"]").nth(1).fill("OMR Road")
    page.locator("input[type=\"text\"]").nth(2).click()
    page.locator("input[type=\"text\"]").nth(2).fill("8th floor")
    page.locator("input[type=\"text\"]").nth(3).click()
    page.locator("input[type=\"text\"]").nth(3).fill("beside holiday inn")
    page.locator("label").filter(has_text="Work").locator("circle").click()
    page.get_by_role("button", name="Save and proceed").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
