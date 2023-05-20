import time

from pages.droppable import DropPable
from selenium.webdriver import ActionChains


def test_droppable(browser):
    droppable_page = DropPable(browser)
    action_chains = ActionChains(browser)

    droppable_page.visit()
    assert not droppable_page.drop.check_css('backgroundColor', 'rgba(70, 130, 180, 1)')
    action_chains.drag_and_drop(
        droppable_page.drag.find_element(),
        droppable_page.drop.find_element()).perform()
    time.sleep(1)
    assert droppable_page.drop.check_css('backgroundColor', 'rgba(70, 130, 180, 1)')

    action_chains.drag_and_drop_by_offset(
        droppable_page.drag.find_element(), -200, 0)
    action_chains.perform()










