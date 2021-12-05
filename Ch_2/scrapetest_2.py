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

# ///////////////////////////////////////////////
# from requests import get # попробуем другой модуль. get позволяет задавать заголовки, чтобы обойти анти-раулинговую защиту
# import requests
# //////////////////////////////////////////////

# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import re

HEADERS_SBER_BANK = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
}


# html = urlopen('http://www.pythonscraping.com/pages/page3.html')
# bs = BeautifulSoup(html, 'html.parser')

# re_exp_txt = '\.\.\/img\/gifts/img.*\.jpg'
# re_exp_txt = '..\/img\/gifts/img.*.jpg'
# re_exp_obj = re.compile(re_exp_txt)
# images = bs.find_all('img', {'src': re_exp_obj})
# for image in images: 
#     a = image.attrs
#     print(image['src'])


# html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
# bs = BeautifulSoup(html, 'html.parser')
# for link in bs.find_all('a'):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])


# html = urlopen('http://en.wikipedia.org/wiki/Kevin_Bacon')
# bs = BeautifulSoup(html, 'html.parser')
# for link in bs.find('div', {'id':'bodyContent'}).find_all(
#     'a', href=re.compile('^(/wiki/)((?!:).)*$')):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])


# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import datetime
# import random
# import re
# import requests


# random.seed(datetime.datetime.now())

HEADERS_WIKI = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
}


# def getLinks(articleUrl):
#     # html = urlopen('http://en.wikipedia.org{}'.format(articleUrl))
#     us_url = 'http://en.wikipedia.org{}'.format(articleUrl)
#     html = requests.get(us_url, headers=HEADERS_WIKI)
#     bs = BeautifulSoup(html.text, 'html.parser')
#     return bs.find('div', {'id':'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))

# links = getLinks('/wiki/Kevin_Bacon')
# while len(links) > 0:
#     newArticle = links[random.randint(0, len(links)-1)].attrs['href']
#     print(newArticle)
#     links = getLinks(newArticle)


# from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import requests

def get_html(pageUrl):
    full_url = 'http://en.wikipedia.org{}'.format(pageUrl)
    get_result = requests.get(full_url, headers=HEADERS_WIKI)
    html = get_result.text
    return html

pages = set()
# def getLinks(pageUrl):
#     global pages
#     # html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
    
#     html = get_html(pageUrl)
   
#     bs = BeautifulSoup(html, 'html.parser')

#     for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
#         if 'href' in link.attrs:
#             if link.attrs['href'] not in pages:
#                 #We have encountered a new page
#                 newPage = link.attrs['href']
#                 print(newPage)
#                 pages.add(newPage)
#                 getLinks(newPage)


def getLinks(pageUrl):
    # global pages
    # html = urlopen('http://en.wikipedia.org{}'.format(pageUrl))
    html = get_html(pageUrl)
    bs = BeautifulSoup(html, 'html.parser')
    try:
        print(bs.h1.get_text())
        print(bs.find(id ='mw-content-text').find_all('p')[0].get_text())
        print(bs.find(id='ca-edit').find('span').find('a').attrs['href'])
    except AttributeError:
        print('This page is missing something! Continuing.')
    
    for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:
                #We have encountered a new page
                newPage = link.attrs['href']
                print('-'*20)
                print(newPage)
                pages.add(newPage)
                getLinks(newPage)


getLinks('')    