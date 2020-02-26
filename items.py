# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

def serialize_price(value):
    return int(value.replace(u'\xa0', u''))

class Sell(scrapy.Item):
    exchange = scrapy.Field()
    
class Rent(scrapy.Item):
    pass

class Ad(scrapy.Item):
    id = scrapy.Field()
    title = scrapy.Field()
    price = scrapy.Field(serializer=serialize_price)
    description = scrapy.Field()
    createdAt = scrapy.Field()
    addedAt = scrapy.Field()
    sectionAlias = scrapy.Field()
    categoryAlias = scrapy.Field()
    storage = scrapy.Field()
    appliedPaidServices = scrapy.Field()
    agent = scrapy.Field()
    agent_id = scrapy.Field()
    phone_id = scrapy.Field()
    photos = scrapy.Field()
    country = scrapy.Field()
    city = scrapy.Field()
    district = scrapy.Field()
    microdistrict = scrapy.Field()
    street = scrapy.Field()
    house_num = scrapy.Field()
    corner_street = scrapy.Field()
    lat = scrapy.Field()
    lon = scrapy.Field()

class Apt(Ad):
    rooms = scrapy.Field()
    building_raw = scrapy.Field()
    building_type = scrapy.Field()
    building_name = scrapy.Field()
    sq_raw = scrapy.Field()
    sq = scrapy.Field()
    sq_l = scrapy.Field()
    sq_k = scrapy.Field()
    floor_raw = scrapy.Field()
    floor = scrapy.Field()
    bathroom = scrapy.Field()
    former_hostel = scrapy.Field()
    year = scrapy.Field()
    floors = scrapy.Field()
    phone = scrapy.Field()
    internet = scrapy.Field()
    balcony = scrapy.Field()
    balcony_g = scrapy.Field()
    door = scrapy.Field()
    parking = scrapy.Field()
    furniture = scrapy.Field()
    flooring = scrapy.Field()
    ceiling = scrapy.Field()
    security = scrapy.Field()
    
    condition = scrapy.Field()

class SellApt(Apt, Sell):
    mortgage = scrapy.Field()

class RentApt(Apt, Rent):
    period = scrapy.Field()
    
class House(Ad):
    rooms = scrapy.Field()
    building_raw = scrapy.Field()
    building_type = scrapy.Field()
    bathroom = scrapy.Field()
    year = scrapy.Field()
    sq_raw = scrapy.Field()
    sq = scrapy.Field()
    sq_l = scrapy.Field()
    sq_k = scrapy.Field()
    sq_land = scrapy.Field()
    floors = scrapy.Field()
    ceiling = scrapy.Field()
    roof = scrapy.Field()
    fence = scrapy.Field()
    sewage = scrapy.Field()
    water = scrapy.Field()
    electricity = scrapy.Field()
    gas = scrapy.Field()
    heating = scrapy.Field()
    phone = scrapy.Field()
    internet = scrapy.Field()
    furniture = scrapy.Field()
    security = scrapy.Field()
    condition = scrapy.Field()
    
class SellHouse(House, Sell):
    mortgage = scrapy.Field()
    
class RentHouse(House, Rent):
    period = scrapy.Field()
    
    
class Dacha(Ad):
    building_type = scrapy.Field()
    floors = scrapy.Field()
    sq = scrapy.Field()
    sq_land = scrapy.Field()
    complex_name = scrapy.Field()
    water = scrapy.Field()
    irrigation = scrapy.Field()
    electricity = scrapy.Field()
    gas = scrapy.Field()
    fence = scrapy.Field()
    phone = scrapy.Field()
    sewage = scrapy.Field()
    
class SellDacha(Dacha, Sell):
    mortgage = scrapy.Field()
    
class RentDacha(Dacha, Rent):
    period = scrapy.Field()   
    
class Office(Ad):
    office_type = scrapy.Field()
    complex_name = scrapy.Field()
    rooms = scrapy.Field()
    sq = scrapy.Field()
    year = scrapy.Field()
    condition = scrapy.Field()
    phone_lines = scrapy.Field()
    ceiling = scrapy.Field()
    security = scrapy.Field()
    entrance = scrapy.Field()
    internet = scrapy.Field()
    parking = scrapy.Field()
    
class SellOffice(Office, Sell):
    mortgage = scrapy.Field()
    
class RentOffice(Office, Rent):
    period = scrapy.Field()
    
class Premise(Ad):
    sq = scrapy.Field()
    sq_land = scrapy.Field()
    year = scrapy.Field()
    condition = scrapy.Field()
    ceiling = scrapy.Field()
    security = scrapy.Field()
    parking = scrapy.Field()
    phone_lines = scrapy.Field()
    internet = scrapy.Field()
    
class SellPremise(Premise, Sell):
    mortgage = scrapy.Field()
    
class RentPremise(Premise, Rent):
    rent_unit = scrapy.Field()
    
class Building(Ad):
    building_type = scrapy.Field()
    sq = scrapy.Field()
    sq_land = scrapy.Field()
    year = scrapy.Field()
    floors = scrapy.Field()
    condition = scrapy.Field()
    phone_lines = scrapy.Field()
    roof = scrapy.Field()
    internet = scrapy.Field()
    ceiling = scrapy.Field()
    parking = scrapy.Field()
    security = scrapy.Field()
    
class SellBuilding(Building, Sell):
    mortgage = scrapy.Field()
    
class RentBuilding(Building, Rent):
    rent_unit = scrapy.Field()
    

class Shop(Ad):
    sq = scrapy.Field()
    kind = scrapy.Field()
    shop_type = scrapy.Field()
    complex_name = scrapy.Field()
    phone = scrapy.Field()
    internet = scrapy.Field()
    security = scrapy.Field()

class SellShop(Shop, Sell):
    pass

class RentShop(Shop, Rent):
    rent_unit = scrapy.Field()
    
class Warehouse(Ad):
    warehouse_type = scrapy.Field()
    year = scrapy.Field()
    sq_land = scrapy.Field()
    sq_prod = scrapy.Field()
    sq_storage = scrapy.Field()
    sq_office = scrapy.Field()
    ceiling_prod = scrapy.Field()
    ceiling_storage = scrapy.Field()
    rail = scrapy.Field()
    max_energy = scrapy.Field()
    power_plant = scrapy.Field()
    communications = scrapy.Field()
    phone_lines = scrapy.Field()
    
class SellWarehouse(Warehouse, Sell):
    mortgage = scrapy.Field()
    
class RentWarehouse(Warehouse, Rent):
    pass
    
class Other(Ad):
    sq = scrapy.Field()
    sq_land = scrapy.Field()
    estate_type = scrapy.Field()
    business = scrapy.Field()
    location = scrapy.Field()
    communications = scrapy.Field()

class SellOther(Other, Sell):
    mortgage = scrapy.Field()
    
class RentOther(Other, Rent):
    pass
    
class Land(Ad):
    sq = scrapy.Field()
    divisible = scrapy.Field()
    location = scrapy.Field()
    kind = scrapy.Field()
    communications = scrapy.Field()

class SellLand(Land, Sell):
    mortgage = scrapy.Field()
    
class Room(Ad):
    sq = scrapy.Field()
    floor = scrapy.Field()
    phone = scrapy.Field()
    internet = scrapy.Field()
    furniture = scrapy.Field()
    
class RentRoom(Room, Rent):
    pass
    
    
class Agent(scrapy.Item):
    id = scrapy.Field()
    agent_type = scrapy.Field()
    name = scrapy.Field()
    address = scrapy.Field()
    time = scrapy.Field()
    

    
    
    