from pages.webtables import WebTables


def test_sort(browser):
    web_tables = WebTables(browser)

    web_tables.visit()
    web_tables.header_first_name.click()
    assert web_tables.header_first_name.get_dom_attribute("class") == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'
    web_tables.header_first_name.click()
    assert web_tables.header_first_name.get_dom_attribute("class") == 'rt-th rt-resizable-header -sort-desc -cursor-pointer'

