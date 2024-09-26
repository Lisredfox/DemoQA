import time

from pages.progress_bar import ProgressBar

def test_progress_bar(browser):
    page = ProgressBar(browser)

    page.visit()
    time.sleep(2)

    page.start_btn.click()

    while True:
        if page.progressbar.get_dom_attribute("aria-valuenow") == "51":
            page.start_btn.click()
            break

    time.sleep(2)