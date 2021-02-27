# Scrapy-douban-movie
> 豆瓣电影排名爬取 - 仅供学习

### 依赖环境
> mongodb、scrapy、pymongo

```
brew tap mongodb/brew
brew install mongodb-community@4.4
```
```
@ 符号后面的 4.4 是最新版本号。
安装信息：
配置文件：/usr/local/etc/mongod.conf
日志文件路径：/usr/local/var/log/mongodb
数据存放路径：/usr/local/var/mongodb
```
brew 启动：
```
brew services start mongodb-community@4.4
```
brew 停止：
```
brew services stop mongodb-community@4.4
```

scrapy 安装
```
pip3 install scrapy
or
sudo pip3 install Scrapy --upgrade --ignore-installed six
```


### 启动
第一种
```
python3 main.py
```

```
# 项目启动
scrapy crawl douban_spider

# 启动并导出文件
导出csv 
scrapy crawl douban_spider -o test.csv

导出json
scrapy crawl douban_spider -o test.json
```