from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.linkextractors import LinkExtractor
import urllib
from bs4 import BeautifulSoup

class RecursiveSpider(CrawlSpider):
    name = "ry"
    allowed_domains = ["nuevaya.com.ni"]
    start_urls = ['http://nuevaya.com.ni']
    
    rules = (
        Rule(SgmlLinkExtractor(allow = ("nuevaya.com.ni/*",)), callback = 'parse_item', follow=False),)
        
    def parse_item(self, response) :
        sel = Selector(response)
        item = RecursiveItem()
        item['URL'] = response.request.url
        f = urllib.urlopen("http://nuevaya.com.ni")
        s = f.read()
        f.close()
        soup = BeautifulSoup(s, 'html.parser')
        for div in soup.find_all('div'):
            idTitulo = (div.get('id'))
        print idTitulo
        item['TITLE'] = sel.xpath('//*[@id="post-'+idTitulo+'"]/div[1]/header/h1/text()').extract()
        item['CONTENT'] = sel.xpath('//*[@id="post-'+idTitulo+'"]/div[3]/p/text()').extract()
        return item
        
        
        
        
        
        
        
        
        