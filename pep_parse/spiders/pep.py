import scrapy
from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse_pep(self, response):
        pep_number = response.css('ul.breadcrumbs > li + li + li::text').get()
        data = {
            'number': pep_number.replace('PEP ', ''),
            'name': response.css('h1.page-title::text').get(),
            'status': response.css('dt:contains("Status") + dd::text').get()
        }
        yield PepParseItem(data)

    def parse(self, response):
        table = response.css('section[id="numerical-index"]')
        pep_links = table.css('a[class="pep reference internal"]::attr(href)').getall()
        for link in pep_links:
            yield response.follow(link, callback=self.parse_pep)

