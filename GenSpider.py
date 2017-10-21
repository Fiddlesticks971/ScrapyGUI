
from scrapy.http import Request
from scrapy.selector import Selector
from scrapy.spiders import Spider

class Spider(Spider):
    def __init__(self,_name,_target,_domain):
        self.domain = _domain
        self.name = _name
        self.start_urls= [_tartget]
    def parse(self,response):
        print('go spider')
        
