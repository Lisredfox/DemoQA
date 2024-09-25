from pages.koup import Koup
from pages.koup_add import KoupAdd

def test_koup_add(browser):
    koup_page = Koup(browser)
    koup_add = KoupAdd(browser)
    koup_page.visit()

    assert koup_page.remove_elements.get_text() == 'Add/Remove Elements'
    koup_page.remove_elements.click()

    assert koup_add.add_element.get_text() == 'Add Element'

    assert koup_add.add_element.get_dom_attribute("onclick") == "addElement()"

    koup_add.add_element.click_x(4)
    assert koup_add.delete_btns.check_count_elements(4)
    for element in koup_add.delete_btns.find_elements():
        assert element.text == "Delete"
    while koup_add.delete_btns.exist():
        koup_add.delete_btns.click()
    assert not koup_add.delete_btns.exist()