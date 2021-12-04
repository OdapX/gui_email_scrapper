from tkinter import *
import tkinter as tk
import os
import zipfile
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import re
from time import sleep

import os
import zipfile
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import re
import threading

# --------------------------Global Variables-----------------
PROXY_LIST = [
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
sites = []
niches = []

# -----------------------------------------------Set up Proxies --------------------------------------


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


def Main_SCRAPP(PROXY_LIST):
    i = 0
    proxy = PROXY_LIST[i]
    driver = get_chromedriver(use_proxy=True, PROXY_HOST=proxy['PROXY_HOST'],
                              PROXY_PORT=proxy['PROXY_PORT'], PROXY_USER=proxy['PROXY_USER'], PROXY_PASS=proxy['PROXY_PASS'])
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
                proxy = PROXY_LIST[i]

                driver = get_chromedriver(use_proxy=True, PROXY_HOST=proxy['PROXY_HOST'],
                                          PROXY_PORT=proxy['PROXY_PORT'], PROXY_USER=proxy['PROXY_USER'], PROXY_PASS=proxy['PROXY_PASS'])

    except:
        pass


def main():
    get_data()
    print("********here*******")
    sleep(3)
    threading.Thread(target=Main_SCRAPP(PROXY_LIST)).start()


def get_data():
    sites = sites_entry.get("1.0", "end").splitlines()

    niches = niches_entry.get("1.0", "end").splitlines()

    Proxy_config = {
        'PROXY_HOST': '',
        'PROXY_PORT': '',
        'PROXY_USER': '',
        'PROXY_PASS': ''

    }

    proxies = proxies_entry.get("1.0", "end")
    for proxy in proxies.splitlines():
        if(proxy == ''):
            pass
        else:
            configs = proxy.split(':')
            Proxy_config['PROXY_HOST'] = configs[0]
            Proxy_config['PROXY_PORT'] = configs[1]
            Proxy_config['PROXY_USER'] = configs[2]
            Proxy_config['PROXY_PASS'] = configs[3]
            PROXY_LIST.append(Proxy_config)


def output_mails(emails):
    Emails_output.insert(1.0, PROXY_LIST)


def printe():
    print("wtf")


# Container  of all franmes == root window
Global_View = Tk()
Global_View.state("zoomed")
Global_View.config(bg="#054861")


# frames inside

Left_frame = Frame(Global_View)
Right_frame = Frame(Global_View)

Right_frame.config(bg="blue", width=900)
Right_frame.pack(fill=tk.BOTH, side=RIGHT)

Emails_output = Text(Right_frame, height=50)
Emails_output.place(x=10, y=30)

# set frame to the left

Left_frame.config(bg="green", width=900)
Left_frame.pack(fill=tk.BOTH, side=LEFT)
# left frame components
site_title = Label(Left_frame, text="WEBSITES AREA")
niche_title = Label(Left_frame, text="NICHES AREA")

site_title.config(bg="green", font=("Montserrat", 22),
                  height="1", fg="white")
site_title.place(x=230, y=20)

niche_title.config(bg="green", font=("Montserrat", 22),
                   height="1", fg="white")

niche_title.place(x=230, y=240)


sites_entry = Text(Left_frame, height=10)
niches_entry = Text(Left_frame, height=10)


sites_entry.place(x=25, y=60)
niches_entry.place(x=25, y=290)

proxies_title = Label(Left_frame, text="PROXIES AREA")
proxies_title.config(bg="green", font=("Montserrat", 22),
                     height="1", fg="white")
proxies_title.place(x=230, y=490)

proxies_entry = Text(Left_frame, height=10)

proxies_entry.place(x=25, y=530)


btn = Button(Left_frame, text="Connect",
             command=main)

btn.place(x=250, y=800,)

Global_View.mainloop()
