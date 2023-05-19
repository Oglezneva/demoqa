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
        #self.new_first_name = WebElements(driver, '#app > div > div > div.row > div.col-12.mt-4.col-md-6 > div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.rt-table > div.rt-tbody > div:nth-child(4) > div > div:nth-child(1)')
        self.new_first_name = WebElements(driver, 'div.rt-tbody > div:nth-child(4) > div > div:nth-child(4)')
        #self.new_first_name = WebElements(driver, 'div:nth-child(3) > div > div:nth-child(4)')
        self.pencil = WebElements(driver, '#edit-record-4 > svg > path')
        self.delete = WebElements(driver, '#delete-record-4 > svg > path')
        self.rows = WebElements(driver, 'div.web-tables-wrapper > div.ReactTable.-striped.-highlight > div.pagination-bottom > div > div.-center > span.select-wrap.-pageSizeOptions > select')
        self.pagination_option_5 = WebElements(driver, '.pagination-bottom select option[value="5"]')
