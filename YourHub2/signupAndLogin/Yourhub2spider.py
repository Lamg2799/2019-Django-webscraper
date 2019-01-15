import scrapy
from scrapy import Spider
from scrapy import Request
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
class ProductSpider(scrapy.Spider):
    product = input("What product are you looking for? Keywords help for specific products: ")
    spider_name = "ProductSpider"
    allowed_domains=['www.amazon.ca']
    start_urls = ['https://www.amazon.ca/s/ref=nb_sb_noss_2?url=search-alias%3Daps&field-keywords='+product]
    #so that websites will not block access to the spider
    download_delay = 30
    def parse(self, response):
        # xpath is similar to an address that is used to find certain elements in HTML code,this info is then extracted
        product_title = response.xpath('//*/div/div/div/div[2]/div[1]/div[1]/a/@title').extract()
        product_price = response.xpath('//span[contains(@class,"s-price")]/text()').extract()
        product_url = response.xpath('//*/div/div/div/div[2]/div[1]/div[1]/a/@href').extract()
        # yield goes through everything once, saves its spot, does not save info but sends it to the pipeline to get processed if need be
        yield{'product_title': product_title, 'product_price': product_price, 'url': product_url,}
                               #it is checking the same url, no generality, need to find, maybe just do like 5 pages, also see if you can have it sort from high to low and find match with certain amount of key words

