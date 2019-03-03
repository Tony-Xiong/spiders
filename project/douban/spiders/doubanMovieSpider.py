
import scrapy
from project.items import MovieItem


class MovieSpider(scrapy.Spider):
    # 爬虫名字
    name = 'douban_spider'
    # 允许的域名
    allowed_domains = ['movie.douban.com']
    # 入口url
    start_urls = ['http://movie.douban.com/top250']

    def parse(self, response):

        # for title in response.css('span.title'):
        #     yield {'title': title.css('span ::text').extract_first()}

        for info in response.css('div.item'):
            item = MovieItem()
            item['num'] = info.css('div.pic em::text').extract()
            item['name'] = info.css('div.pic a img::attr(alt)').extract()
            p = info.css('div.info div.bd p')
            item['intro'] = p[0].css('::text').extract()
            rate = info.css('div.info div.bd div.star span')
            item['eval'] = rate[3].css('::text').extract()
            item['star'] = info.css('span.rating_num::text').extract()
            item['desc'] = info.css('div.info div.bd p span::text').extract()
            item['img'] = info.css('div.pic a img::attr(src)').extract()
            yield item

        for next_page in response.css('span.next > a'):
            yield response.follow(next_page, self.parse)

