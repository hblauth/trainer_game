from selenium import webdriver
import time
driver = webdriver.Chrome('/Users/henry/code/PATH/chromedriver')
driver.get('https://stockx.com/crocs-classic-clog-justin-bieber')

# Click to confim location & language
actions = webdriver.ActionChains(driver)

# Full name is css-wqkul-CancelButton-ConfirmButton et9rxoe1, but unsure if changes
actions.move_to_element(driver.find_element_by_class_name('css-wqkul-CancelButton-ConfirmButton'))
actions.click()
actions.perform()
time.sleep(3)

elements = driver.find_elements_by_class_name("highcharts-series.highcharts-series-0.highcharts-area-series > path")

data = [element.get_attribute('d') for element in elements]