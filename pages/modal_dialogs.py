from pages.base_page import BasePage
from components.components import WebElements


class ModalDialogs(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/modal-dialogs'
        super().__init__(driver, self.base_url)

        self.btns_third_menu = WebElements(driver, 'div:nth-child(3) > div > ul > li')
        self.main_icon = WebElements(driver, '#app > header > a > img')
        self.btn_small_modal = WebElements(driver, '#showSmallModal')
        self.small_modal = WebElements(driver, 'body > div.fade.modal.show > div > div > div.modal-header')
        self.btn_close_after_small = WebElements(driver, '#closeSmallModal')
        self.btn_large_modal = WebElements(driver, '#showLargeModal')
        self.large_modal = WebElements(driver, 'body > div.fade.modal.show > div > div > div.modal-header')
        self.btn_close_after_large = WebElements(driver, '#closeLargeModal')


