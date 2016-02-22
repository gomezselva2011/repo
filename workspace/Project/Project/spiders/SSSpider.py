from scrapy.selector import Selector
from scrapy.spider import BaseSpider
from Project.items import ProjectItem

class ProjectSpider(BaseSpider):
    name = "start"
    allowed_domains = ["elnuevodiario.com.ni"]
    start_urls = ['http://www.elnuevodiario.com.ni/sucesos/']
    
    def parse(self, response):
        sel = Selector(response)
        item = ProjectItem()
        item['title'] = sel.xpath('/html/body/main/section/section/div/div[1]/div[1]/div/section/article/div/div/h2/a/text()').extract()
        item['link'] = sel.xpath('/html/body/main/section/section/div/div[1]/div[1]/div/section/article/div/div/h2/a/@href').extract()
        return item
        
        