##################### HEAD #######################

#Python 3 library

from urllib.request import urlopen 
from urllib.error import HTTPError 
from bs4 import BeautifulSoup

################### FUNCTIONS ####################


def getUrl(url): 

    try:
        html = urlopen(url)
        print(url)
    except:
        html = urlopen("http://"+ url)
        print(url)

    bs_obj = BeautifulSoup(html.read(), "lxml")

    return bs_obj

bs_obj = getUrl("http://www.pythonforbeginners.com/python-on-the-web/web-scraping-with-beautifulsoup/")
print(bs_obj)
print(" " * 3000)
print(bs_obj.find_all("li"))