from pages.webtables import WebTables


def test_registration_form(browser):
    web_tables = WebTables(browser)

    web_tables.visit()
    assert web_tables.btn_add.exist()
    web_tables.btn_add.click()
    assert web_tables.modal_content.exist()
    web_tables.btn_submit.click()
    assert web_tables.modal_content.exist()
    web_tables.first_name.send_keys('Alena')
    web_tables.last_name.send_keys('Oglezneva')
    web_tables.email.send_keys('oglezneva@yahoo.com')
    web_tables.age.send_keys('29')
    web_tables.salary.send_keys('3000')
    web_tables.department.send_keys('development')
    web_tables.btn_submit.click()
    assert web_tables.new_first_name.get_text() == 'Alena'
    web_tables.pencil.click()
    assert web_tables.modal_content.exist()
    web_tables.first_name.clear()
    web_tables.first_name.send_keys('Maria')
    web_tables.btn_submit.click()
    assert web_tables.new_first_name.get_text() == 'Maria'
    web_tables.delete.click()
    assert not web_tables.new_first_name.get_text() == 'Alena'


def
