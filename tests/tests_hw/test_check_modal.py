from pages.modal_dialogs import ModalDialogs
import time

def test_check_modal(browser):
    modal_dialogs = ModalDialogs(browser)

    modal_dialogs.visit()
    assert modal_dialogs.smallmodal_btn.exist()
    assert modal_dialogs.largemodal_btn.exist()
    modal_dialogs.smallmodal_btn.click()
    assert modal_dialogs.smallmodal_btn.exist()
    time.sleep(2)
    assert modal_dialogs.closeSmallmodal.exist()
    modal_dialogs.closeSmallmodal.click()
    time.sleep(2)
    assert not modal_dialogs.smallmodal.exist()
    modal_dialogs.largemodal_btn.click()
    assert modal_dialogs.closeLargemodal.exist()
    assert modal_dialogs.smallmodal.exist()
    modal_dialogs.closeLargemodal.click()
    assert not modal_dialogs.smallmodal.exist()