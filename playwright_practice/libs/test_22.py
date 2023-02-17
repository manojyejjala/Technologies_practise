from playwright.sync_api import Playwright


def test_run(playwright: Playwright):
    try:
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
        page.locator("#duckbar_static").get_by_role(
            "link", name="Images").click()
        page.locator("#duckbar_static").get_by_role("link", name="All").click()
        page.get_by_role(
            "link", name="Giant Panda | National Geographic - Animals").click()
        page.goto("https://duckduckgo.com/?va=t&t=he&q=panda&ia=web")
        page.get_by_role(
            "link", name="Giant panda - Wikipedia").click()
        page.goto("https://duckduckgo.com/?va=t&t=he&q=panda&ia=web")
        page.get_by_role(
            "link", name="Red panda's San Diego Zoo escape accomplished by climbing tree").click()
        page.goto("https://duckduckgo.com/?va=t&t=he&q=panda&ia=web")
        page.get_by_role(
            "link", name="Top 10 facts about Pandas | WWF").click()
        page.goto("https://duckduckgo.com/?va=t&t=he&q=panda&ia=web")
        page.get_by_role(
            "link", name="Panda Express - An American Chinese Restaurant").click()
        page.wait_for_timeout(5000)
    except Exception as e:
        print(e)


# with sync_playwright() as playwright:
#   test_run(playwright)
