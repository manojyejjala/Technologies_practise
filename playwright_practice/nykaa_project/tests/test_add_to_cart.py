# from playwright.sync_api import Playwright, sync_playwright, expect


# def test_run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://www.nykaa.com/")
#     page.get_by_role("button", name="Google").click()
#     page.get_by_role("textbox", name="Email or phone").click()
#     page.get_by_role("textbox", name="Email or phone").fill(
#         "test.mail199302@gmail.com")
#     page.get_by_role("textbox", name="Email or phone").click()
#     page.get_by_role("textbox", name="Email or phone").press("Enter")
#     page.get_by_role("textbox", name="Enter your password").click()
#     page.get_by_role("textbox", name="Enter your password").fill("test")
#     page.get_by_role("checkbox", name="Show password").check()
#     page.get_by_role("textbox", name="Enter your password").click()
#     page.get_by_role("textbox", name="Enter your password").fill("test.mail93")
#     page.get_by_role("textbox", name="Enter your password").click()
#     page.get_by_role("textbox", name="Enter your password").press("Enter")
#     page.get_by_role("textbox", name="Enter your password").fill("test_mail93")
#     page.get_by_role("textbox", name="Enter your password").press("Enter")
#     page.goto("https://www.nykaa.com/?login=1")
#     page.get_by_placeholder("Search on Nykaa").click()
#     page.get_by_placeholder("Search on Nykaa").fill("body lotions")
#     page.locator(".multiline-elpisses").first.click()
#     page.goto("https://www.nykaa.com/cetaphil-cleansing-hydrating-regime-for-all-skin-types/p/1017249?productId=1017249&pps=19")
#     page.get_by_role("button", name="Add to Bag").first.click()

#     # ---------------------
#     context.close()
#     browser.close()


# with sync_playwright() as playwright:
#     test_run(playwright)






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
    page.frame_locator("#mobmapping_frame iframe").get_by_role("button").first.click()
    page.get_by_placeholder("Search on Nykaa").click()
    page.get_by_placeholder("Search on Nykaa").fill("body lotion")
    page.locator(".multiline-elpisses").first.click()
    with page.expect_popup() as page1_info:
        page.locator("//img[@alt='Nykaa Wanderlust Body Lotion - French Lavender']").click()
    page1 = page1_info.value
    page1.get_by_placeholder("Enter pincode").click()
    page1.get_by_placeholder("Enter pincode").fill("530004")
    page1.get_by_role("button", name="Check").click()
    page1.get_by_role("button", name="Add to Bag").first.click()
    page1.locator("#header_id").get_by_text("Test").click()
    page1.get_by_role("button", name="Logout").click()
    page1.get_by_text("Logout").nth(2).click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_run(playwright)

