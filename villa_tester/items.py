import scrapy


class VillaScraperItem(scrapy.Item):
    url = scrapy.Field(serializer=str)
    where_from = scrapy.Field(serializer=str)
    error_message = scrapy.Field(serializer=str)
    link_text = scrapy.Field(serializer=str)
