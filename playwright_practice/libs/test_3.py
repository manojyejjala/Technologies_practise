


def test_run(page):
    page.goto("https://www.google.com/")
    page.get_by_role("combobox", name="Search").click()
    page.get_by_role("combobox", name="Search").fill("geek for geeks")
    page.get_by_role("combobox", name="Search").press("Enter")
    page.get_by_text("results")

    

