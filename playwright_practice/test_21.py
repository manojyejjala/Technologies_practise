from playwright.sync_api import sync_playwright, Playwright


def test_run(playwright: Playwright) -> None:
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
    page.goto("https://duckduckgo.com/?va=t&t=hf&q=panda&ia=web")
    page.get_by_role("link", name="Giant panda - Wikipedia").click()
    page.get_by_role("navigation", name="Contents").get_by_role(
        "link", name="Classification").click()
    page.get_by_role("link", name="Olfactory communication").click()
    page.get_by_role("link", name="Human use and interaction").click()
    page.wait_for_timeout(5000)
    context.tracing.stop(path='trace_21.zip')


with sync_playwright() as playwright:
    test_run(playwright)
