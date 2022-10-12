from itertools import groupby
from operator import itemgetter
from pathlib import Path

from hssp import Spider, Response
from hssp.item import Item, Field


class WenZhenItem(Item):
    parent = Field()
    title = Field(css_select='.book-detail-title::text')
    content = Field(xpath_select='//div[@class="book-detail-content"]//text()', many=True)

    def _clean_content(self, content: list):
        return '\n'.join(content)


class WenZhen(Spider):
    start_urls = ['https://www.iwzbz.com/artical/pcbook/v2/3_1_4.html']

    async def parse(self, response: Response):
        catalog_dict = {}
        zong = response.css('#catalog a[target="_blank"]')
        zong_name = zong.css('p::text').get()
        zong_urls = zong.css('::attr(href)').get()
        catalog_dict[zong_name] = response.to_url(zong_urls)

        for child in response.css('a[href="#"][class="catalogitem"]'):
            name = child.css("::text").get()
            vid = child.css('::attr(val)').get()
            urls = response.css(f"#childitem{vid} a::attr(href)").getall()
            urls = response.to_url(urls)
            catalog_dict[name] = urls

        for name, urls in catalog_dict.items():
            for url in urls:
                yield self.get(url, callback=self.parse_content, metadata={"parent": name})

    async def parse_content(self, response: Response):
        parent = response.metadata['parent']
        item = await WenZhenItem.extract(response=response)
        item.parent = parent
        yield item


def save_md(content: str, name: str):
    content = content.replace('\n\n', '\n')
    path = Path('D:\\Users\\Documents\\穷通宝鉴') / f"{name}.md"
    path.parent.mkdir(exist_ok=True)
    with path.open('wt', encoding='utf-8') as f:
        f.write(content)


def main():
    result = WenZhen.start().item_mgr.to_data()

    for k, v in groupby(result, itemgetter('parent')):  # type: str, list
        content = f"# {k}\n"
        content += '\n'.join([f"## {data['title']}\n{data['content']}" for data in v])
        save_md(content, k)


if __name__ == '__main__':
    main()
