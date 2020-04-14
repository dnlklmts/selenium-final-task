from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_product_page_url()

    def add_product_to_basket(self):
        self.should_be_add_to_basket_button()
        self.add_to_basket()

    def check_success_message(self):
        self.should_be_success_message()
        self.should_be_title_in_success_msg()
        self.should_be_correct_title()

    def check_basket_info_message(self):
        self.should_be_basket_info_msg()
        self.should_be_total_cost_in_basket_info_msg()
        self.should_be_correct_price()

    def should_be_product_page_url(self):
        assert 'catalogue' in self.browser.current_url, (
                'This is not product page')

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BTN), (
                'There is no "Add to basket" button on the page')

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MSG), (
                'Success message is presented, but should not be')

    def add_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BTN)
        add_to_basket_btn.click()

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MSG), (
                'There is no success message after add product to basket')

    def should_be_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MSG), (
                'Success message is presented, but should be disappeared')

    def should_be_title_in_success_msg(self):
        assert self.is_element_present(*ProductPageLocators.TITLE_IN_MSG), (
                'There is no title in success message on the page')

    def should_be_correct_title(self):
        title_in_msg = self.browser.find_element(*ProductPageLocators.TITLE_IN_MSG).text
        correct_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE).text
        assert correct_title == title_in_msg, (
                'The product title is different from added item')

    def should_be_basket_info_msg(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_TOTAL_MSG), (
                'There is no basket total info')

    def should_be_total_cost_in_basket_info_msg(self):
        assert self.is_element_present(*ProductPageLocators.TOTAL_COST), (
                'There is no total cost in basket info message')

    def should_be_correct_price(self):
        total_cost = self.browser.find_element(*ProductPageLocators.TOTAL_COST).text[1:]
        correct_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text[1:]
        assert float(correct_price) == float(total_cost), (
                'The total cost is different from price of added product')
