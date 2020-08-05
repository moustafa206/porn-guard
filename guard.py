from PIL import Image
import time
import os
import requests
import browserhistory as detect
import csv
p = "porn"
d = input('How many days without porn:')
b = int(d * 86400)
a = 0
k = 43200
q = 43190
while (a < b):
    a = a + 1
    print(a)
    if a == 172800:
        im = Image.open(requests.get('https://c.top4top.io/p_1678yk33h1.jpg', stream=True).raw)
        im.show()
    time.sleep(1)
    os.system('cls')
    if a == 43190:
        q = q * 2
        print('close google chrome for the history check or it will be terminated')
    if a == k:
        k = k * 2
        os.system('taskkill /F /IM chrome.exe /T')
        history = detect.get_browserhistory()
        if p in history:
            im = Image.open(requests.get('https://media.tenor.com/images/be9f823259c6a776f97b475837d3f617/raw', stream=True).raw)
            im.show()
            a = 1
    


