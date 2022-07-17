from selenium.webdriver.common.by import By


class RegisterPage:
    FIRST_NAME = (By.CSS_SELECTOR, '#input-firstname')
    LAST_NAME = (By.CSS_SELECTOR, '#input-lastname')
    EMAIL = (By.CSS_SELECTOR, '#input-email')
    PHONE = (By.CSS_SELECTOR, '#input-telephone')
    PASS = (By.CSS_SELECTOR, '#input-password')
    PASS_AGAIN = (By.CSS_SELECTOR, '#input-confirm')
    BUTT = (By.CSS_SELECTOR, '#content > form > div > div > input.btn.btn-primary')
    ERROR = (By.CSS_SELECTOR, '#account-register > div.alert.alert-danger.alert-dismissible')
