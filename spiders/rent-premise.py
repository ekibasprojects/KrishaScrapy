from krishascrapy.items import RentPremise
from .spider import PremiseSpider

class RentPremiseSpider(PremiseSpider):
    name = "rent-premise"
    list_url_template = 'https://krisha.kz/arenda/pomeshhenija/?page='
    
    def __init__(self):
        self.ad = RentPremise()
    
    def parse_ad(self, response):
        ad = super().parse_ad(response)
        ad['rent_unit'] = self.getFieldValue(response, 'rent.square')
        
        return ad