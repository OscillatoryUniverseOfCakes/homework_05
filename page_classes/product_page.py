from selenium.webdriver.common.by import By


class ProductPage:
    BUTTON_CART = (By.CSS_SELECTOR, '#button-cart')
    FORM_ERROR = (By.CSS_SELECTOR, '#product > div.form-group.required.has-error')
    DESCRIPTION = (By.CSS_SELECTOR, '.text-danger')
    TITLE = (By.CSS_SELECTOR, '#content > div > div.col-sm-4 > h1')
    TAB = (By.CSS_SELECTOR, '#content > div > div.col-sm-8 > ul.nav.nav-tabs')
