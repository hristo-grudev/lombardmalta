import scrapy


class LombardmaltaItem(scrapy.Item):
    title = scrapy.Field()
    description = scrapy.Field()
