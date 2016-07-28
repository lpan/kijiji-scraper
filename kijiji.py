import sys
import pickle
import webbrowser
import requests
import os.path
from bs4 import BeautifulSoup

class Listings(object):
    def __init__(self, titles, prices, links, size):
        self.titles = titles
        self.prices = prices
        self.links = links
        self.size = size