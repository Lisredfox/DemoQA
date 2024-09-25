from pages.webtables_page import WebTables
import time

def test_tables(browser):
    web_tables = WebTables(browser)

    web_tables.visit()
    assert not web_tables.no_rows_found.exist()

    while web_tables.delete_button.exist():
        web_tables.delete_button.click()

    time.sleep(2)
    assert web_tables.no_rows_found.exist()