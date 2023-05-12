from pages.test_box import TextBox


def test_placeholder(browser):
    textbox = TextBox(browser)

    textbox.visit()
    assert textbox.full_name.get_dom_attribute("placeholder") == 'Full Name'



