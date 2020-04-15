from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, '#login_link')
    BASKET_LINK = (By.CSS_SELECTOR, 'div.basket-mini a')


class LoginPageLocators():
    REG_FORM = (By.ID, 'register_form')
    LOGIN_FORM = (By.ID, 'login_form')


class ProductPageLocators():
    ADD_TO_BASKET_BTN = (By.CLASS_NAME, 'btn-add-to-basket')
    PRODUCT_TITLE = (By.TAG_NAME, 'h1')
    PRODUCT_PRICE = (By.CSS_SELECTOR, 'p.price_color')
    SUCCESS_MSG = (By.CLASS_NAME, 'alert-success')
    TITLE_IN_MSG = (By.CSS_SELECTOR, '.alert-success strong')
    BASKET_TOTAL_MSG = (By.CLASS_NAME, 'alert-info')
    TOTAL_COST = (By.CSS_SELECTOR, '.alert-info strong')


class BasketPageLocators():
    BASKET_EMPTY_MESSAGE = (By.CSS_SELECTOR, 'div#content_inner > p')
    BASKET_ITEMS_LIST = (By.CSS_SELECTOR, 'div.basket-items')
