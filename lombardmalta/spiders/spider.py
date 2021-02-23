import scrapy

from scrapy.loader import ItemLoader
from ..items import LombardmaltaItem
from itemloaders.processors import TakeFirst


class LombardmaltaSpider(scrapy.Spider):
	name = 'lombardmalta'
	start_urls = ['https://www.lombardmalta.com/en/news']

	def parse(self, response):
		post_links = response.xpath('//div[@class="media-body"]/a/@href').getall()
		yield from response.follow_all(post_links, self.parse_post)

	def parse_post(self, response):
		title = response.xpath('//h2/text()').get()
		description = response.xpath('//div[@class="col-md-12 remove-padding-left"]//text()[normalize-space() and not(ancestor::h1 | ancestor::h2)]').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description).strip()

		item = ItemLoader(item=LombardmaltaItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)

		return item.load_item()
