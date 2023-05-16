import time

from pages.webtables import WebTables


def test_webtables(browser):
    web_tables = WebTables(browser)

    web_tables.visit()

    assert not web_tables.rows.exist()

    while web_tables.btn_delete.exist():
        web_tables.btn_delete.click()
    time.sleep(3)
    assert web_tables.rows.exist()



