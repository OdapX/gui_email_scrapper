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


'''
QPushButton#startBtn {
    background-color: #43A047;
    color:white
    border-radius: 14px;
    font: 20pt MS Shell Dlg 2;
}

QPushButton#startBtn:hover {
    background-color: #64b5f6;
    color: #fff;
}

QPushButton#startBtn:pressed {
    background-color: red;
}
'''
