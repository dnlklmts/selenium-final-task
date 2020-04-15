from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_page_url()

    def should_be_basket_page_url(self):
        assert 'basket' in self.browser.current_url, (
                'This is not basket page')

    def should_not_be_items_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS_LIST), (
                'There are items in the basket, but should not be')

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY_MESSAGE), (
                'There is no message in empty basket')

    def should_be_correct_empty_basket_message(self):
        current_basket_msg = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_MESSAGE).text
        assert 'Your basket is empty.' in current_basket_msg, (
                'There is wrong message in empty basket')
