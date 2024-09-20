from pages.accordion import Accordion
import time

def test_visible_accordion(browser):
    elements_page = Accordion(browser)

    elements_page.visit()
    assert elements_page.element.visible()
    elements_page.element_section1.click()
    time.sleep(2)
    assert not elements_page.element_section1_check.visible()

def test_visible_accordion_default(browser):
    elements_page = Accordion(browser)

    elements_page.visit()
    assert not elements_page.element_section2_child1.visible()
    assert not elements_page.element_section2_child2.visible()
    assert not elements_page.element_section3.visible()