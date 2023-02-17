from playwright.sync_api import Playwright, sync_playwright, expect


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://www.zomato.com/")
    page.get_by_text("Log in").click()
    page.get_by_text("Log in").click()
    page.get_by_text("Log in").click()
    with page.expect_popup() as page1_info:
        page.frame_locator("#auth-login-ui").get_by_role("button", name="Continue with Google").click()
    page1 = page1_info.value
    page1.get_by_role("textbox", name="Email or phone").click()
    page1.get_by_role("textbox", name="Email or phone").fill("test.mail199302@gmail.com")
    page1.get_by_role("button", name="Next").click()
    page1.get_by_role("checkbox", name="Show password").check()
    page1.get_by_role("textbox", name="Enter your password").click()
    page1.get_by_role("textbox", name="Enter your password").fill("test_mail93")
    page1.get_by_role("button", name="Next").click()
    page1.goto("https://accounts.google.com/signin/oauth/consent?authuser=0&part=AJi8hAMjVki3gxU_SCm5-KTydbJdhIq252dolZDeA7RJVMea8yddzt74cX_pyH4kaIhO8-Dpep1O0qk0SzFAnt44KaEtPNKtcJgWAY7r-8PknqqiGhb5ZDw7mMppd_6qR4usmPdjx8e324HEUqAQT3CJz_ICbVB4p3j2swDMkYExfGWK8Aip5V7g4yRJmrSA1Nfyg4QFfVSfOjTh4i6yusJH5VbsArR_Qw_fsMadPbYgek1XEGeCsk--O1GyFOM5ux8AHWjY4KRyuY9tsN_6NDumZBC57UycKs51YxSolGvINqveS3WmTnyRwzQ99DQ7NKGG4C51dmzCsyH881bMwJjfmkD573KX_pnKukgEEuFofIlug7rUOoqe1rj1SyIghJgEjlQ1ody4wQutETxcVsnQR-Q0aRKSXRPV_fZYCj9QRr1N3-E2yH4&as=S135207177%3A1675621048154338&client_id=442739719837.apps.googleusercontent.com&rapt=AEjHL4PyCeYeinzhWiM2RmDBVcFeffgjor0qYmXqrNtkpL-KYwzru6DTdJUO7BdZvIpSWziOYSNEYQ4Vf7X0ZGNmIxhGy7VtUw#")
    page1.close()
    page.goto("https://www.zomato.com/")

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    test_run(playwright)
