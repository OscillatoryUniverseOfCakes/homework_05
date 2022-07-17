from selenium.webdriver.common.by import By


class DesktopPage:
    LIST_ITEMS = (By.CSS_SELECTOR, '#column-left > div.list-group > a.list-group-item')
    PROD_CARD = (By.CSS_SELECTOR, '.product-layout product-grid col-lg-4 col-md-4 col-sm-6 col-xs-12')
    CHANGE_VIEW_BUTTON = (By.CSS_SELECTOR, '#list-view')
    ADD_TO_WISH = (By.CSS_SELECTOR,
                   '#content > div:nth-child(7) > div:nth-child(1) > div > div:nth-child(2) > div.button-group '
                   '> button:nth-child(2)')
    SUCC_ALERT = (By.CSS_SELECTOR, '#product-category > div.alert.alert-success')
