from selenium.webdriver.common.by import By


class IndexPage:
    SWIPER = (By.CSS_SELECTOR, '#slideshow0')
    NEXT_PIC_BUTT = (By.CSS_SELECTOR, '#content > div.slideshow.swiper-viewport > div.swiper-pagination.slideshow0'
                                      '.swiper-pagination-clickable.swiper-pagination-bullets > '
                                      'span.swiper-pagination-bullet.swiper-pagination-bullet-active')
    NEXT_PIC = (By.CSS_SELECTOR, '#slideshow0 > div > div.swiper-slide.text-center.swiper-slide-active > img')
    PROD_ROW = (By.CSS_SELECTOR, '#slideshow0 > div')
    PROMO_ROW = (By.CSS_SELECTOR, '.swiper-pagination-bullet')
