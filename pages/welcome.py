from pages.base_page import BasePage
from components.components import WebElements


class WelCome(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://the-internet.herokuapp.com/'
        super().__init__(driver, self.base_url)

        self.href = WebElements(driver, '#content > ul > li:nth-child(2) > a')
