from pages.links import Links


def test_window_tab(browser):
    links_page = Links(browser)

    links_page.visit()
    assert links_page.btn_home.exist()
    assert links_page.btn_home.get_text() == 'Home'
    assert links_page.btn_home.get_dom_attribute('href') == 'https://demoqa.com'
    assert links_page.btn_home.get_dom_attribute('target') == '_blank'

    links_page.btn_home.click()
    browser.switch_to.window(browser.window_handles[1])
