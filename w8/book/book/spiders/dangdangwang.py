import scrapy
import json


class DangdangwangSpider(scrapy.Spider):
    name = "dangdangwang"
    allowed_domains = ["e.dangdang.com"]
    start_urls = ["http://e.dangdang.com/media/api.go?action=mediaCategoryLeaf&promotionType=1&deviceSerialNo=html5&macAddr=html5&channelType=html5&permanentId=20231108154455819299767839324518905&returnType=json&channelId=70000&clientVersionNo=6.8.0&platformSource=DDDS-P&fromPlatform=106&deviceType=pconline&token=&start=42&end=62&category=JSJWL&dimension=dd_sale&order=0"]

    def parse(self, response):
        json_list = json.loads(response.text)
        
        for i in json_list['data']['saleList']: #遍历每一本书 获取其中需要的数据
            author = i['mediaList'][0]["authorPenname"]
            imgSrc = i['mediaList'][0]["coverPic"]
            name = i['mediaList'][0]["title"]
            price =i['mediaList'][0]["lowestPrice"]
            print(author,name,imgSrc,price)
            
            #导入items.py 中的类 也就是我们刚刚定义好的数据结构 会定义成一个字典格式的数据结构
            from book.items import BookItem
            book = BookItem(author=author,imgSrc=imgSrc,name=name,price=price)
            
            yield book
