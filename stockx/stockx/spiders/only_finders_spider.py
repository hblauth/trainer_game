from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import re

def scroll(driver, timeout):
    scroll_pause_time = timeout

    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(scroll_pause_time)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        # if new_height == last_height:
        if new_height > 5000:
            # If heights are the same it will exit the function
            break
        last_height = new_height

chrome_options = webdriver.ChromeOptions()
# 1
chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
# 2
chrome_options.add_experimental_option('useAutomationExtension', False)

# chrome_options.add_argument('--headless')

driver = webdriver.Chrome('/Users/henry/code/PATH/chromedriver', options=chrome_options)
driver.implicitly_wait(30)
# Can't do this any more .: switch to firefox
# driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

driver.get('https://onlyfinder.com/profiles?q=location:%22United%20Kingdom%22%20anal')

driver.quit()

# Bypassing selenium detection
# Try pausing JavaScript before navigate to site, wait, re-enable
# What are CSRF tokens?
# https://stackoverflow.com/questions/33225947/can-a-website-detect-when-you-are-using-selenium-with-chromedriver

# 1: fail
# 2: fail
# 3: fail
# 1 & 2: fail


print(WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".result a > divlink"))).get_attribute("innerHTML"))

print(driver.find_element_by_css_selector('.result a').get_attribute('innerHTML'))
print(driver.find_element_by_css_selector('.result a').get_attribute('href'))

scroll(driver, 2.1)

soup = BeautifulSoup(driver.page_source, 'lxml')
soup_b = BeautifulSoup(driver.page_source, 'html.parser')

driver.quit()

# results
results = soup.find_all('div', class_='result')
results_b = soup_b.find_all('div', class_='result')

result = results[1]
result_b = results_b[1]

output = []

for result in results:
  info = {}
  try:
    info['username'] = result.find('h3').get_text()
  info['bio_trunc'] = result.find('div', class_='pb-3 text-muted about').get_text()

  numbers = result.find_all('span', class_='mr-3 profile-info')
  info['likes'] = re.sub(',',  '', numbers[0].get_text().strip())
  info['photos'] = re.sub(',',  '', numbers[1].get_text().strip())
  info['videos'] = re.sub(',',  '', numbers[2].get_text().strip())
  info['price'] = re.sub(',',  '', result.find_all('span', class_='profile-info')[-1].strong.get_text().strip())

  output.append(info)

# ------------------------------------------------------------------------------------------------------------------------------------------------
# Try with firefox
from selenium.webdriver.firefox.options import Options

options = Options()

driver = webdriver.Firefox(options=options ,executable_path='./geckodriver')



# ------------------------------------------------------------------------------------------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# Your options may be different
options.set_preference('permissions.default.image', 2)
options.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', False)


def all_links(url):
    # Setup the driver. This one uses firefox with some options and a path to the geckodriver
    # implicitly_wait tells the driver to wait before throwing an exception
    driver.implicitly_wait(30)
    # driver.get(url) opens the page
    driver.get(url)
    # This starts the scrolling by passing the driver and a timeout
    scroll(driver, 5)
    # Once scroll returns bs4 parsers the page_source
    soup_a = BeautifulSoup(driver.page_source, 'lxml')
    # Them we close the driver as soup_a is storing the page source
    driver.close()

    # Empty array to store the links
    links = []

    # Looping through all the a elements in the page source
    for link in soup_a.find_all('a'):
        # link.get('href') gets the href/url out of the a element
        links.append(link.get('href'))

    return links