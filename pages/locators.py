from selenium.webdriver.common.by import By

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_FORM_EMAIL = (By.CSS_SELECTOR, "#register_form input[type='email']")
    REGISTER_FORM_PASSWORD = (By.CSS_SELECTOR, "#register_form input[name='registration-password1']")
    REGISTER_FORM_PASSWORD_CONF = (By.CSS_SELECTOR, "#register_form input[name='registration-password2']")
    BUTTON_SUBMIT_REGISTER = (By.CSS_SELECTOR, "button[name='registration_submit']")

class ProductPageLocators():
    BUTTON_ADD_TO_BASKET = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_ADDED_TO_BASKET = (By.CSS_SELECTOR, "div.alertinner strong")
    MESSAGE_ADDED_TO_BASKET = (By.CSS_SELECTOR, "div.alertinner")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    BASKET_PRICE = (By.CSS_SELECTOR, ".basket-mini")

class BasketPageLocators():
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "div.content p")
    BASKET_ITEMS = (By.CSS_SELECTOR, "div.basket-items")

class PageWithHeaderLocators():
    LINK_VIEW_BASKET = (By.CSS_SELECTOR, "div .basket-mini a.btn.btn-default")
