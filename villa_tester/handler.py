import imp
import json
import statistics
import sys
from datetime import datetime

import pytz
from scrapy.crawler import CrawlerProcess

from settings import SCRAPY_SETTINGS, TIMEZONE
from spiders.auto_scraper import VillaSpider

sys.modules["sqlite"] = imp.new_module("sqlite")
sys.modules["sqlite3.dbapi2"] = imp.new_module("sqlite.dbapi2")


def lambda_handler(event, context):
    tz = pytz.timezone(TIMEZONE)
    now_str = datetime.now(tz).strftime("%d-%m-%Y_%H:%M")

    scrapy_settings = SCRAPY_SETTINGS
    scrapy_settings["FEED_URI"] = scrapy_settings["FEED_URI"].format(now_str)

    process = CrawlerProcess(scrapy_settings)
    process.crawl(VillaSpider)
    crawler = process.create_crawler(VillaSpider)
    process.crawl(crawler)
    process.start()

    stats = crawler.stats.get_stats()
    total_time = (stats['finish_time'] - stats['start_time']).total_seconds() / 60
    mean_response_time = statistics.mean(crawler.spider.response_times)

    result = f"{stats['downloader/request_count']} requests in  {round(total_time, 2)} minutes" \
             f" with average response time of {round(mean_response_time, 2)} seconds"

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": result,
        }),
    }
