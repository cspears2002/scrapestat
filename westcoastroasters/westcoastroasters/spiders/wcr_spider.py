from scrapy.spider import BaseSpider
from scrapy.selector import Selector

from westcoastroasters.items import WestCoastRoastingItem

class WCRSpider(BaseSpider):
  name = "wcr"
  start_urls = ["http://www.westcoastroasting.com"]

  def parse(self, response):
    # Pull out the names and prices for the top sellers
    sel = Selector(response)
    top_sellers = sel.xpath(
      '//div[@id="SideTopSellers"]/div[@class="BlockContent"]/ul/li/div[@class="ProductDetails"]'
    )
    bean_names = top_sellers.xpath('strong/a/text()').extract()
    bean_prices = top_sellers.xpath('div[@class="ProductPriceRating"]/em/text()').extract()
    
    # Pass data to items
    items = []
    for name, price in zip(bean_names, bean_prices):
      item = WestCoastRoastingItem()
      item['bean_name'] = name
      item['price'] = price
      items.append(item)
    return items
# top_sellers_names = sel.xpath('//div[@id="SideTopSellers"]/div[@class="BlockContent"]/ul/li/div[@class="ProductDetails"]/strong/a/text()').extract()
# top_sllers_prices = sel.xpath('//div[@id="SideTopSellers"]/div[@class="BlockContent"]/ul/li/div[@class="ProductDetails"]/div[@class="ProductPriceRating"]/em/text()').extract()