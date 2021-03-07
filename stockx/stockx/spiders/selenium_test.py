from selenium import webdriver
import time

# Doesn't work with headless - think have to load javascript
chrome_options = webdriver.ChromeOptions()
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

data

# Average price over time

url = 'https://stockx.com/api/products/21461590-3e35-42ad-858b-836e2a50cbb2/chart?start_date=all&end_date=2021-02-16&intervals=100&format=highstock&currency=GBP&country=GB'

headers = {
'authority' : 'stockx.com',
'path' : '/api/products/21461590-3e35-42ad-858b-836e2a50cbb2/chart?start_date=all&end_date=2021-02-16&intervals=100&format=highstock&currency=GBP&country=GB',
'scheme' : 'https',
'accept' : '*/*',
'accept-encoding' : 'gzip, deflate, br',
'accept-language' : 'en-US,en;q=0.9,el;q=0.8,es;q=0.7',
'appos' : 'web',
'appversion' : '0.1',
'authorization' : 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5USkNNVVEyUmpBd1JUQXdORFk0TURRelF6SkZRelV4TWpneU5qSTNNRFJGTkRZME0wSTNSQSJ9.eyJodHRwczovL3N0b2NreC5jb20vY3VzdG9tZXJfdXVpZCI6Ijk3ZmVhOWJmLTgyNGYtMTFlOS04ODgwLTEyZGViOTA5ZTk3YyIsImh0dHBzOi8vc3RvY2t4LmNvbS9nYV9ldmVudCI6IkxvZ2dlZCBJbiIsImlzcyI6Imh0dHBzOi8vYWNjb3VudHMuc3RvY2t4LmNvbS8iLCJzdWIiOiJhdXRoMHw5N2ZlYTliZi04MjRmLTExZTktODg4MC0xMmRlYjkwOWU5N2MiLCJhdWQiOiJnYXRld2F5LnN0b2NreC5jb20iLCJpYXQiOjE2MTM1MTA5ODUsImV4cCI6MTYxMzU1NDE4NSwiYXpwIjoiT1Z4cnQ0VkpxVHg3TElVS2Q2NjFXMER1Vk1wY0ZCeUQiLCJzY29wZSI6Im9mZmxpbmVfYWNjZXNzIn0.qGWfQBrbvKu6EZjKzJfN58fpaaWwAcYEU0piC4P1NISBMQ2eF9tXqCEiBZJIIfK3e8g-T3erB0oAqB54ZbY857Om3Q5Ulzl3ij9pxoVjrjaIxjbNeAzYV1A209pbLvNgUpP6M72pzbLbIR5kawATPsIoEOx8DhNME6W3_07O7amEaAR111xbYyfFNG9qhIeYN45RT9D4Nj3gFQkiJXdBt8ovLajBXN_WznvWYpzQGrzDLjd8sEo8d8Eg165LNFldHSBptuH9vIL0kbesAUZsqjLo87T_Gv41FKrAFN8Qs-cgUTgiUJ4y_Lop01Lm5BwfDCVs0c6MIdI-CD2VxQbzcQ',
'cache-control' : 'no-cache',
'cookie': '_ALGOLIA=anonymous-699c45f9-9c00-4dcf-898d-c44c91443e72; mfaLogin=err; ajs_user_id=%2297fea9bf-824f-11e9-8880-12deb909e97c%22; ajs_anonymous_id=%226f0c9540-5197-4763-96d1-4332876b5f05%22; stockx_seen_ask_new_info=true; stockx_seen_sales_overlay=true; stockx_multi_edit_seen=true; default_buy_now=undefined; show_recommended_homepage=false; related_products_position=undefined; stockx_market_country=GB; stockx_follow_explanation=true; stockx_default_streetwear_size=M; covid_banner=true; stockx_seen_bid_new_info=true; stockx_bid_ask_spread_seen=true; _ga=GA1.2.2123932771.1592381140; _fbp=fb.1.1592381152211.284629395; _px_f394gi7Fvmc43dfg_user_id=YjkwZDUyYTAtYmY2ZC0xMWVhLWE1ZTctNzU5Y2ZlMzg2NDAx; _px_uAB=MTk5Mnx0cnVl; show_chatbot=undefined; sell_ui_refresh=undefined; show_order_status_covid_faq=undefined; web_covid_delay_messaging_pre_checkout_ask=undefined; web_covid_delay_messaging_post_checkout_ask=undefined; web_covid_delay_messaging_selling=undefined; web_covid_delay_messaging_buying=undefined; web_covid_delay_messaging_ask_status=undefined; web_covid_delay_messaging_bid_status=undefined; web_covid_delay_messaging_pre_checkout_buy=undefined; web_covid_delay_messaging_post_checkout_buy=undefined; henryblauthgmailcoman_reload=1598358514; below_retail_type=; bid_ask_button_type=undefined; brand_tiles_version=; browse_page_tile_size_update_web=undefined; bulk_shipping_enabled=false; default_apple_pay=false; intl_payments=undefined; multi_edit_option=undefined; product_page_affirm_callout_enabled_web=undefined; related_products_length=undefined; riskified_recover_updated_verbiage=false; show_all_as_number=false; show_bid_education=; show_bid_education_times=1; show_how_it_works=undefined; show_watch_modal=false; pdp_refactor_web=undefined; recently_viewed_web_home=undefined; bulk_shipping_eligibility=undefined; ops_delay_messaging_pre_checkout_ask=undefined; ops_delay_messaging_post_checkout_ask=undefined; ops_delay_messaging_selling=undefined; ops_delay_messaging_buying=undefined; ops_delay_messaging_ask_status=undefined; ops_delay_messaging_bid_status=undefined; ops_delay_messaging_pre_checkout_buy=undefined; ops_delay_messaging_post_checkout_buy=undefined; utility_banner=true; _gcl_au=1.1.42853495.1609615304; stockx_default_sneakers_size=9.5; _pxvid=53bb21cb-54d3-11eb-ae61-0242ac12000e; __cfduid=de44e771b8e3327f4c18885549ee2e33b1612291637; language_code=en; stockx_selected_locale=en; stockx_selected_region=GB; stockx_dismiss_modal=true; stockx_dismiss_modal_set=2021-02-02T18%3A52%3A45.094Z; stockx_dismiss_modal_expiration=2022-02-02T18%3A52%3A45.092Z; stockx_homepage=sneakers; stockx_user_logged_in=true; stockx_user_shipping_region=GB; token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6Ik5USkNNVVEyUmpBd1JUQXdORFk0TURRelF6SkZRelV4TWpneU5qSTNNRFJGTkRZME0wSTNSQSJ9.eyJodHRwczovL3N0b2NreC5jb20vY3VzdG9tZXJfdXVpZCI6Ijk3ZmVhOWJmLTgyNGYtMTFlOS04ODgwLTEyZGViOTA5ZTk3YyIsImh0dHBzOi8vc3RvY2t4LmNvbS9nYV9ldmVudCI6IkxvZ2dlZCBJbiIsImlzcyI6Imh0dHBzOi8vYWNjb3VudHMuc3RvY2t4LmNvbS8iLCJzdWIiOiJhdXRoMHw5N2ZlYTliZi04MjRmLTExZTktODg4MC0xMmRlYjkwOWU5N2MiLCJhdWQiOiJnYXRld2F5LnN0b2NreC5jb20iLCJpYXQiOjE2MTM1MTA5ODUsImV4cCI6MTYxMzU1NDE4NSwiYXpwIjoiT1Z4cnQ0VkpxVHg3TElVS2Q2NjFXMER1Vk1wY0ZCeUQiLCJzY29wZSI6Im9mZmxpbmVfYWNjZXNzIn0.qGWfQBrbvKu6EZjKzJfN58fpaaWwAcYEU0piC4P1NISBMQ2eF9tXqCEiBZJIIfK3e8g-T3erB0oAqB54ZbY857Om3Q5Ulzl3ij9pxoVjrjaIxjbNeAzYV1A209pbLvNgUpP6M72pzbLbIR5kawATPsIoEOx8DhNME6W3_07O7amEaAR111xbYyfFNG9qhIeYN45RT9D4Nj3gFQkiJXdBt8ovLajBXN_WznvWYpzQGrzDLjd8sEo8d8Eg165LNFldHSBptuH9vIL0kbesAUZsqjLo87T_Gv41FKrAFN8Qs-cgUTgiUJ4y_Lop01Lm5BwfDCVs0c6MIdI-CD2VxQbzcQ; _gid=GA1.2.349898919.1613510989; stockx_session=d32b1b7b-8402-477d-9a2f-ba59446d42d9; _px_7125205957_cs=eyJpZCI6IjFlODllN2IwLTcwOWUtMTFlYi05NTBmLWY1YTYyZDE0MDk4YSIsInN0b3JhZ2UiOnt9LCJleHBpcmF0aW9uIjoxNjEzNTEzMzkzNDgwfQ==; stockx_selected_currency=GBP; is_gdpr=true; cookie_policy_accepted=true; stockx_ip_region=GB; stockx_product_visits=485; _gat=1; _dd_s=rum=0&expire=1613512504284',
'dnt' : '1',
'pragma': 'no-cache',
'referer' : 'https://stockx.com/nike-dunk-low-ceramic-2020',
'sec-ch-ua' : '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
'sec-ch-ua-mobile': '?0',
'sec-fetch-dest' : 'empty',
'sec-fetch-mode' : 'cors',
'sec-fetch-site': 'same-origin',
'user-agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
'x-requested-with' : 'XMLHttpRequest'}

import requests as r
resp = r.get(url, headers=headers)

resp.json()


# Transactions
URL = 'https://stockx.com/api/products/7de8f559-237d-4c83-bc7e-c64858bdfb12/activity?state=480&currency=GBP&limit=10&page=1&sort=createdAt&order=DESC&country=GB'

:authority: stockx.com
:method: GET
:path: /api/products/7de8f559-237d-4c83-bc7e-c64858bdfb12/activity?state=480&currency=GBP&limit=10&page=1&sort=createdAt&order=DESC&country=GB
:scheme: https
accept: */*
accept-encoding: gzip, deflate, br
accept-language: en-US,en;q=0.9
appos: web
appversion: 0.1
authorization
cache-control: no-cache
cookie: __cfduid=d4465f5b71df69ffe9d29ccfcc0e2cd3a1613541505; stockx_homepage=sneakers; language_code=en; stockx_market_country=GB; _pxvid=27adc05c-70e5-11eb-b9c1-0242ac120005; stockx_session=2c9716d2-793e-4810-b35e-45f7bd11e122; _gcl_au=1.1.106436377.1613541509; below_retail_type=; brand_tiles_version=v1; bulk_shipping_enabled=true; default_apple_pay=false; intl_payments=true; multi_edit_option=beatLowestAskBy; product_page_affirm_callout_enabled_web=false; related_products_length=v2; riskified_recover_updated_verbiage=true; show_all_as_number=false; show_how_it_works=true; show_watch_modal=true; pdp_refactor_web=undefined; recently_viewed_web_home=false; salesforce_chatbot_prod=true; web_low_inv_checkout=v1; home_vertical_rows_web=true; ops_banner_id=blteaa2251163e21ba6; _px_f394gi7Fvmc43dfg_user_id=MmMyOTdiZjAtNzBlNS0xMWViLWEzNDktYjFlMGM2NzRmOWMz; _pk_id.421.1a3e=3c151513b8deba33.1613541517.1.1613541517.1613541517.; _pk_ses.421.1a3e=1; IR_gbd=stockx.com; IR_9060=1613541517322%7C0%7C1613541517322%7C%7C; _scid=131bbf34-3afa-43c5-bab5-b9544d39d76f; IR_PI=2dc1818a-70e5-11eb-b537-42010a24662c%7C1613627917322; _fbp=fb.1.1613541519546.1690476655; lastRskxRun=1613541521253; rskxRunCookie=0; rCookie=ntk8yh3plbfpscbbwcnc7ekl90ylxm; QuantumMetricUserID=d5976294496c01f484f1111752ff0ee1; QuantumMetricSessionID=0a03ad9c2ffb6db60b0a60c0a8334c47; _dd_s=rum=0&expire=1613542429859; _px3=2493a86e8e6ce51f72360e53a5e0450513e809e7a3ad9c92d01e6423d472c1a2:b2FeLN4NSR/+nykhsxlEwe8uun8NO1Kl/W7cow2sSj7EhsL6x4lMY43ZIkTb1BVJbd8epHifKuOMcK9O7Aof1Q==:1000:W3Gq5UqqyluTQZFrRNaYP2qvq+8SmLioVuanlNpZkrkAwEb6wyncj31FGFFG6pYyq4GR1fkM39dAuR9FOrHtKbcgHGurKns3cxxCW/qjAplGn9bi0xuguOZEO7tFzsAzs5HxZyQA33uSfinNgefaZMcelhkacACuOVV5mP2rclg=; is_gdpr=true; stockx_ip_region=GB; stockx_product_visits=2; _px_7125205957_cs=eyJpZCI6IjJjMjc1OTEwLTcwZTUtMTFlYi1hMzQ5LWIxZTBjNjc0ZjljMyIsInN0b3JhZ2UiOnt9LCJleHBpcmF0aW9uIjoxNjEzNTQzMzMzOTY5fQ==
dnt: 1
pragma: no-cache
referer: https://stockx.com/nike-dunk-low-ceramic-2020
sec-ch-ua: "Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"
sec-ch-ua-mobile: ?0
sec-fetch-dest: empty
sec-fetch-mode: cors
sec-fetch-site: same-origin
user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36
x-requested-with: XMLHttpRequest

params
state: 480
currency: GBP
limit: 10
page: 1
sort: createdAt
order: DESC
country: GB
