import scrapy


class PrivateimoveisSpider(scrapy.Spider):
    name = "privateimoveis"
    allowed_domains = ["privateimoveis.com"]
    start_urls = ["https://privateimoveis.com/"]

    def parse(self, response):
        pass
