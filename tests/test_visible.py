from pages.elements_page import ElementsPage
import time


def test_visible_btn_sidebar(browser):
    element = ElementsPage(browser)

    element.visit()
    #element.btn_sidebar_first.click()
   #time.sleep(3)
    #assert element.btn_sidebar_first_textbox.exist()
    assert element.btn_sidebar_first_textbox.visible()


def test_not_visible_btn_sidebar(browser):
    element = ElementsPage(browser)

    element.visit()
    assert element.btn_sidebar_first_checkbox.visible()
    element.btn_sidebar_first.click()
    time.sleep(2)
    assert not element.btn_sidebar_first_textbox.visible()
