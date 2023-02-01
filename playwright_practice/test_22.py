from playwright.sync_api import sync_playwright, Playwright


def test_run(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page.goto("https://duckduckgo.com/")
    page.get_by_placeholder("Search the web without being tracked").click()
    page.get_by_placeholder(
        "Search the web without being tracked").fill("panda")
    page.get_by_placeholder(
        "Search the web without being tracked").press("Enter")
    page.locator("#duckbar_static").get_by_role("link", name="Images").click()
    page.locator("#duckbar_static").get_by_role("link", name="All").click()
    page.get_by_role(
        "link", name="Giant Panda | National Geographic - Animals").click()
    page.goto("https://duckduckgo.com/?va=t&t=he&q=panda&ia=web")
    page.get_by_role(
        "link", name="Giant Panda | Facts, Habitants, Population, &Diet | Britannica").click()
    page.wait_for_timeout(5000)


with sync_playwright() as playwright:
    test_run(playwright)
