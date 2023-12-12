import os
from dotenv import load_dotenv, dotenv_values
from playwright.sync_api import sync_playwright

load_dotenv()

URL = 'https://hashtagbasketball.com/fantasy-basketball-rankings'

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=50)
    page = browser.new_page()
    page.goto(URL)
    page.locator('#ContentPlaceHolder1_DDSHOW').select_option('900')
    page.locator('#ContentPlaceHolder1_DropDownList1').select_option('On')
    page.locator('#ContentPlaceHolder1_DDDURATION').select_option('30')
    page.locator('#ContentPlaceHolder1_CBTO').uncheck()
    page.wait_for_timeout(10000)
    content = page.content()
    with open(f'{os.getenv('FILES_DIR')}/content_30.html', 'w+', encoding='utf-8') as f:
        f.write(content)
    browser.close()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, slow_mo=50)
    page = browser.new_page()
    page.goto(URL)
    page.locator('#ContentPlaceHolder1_DDSHOW').select_option('900')
    page.locator('#ContentPlaceHolder1_DropDownList1').select_option('On')
    page.locator('#ContentPlaceHolder1_DDDURATION').select_option('14')
    page.locator('#ContentPlaceHolder1_CBTO').uncheck()
    page.wait_for_timeout(10000)
    content = page.content()
    with open(f'{os.getenv('FILES_DIR')}/content_14.html', 'w+', encoding='utf-8') as f:
        f.write(content)
    browser.close()   