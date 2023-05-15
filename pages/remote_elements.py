from pages.base_page import BasePage
from components.components import WebElements


class RemoteElements(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://the-internet.herokuapp.com/add_remove_elements/'
        super().__init__(driver, self.base_url)

        self.btn_add = WebElements(driver, '#content > div > button')
        self.btn_delete = WebElements(driver, '#elements > button')
