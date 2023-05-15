from pages.base_page import BasePage
from components.components import WebElements


class TextBox(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/text-box'
        super().__init__(driver, self.base_url)

        self.full_name = WebElements(driver, '#userName')
        self.current = WebElements(driver, '#currentAddress-wrapper #currentAddress')
        self.submit = WebElements(driver, '#submit')
        self.full_name_output = WebElements(driver, '#name')
        self.address_output = WebElements(driver, '#output #currentAddress')
