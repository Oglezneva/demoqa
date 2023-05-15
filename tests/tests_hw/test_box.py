import time

from pages.test_box import TextBox
from pages.form_page import FormPage


def test_box(browser):
    test_full_name = 'John Doe'
    test_address = 'Saint-Petersburg'
    expected_full_name = 'Name:' + test_full_name
    expected_address = 'Current Address :' + test_address

    textbox = TextBox(browser)
    textbox.visit()
    textbox.full_name.send_keys(test_full_name)
    textbox.current.send_keys(test_address)
    textbox.submit.click()

    assert textbox.full_name_output.get_text() == expected_full_name
    assert textbox.address_output.get_text() == expected_address


def test_placeholder(browser):
    form_page = FormPage(browser)

    form_page.visit()
    assert form_page.first_name.get_dom_attribute("placeholder") == 'First Name'
    assert form_page.last_name.get_dom_attribute("placeholder") == 'Last Name'


def test_state_2(browser):
    form_page = FormPage(browser)
    form_page.visit()
    time.sleep(2)
    form_page
