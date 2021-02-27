from scrapy import cmdline

cmdline.execute('scrapy crawl douban_spider'.split())


"""
# 项目启动
scrapy crawl douban_spider

# 启动并导出文件
导出csv 
scrapy crawl douban_spider -o test.csv
导出json
scrapy crawl douban_spider -o test.json



"""