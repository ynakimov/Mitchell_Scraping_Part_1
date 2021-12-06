# from urllib.request import urlopen

# html = urlopen('http://pythonscraping.com/pages/page1.html')
# print(html.read())

# date в timestamp в python

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page1.html')
# bs = BeautifulSoup(html.read(), 'html.parser')
# bs = BeautifulSoup(html, 'html.parser')
bs = BeautifulSoup(html, 'lxml')
print(bs.h1)

# date в timestamp в python
import time
import datetime
s = "02/08/2021"
s_timestamp = time.mktime(datetime.datetime.strptime(s, "%d/%m/%Y").timetuple())
print(s_timestamp)
g = '1638219600000'
h = '1627851600000'