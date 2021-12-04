import os
import zipfile
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import re
from time import sleep


class Bot:

    proxy_counter = 0

    def __init__(self, PROXY_LIST, sites, niches):

        self.sites = sites
        self.niches = niches
        self.PROXY_LIST = PROXY_LIST

    def configure_webdriver(self):
        Proxy_Conf = self.PROXY_LIST[self.proxy_counter]

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
            """ % (Proxy_Conf['PROXY_HOST'], Proxy_Conf['PROXY_PORT'], Proxy_Conf['PROXY_USER'], Proxy_Conf['PROXY_PASS'])
        self.proxy_counter += 1

        return {
            'manifest_json': manifest_json,
            'background_js': background_js
        }

    def get_chromedriver(self, use_proxy=True, user_agent=None):

        path = os.path.dirname(os.path.abspath(__file__))
        chrome_options = webdriver.ChromeOptions()
        if use_proxy:
            pluginfile = 'proxy_auth_plugin.zip'
            config = self.configure_webdriver()
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

    def get_page(self, driver, query):
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

    def scrap(self, driver):
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

    def Main_SCRAPP(self):

        driver = self.get_chromedriver(PROXY_LIST)

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

                    self.get_page(driver, query)
                    while(1):

                        self.scrap(driver)

                        try:

                            driver.find_element(
                                By.ID, "pnnext").click()

                        except:
                            break

                    driver.quit()

                    driver = self.get_chromedriver(PROXY_LIST)

        except:
            pass


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
