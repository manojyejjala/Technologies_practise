
def test_run(page):
    # browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context()
    # page = context.new_page()
    page.goto("https://indianexpress.com/")
    page.get_by_role("banner").get_by_text("Trending").click()
    page.get_by_role("banner").get_by_text("Trending").click()
    page.get_by_role("listitem").filter(has_text="Trending").click()
    with page.expect_popup() as page1_info:
        page.locator("#navbar").get_by_role("link", name="Technology").click()
    page1 = page1_info.value
    page1.get_by_text("Sundar Pichai on Google layoffs: Take full responsibility for decisions that led").click()

    # ---------------------
    # context.close()
    # browser.close()

