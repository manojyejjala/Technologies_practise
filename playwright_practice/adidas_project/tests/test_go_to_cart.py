import time


def test_run(page, credentials):
    username = credentials["username"]
    password = credentials["password"]
    page.goto("https://www.adidas.co.in/")
    page.get_by_role("link", name="log in").click()
    page.get_by_role("textbox", name="Email").fill(username)
    page.get_by_role("textbox", name="Password").fill(password)
    page.get_by_role("checkbox", name="Keep me logged in. More info").click()
    page.get_by_role("button", name="Log in").click()
    page.locator("//a[@role='menu'][normalize-space()='MEN']").click()
    time.sleep(5)
    page.locator(
        "//section[@data-testid='teaser-block-wrapper']//section[1]//a[1]").click()
    time.sleep(5)
    page.locator(
        "//div[16]//div[1]//div[1]//div[1]//div[1]//div[1]//div[1]//div[1]//a[1]//img[1]").click()
    time.sleep(5)
    page.get_by_role("button", name="2XL").click()
    page.get_by_role("button", name="ADD TO BAG").click()
    page.get_by_role("link", name="VIEW BAG").click()
    time.sleep(5)
    page.get_by_role("button", name="Checkout").click()
    page.get_by_role("link", name="log in").click()
    page.get_by_role("tab", name="ACCOUNT").click()
    page.get_by_role("link", name="Log out").click()
