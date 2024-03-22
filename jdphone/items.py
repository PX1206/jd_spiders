# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JdphoneItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()  # 标题

    price = scrapy.Field()  # 价格

    comment_num = scrapy.Field()  # 评价条数

    url = scrapy.Field()  # 商品链接

    info = scrapy.Field()  # 详细信息

    meta_title = scrapy.Field()

    meta_description = scrapy.Field()

    meta_keywords = scrapy.Field()
