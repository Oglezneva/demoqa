from pages.base_page import BasePage
from components.components import WebElements


class DropPable(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/droppable/'
        super().__init__(driver, self.base_url)

        self.drag = WebElements(driver, '#draggable')
        self.drop = WebElements(driver, '#droppable')
