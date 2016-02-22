from scrapy.selector import Selector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from Recursive.items import RecursiveItem

class RecursiveSpider(CrawlSpider):
    name = "nd"
    allowed_domains = ["elnuevodiario.com.ni"]
    start_urls = ['http://www.elnuevodiario.com.ni/sucesos/']
    
    rules = (
        Rule(SgmlLinkExtractor(allow = ("/sucesos/*",)), callback = 'parse_item', follow=False),)
        
    def parse_item(self, response) :
        sel = Selector(response)
        item = RecursiveItem()
        item['URL'] = response.request.url
        item['TITLE'] = sel.xpath('/html/body/main/section/section/section/header/section/div[1]/h1/text()').extract()
        item['CONTENT'] = sel.xpath('/html/body/main/section/section/section/section/div[2]/p/text()').extract()
        return item
        