from pages.base_page import BasePage
from components.components import WebElements


class ElementsPage(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/elements'
        super().__init__(driver, self.base_url)

        self.text_element = WebElements(driver, '#app > div > div > div.pattern-backgound.playgound-header')
        self.icon = WebElements(driver, '#app > header >a')
        self.btn_sidebar_first = WebElements(driver, 'div:nth-child(1) > span > div')
        self.btn_sidebar_first_textbox = WebElements(driver, '#item-0')
        self.btn_sidebar_first_checkbox = WebElements(driver, 'div:nth-child(1) > div > ul > #item-1 > span')
        self.btns_first_menu = WebElements(driver, 'div:nth-child(1) > div > ul > li')
