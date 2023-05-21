from pages.base_page import BasePage
from components.components import WebElements


class Alert(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/alerts'
        super().__init__(driver, self.base_url)

        self.btn_alert = WebElements(driver, '#alertButton')
        self.btn_confirm = WebElements(driver, '#confirmButton')
        self.blok = WebElements(driver, '#confirmResult')
        self.btn_prom = WebElements(driver, '#promtButton')
        self.prompt_result = WebElements(driver, '#promptResult')
        self.timer_alert_button = WebElements(driver, '#timerAlertButton')
