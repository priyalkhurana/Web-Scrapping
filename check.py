import scrapy
import re
from locations.categories import Code
from locations.items import GeojsonPointItem

class TimhortonsSpider(scrapy.Spider):
    chain_name = 'timhorton'
    name = "timhortons_mex_dac"
    brand_name = 'Tim Hortons'
    spyder_type = 'chain'
    spider_chain_name = 'Tim Horton'
    spider_chain_id = 1397
    spider_categories = [Code.COFFEE_SHOP]

    allowed_domain=['https://timhortonsmx.com/es/index.html']
    start_urls=['https://timhortonsmx.com/es/suscursales.php']

    def parse(self,response):
        location= response.css('div.box')

        for loc in location:
            Address= loc.css('div.div-text::text')
            if Address:
                #extracting address
                address_match= re.search(r'Dirección:\s*([^<]+)', Address)
                extracted_address = address_match.group(1).strip() if address_match else None

                #extracting neighbourhood
                colonia_match = re.search(r'Colonia:\s*([^<]+)', Address)
                colonia = colonia_match.group(1).strip() if colonia_match else None

                #extracting ZIP
                cp_match = re.search(r'C.P.:\s*([^<]+)', Address)
                cp = cp_match.group(1).strip() if cp_match else None

                #extracting CITY
                ciudad_match = re.search(r'Ciudad:\s*([^<]+)', Address)
                ciudad = ciudad_match.group(1).strip() if ciudad_match else None
                data = {
                'chain_name': self.spider_chain_name,
                'chain_id': self.spider_chain_id,
                'brand': self.brand_name,
                'ref': loc.css('span.location-label::text').get(), 
                'name': loc.css('span.location-city::text').get(),
                'city': ciudad,
                'state':colonia,
                'addr_full': extracted_address,
                'postcode' : cp
                }
                yield GeojsonPointItem(**data)
