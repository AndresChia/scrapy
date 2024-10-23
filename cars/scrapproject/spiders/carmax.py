import scrapy


class CarmaxSpider(scrapy.Spider):
    name = "carmax"
    allowed_domains = ["Carmaxcolombia.com.co"]
    start_urls = ["https://www.carmaxcolombia.com.co/?jsf=jet-engine&pagenum=1",
                  "https://www.carmaxcolombia.com.co/?jsf=jet-engine&pagenum=2",
                  "https://www.carmaxcolombia.com.co/?jsf=jet-engine&pagenum=3",
                  "https://www.carmaxcolombia.com.co/?jsf=jet-engine&pagenum=4",
                  "https://www.carmaxcolombia.com.co/?jsf=jet-engine&pagenum=5",
                  "https://www.carmaxcolombia.com.co/?jsf=jet-engine&pagenum=6",
                  "https://www.carmaxcolombia.com.co/?jsf=jet-engine&pagenum=7"]

    def parse(self, response):
        for selector in response.css('.elementor-widget-wrap'):
            if len(selector.css('.jet-listing-dynamic-field__content').extract()) == 1:
                yield {
                    'name': selector.css('.jet-listing-dynamic-field__content::text').get(),
                    'price': selector.css('bdi::text').get(),
                    'image': selector.css("img").xpath("@src").getall()[1]
                }


        


