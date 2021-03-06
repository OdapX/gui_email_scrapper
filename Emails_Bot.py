
import os
import zipfile
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import re
import sqlite3


class Bot:

    # will be used to disable launching another request on a running instance
    # -make sue clicking start button many times doesn't break the code

    Finished_Scrapping = False

    Error = False

    Proxy_Blocked = False
    # wil be used to stop scrapping on stop-botton clicked

    Exit = False
    # Initiate the data needed for scrapping
    Websites = []
    Niches = []
    # keep count of the proxy used
    Counter = 0

    # current niche will be used to let the user know what niche is the program at.

    Current_Niche = ""

    Driver = None
    # driver configs
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

    background_js = ""
    # Initialize the Proxy list to be used

    def __init__(self, PROXY_LIST, Websites, Niches):
        self.PROXY_LIST = PROXY_LIST
        self.Websites = Websites
        self.Niches = Niches

    # Setup_Configuration will use a new proxy each time
    # it is called , when we finish the whole PROXY_LIST
    # we go back to the first proxy and we rotate that way

    def Setup_Configurations(self):
        PROXY_HOST = self.PROXY_LIST[self.Counter]["PROXY_HOST"]
        PROXY_PORT = self.PROXY_LIST[self.Counter]["PROXY_PORT"]
        PROXY_USER = self.PROXY_LIST[self.Counter]["PROXY_USER"]
        PROXY_PASS = self.PROXY_LIST[self.Counter]["PROXY_PASS"]
        self.background_js = """
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
        """ % (
            PROXY_HOST,
            PROXY_PORT,
            PROXY_USER,
            PROXY_PASS,
        )

        self.Counter += 1
        print(self.Counter)

    # //TODO:Execute this First in main

    # set up the driver with a proxy
    # Calling the  Setup_Configuration() to configure
    # commit the new Driver to the instance in the end of configuration

    def Setup_Driver(self):

        path = os.path.dirname(os.path.abspath(__file__))
        chrome_options = webdriver.ChromeOptions()
        pluginfile = "./public/proxy_auth_plugin.zip"

        self.Setup_Configurations()

        with zipfile.ZipFile(pluginfile, "w") as zp:
            zp.writestr("manifest.json", self.manifest_json)
            zp.writestr("background.js", self.background_js)
        chrome_options.add_extension(pluginfile)

        self.Driver = webdriver.Chrome(
            os.path.join(path, "public", "chromedriver.exe"), chrome_options=chrome_options
        )

    # Launch_Browser to be only used after the Driver is setup
    # using the Setup_Driver function.
    def Scrap_one_Niche(self, query, niche, website):

        if self.Exit:
            try:
                self.Driver.quit()
                return
            except:
                return
        else:

            try:
                self.Driver.get("https://www.google.com/")

                input = self.Driver.find_element(
                    By.XPATH,
                    "/ html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input",
                )
                input.send_keys(query)

                self.Driver.find_element(
                    By.XPATH,
                    "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]",
                ).click()

            except:
                self.Proxy_Blocked = True
                print("BLOCKED")
                return

            while True:
                if self.Exit:
                    try:
                        self.Driver.quit()
                        return
                    except:
                        self.Error = True
                        return
                else:
                    try:
                        # TODO:write this in a database instead of a txt file

                        data = self.Driver.find_element(
                            By.XPATH, '//*[@id="rso"]')

                        line = str(data.text)
                        matches = re.findall(r"[\w.+-]+@[\w-]+\.[\w.-]+", line)
                        con = sqlite3.connect(os.path.join(
                            os.path.dirname(os.path.abspath(__file__)), "lightDatabase", "Emails.db"))
                        cur = con.cursor()
                        for match in matches:
                            if match[-1] == ".":
                                match = match[0:-1]
                                try:
                                    cur.execute(
                                        "insert into Emails values(?,?,?)",
                                        (match, niche, website),
                                    )

                                except:
                                    pass
                        con.commit()
                        con.close()
                        try:
                            self.Driver.execute_script(
                                "window.scrollTo(0, document.body.scrollHeight);"
                            )
                        except:
                            self.Proxy_Blocked = True
                            print("BLOCKED")

                        self.Driver.find_element(By.ID, "pnnext").click()
                    except:
                        break

    def All_Scrapper(self):
        if self.Exit:
            return

        else:
            try:
                self.Setup_Driver()
            except:
                print("error Launching..Aborting")
                self.Error = True
                return

            try:
                for website in self.Websites:
                    for niche in self.Niches:
                        if self.Exit:
                            try:
                                self.Driver.quit()
                                return
                            except:
                                self.Error = True
                                return

                        else:
                            self.Current_Niche = niche
                            query = f'site:{website} niche:"{niche}" "@gmail.com"'

                            # scrap one niche according to the query string
                            # when a proxy is blocked close the driver and
                            # launch new one with a new proxy and scrap the niche
                            # in use again.
                            try:
                                self.Scrap_one_Niche(query, niche, website)
                                if self.Proxy_Blocked:
                                    self.Proxy_Blocked = False
                                    self.Driver.quit()
                                    print("here")
                                    self.Setup_Driver()
                                    self.Scrap_one_Niche(query, niche, website)

                            except:
                                self.Error = True
                                pass
                self.Finished_Scrapping = True
                self.Driver.quit()

            except:
                self.Error = True
                return


# PROXY_LIST = [
#     {
#         'PROXY_HOST': '186.65.117.169',
#         'PROXY_PORT': '9582',
#         'PROXY_USER': '2c91Ug',
#         'PROXY_PASS': '6MEc6s'

#     },


#     {
#         'PROXY_HOST': '46.232.14.210',
#         'PROXY_PORT': '8000',
#         'PROXY_USER': 'jHmVb5',
#         'PROXY_PASS': 'VaDjAG'

#     },
#     {
#         'PROXY_HOST': '46.232.15.30',
#         'PROXY_PORT': '8000',
#         'PROXY_USER': 'jHmVb5',
#         'PROXY_PASS': 'VaDjAG'
#     },


# ]
# websites = ['instagram.com']
# niches = ['dogs', 'cats']
# bit = Bot(PROXY_LIST, websites, niches)

# bit.All_Scrapper()
