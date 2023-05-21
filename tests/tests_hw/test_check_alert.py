import time
from pages.alerts import Alert


def test_check_alert(browser):
    alerts_page = Alert(browser)

    alerts_page.visit()
    assert alerts_page.timer_alert_button.exist()
    alerts_page.timer_alert_button.click()
    time.sleep(5)
    alerts_page.alert()
