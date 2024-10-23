import scrapy


class AutoselectoSpider(scrapy.Spider):
    name = "autoselecto"
    allowed_domains = ["www.autoselecto.com"]
    start_urls = ["https://www.autoselecto.com/categoria-producto/vehiculos/vehiculos-usados/page/1/"]

    def parse(self, response):
        for selector in response.css('.product'):
       
            name=selector.css('.name a::text').get()
            print(name)
        
            auxName=selector.css('.woocommerce-Price-amount bdi::text').getall()
            if len(auxName)> 0:
                price=auxName[-1]
            else:
                print(0)
                price=0
    

            auxImage=selector.css("img").xpath("@data-src").getall()
            if len(auxImage)> 0:
                image=auxImage[0]
            else:
                image=selector.css("img").xpath("@src").getall()[-1]

            print(image)

            yield {    
                'name': name,
                'price': price,
                'image': image
            }
    

        next_page_link =response.css('.page-numbers a.next::attr(href)').extract_first()
  

        if next_page_link:
            print("-------------   "+next_page_link+" --------------")
            yield response.follow(next_page_link)
           


