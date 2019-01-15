import scrapy
from scrapy import Spider
from scrapy import Request
from Yourhub2.signupAndLogin.models import Items
class image_scraper(scrapy.Spider):
    items = Items.objects.all()
    name = "Product_spider"
    allowed_domains=['www.google.ca']
    for i in Items:
        start_urls = ['https://www.google.com/search?q='+str("+".join(i.Item))+'&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjsoa2lv_LcAhVIR60KHZRVBaQQ_AUICygC&biw=1280&bih=615']
        #so that websites will not block access to the spider
        download_delay = 30
        def parse(self, response):
        # xpath is similar to an address that is used to find certain elements in HTML code,this info is then extracted
            image_link = response.xpath('//img/@src').extract()
        # yield goes through everything once, saves its spot, does not save info but sends it to the pipeline to get processed if need be
            yield{'image':image_link,}
