#project 
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from binaz.items import HouseItem
from scrapy.http.request import Request


class Binaaz(CrawlSpider):
    name = "binaz"
    page_count = 0
    ev_count = 1
    page = 1
    start_urls = [
        "https://bina.az/alqi-satqi/menziller?page=2",
    ]

    rules = (
        Rule(LinkExtractor(restrict_css='.slider_controls'), callback="parse_house"),
         Rule(LinkExtractor(restrict_css='span.next' ),follow=True)

    )

    def parse_house(self, response):
        house_item = HouseItem()

        house_item["evin_url"] = response.url
        house_item["ev_qiy"] = response.css("p span.price-val::text").get()
        house_item["ev_kur"] = response.css("p span.price-cur::text").get()
        house_item["ev_kvm_degeri"] = response.css("div.unit-price::text").get()
        house_item["kategoriya"] = response.css("table.parameters tr:nth-child(1) td::text")[1].get()
        house_item["mertebe"] = response.css("table.parameters tr:nth-child(2) td::text")[1].get()
        house_item["kvm"] = response.css("table.parameters tr:nth-child(3) td::text")[1].get()
        house_item["otaq"] = response.css("table.parameters tr:nth-child(4) td::text")[1].get()
        house_item["kupca"] = response.css("table.parameters tr:nth-child(5) td::text")[1].get()
        house_item["temir"] = response.css("table.parameters tr:nth-child(6) td::text")[1].get()
        house_item["ev_qeyd"] = response.css("article p::text").get()
        house_item["vasiteci"] = response.css("div.name::text").get()

        return house_item