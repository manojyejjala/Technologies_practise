import time
# import pdb


def test_run(page, credentials):
    username = credentials["username"]
    password = credentials["password"]
    page.goto("https://www.adidas.co.in/")
    # breakpoint()
    # pdb.set_trace()
    page.get_by_role("link", name="log in").click()
    page.get_by_role("textbox", name="Email").fill(username)
    page.get_by_role("textbox", name="Password").fill(password)
    page.get_by_role("checkbox", name="Keep me logged in. More info").click()
    page.get_by_role("button", name="Log in").click()
    page.get_by_role("link", name="log in").click()
    time.sleep(5)
    page.get_by_role("tag", name="ACCOUNT").click()
    page.locator("//a[normalize-space()='returns']").click()
    time.sleep(5)
    page.go_back()
    time.sleep(5)
    page.locator("//a[normalize-space()='Log out']").click()
