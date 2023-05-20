import time
from pages.alerts import Alert


def test_alert(browser):
    alerts = Alert(browser)

    alerts.visit()
    assert not alerts.alert()

    alerts.btn_alert.click()
    time.sleep(2)
    assert alerts.alert()
    alerts.alert().accept()


def test_alert_text(browser):
    alerts = Alert(browser)

    alerts.visit()
    alerts.btn_alert.click()
    time.sleep(2)

    assert alerts.alert().text == 'You clicked a button'
    alerts.alert().accept()
    assert not alerts.alert()


def test_confirm(browser):
    alerts = Alert(browser)

    alerts.visit()
    alerts.btn_confirm.click()
    time.sleep(2)
    alerts.alert().dismiss()
    assert alerts.blok.get_text() == 'You selected Cancel'


def test_prompt(browser):
    alerts = Alert(browser)
    name = 'John Doe'
    pass_name = 'You entered ' + name

    alerts.visit()
    alerts.btn_prom.click()
    time.sleep(2)
    alerts.alert().send_keys(name)
    alerts.alert().accept()
    assert alerts.prompt_result.get_text() == pass_name
    time.sleep(2)

