import scrapy
from douban.items import DoubanItem


class DoubanSpiderSpider(scrapy.Spider):
    # 爬虫名字
    name = 'douban_spider' 
    # 允许域名
    allowed_domains = ['movie.douban.com']
    # 入口url，扔到调度器
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        """
        默认解析
        """
        movie_list = response.xpath("//div[@class='article']//ol[@class='grid_view']/li")
        
        for item in movie_list:
            # 单个item导入
            douban_item = DoubanItem()
            douban_item['serial_number'] = item.xpath(".//div[@class='item']//em/text()").extract_first()
            douban_item['movie_name'] = item.xpath(".//div[@class='info']/div[@class='hd']/a/span[1]/text()").extract_first()
            # 多行数据处理空格和\n
            content = item.xpath(".//div[@class='info']//div[@class='bd']/p[1]/text()").extract()
            douban_item['introduce'] = str(list(map(lambda item:"".join(item.split()),content))[1])
            douban_item['star'] = item.xpath(".//span[@class='rating_num']/text()").extract_first()
            douban_item['evaluate'] = item.xpath(".//div[@class='star']/span[4]/text()").extract_first()
            douban_item['describe'] = item.xpath(".//p[@class='quote']/span/text()").extract_first()
            # 将数据yield到pipelines中
            yield douban_item
        
        # 获取下一页的xpath
        next_link = response.xpath("//span[@class='next']/link/@href").extract()
        if next_link:
            next_link = next_link[0]
            yield scrapy.Request('https://movie.douban.com/top250'+next_link ,callback=self.parse)
            







