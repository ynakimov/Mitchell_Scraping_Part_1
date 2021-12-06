
# from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

import requests

pages = set()
random.seed(datetime.datetime.now().minute)

HEADERS_SBER_BANK = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
}
HEADERS_WIKI = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
}
HEADERS_ORELLY = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36',
}

last_external_link = 'http://oreilly.com'
prelast_external_link = ''

def get_html(startingPage, label_redirects=1):
    result = {
        'html':'',
        'status':0
    }
    if label_redirects == 1:
        allow_redirects = True
    else:
        allow_redirects = False

    # full_url = 'http://en.wikipedia.org{}'.format(pageUrl)
    get_result = requests.get(startingPage, headers=HEADERS_ORELLY, allow_redirects=allow_redirects)
    result['status'] = get_result.status_code
    html = get_result.text
    result['html'] = html

    return result


def getInternalLinks(bs, includeUrl):
    includeUrl = '{}://{}'.format(urlparse(includeUrl).scheme, urlparse(includeUrl).netloc)
    internalLinks = []

    #Finds all links that begin with a "/"
    for link in bs.find_all('a', href=re.compile('^(/|.*'+includeUrl+')')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                if(link.attrs['href'].startswith('/')):
                    internalLink = includeUrl+link.attrs['href']
                else:
                    internalLink = link.attrs['href']
            if internalLink not in internalLinks:
                internalLinks.append(internalLink)
    return internalLinks


#Retrieves a list of all external links found on a page
def getExternalLinks(bs, excludeUrl):
    externalLinks = []
    #Finds all links that start with "http" that do
    #not contain the current URL
    for link in bs.find_all('a', href=re.compile('^(http|www)((?!'+excludeUrl+').)+(?!(\.pdf|\.xls|\.doc))$')):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks


def getRandomExternalLink(startingPage):
    # html = urlopen(startingPage)
    
    global last_external_link

    result = get_html(startingPage)
    if result['status'] == 200:
        html = result['html']
    else:
       html = get_html(last_external_link)

    bs = BeautifulSoup(html, 'html.parser')
    externalLinks = getExternalLinks(bs, urlparse(startingPage).netloc)

    if len(externalLinks) == 0:
        print('No external links, looking around the site for one')
        domain = '{}://{}'.format(urlparse(startingPage).scheme, urlparse(startingPage).netloc)
        internalLinks = getInternalLinks(bs, domain)
        if len(internalLinks) == 0:
            return getRandomExternalLink(last_external_link)
            
        else:
            return getRandomExternalLink(internalLinks[random.randint(0,
                                    len(internalLinks)-1)]) 
    else:
        last_external_link = startingPage
        externalLink = externalLinks[random.randint(0, len(externalLinks)-1)]
        return externalLink


def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink(startingSite)
    print('Random external link is: {}'.format(externalLink))
    followExternalOnly(externalLink)

            
followExternalOnly(last_external_link)