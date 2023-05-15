from pages.welcome import WelCome
from pages.remote_elements import RemoteElements


def test_icon_exist(browser):
    welcome = WelCome(browser)
    remote_elements = RemoteElements(browser)

    welcome.visit()
    assert welcome.href.exist()

    welcome.href.click()
    assert remote_elements.equal_url()

    remote_elements.btn_add.exist()
    assert remote_elements.btn_add.get_dom_attribute("onclick") == 'addElement()'
    remote_elements.btn_add.click(4)
    assert remote_elements.btn_delete.check_count_elements(4)
    for element in remote_elements.btn_delete.find_elements():
        assert element.text == 'Delete'
    remote_elements.btn_delete.click(4)
    assert not remote_elements.btn_delete.exist()


#клик пока кнопка есть
# while remote_elements.btn_delete.exist():
#     remote_elements.btn_delete.click()
#
#     assert not remote_elements.btn_delete.exist()