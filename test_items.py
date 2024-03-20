from selenium.webdriver.common.by import By
import time

def test_add_to_cart_button_is_displayed(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207"
    print("\nstart browser for test..")
    browser.get(link)
    time.sleep(30)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-lg.btn-primary.btn-add-to-basket") 
    assert button, 'Button not found!'
