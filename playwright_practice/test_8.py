
def test_run(page):
    page.goto("https://timesofindia.indiatimes.com/")
    page.get_by_role("button", name="Maybe later").click()
    page.get_by_role("link", name="Over 50 injured in 3 jallikattu events in Trichy Over 50 injured in 3 jallikattu events in Trichy").click()
    with page.expect_popup() as page1_info:
        page.frame_locator("#ifr_504001-197157848").get_by_role("link", name="Live: 19 hurt during Jallikattu event in TN Times of India").click()
    page1 = page1_info.value
    page1.get_by_role("img", name="Tamil Nadu | 19 people were injured in Avaniyapuram Jallikattu event and 11 people were referred to Government Rajaji Hospital in Madurai for further treatment: Revenue department").click()

