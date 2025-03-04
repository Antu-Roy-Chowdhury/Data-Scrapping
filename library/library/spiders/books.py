import scrapy
from pathlib import Path

class BooksSpider(scrapy.Spider):
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def start_requests(self):
        urls = [
            "https://books.toscrape.com/catalogue/category/books/travel_2/index.html",
            "https://books.toscrape.com/catalogue/category/books/romance_8/index.html",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = f"books-{page}.html"
        bookDetails = {}
        # Path(filename).write_bytes(response.body)
        self.log(f"Saved file {filename}")
        
        cards = response.css(".product_pod")
        for card in cards:
            # bookDetails["image"] = card.css("img::attr(src)").get()
            # bookDetails["title"] = card.css("h3 a::attr(title)").get()
            # bookDetails["price"] = card.css(".price_color::text").get()
            # bookDetails["rating"] = card.css(".star-rating::attr(class)").get()
            # yield bookDetails
            img = card.css(".image_container img")
            print(img.attrib["src"])
            title = card.css("h3>a::text").get()
            print(title)
            ratting = card.css(".star-rating").attrib("class").split(" ")[1]            
            print(ratting)
