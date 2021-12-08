from time import sleep
import threading

PROXY_HOST = "123"
PROXY_PORT = "12553"
PROXY_USER = "yahya"
PROXY_PASS = "benzh"
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


def foo(t):
    sleep(10)
    t.cancel()


def printit():
    t = threading.Timer(5.0, printit).start()

    print("Hello, World!")
    foo(t)


printit()
# continue with the rest of your code
