from playwright.sync_api import sync_playwright, Playwright


def test_run(playwright: Playwright):
    browser = playwright.chromium.launch(headless=False)
    # context = browser.new_context(
    #     record_video_dir="../videos",
    #     record_video_size={"width": 640, "height": 480})
    context = browser.new_context()
    page = context.new_page()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page.goto("https://testingbot.com/")
    page.get_by_role("link", name="Start a free trail").click()
    page.wait_for_timeout(5000)
    context.tracing.stop(path="trace19.zip")

with sync_playwright() as playwright:
    test_run(playwright)

