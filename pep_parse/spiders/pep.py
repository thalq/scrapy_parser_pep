import re

import scrapy
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):

    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse_pep(self, response):
        name = response.css('h1.page-title::text').get()
        number = (re.findall(r'(\d+)', name))[0]
        data = {
            'number': number,
            'name': name,
            'status': response.css('dt:contains("Status") + dd::text').get()
        }
        yield PepParseItem(data)

    def parse(self, response):

        table = response.css('section[id="numerical-index"]')
        pep_links = table.css(
            'a[class="pep reference internal"]::attr(href)'
        ).getall()
        for link in pep_links:
            yield response.follow(link, callback=self.parse_pep)
