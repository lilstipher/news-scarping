import scrapy



class DummySpider(scrapy.Spider):
    name = 'test'
    def start_requests(self):
        urls = [
            'https://www.wikipedia.org/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self,response):
       self.log(response.body)