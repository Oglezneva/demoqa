from pages.demoqa import DemoQa
from pages.elements_page import ElementsPage


def test_footer(browser):
    demo_qa_page = DemoQa(browser)

    demo_qa_page.visit()
    assert demo_qa_page.footer.get_text() == '© 2013-2020 TOOLSQA.COM | ALL RIGHTS RESERVED.'


def test_check_center_text(browser):
    demo_qa_page = DemoQa(browser)

    demo_qa_page.btn_elements.click()
    assert demo_qa_page.lead.get_text() == 'Please select an item from left to start practice.'


def test_page_elements(browser):
    element = ElementsPage(browser)

    element.visit()
    assert element.text_element.get_text() == 'Elements'
    assert element.icon.exist()
    assert element.btn_sidebar_first.exist()
    assert element.btn_sidebar_first_textbox.exist()

