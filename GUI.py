from tkinter import *
import tkinter as tk
from Emails_Bot import Bot


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


def go():
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
    websites = ['instagram.com']
    niches = ['dogs', 'cats', 'boooty']
    bit = Bot(PROXY_LIST, websites, niches)
    bit.All_Scrapper()


# Container  of all franmes == root window
Global_View = Tk()
width = 750
height = 750
Global_View.geometry(f"{width}x{height}")
# Global_View.state("zoomed")
Global_View.config(bg="#054861")


# frames inside

Left_frame = Frame(Global_View)
Right_frame = Frame(Global_View)

Right_frame.config(bg="blue", width=width/2)
Right_frame.pack(fill=tk.BOTH, side=RIGHT)

Emails_output = Text(Right_frame, height=50)
Emails_output.place(x=10, y=30)

# set frame to the left

Left_frame.config(bg="green", width=width/2)
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
             command=go)

btn.place(x=250, y=800,)

Global_View.mainloop()
