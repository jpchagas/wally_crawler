import scrapy
from mongoengine import *


class PrivateimoveisSpider(scrapy.Spider):
    name = "privateimoveis"
    allowed_domains = ["privateimoveis.com"]
    start_urls = ["https://privateimoveis.com/imovel/venda/apartamento-3-dormitorios-bairro-petropolis-121m2/porto-alegre/46267"]
    connect('local')


    def parse(self, response):
        property_type = response.xpath("/html/body/app-root/default-root/div[1]/app-property/div[1]/div[3]/div[1]/div/div[1]/text()").get()
        neighborhood = response.xpath("/html/body/app-root/default-root/div[1]/app-property/div[1]/div[3]/div[2]/div[1]/div/text()").get()
        source_id = response.xpath("/html/body/app-root/default-root/div[1]/app-property/div[1]/div[3]/div[1]/div/div[2]/text()").get()
        value = response.xpath("/html/body/app-root/default-root/div[1]/app-property/div[1]/div[3]/div[2]/div[2]/div/text()").get()
        rooms = response.xpath("/html/body/app-root/default-root/div[1]/app-property/div[1]/div[3]/div[3]/div[1]/div/div[1]/text()").get()
        garage =  response.xpath("/html/body/app-root/default-root/div[1]/app-property/div[1]/div[3]/div[3]/div[1]/div/div[2]/text()").get()
        m2 = response.xpath("/html/body/app-root/default-root/div[1]/app-property/div[1]/div[3]/div[3]/div[1]/div/div[3]/text()").get()
        title = response.xpath("//title/text()").get()
        description = response.xpath("/html/body/app-root/default-root/div[1]/app-property/div[1]/div[3]/div[4]/div[1]/div[2]/p[1]/text()").get()
        real_state = "private imoveis"
        property_features = response.xpath('//div[@id="collapseFeature"]/div/text()').getall()
        condo_features = response.xpath('//div[@id="collapseInfra"]/div/text()').getall()
            
        
        yield{
            # TODO: implement a way to get the images addresses
            'property_type': property_type,
            'neighborhood': neighborhood,
            'source_id': source_id,
            'value': value,
            'rooms': rooms,
            'garage': garage,
            'm2': m2,
            'title': title,
            'description': description,
            'real_state': real_state,
            'property_features' : property_features,
            'condo_features': condo_features
        }
