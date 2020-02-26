from krishascrapy.items import RentBuilding
from .spider import BuildingSpider

class RentBuildingSpider(BuildingSpider):
    name = "rent-building"
    list_url_template = 'https://krisha.kz/arenda/zdanija/?page='
    
    def __init__(self):
        self.ad = RentBuilding()
    
    def parse_ad(self, response):
        ad = super().parse_ad(response)
        ad['rent_unit'] = self.getFieldValue(response, 'rent.square')
        
        return ad