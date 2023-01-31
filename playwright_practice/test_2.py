# import pytest
# from playwright.sync_api import sync_playwright


def test_google(page):
    page.goto('https://google.com')
    page.get_by_role('combobox').fill('geekforgeek')
    page.keyboard.press('Enter')
    page.get_by_role('combobox').click()
    geek = page.query_selector_all('.text')
    print(geek)
    page.wait_for_timeout(10000)
    


