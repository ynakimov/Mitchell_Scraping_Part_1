# from urllib.request import urlopen
# from bs4 import BeautifulSoup

# html = urlopen('http://www.pythonscraping.com/pages/warandpeace.html')
# bs = BeautifulSoup(html, "html.parser")

# nameList = bs.findAll('span', {'class': 'green'})
# for name in nameList:
#     print(name.get_text())

# titles = bs.find_all(['h1', 'h2','h3','h4','h5','h6'])
# print([title for title in titles])   

# allText = bs.find_all('span', {'class':{'green', 'red'}})
# print([text for text in allText])
# for text in allText:
#     print(f"{text}\n")

# nameList = bs.find_all(text='the prince')
# print(len(nameList))    

# title = bs.find_all(id='title', class_='text')
# # print(f"{title}\n")
# for text in title:
#     print(f"{text}\n")

# html = urlopen('http://www.pythonscraping.com/pages/page3.html')
# bs = BeautifulSoup(html, 'html.parser')
# children = bs.find('table',{'id':'giftList'}).children
# for child in children:
#     print(child)

# for sibling in bs.find('table', {'id':'giftList'}).tr.next_siblings:
#     print(sibling) 
# tag_picture = bs.find('img',{'src':'../img/gifts/img1.jpg'})
# tag_picture_parent = tag_picture.parent
# tag_picture_parent_previous_sibling = tag_picture_parent.previous_sibling
# print(f'tag_picture:\n {tag_picture}')
# print(f'tag_picture_parent:\n {tag_picture_parent}')
# print(f'tag_picture_parent_previous_sibling:\n {tag_picture_parent_previous_sibling}')
# print(tag_picture_parent_previous_sibling.get_text())

HEADERS_SBER_BANK = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
}

from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')

re_exp_txt = '\.\.\/img\/gifts/img.*\.jpg'
re_exp_txt = '..\/img\/gifts/img.*.jpg'
re_exp_obj = re.compile(re_exp_txt)
images = bs.find_all('img', {'src': re_exp_obj})
for image in images: 
    a = image.attrs
    print(image['src'])
