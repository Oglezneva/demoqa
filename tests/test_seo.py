import time

import pytest
from pages.demoqa import DemoQa
from pages.browser_tab import BrowserPage
from pages.accordion import Accordion
from pages.alerts import Alert


def test_seo(browser):
    demo_qa_page = DemoQa(browser)

    demo_qa_page.visit()
    assert browser.title == demo_qa_page.pageData['title']


@pytest.mark.parametrize('pages', [Accordion, Alert, DemoQa, BrowserPage])
def test_check_title_all_pages(browser, pages):
    page = pages(browser)
    demo_qa_page = DemoQa(browser)

    page.visit()
    time.sleep(2)
    assert browser.title == demo_qa_page.pageData['title']






