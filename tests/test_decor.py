import time
from functools import reduce

import pytest
from pages.demoqa import DemoQa
from pages.radio import Radio


@pytest.mark.skip
def test_decor(browser):
    demo = DemoQa(browser)

    demo.visit()
    assert demo.h5.check_count_elements(6)

    for element in demo.h5.find_elements():
        assert element.text != ''


@pytest.mark.skipif(False, reason="просто пропуск")
def test_decor_1(browser):
    radio = Radio(browser)

    radio.visit()
    radio.yes.click()
    assert radio.text_check.get_text() == 'Yes'
    time.sleep(2)

    radio.impressive.click()
    assert radio.text_check.get_text() == 'Impressive'

    assert 'disabled' in radio.no.get_dom_attribute('class')