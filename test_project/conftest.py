import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            record_video_dir="../videos",
            record_video_size={"width": 640, "height": 480})
        page = context.new_page()
        yield page
        context.close()
