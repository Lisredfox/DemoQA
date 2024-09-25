from pages.webtables_page import WebTables
import time

def test_sort(browser):
    webtable = WebTables(browser)
    webtable.visit()

    for element in webtable.header_resize.find_elements():
        time.sleep(2)
        element.click()
        assert element.get_dom_attribute("class") == "rt-th rt-resizable-header -sort-asc -cursor-pointer"
        time.sleep(2)
    time.sleep(5)