from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from Recursive.items import RecursiveItem
import urlparse

class RecursiveSpider(CrawlSpider):
    name = "tn"
    allowed_domains = ["tn8.tv"]
    start_urls = ['http://www.tn8.tv/ultima-hora/']
    
    rules = (
        Rule(SgmlLinkExtractor(allow = ("/ultima-hora/*",)), callback = 'parse_item', follow=False),)
        
    def parse_item(self, response) :
        sel = Selector(response)
        item = RecursiveItem()
        item['URL'] = response.request.url
        idTitulo = item['URL'].split('/')[4].split('-')[0]
        item['TITLE'] = sel.xpath('//*[@id="post-'+idTitulo+'"]/header/h1/text()').extract()
        item['CONTENT'] = sel.xpath('//*[@id="post-'+idTitulo+'"]/div[2]/p[1]/text()').extract()
        return item
        