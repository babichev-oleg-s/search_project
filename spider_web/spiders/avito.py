import scrapy

class AvitoSpider(scrapy.Spider):
    name = 'avito'
    allowed_domains = ['avito.ru']
    start_urls = ['https://www.avito.ru/moskva_i_mo/sobaki?q=%D1%81%D0%BE%D0%B1%D0%B0%D0%BA%D0%B']


    def parse(self, response):
         pass
