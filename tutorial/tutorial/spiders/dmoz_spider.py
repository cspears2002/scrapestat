class DmozSpider(object):
  name = "dmoz"
  allowed_domains = ["dmoz.org"]
  start_urls = [
    "http://www.dmoz.org/Computers/Programming/Languages/Python/Books/",
    "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
  ]

  @classmethod
  def from_crawler(cls, crawler):
    spider = crawler.spiders
    return cls(spider)

  def parse(self, response):
    filename = response.url.split("/")[-2]
    open(filename, 'wb').write(response.body)