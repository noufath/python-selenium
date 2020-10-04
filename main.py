import os
import time

from selenium import webdriver
from selenium.webdriver.common import actions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as exp_cond
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


WAIT_TIME = 20
email = ''
passwd = ''

driver = webdriver.Chrome(executable_path=os.path.abspath('chromedriver.exe'))
driver.get('https://stackoverflow.com/users/login?ssrc=head&returnurl=https%3a%2f%2fstackoverflow.com%2f')

# Use this code if login using gmail account

# driver.find_element_by_css_selector('.grid--cell.s-btn.s-btn__icon.s-btn__google.bar-md.ba.bc-black-3').click()
# driver.find_element_by_id('identifierId').send_keys(email)
# driver.find_element_by_id('identifierNext').click()
# wait until password textbox clickable
# passwd_element = WebDriverWait(driver, WAIT_TIME).until(
#    exp_cond.element_to_be_clickable((By.NAME, 'password'))
# )

# passwd_element.send_keys(passwd)
# driver.find_element_by_css_selector('.VfPpkd-dgl2Hf-ppHlrf-sM5MNb').click()

driver.find_element_by_id('email').send_keys(email)
driver.find_element_by_id('password').send_keys(passwd)
driver.find_element_by_id('submit-button').click()


menu_item = WebDriverWait(driver, WAIT_TIME).until(
    exp_cond.element_to_be_clickable((By.CSS_SELECTOR, '.-item.site-switcher-item'))
)

menu_item.click()


driver.find_element_by_link_text('log out').click()

check_boxlogout = WebDriverWait(driver, WAIT_TIME).until(
    exp_cond.element_to_be_clickable((By.CSS_SELECTOR, '.grid--cell.pt2'))
)

check_boxlogout.click()

# button_logout = WebDriverWait(driver, WAIT_TIME).until(
#     exp_cond.element_to_be_clickable((By.CSS_SELECTOR, '.grid--cell.s-btn.s-btn__primary'))
# )

# button_logout.sendKeys(Keys.RETURN)

# driver.find_elements_by_class_name('.grid--cell.s-btn.s-btn__primary').click()

driver.implicitly_wait(WAIT_TIME)
button_logout = driver.find_element_by_css_selector('.wmx3.mx-auto.mb24.p24.bg-white.bar-lg.auth-shadow')
button_logout.submit()






