from pages.accordion import Accordion
import time


def test_visible_accordion(browser):
    accordion_page = Accordion(browser)

    accordion_page.visit()
    assert accordion_page.content_first.visible()
    accordion_page.btn_section_first.click()
    time.sleep(2)
    assert not accordion_page.content_first.visible()


def test_visible_accordion_default(browser):
    accordion_page = Accordion(browser)

    accordion_page.visit()
    assert not accordion_page.content_second.visible()
    assert not accordion_page.content_second_part2.visible()
    assert not accordion_page.content_third.visible()
