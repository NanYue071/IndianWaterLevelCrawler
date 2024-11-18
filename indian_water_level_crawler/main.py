# _*_ coding: utf-8 _*_
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

if __name__ == "__main__":
    process = CrawlerProcess(get_project_settings())

    process.crawl("ship")
    print('-----爬虫启动-----')
    process.start()
