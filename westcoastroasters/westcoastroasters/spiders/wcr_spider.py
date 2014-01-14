from scrapy.spider import BaseSpider
from scrapy.selector import Selector

class WCRSpider(BaseSpider):
  name = "wcr"
  start_urls = ["http://www.westcoastroasting.com"]

  def parse(self, response):
    sel = Selector(response)
    top_sellers = sel.xpath('//div[@id="SideTopSellers"]/div[@class="BlockContent"]/ul/li/div[@class="ProductDetails"]')
    bean_names = top_sellers.xpath('strong/a/text()').extract()
    bean_prices = top_sellers.xpath('div[@class="ProductPriceRating"]/em/text()').extract()
    print bean_names, bean_prices
# top_sellers_names = sel.xpath('//div[@id="SideTopSellers"]/div[@class="BlockContent"]/ul/li/div[@class="ProductDetails"]/strong/a/text()').extract()
# top_sllers_prices = sel.xpath('//div[@id="SideTopSellers"]/div[@class="BlockContent"]/ul/li/div[@class="ProductDetails"]/div[@class="ProductPriceRating"]/em/text()').extract()