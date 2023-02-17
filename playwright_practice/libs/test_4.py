def test_run(page):
    

    page.goto("https://www.google.com/")
    page.get_by_role("combobox", name="Search").fill("apple")
    page.keyboard.press("Enter")
    page.close()
    

