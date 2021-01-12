from selenium import webdriver
import time

# Doesn't work with headless - think have to load javascript
# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')

driver = webdriver.Chrome('/Users/henry/code/PATH/chromedriver', options=chrome_options)
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

driver.quit()

# NB. Could also use driver.execute_script on these:
# <script async data-chunk="components-pageSwitcherContainer" src="https://web-assets.stockx.com/highcharts.e50ee5dc.bundle.fb08dafb9f644a87006dbff70b135716f0c7b399.js"></script>
# <script async data-chunk="components-pageSwitcherContainer" src="https://web-assets.stockx.com/common.a3608e05.bundle.fb08dafb9f644a87006dbff70b135716f0c7b399.js"></script>
# <script async data-chunk="components-pageSwitcherContainer" src="https://web-assets.stockx.com/components-pageSwitcherContainer.e529af98.bundle.fb08dafb9f644a87006dbff70b135716f0c7b399.js"></script>

