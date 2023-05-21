from pages.webtables import WebTables


def test_sort(browser):
    web_tables = WebTables(browser)

    web_tables.visit()
    assert web_tables.header_first_name.get_dom_attribute("class") == 'rt-th rt-resizable-header -sort-desc -cursor-pointer'
    web_tables.header_first_name.click()
    assert web_tables.header_first_name.get_dom_attribute("class") == 'rt-th rt-resizable-header -sort-asc -cursor-pointer'



4.	* в файле test_window_tab.py автоматизируйте тест кейс:
a.	Страница https://demoqa.com/links
b.	На странице имеется ссылка “Home”
c.	текст ссылки == “Home”
d.	href ссылки == “https://demoqa.com”
e.	При клике на ссылку открывается новая вкладка
