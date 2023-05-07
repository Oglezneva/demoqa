from pages.base_page import BasePage
from components.components import WebElements


class Accordion(BasePage):
    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/accordian'
        super().__init__(driver, self.base_url)

        self.content_first = WebElements(driver, '#section1Content > p')
        self.btn_section_first = WebElements(driver, '#section1Heading')
        self.content_second = WebElements(driver, '#section2Content > p:nth-child(1)')
        self.content_second_part2 = WebElements(driver, '#section2Content > p:nth-child(2)')
        self.content_third = WebElements(driver, '#section3Content > p')
