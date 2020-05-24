from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from settings import ERROR_MESSAGES
from items import VillaScraperItem

link_traceback = {}


class VillaSpider(CrawlSpider):
    name = 'VillaSpider'
    allowed_domains = ['blog.pazmi.no']
    link_extractor = LinkExtractor(deny=(r".+\?p=[0-9]+.*", r".+\/[0-9]{3,10}(\-[a-zA-Z0-9])+.*"))
    # allowed_domains = ['shoponline.villamarket.com']
    response_times = []
    start_urls = [
        # 'https://shoponline.villamarket.com'
        "https://blog.pazmi.no/"
    ]

    rules = (
        Rule(link_extractor, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        links = self.link_extractor.extract_links(response)
        for link in links:
            if not link.nofollow:
                link_traceback[link.url] = f"{response.url} ----> {link.text.strip()}"

        response_time = response.meta.get("download_latency")
        if response_time:
            self.response_times.append(response_time)

        if response.status >= 400:
            yield VillaScraperItem(url=response.url, where_from=link_traceback.get(response.url, "Main Page"),
                                   error_message=f"{response.status} - {ERROR_MESSAGES.get(response.status)}",
                                   link_text=response.meta["link_text"])
