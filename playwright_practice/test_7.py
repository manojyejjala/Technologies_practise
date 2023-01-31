def test_run(page):
    page.goto("https://www.hindustantimes.com/")
    page.frame_locator("internal:attr=[title=\"webpush-onsite\"i]").get_by_role("button", name="I'll do this later").click()
    page.locator("#cohort_subnav").get_by_role("link", name="Trending").click()
    page.locator("#dataHolder").get_by_role("link", name="Man fired from Microsoft after working for 21 years shares bittersweet post").click()
    page.get_by_role("list").filter(has_text="Home Latest News India World Cities Entertainment Cricket Lifestyle Astrology Ed").get_by_role("link", name="Cricket").click()
    page.locator("#dataHolder").get_by_role("link", name="'If your Man of the Match is dropped...': Kapil Dev after harsh Suryakumar call").click()



