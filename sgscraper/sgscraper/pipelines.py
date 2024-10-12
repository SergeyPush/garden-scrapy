# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from .items import MenuItem
import re


class SgscraperPipeline:
    def process_item(self, item: MenuItem, spider):
        adapter = ItemAdapter(item)
        description = adapter.get("description")
        if isinstance(description, str):
            adapter["weight"] = description.split("⚖")[1] if len(description.split("⚖")) > 1 else ""
        return item
