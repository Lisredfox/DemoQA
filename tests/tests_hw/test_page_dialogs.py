import time
from pages.modal_dialogs import ModalDialogs
from conftest import browser

def test_modal_elements(browser):
    modal_dialog_page = ModalDialogs(browser)

    modal_dialog_page.visit()
    assert modal_dialog_page.btns_menu.check_count_elements(count=5)

def test_navigation_modal(browser):
    modal_dialog_page = ModalDialogs(browser)

    modal_dialog_page.visit()
    modal_dialog_page.refresh()
    modal_dialog_page.icon.click()
    modal_dialog_page.back()
    time.sleep(2)
    browser.set_window_size(900, 400)
    modal_dialog_page.forward()
    time.sleep(2)
    assert modal_dialog_page.get_url() == "https://demoqa.com/"
    assert browser.title() == "DEMOQA"
    browser.set_window_size(1000, 1000)
