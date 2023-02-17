import time
# import pdb


def test_run(credentials, page):
    username = credentials["username"]
    password = credentials["password"]
    page.goto("https://www.w3schools.com/")
    page.get_by_role("link", name="Log in").click()
    time.sleep(10)
    page.locator("//input[@id='modalusername']").fill(username)
    page.locator("//input[@id='current-password']").fill(password)
    page.get_by_role("button", name="Log in").click()
    page.mouse.wheel(10, -50)
    time.sleep(10)
    page.locator("//div[@id='root']//div//div//div//div//div//button[@type='button'][normalize-space()='Browse all tutorials']").click()
    time.sleep(10)
    page.get_by_role("button", name="Read more").click()
    page.get_by_role("button", name="Get started").click()
    page.locator("//*[name()='path' and @id='mypage_circle1']").click()
    page.get_by_role("button", name="logout").click()
