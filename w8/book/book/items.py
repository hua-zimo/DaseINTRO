# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    name = scrapy.Field()   #书名
    author = scrapy.Field() #作者
    imgSrc = scrapy.Field() #图片
    price = scrapy.Field()  #价格
    pass
