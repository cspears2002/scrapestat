from scrapy.spider import BaseSpider

class WCRSpider(BaseSpider):
  name = "wcr"
  start_urls = ["http://www.westcoastroasting.com"]

  def parse(self, response):
    filename = "beans.txt"
    open(filename, 'wb').write(response.body)