from playwright.sync_api import Playwright, sync_playwright


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page.goto("http://www.deccanchronicle.com/")
    page.get_by_role("list").filter(
        has_text="NationSouthWorldEntertainmentJobsSportsTechnologyLifestyleGallery More... Busine"
        ).get_by_role("link", name="Nation").click()
    page.get_by_role("link", name="Technology").click()
    page.get_by_role(
        "link", name="Micro-blogging platform Twitter has finally made its Blue subscription available for purchase via the Android app. Android users can now get Twitter Blue subscriptions Custom app icons, easier navigation of bookmarked tweets, aligned in folders, and the app can have a different theme are also available").click()
    page.locator("#storyBody").get_by_role("link", name="Technology").click()
    page.get_by_role("link", name="Hyderabad residents are enthused by the launch of 5G services, despite it being available only on a handful of phones and in select pockets. (Representational image: PTI) Hyderabad residents enthused by launch of 5G services").click()
    page.locator("p > a").first.click()
    page.get_by_role("link", name="Corporate Insolvency Resolution Process").click()
    page.get_by_role("link", name="Technology").click()
    page.goto("https://www.deccanchronicle.com/nation/in-other-news/220123/whatsapp-users-sceptical-of-latest-update.html")
    page.get_by_role("link", name="Reliance Digital is offering discouts on purchases made through debit and credit cards till January 29. (Photo: Twitter) Reliance Digital offers Rs 20K discount on purchases through cards").click()
    page.locator(".col-lg-12 > div:nth-child(4)").click()
    page.locator("p > a").first.click()
    context.tracing.stop(path="trace10.zip")


with sync_playwright() as playwright:
    test_run(playwright)
