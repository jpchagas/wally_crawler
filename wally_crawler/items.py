# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WallyCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    property_type = scrapy.Field()
    neighborhood = scrapy.Field()
    source_id = scrapy.Field()
    value = scrapy.Field()
    rooms = scrapy.Field()
    garage = scrapy.Field()
    m2 = scrapy.Field()
    title = scrapy.Field()
    description = scrapy.Field()
    real_state = scrapy.Field()
    property_features = scrapy.Field()
    condo_features = scrapy.Field()
