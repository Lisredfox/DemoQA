from pages.webtables_page import WebTables
import time

def test_webtables(browser):
    webtables = WebTables(browser)
    webtables.visit()

    assert webtables.add_button.exist()
    webtables.add_button.click()
    assert webtables.window.exist()
    webtables.submit_button.click()
    assert webtables.window.exist()
    webtables.first_name.send_keys("Marina")
    webtables.last_name.send_keys("Galeeva")
    webtables.email.send_keys("mary@mail.ru")
    webtables.age.send_keys("25")
    webtables.salary.send_keys("123")
    webtables.department.send_keys("StPetersburg")
    webtables.submit_button.click_force()
    assert not webtables.window.exist()
    assert webtables.record.exist()
    webtables.edit_record_button.click()
    assert webtables.window.exist()
    webtables.first_name.clear()
    webtables.first_name.send_keys("Sasha")
    webtables.submit_button.click()
    time.sleep(2)
    webtables.delete_button_2.click_force()
    time.sleep(2)