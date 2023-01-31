from playwright.sync_api import Playwright, sync_playwright


def test_run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    context.tracing.start(screenshots=True, snapshots=True, sources=True)
    page.goto("https://www.deccanherald.com/")
    page.locator("#hdr_hori_menu").get_by_role("link", name="Cricket").click()
    page.get_by_role("link", name="Unless injured, key players to compete in IPL: Dravid Unless injured, key players to compete in IPL: Dravid... 23rd Jan 2023").click()
    page.locator("#topmenu").get_by_role("link", name="Home").click()
    page.locator("#home-more-top-stories-and-dh-videos").get_by_role("link", name="Biden's secret documents: the drip, drip of revelations Biden's secret documents: the drip, drip of revelations... 2 hrs ago").click()
    page.locator("#topmenu").get_by_role("link", name="Home").click()
    page.locator("#hdr_hori_menu").get_by_role("link", name="Home").click()
    page.locator("#hdr_hori_menu").get_by_role("link", name="Home").click()
    page.get_by_role("link", name="Constant Russian shelling and attacks: Zelenskyy Constant Russian shelling and attacks: Zelenskyy 4:06 am").click()
    page.goto("https://www.deccanherald.com/international/world-news-politics/power-restoration-underway-in-pakistan-nationwide-outage-govt-says-1184022.html")
    page.get_by_role("link", name="Elon Musk testifies in 2nd day of Tesla tweet trial Elon Musk testifies in 2nd day of Tesla tweet... 1:35 am").click()
    page.goto("https://www.deccanherald.com/international/world-news-politics/who-wants-all-substandard-medicines-removed-from-market-1183982.html")
    page.goto("https://www.deccanherald.com/international/world-news-politics/elon-musk-testifies-in-2nd-day-of-tesla-tweet-trial-1184020.html")
    page.get_by_role("link", name="Sunak orders probe into tax scandal-hit Tory chief Sunak orders probe into tax scandal-hit Tory chief... 23rd Jan 2023").click()
    page.goto("https://www.deccanherald.com/international/world-news-politics/maldives-supports-indias-candidature-for-unsc-non-permanent-membership-1183881.html")
    page.get_by_role("link", name="Russia's Lavrov says fight with West 'almost real war' Russia's Lavrov says fight with West 'almost real war'... 23rd Jan 2023").click()
    page.goto("https://www.deccanherald.com/international/world-news-politics/musk-to-return-to-stand-in-fraud-trial-over-2018-tesla-tweet-1183842.html")
    page.goto("https://www.deccanherald.com/international/world-news-politics/russias-lavrov-says-conflict-with-west-almost-a-real-war-1183862.html")
    page.goto("https://www.deccanherald.com/international/world-news-politics/musk-to-return-to-stand-in-fraud-trial-over-2018-tesla-tweet-1183842.html")
    page.get_by_role("link", name="Musk to take stand again in Tesla tweet fraud trial Musk to take stand again in Tesla tweet fraud... 23rd Jan 2023").click()
    page.goto("https://www.deccanherald.com/international/world-news-politics/pakistan-central-bank-raises-key-rate-by-100-bps-to-contain-inflation-1183840.html")
    page.goto("https://www.deccanherald.com/international/world-news-politics/musk-to-return-to-stand-in-fraud-trial-over-2018-tesla-tweet-1183842.html")
    page.locator("#main-wrapper").get_by_role("button", name="Next").click()
    page.locator("#main-wrapper").get_by_role("button", name="Next").click()
    page.get_by_role("link", name="Russia downgrades relations with Estonia, expels envoy Russia downgrades relations with Estonia, expels envoy 23rd Jan 2023").click()
    page.locator("#logo").click()
    context.tracing.stop(path="trace11.zip")


with sync_playwright() as playwright:
    test_run(playwright)







# from playwright.sync_api import Playwright, sync_playwright, expect


# def test_run(playwright: Playwright) -> None:
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     context.tracing.start(screenshots=True, snapshots=True, sources=True)
#     page = context.new_page()
#     page.goto("https://www.deccanherald.com/")
#     page.locator("#hdr_hori_menu").get_by_role("link", name="National").click()
#     page.locator("#national-politics").get_by_role("link", name="Congress to hold pressers to flag BJP govt's failures Congress to hold pressers to flag BJP govt's failures... an hour ago").click()
#     with page.expect_popup() as page1_info:
#         page.get_by_role("link", name="Rahul Gandhi to hoist tricolour in Srinagar to mark end of Bharat Jodo Yatra").click()
#     page1 = page1_info.value
#     context.tracing.stop(path="trace4.zip")


# with sync_playwright() as playwright:
#     test_run(playwright)
