# -*- coding: utf-8 -*-
from scrapy.linkextractors.sgml import SgmlLinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class PokecrawlerSpider(CrawlSpider):
    name = "pokecrawler"
    allowed_domains = ["dentrodapokebola.com"]
    start_urls = (
        'http://www.dentrodapokebola.com/',
    )
    f = open('log.txt', 'a')
    seen_urls = []

    rules = (Rule(SgmlLinkExtractor(deny=('tag', 'facebook', 'google-plus', 'twitter', 'comment', 'replytocom'))
                  , callback='parse_url', follow=True),)

    def parse_url(self, response):
        url = response.url
        if url not in self.seen_urls:
            self.seen_urls.append(url)
            if 'http://dentrodapokebola.com/eventos/hide-seek' in url:
                self.f.write(url.encode('ascii', 'ignore')+'\n')
