from pages.base_page import BasePage
from components.components import WebElements


class FormPage(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/automation-practice-form'
        super().__init__(driver, self.base_url)

        self.first_name = WebElements(driver, '#firstName')
        self.last_name = WebElements(driver, '#lastName')
        self.user_email = WebElements(driver, '#userEmail')
        self.gender_radio_1 = WebElements(driver, '#gender-radio-1')
        self.user_number = WebElements(driver, '#userNumber')
        self.btn_submit = WebElements(driver, '#submit')
        self.modal_dialog = WebElements(driver, 'body > div.fade.modal.show > div')
        self.btn_close_modal = WebElements(driver, '#closeLargeModal')
        self.hobbies = WebElements(driver, '#hobbiesWrapper > div.col-md-9.col-sm-12 > div:nth-child(1)')
        self.current_address = WebElements(driver, '#currentAddress')

