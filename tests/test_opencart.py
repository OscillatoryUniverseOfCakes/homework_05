from page_classes.login_admin_page import LoginAdminPage
from page_classes.product_page import ProductPage
from page_classes.desktop_page import DesktopPage
from page_classes.index_page import IndexPage
from page_classes.register_page import RegisterPage

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_login_page(browser, base_url):
    browser.get(base_url + "admin")
    browser.find_element(*LoginAdminPage.USERNAME_INPUT)
    browser.find_element(*LoginAdminPage.PASSWORD_INPUT)
    browser.find_element(*LoginAdminPage.SUBMIT_BUTTON)
    browser.find_element(*LoginAdminPage.FORGOTTEN_PASSWORD)
    browser.find_element(*LoginAdminPage.OPENCART_LINK)


def test_product_page(browser, base_url):
    browser.get(base_url + "canon-eos-5d")
    button_cart = browser.find_element(*ProductPage.BUTTON_CART)
    button_cart.click()
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located(ProductPage.FORM_ERROR))
    browser.find_element(*ProductPage.DESCRIPTION)
    browser.find_element(*ProductPage.TITLE)
    browser.find_element(*ProductPage.TITLE)
    browser.find_elements(*ProductPage.TAB)


def test_catalog(browser, base_url):
    browser.get(base_url + "desktops")
    items_list = browser.find_elements(*DesktopPage.LIST_ITEMS)
    assert len(items_list) >= 8
    products = browser.find_elements(*DesktopPage.PROD_CARD)
    assert len(products) <= 15
    browser.find_element(*DesktopPage.CHANGE_VIEW_BUTTON)
    button_wish = browser.find_element(*DesktopPage.ADD_TO_WISH)
    button_wish.click()
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located(DesktopPage.SUCC_ALERT))


def test_main_page(browser, base_url):
    browser.get(base_url)
    browser.find_elements(*IndexPage.SWIPER)
    browser.find_element(*IndexPage.NEXT_PIC_BUTT)
    WebDriverWait(browser, 4).until(EC.visibility_of_element_located(IndexPage.NEXT_PIC))
    browser.find_element(*IndexPage.PROD_ROW)
    promo_row = browser.find_elements(*IndexPage.PROMO_ROW)
    assert len(promo_row) == 13


def test_register_page(browser, base_url):
    browser.get(base_url + 'index.php?route=account/register')
    browser.find_element(*RegisterPage.FIRST_NAME)
    browser.find_element(*RegisterPage.LAST_NAME)
    browser.find_element(*RegisterPage.EMAIL)
    browser.find_element(*RegisterPage.PHONE)
    browser.find_element(*RegisterPage.PASS)
    browser.find_element(*RegisterPage.PASS_AGAIN)
    submit = browser.find_element(*RegisterPage.BUTT)
    submit.click()
    WebDriverWait(browser, 3).until(EC.visibility_of_element_located(RegisterPage.ERROR))
