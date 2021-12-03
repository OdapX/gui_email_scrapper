from tkinter import *
import os
import zipfile
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import re

import os
import zipfile
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import re
# -----------------------------------------------Set up Proxies --------------------------------------
sites = ['instagram.com', 'facebook.com']
niches = ['dogs', 'cats']
# configure proxy


def configure_webdriver(PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS):

    manifest_json = """
        {
            "version": "1.0.0",
            "manifest_version": 2,
            "name": "Chrome Proxy",
            "permissions": [
                "proxy",
                "tabs",
                "unlimitedStorage",
                "storage",
                "<all_urls>",
                "webRequest",
                "webRequestBlocking"
            ],
            "background": {
                "scripts": ["background.js"]
            },
            "minimum_chrome_version":"22.0.0"
        }
        """

    background_js = """
        var config = {
                mode: "fixed_servers",
                rules: {
                singleProxy: {
                    scheme: "http",
                    host: "%s",
                    port: parseInt(%s)
                },
                bypassList: ["localhost"]
                }
            };

        chrome.proxy.settings.set({value: config, scope: "regular"}, function() {});

        function callbackFn(details) {
            return {
                authCredentials: {
                    username: "%s",
                    password: "%s"
                }
            };
        }

        chrome.webRequest.onAuthRequired.addListener(
                    callbackFn,
                    {urls: ["<all_urls>"]},
                    ['blocking']
        );
        """ % (PROXY_HOST, PROXY_PORT, PROXY_USER, PROXY_PASS)

    return {
        'manifest_json': manifest_json,
        'background_js': background_js
    }

# create a chromedriver instance


def get_chromedriver(use_proxy=False, user_agent=None, PROXY_HOST=None, PROXY_PORT=None, PROXY_USER=None, PROXY_PASS=None):

    path = os.path.dirname(os.path.abspath(__file__))
    chrome_options = webdriver.ChromeOptions()
    if use_proxy:
        pluginfile = 'proxy_auth_plugin.zip'
        config = configure_webdriver(
            PROXY_HOST=PROXY_HOST, PROXY_PORT=PROXY_PORT, PROXY_USER=PROXY_USER, PROXY_PASS=PROXY_PASS)
        with zipfile.ZipFile(pluginfile, 'w') as zp:
            zp.writestr("manifest.json", config['manifest_json'])
            zp.writestr("background.js", config['background_js'])
        chrome_options.add_extension(pluginfile)
    if user_agent:
        chrome_options.add_argument('--user-agent=%s' % user_agent)
    driver = webdriver.Chrome(
        os.path.join(path, 'chromedriver'),
        chrome_options=chrome_options)
    return driver

# -----------------------------------------------Main Part --------------------------------------


def get_page(driver, query):
    try:
        driver.get("https://www.google.com/")
        sleep(2)
        input = driver.find_element(
            By.XPATH, '/ html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        input.send_keys(query)
        sleep(2)
        driver.find_element(
            By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').click()

        sleep(2)
    except:
        pass


def scrap(driver):
    try:
        data = driver.find_element(
            By.XPATH, '//*[@id="rso"]')

        line = str(data.text)
        matches = re.findall(r'[\w.+-]+@[\w-]+\.[\w.-]+', line)
        unique_emails = set()
        my_file = open("emails.txt", "a+", encoding='utf-8')

        for match in matches:
            if match[-1] == '.':
                match = match[0: -1]
            unique_emails.add(match)

        for email in unique_emails:
            my_file.write(email + '\n')
        my_file.close()

        driver.execute_script(
            "window.scrollTo(0, document.body.scrollHeight);")
    except:
        pass


def Main_SCRAPPER(driver, list_of_proxies):
    i = 0

    try:
        for site in sites:
            my_file = open("emails.txt", "a+", encoding='utf-8')
            my_file.write("SITE   : "+site+" _________" "\t")
            my_file.close()
            for niche in niches:

                query = f' site:{site} "{niche}" "@gmail.com" '
                my_file = open("emails.txt", "a+", encoding='utf-8')
                my_file.write("______NICHE   : "+niche+" _________\n")
                my_file.close()

                get_page(driver, query)
                while(1):

                    scrap(driver)

                    try:

                        driver.find_element(
                            By.ID, "pnnext").click()

                    except:
                        break
                i += 1
                driver.quit()
                proxy = list_of_proxies[i]

                driver = get_chromedriver(use_proxy=True, PROXY_HOST=proxy['PROXY_HOST'],
                                          PROXY_PORT=proxy['PROXY_PORT'], PROXY_USER=proxy['PROXY_USER'], PROXY_PASS=proxy['PROXY_PASS'])

    except:
        pass


def main():

    List_of_Proxies = [
        {
            'PROXY_HOST': '186.65.117.169',
            'PROXY_PORT': '9582',
            'PROXY_USER': '2c91Ug',
            'PROXY_PASS': '6MEc6s'

        },



        {
            'PROXY_HOST': '46.232.14.210',
            'PROXY_PORT': '8000',
            'PROXY_USER': 'jHmVb5',
            'PROXY_PASS': 'VaDjAG'

        },
        {
            'PROXY_HOST': '46.232.15.30',
            'PROXY_PORT': '8000',
            'PROXY_USER': 'jHmVb5',
            'PROXY_PASS': 'VaDjAG'

        },



    ]
    proxy = List_of_Proxies[0]
    driver = get_chromedriver(use_proxy=True, PROXY_HOST=proxy['PROXY_HOST'],
                              PROXY_PORT=proxy['PROXY_PORT'], PROXY_USER=proxy['PROXY_USER'], PROXY_PASS=proxy['PROXY_PASS'])
    Main_SCRAPPER(driver, List_of_Proxies)


def pr():

    print(site.get(), niche.get())


View = Tk()


View.geometry("1000x600")

btn = Button(View, text="Scrap", command=pr)
btn.pack()

site = StringVar()
niche = StringVar()
sites_entry = Entry(textvariable=site, width=30)
niches_entry = Entry(textvariable=niche, width=30)
sites_entry.place(x=60, y=60)
niches_entry.place(x=60, y=80)
View.mainloop()
