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
# 3
# driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

driver.get('https://onlyfinder.com/profiles?q=location:%22United%20Kingdom%22%20anal')

driver.quit()

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


<div class="result">
<div class="img-avatar align-top m-3" data-img="avatar.jpg" data-username="" style="background:url('https://public.onlyfans.com/files/thumbs/w480/r/rv/rvu/rvuamdcmew3yftynduagesmmqfd2tg231609542997/avatar.jpg'),url('/static/noprofile.jpg');">
<a class="divLink" data-img="avatar.jpg" data-pos="2" data-username="" href="https://onlyfans.com/" rel="nofollow" target="_blank"></a>
</div>
<div class="result-container col-sm-7">
<a data-pos="2" data-username="" href="https://onlyfans.com/" rel="nofollow" target="_blank">
                            onlyfans.com &gt; <br/>
<h3>Anal Annabelle</h3>
</a>
<div class="pb-3 text-muted about">😈 YOUR DIRTY ANAL SLUT 😈https://linktr.ee/XanalannabellexHey Everyone!I’m so glad to have you here ❤️I’m here for your kinky fantasies so don’t be scared to come play with me 😈My DMs are always open for CUSTOM REQ ...</div>
<div>
<span class="mr-3 profile-info"><i class="fas fa-heart"></i> <strong>2,085</strong></span>
<span class="mr-3 profile-info"><i class="fas fa-camera"></i> 175</span>
<span class="mr-3 profile-info"><i class="fas fa-video"></i> 11</span>
<span class="profile-info">Price: <strong>$5.00</strong></span>
</div>
</div></div>










# ------------------------------------------------------------------------------------------------------------------------------------------------





from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup

# Your options may be different
options = Options()
options.set_preference('permissions.default.image', 2)
options.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', False)


def all_links(url):
    # Setup the driver. This one uses firefox with some options and a path to the geckodriver
    driver = webdriver.Firefox(options=options ,executable_path='./geckodriver')
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