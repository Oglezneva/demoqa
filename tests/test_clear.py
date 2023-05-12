import time
from pages.test_box import TextBox


def test_clear(browser):
    textbox = TextBox(browser)

    textbox.visit()
    textbox.full_name.send_keys('TestTest')
    time.sleep(2)
    textbox.full_name.clear()
    time.sleep(2)
    assert textbox.full_name.get_text() == ''

