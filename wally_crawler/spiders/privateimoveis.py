import scrapy


class PrivateimoveisSpider(scrapy.Spider):
    name = "privateimoveis"
    allowed_domains = ["privateimoveis.com"]
    start_urls = ["https://privateimoveis.com/imovel/venda/apartamento-3-dormitorios-bairro-petropolis-121m2/porto-alegre/46267"]

    def parse(self, response):
        yield{
            'title': response.xpath("//title/text()").get(),
            'value': response.xpath("/html/body/app-root/default-root/div[1]/app-property/div[1]/div[3]/div[2]/div[2]/div/text()").get(),
            'id': response.xpath("/html/body/app-root/default-root/div[1]/app-property/div[1]/div[3]/div[1]/div/div[2]/text()").get(),
            'neighborhood': response.xpath("/html/body/app-root/default-root/div[1]/app-property/div[1]/div[3]/div[2]/div[1]/div/text()").get(),
            'type': response.xpath("/html/body/app-root/default-root/div[1]/app-property/div[1]/div[3]/div[1]/div/div[1]/text()").get(),
            'rooms': response.xpath("/html/body/app-root/default-root/div[1]/app-property/div[1]/div[3]/div[3]/div[1]/div/div[1]/text()").get(),
            'garage':  response.xpath("/html/body/app-root/default-root/div[1]/app-property/div[1]/div[3]/div[3]/div[1]/div/div[2]/text()").get(),
            'm2': response.xpath("/html/body/app-root/default-root/div[1]/app-property/div[1]/div[3]/div[3]/div[1]/div/div[3]/text()").get(),
            'description': response.xpath("/html/body/app-root/default-root/div[1]/app-property/div[1]/div[3]/div[4]/div[1]/div[2]/p[1]/text()").get()
        }
