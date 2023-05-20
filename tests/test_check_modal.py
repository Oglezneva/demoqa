from pages.modal_dialogs import ModalDialogs
import requests


def test_check_modal(browser):
    modal_page = ModalDialogs(browser)
    modal_page.requests()

    modal_page.visit()
    assert modal_page.btn_small_modal.exist()
    assert modal_page.btn_large_modal.exist()

    modal_page.btn_small_modal.click()
    assert modal_page.small_modal.exist()
    assert modal_page.btn_close_after_small.exist()
    modal_page.btn_close_after_small.click()
    assert not modal_page.small_modal.exist()

    modal_page.btn_large_modal.click()
    assert modal_page.large_modal.exist()
    assert modal_page.btn_close_after_large.exist()
    modal_page.btn_close_after_large.click()
    assert not modal_page.large_modal.exist()


