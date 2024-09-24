from components.components import WebElement
import time
from pages.text_box import TextBox

def test_text_box(browser):
    text_box = TextBox(browser)

    text_box.visit()
    text_box.name.send_keys('Marina')
    text_box.current_address.send_keys('Nevskiy Str')
    text_box.submit_btn.click_force()
    time.sleep(2)
    assert text_box.name_2.exist()
    assert text_box.current_address.exist()