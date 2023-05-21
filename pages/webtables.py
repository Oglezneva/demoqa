from pages.base_page import BasePage
from components.components import WebElements


class WebTables(BasePage):

    def __init__(self, driver):
        self.base_url = 'https://demoqa.com/webtables'
        super().__init__(driver, self.base_url)
        self.rows = WebElements(driver, 'div.rt-noData')
        self.btn_delete = WebElements(driver, 'span[title="Delete"]')
        self.btn_add = WebElements(driver, '#addNewRecordButton')
        self.modal_content = WebElements(driver, 'body > div.fade.modal.show > div > div')
        self.btn_submit = WebElements(driver, '#submit')
        self.first_name = WebElements(driver, '#firstName')
        self.last_name = WebElements(driver, '#lastName')
        self.email = WebElements(driver, '#userEmail')
        self.age = WebElements(driver, '#age')
        self.salary = WebElements(driver, '#salary')
        self.department = WebElements(driver, '#department')
        self.new_first_name = WebElements(driver, 'div.rt-tbody > div:nth-child(4) > div > div:nth-child(4)')
        self.pencil = WebElements(driver, '#edit-record-4 > svg > path')
        self.delete = WebElements(driver, '#delete-record-4 > svg > path')
        self.rows = WebElements(driver, 'div.pagination-bottom span.select-wrap.-pageSizeOptions > select')
        self.pagination_option_5 = WebElements(driver, '.pagination-bottom select option[value="5"]')

        self.header_first_name = WebElements(driver, 'div.rt-th.rt-resizable-header.-sort-desc.-cursor-pointer')
        self.header_last_name = WebElements(driver, '#app div > div:nth-child(2) > div.rt-resizable-header-content')
        self.header_age = WebElements(driver, '#app div > div:nth-child(3) > div.rt-resizable-header-content')
        self.header_email = WebElements(driver, 'div > div:nth-child(4) > div.rt-resizable-header-content')
        self.header_salary = WebElements(driver, 'div > div:nth-child(5) > div.rt-resizable-header-content')
        self.header_department = WebElements(driver, 'div > div:nth-child(6) > div.rt-resizable-header-content')