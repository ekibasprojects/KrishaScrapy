import scrapy
from scrapy.exceptions import CloseSpider
import pandas as pd

class RentShopSpider(scrapy.Spider):
    name = "phones"
    url_template = 'https://krisha.kz/a/ajaxPhones?id='
    
    def __init__(self):
        self.phones = pd.read_csv('phone_ids.csv')
    
    def start_requests(self):
        phones = self.phones['phone_id']
#        urls = [self.url_template + phone_id for phone_id in phones]
        for phone_id in phones:
            yield scrapy.Request(self.url_template + str(phone_id), headers={'x-requested-with': 'XMLHttpRequest'}, meta={'phone_id': phone_id}, callback=self.parse)

    def parse(self, response):
        yield {
                'phone_id': response.meta['phone_id'],
                'phones': response.body
                }