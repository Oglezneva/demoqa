from pages.base_page import BasePage
from components.components import WebElements


class WebTables(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)
        self.rows = WebElements(driver, 'div.rt-noData')
        self.btn_delete = WebElements(driver, 'span[title="Delete"]')
