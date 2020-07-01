import time
from datetime import datetime as dt

temp_path = 'hosts'
host_path = 'C:\\Windows\\System32\\drivers\\etc\\hosts'  # path of the host.txt file in our machine
redirect = '127.0.0.1'  # web page to redirect after accessing the blocked site
website_list = ['facebook.com', 'www.facebook.com']  # Website's to be blocked

"""Time period during which we want to block the website (24 hrs time format)"""
start_time = 10
end_time = 16

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 10) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day, 16):  # 8am to 4pm
        print('Working hours...')
        with open(host_path, 'r+') as file:
            content = file.read()
            for website in website_list:
                if website in content:  # Here we check if any of our website is there in the website_list or not
                    pass
                else:
                    file.write(f'{redirect} {website}\n')
    else:
        with open(host_path, 'r+') as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in website_list):
                    file.write(line)
            file.truncate()
            print('Fun hours...')
    time.sleep(2)
