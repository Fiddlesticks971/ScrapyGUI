
from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.spiders import Spider

class MySpider(Spider):
    
    name = "AutoSpider"
    
    def __init__(self):
    
        self.domain = "google.com"
        self.start_urls= ["https://www.google.com"]
        
    def parse(self,response):
        print('go spider')
        
