import scrapy
from ..items import MenuItem


class SgSpider(scrapy.Spider):
    name = "sg"
    allowed_domains = ["secret-garden-cafe.ps.me"]
    start_urls = ["https://secret-garden-cafe.ps.me/"]

    def parse(self, response):
        menu_list = MenuItem()

        categories_sections = response.css("section.scroll-spy")

        for category in categories_sections:
            category_name = category.css("h2::text").get()
            product_cards = category.css("div[data-testid=product_block]")

            for product in product_cards:
                menu_list["category"] = category_name
                menu_list["name"] = product.css("p[data-testid=product_name]::text").get()
                menu_list["price"] = product.css("span[data-testid=product_price]::text").get()
                menu_list["description"] = product.css("div[itemprop=description]::text").get()
                menu_list["weight"] = ""
                yield menu_list
