from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from Recursive.items import RecursiveItem
import urlparse


class RecursiveSpider(CrawlSpider):
    name = "ry"
    allowed_domains = ["nuevaya.com.ni"]
    start_urls = ['http://nuevaya.com.ni']
    
    rules = (
        Rule(SgmlLinkExtractor(allow = ("nuevaya.com.ni/*",)), callback = 'parse_item', follow=False),)
        
    def parse_item(self, response) :
        sel = Selector(response)
        item = RecursiveItem()
        item['URL'] = "test"#response.request.url
        Title = (str(response.xpath('//article/@id').extract()).split('-')[1])
        title = Title[0:len(Title)-2]
        item['TITLE'] = sel.xpath('//*[@id="post-'+title+'"]/div[1]/header/h1/text()').extract()
        item['CONTENT'] = sel.xpath('//*[@id="post-'+title+'"]/div[3]/p/text()').extract()
        return item
        
        
        
        
        
        
        
        
        