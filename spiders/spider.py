import scrapy
from scrapy.exceptions import CloseSpider
import json
from krishascrapy.items import Ad
from krishascrapy.items import Apt
from krishascrapy.items import House
from krishascrapy.items import Dacha
from krishascrapy.items import Premise
from krishascrapy.items import Building
from krishascrapy.items import Shop
from krishascrapy.items import Warehouse
from krishascrapy.items import Other
from krishascrapy.items import Land
from krishascrapy.items import Agent

class AdSpider(scrapy.Spider):
    list_url_template = ''
    ad_url_template = '/a/show/'
    
    def __init__(self):
        self.ad = Ad()
    
    def start_requests(self):
        page_count_limit = 6001
        urls = [self.list_url_template + str(i) for i in range(1, page_count_limit)]
        for url in urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        cards = response.css(".a-card")
        if len(cards) > 0:
            for card in cards:
                ad_id = card.attrib['data-id']
                url = self.ad_url_template + ad_id
                request = scrapy.Request(response.urljoin(url), callback=self.parse_ad)
                yield request
        else:
            raise CloseSpider('No more results.')
            
    # test: 1 page 5 ads
#    def parse(self, response):
#        cards = response.css(".a-card")
#        if len(cards) > 0:
#            for i in range(5):
#                ad_id = cards[i].attrib['data-id']
#                url = self.ad_url_template + ad_id
#                request = scrapy.Request(response.urljoin(url), callback=self.parse_ad)
#                yield request
#        else:
#            raise CloseSpider('No more results.')
            
    def parse_ad(self, response):
        ad = self.ad
        
        jsdata = response.xpath("//*[contains(@id, 'jsdata')]/text()").get().strip()
        jsdata_json = json.loads(jsdata.strip('var data = ')[:-1])
        advert = jsdata_json['advert']
        ad['id'] = advert['id']
        ad['storage'] = advert['storage']
        ad['createdAt'] = advert['createdAt']
        ad['addedAt'] = advert['addedAt']
        ad['sectionAlias'] = advert['sectionAlias']
        ad['categoryAlias'] = advert['categoryAlias']
        ad['photos'] = advert['photos']
        address = advert['address']
        ad['country'] = address['country']
        ad['city'] = address['city'] if 'city' in address else ''
        ad['district'] = address['district'] if 'district' in address else ''
        ad['microdistrict'] = address['microdistrict'] if 'microdistrict' in address else ''
        ad['street'] = address['street'] if 'street' in address else ''
        ad['house_num'] = address['house_num'] if 'house_num' in address else ''
        ad['corner_street'] = address['corner_street'] if 'corner_street' in address else ''
        ad_map = advert['map']
        ad['lat'] = ad_map['lat']
        ad['lon'] = ad_map['lon']
        
        ad['title'] = response.css('.offer__advert-title h1::text').get().strip()
        
        description_items = response.css('.offer__description .text .a-text-white-spaces::text').getall()
        ad['description'] = list(map(lambda x: x.strip(), description_items))
        ad['price'] = response.css('.offer__price::text').get().strip()
        
        dig_data_text = response.xpath("//script[contains(text(), 'window.digitalData')]/text()").get().strip()
        dig_data = json.loads(dig_data_text.strip('window.digitalData = ')[:-1])
        ad['appliedPaidServices'] = dig_data['product']['appliedPaidServices']
        
        users = response.xpath('//div[has-class("user-type-3")] | //div[has-class("user-type-2")]')
        if len(users):
            if len(users.xpath('//div[has-class("user-type-2")]')):
                ad['agent'] = 2
            elif len(users.xpath('//div[has-class("user-type-3")]')):
                ad['agent'] = 3
            ad['agent_id'] = users.attrib['data-id']
        else:
            ad['agent'] = 1
        
        ad['phone_id'] = response.xpath("//*[contains(@id, 'tm-telephone-body')]").attrib['data-id']
        
        return ad
        
    def getFieldValue(self, response, fieldAlias):
        els = response.xpath("//*[contains(@data-name, '" + fieldAlias + "')]")
        if len(els):
            prim = els.css(".offer__advert-short-info")
            if len(prim):
                return prim.css('::text').get().strip()
            else:
                return  els.xpath('following-sibling::dd[1]/text()').get().strip()

class AptSpider(AdSpider):
    def __init__(self):
        self.ad = Apt()
        
    def parse_ad(self, response):
        ad = super().parse_ad(response)
        ad['building_raw'] = self.getFieldValue(response, 'flat.building')
            
        # Might change to handle 2 elements    
        building_name_els = response.xpath("//*[contains(@data-name, 'map.complex')]")
        if len(building_name_els):
            ad['building_name'] = building_name_els.css('.offer__advert-short-info *::text').get().strip()
        else:
            ad['building_name'] = ""
            
        ad['sq_raw'] = self.getFieldValue(response, 'live.square')
        ad['floor_raw'] = self.getFieldValue(response, 'flat.floor')  
        ad['bathroom'] = self.getFieldValue(response, 'flat.toilet')
        ad['former_hostel'] = self.getFieldValue(response, 'flat.priv_dorm')            
        ad['phone'] = self.getFieldValue(response, 'flat.phone')
        ad['internet'] = self.getFieldValue(response, 'inet.type')
        ad['balcony'] = self.getFieldValue(response, 'flat.balcony')
        ad['balcony_g'] = self.getFieldValue(response, 'flat.balcony_g')
        ad['door'] = self.getFieldValue(response, 'flat.door')
        ad['parking'] = self.getFieldValue(response, 'flat.parking')
        ad['furniture'] = self.getFieldValue(response, 'flat.furniture')
        ad['flooring'] = self.getFieldValue(response, 'flat.flooring')
        ad['ceiling'] = self.getFieldValue(response, 'flat.ceiling')
        ad['security'] = self.getFieldValue(response, 'flat.security')
        ad['condition'] = self.getFieldValue(response, 'flat.renovation')
        
        #ad['rooms'] = ""
        #ad['buildin_type'] = ""
        #ad['year'] = ""
        #ad['sq'] = ""
        #ad['sq_l'] = ""
        #ad['sq_k'] = ""
        #ad['floor'] = ""
        #ad['floors'] = ""

        return ad
    
class HouseSpider(AdSpider):
    def __init__(self):
        self.ad = House()
        
    def parse_ad(self, response):
        ad = super().parse_ad(response)
 
        ad['building_raw'] = self.getFieldValue(response, 'house.building')
            
        ad['sq_raw'] = self.getFieldValue(response, 'live.square')
        ad['sq_land'] = self.getFieldValue(response, 'land.square')
        ad['bathroom'] = self.getFieldValue(response, 'house.toilet')
        ad['floors'] = self.getFieldValue(response, 'house.floor_num') 
        ad['ceiling'] = self.getFieldValue(response, 'ceiling') 
        ad['roof'] = self.getFieldValue(response, 'house.roof')
        ad['fence'] = self.getFieldValue(response, 'land.fence')
        
        ad['sewage'] = self.getFieldValue(response, 'cmtn.sewage')
        ad['water'] = self.getFieldValue(response, 'cmtn.water')
        ad['electricity'] = self.getFieldValue(response, 'cmtn.electricity')
        ad['gas'] = self.getFieldValue(response, 'cmtn.gas')
        ad['heating'] = self.getFieldValue(response, 'cmtn.heating')
        ad['phone'] = self.getFieldValue(response, 'cmtn.phone')
        ad['internet'] = self.getFieldValue(response, 'inet.type')
        ad['furniture'] = self.getFieldValue(response, 'live.furniture')
        ad['security'] = self.getFieldValue(response, 'house.security')
        ad['condition'] = self.getFieldValue(response, 'house.renovation')
        
        #ad['rooms'] = ""
        #ad['building_type'] = ""
        #ad['year'] = ""
        #ad['sq'] = ""
        #ad['sq_l'] = ""
        #ad['sq_k'] = ""

        return ad
    
class DachaSpider(AdSpider):
    def __init__(self):
        self.ad = Dacha()
        
    def parse_ad(self, response):
        ad = super().parse_ad(response)
        
        ad['building_type'] = self.getFieldValue(response, 'dacha.building')
        ad['floors'] = self.getFieldValue(response, 'house.floor_num')
        ad['sq'] = self.getFieldValue(response, 'live.square')
        ad['sq_land'] = self.getFieldValue(response, 'land.square')
        ad['complex_name'] = self.getFieldValue(response, 'dacha.complex_name')
        ad['water'] = self.getFieldValue(response, 'cmtn.water')
        ad['irrigation'] = self.getFieldValue(response, 'cmtn.irrigation')
        ad['electricity'] = self.getFieldValue(response, 'cmtn.electricity')
        ad['gas'] = self.getFieldValue(response, 'cmtn.gas')
        ad['fence'] = self.getFieldValue(response, 'land.fence')
        ad['phone'] = self.getFieldValue(response, 'cmtn.phone')
        ad['sewage'] = self.getFieldValue(response, 'cmtn.sewage')        

        return ad
    
class OfficeSpider(AdSpider):
    def __init__(self):
        self.ad = Dacha()
        
    def parse_ad(self, response):
        ad = super().parse_ad(response)
        
        ad['office_type'] = self.getFieldValue(response, 'office.type')
        ad['complex_name'] = self.getFieldValue(response, 'office.complex_name')
        ad['rooms'] = self.getFieldValue(response, 'com.rooms')
        ad['sq'] = self.getFieldValue(response, 'com.square')
        ad['year'] = self.getFieldValue(response, 'house.year')
        ad['condition'] = self.getFieldValue(response, 'office.renovation')
        ad['phone_lines'] = self.getFieldValue(response, 'com.phonenum')
        ad['ceiling'] = self.getFieldValue(response, 'ceiling')
        ad['security'] = self.getFieldValue(response, 'com.security')
        ad['entrance'] = self.getFieldValue(response, 'com.entrance')
        ad['internet'] = self.getFieldValue(response, 'inet.type')
        ad['parking'] = self.getFieldValue(response, 'com.parking')

        return ad
    
    
class PremiseSpider(AdSpider):
    def __init__(self):
        self.ad = Premise()
        
    def parse_ad(self, response):
        ad = super().parse_ad(response)
        
        ad['sq'] = self.getFieldValue(response, 'com.square')
        ad['sq_land'] = self.getFieldValue(response, 'land.square')
        ad['year'] = self.getFieldValue(response, 'house.year')
        ad['condition'] = self.getFieldValue(response, 'com.renovation')
        ad['ceiling'] = self.getFieldValue(response, 'ceiling')
        ad['security'] = self.getFieldValue(response, 'com.security')
        ad['parking'] = self.getFieldValue(response, 'com.parking')
        ad['phone_lines'] = self.getFieldValue(response, 'com.phonenum')
        ad['internet'] = self.getFieldValue(response, 'inet.type')

        return ad
    
class BuildingSpider(AdSpider):
    def __init__(self):
        self.ad = Building()
        
    def parse_ad(self, response):
        ad = super().parse_ad(response)
        
        ad['building_type'] = self.getFieldValue(response, 'building.building')
        ad['sq'] = self.getFieldValue(response, 'com.square')
        ad['sq_land'] = self.getFieldValue(response, 'land.square')
        ad['year'] = self.getFieldValue(response, 'house.year')
        ad['floors'] = self.getFieldValue(response, 'house.floor_num')
        ad['condition'] = self.getFieldValue(response, 'com.renovation')
        ad['phone_lines'] = self.getFieldValue(response, 'com.phonenum')
        ad['roof'] = self.getFieldValue(response, 'house.roof')
        ad['internet'] = self.getFieldValue(response, 'inet.type')
        ad['ceiling'] = self.getFieldValue(response, 'ceiling')
        ad['parking'] = self.getFieldValue(response, 'com.parking')
        ad['security'] = self.getFieldValue(response, 'com.security')
        
        return ad
    
class ShopSpider(AdSpider):
    def __init__(self):
        self.ad = Shop()
        
    def parse_ad(self, response):
        ad = super().parse_ad(response)
        
        ad['sq'] = self.getFieldValue(response, 'com.square')
        ad['kind'] = self.getFieldValue(response, 'shop.kind')
        ad['shop_type'] = self.getFieldValue(response, 'shop.type')
        ad['complex_name'] = self.getFieldValue(response, 'shop.complex_name')
        ad['phone'] = self.getFieldValue(response, 'cmtn.phone')
        ad['internet'] = self.getFieldValue(response, 'inet.type')
        ad['security'] = self.getFieldValue(response, 'com.security')
        
        return ad
    
class WarehouseSpider(AdSpider):
    def __init__(self):
        self.ad = Warehouse()
        
    def parse_ad(self, response):
        ad = super().parse_ad(response)
        
        ad['warehouse_type'] = self.getFieldValue(response, 'indust.type')
        ad['year'] = self.getFieldValue(response, 'house.year')
        ad['sq_land'] = self.getFieldValue(response, 'land.square')
        ad['sq_prod'] = self.getFieldValue(response, 'indust.prod_square')
        ad['sq_storage'] = self.getFieldValue(response, 'indust.store_square')
        ad['sq_office'] = self.getFieldValue(response, 'indust.office_square')
        ad['ceiling_prod'] = self.getFieldValue(response, 'indust.prod_ceiling')
        ad['ceiling_storage'] = self.getFieldValue(response, 'indust.store_ceiling')
        ad['rail'] = self.getFieldValue(response, 'indust.rail')
        ad['max_energy'] = self.getFieldValue(response, 'indust.max_electr')
        ad['power_plant'] = self.getFieldValue(response, 'indust.electr_station')
        ad['communications'] = self.getFieldValue(response, 'com.communications')
        ad['phone_lines'] = self.getFieldValue(response, 'com.phonenum')
        
        return ad
    
class LandSpider(AdSpider):
    def __init__(self):
        self.ad = Land()
        
    def parse_ad(self, response):
        ad = super().parse_ad(response)
        
        ad['sq'] = self.getFieldValue(response, 'land.square_a')
        ad['divisible'] = self.getFieldValue(response, 'land.separable')
        ad['location'] = self.getFieldValue(response, 'land.type')
        ad['kind'] = self.getFieldValue(response, 'land.earmarked')
        ad['communications'] = self.getFieldValue(response, 'com.communications')
        
        return ad
    
class RoomSpider(AdSpider):
    def __init__(self):
        self.ad = Land()
        
    def parse_ad(self, response):
        ad = super().parse_ad(response)
        
        ad['sq'] = self.getFieldValue(response, 'live.square')
        ad['floor'] = self.getFieldValue(response, 'flat.floor')
        ad['phone'] = self.getFieldValue(response, 'flat.phone')
        ad['internet'] = self.getFieldValue(response, 'inet.type')
        ad['furniture'] = self.getFieldValue(response, 'live.furniture')
        
        return ad
    
class OtherSpider(AdSpider):
    def __init__(self):
        self.ad = Other()
        
    def parse_ad(self, response):
        ad = super().parse_ad(response)
        
        ad['sq'] = self.getFieldValue(response, 'com.square')
        ad['sq_land'] = self.getFieldValue(response, 'land.square_a')
        ad['estate_type'] = self.getFieldValue(response, 'estate.type')
        ad['business'] = self.getFieldValue(response, 'estate.is_buss')
        ad['location'] = self.getFieldValue(response, 'land.type')
        ad['communications'] = self.getFieldValue(response, 'com.communications')
        
        return ad
    
    
class AgentSpider(scrapy.Spider):
    list_url_template = ''
    card_class = ''
    agent_url_template = '/pro/'
    
    def __init__(self):
        self.agent = Agent()
    
    def start_requests(self):
        page_count_limit = 500
        urls = [self.list_url_template + str(i) for i in range(1, page_count_limit)]
        for url in urls:
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        cards = response.css(self.card_class)
        if len(cards) > 0:
            for card in cards:
                url = card.attrib['href']
                request = scrapy.Request(response.urljoin(url), callback=self.parse_agent)
                yield request
        else:
            raise CloseSpider('No more results.')
            
    # test: 1 page 5 agents
#    def parse(self, response):
#        cards = response.css(self.card_class)
#        if len(cards) > 0:
#            for i in range(5):
#                url = cards[i].attrib['href']
#                request = scrapy.Request(response.urljoin(url), callback=self.parse_agent)
#                yield request
#        else:
#            raise CloseSpider('No more results.')
            
    def parse_agent(self, response):
        agent = self.agent
            
        phone_id = response.xpath("//*[contains(@id, 'tm-telephone-body')]")
        if len(phone_id):
            agent['id'] = phone_id.attrib['data-id']        
        
        return agent


        