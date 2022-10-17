from .text_tilling import auto_text_tilling,text_tilling
from bs4 import BeautifulSoup
from tkitreadability import tkitReadability
from .img import get_markdown_images,get_markdown_images_format
"""段落分割，并且对图片进行提取

"""

def auto_cut_markdown(text,is_html=False):
    """
    段落分割，并且对图片进行提取
    The auto_cut_markdown function takes a string of markdown text as input, and returns a list of dictionaries. Each dictionary contains the following key-value pairs:
        - images: A list of image URLs found in the markdown text.
        - text: The plaintext extracted from the markdown body.

    :param text: Used to Specify the text to be processed.
    :return: A generator object.

    :doc-author: Trelent
    """

    Readability = tkitReadability()
    out=text_tilling(text)
    for it in out:
        # print("================================")
        # print(it)
        item={"images":[],"text":''}
        if is_html:
            html=it
        else:
            html=Readability.markdown2Html(it)
        soup = BeautifulSoup(html,features="lxml")
        for ii,img in enumerate(soup.find_all('img')):

            img_info={
                "src":img.get("src"),
                "title":img.get("title"),
                "alt":img.get("alt"),
                # "width":img['width'],
                # "height":img['height']
                }
            item['images'].append(img_info)

        text=soup.get_text()
        item['text']=text
        yield item


def auto_cut_paragraph(text,is_html=False):
    """提取图片和段落
    """
    # print("hh")
    Readability = tkitReadability()
    # out=text_tilling(text)
    if is_html:
        text=Readability.html2markdown(text)
        # text=Readability.markdown2Html(text)
    # print("================================================")
    # print(text)
    items,images_list=get_markdown_images_format(text)
    # print(items,images_list)
    sents=[]
    images={}
    start=0
    for it,image in zip(items,images_list):

        if image is None:
            sents.append(it)
            pass
        else:
            # print(sents)
            paragraph="".join(sents)
            # print("================================")
            # print(paragraph)
            end=len(paragraph.split("."))
            # print(start,end)
            # start=end
            # image['index']=[]
            # img={"images":image,'index':end}
            # images.append(img)
            images[end]=image

    # print(images)

    return {"images":images,"sents":sents}

def back2text(content):
    sents=content['sents']
    # newsents=
    newsents=[]
    # for img in content['images']:
    #     newsents=newsents+sents[:img['index']]
    for i,sent in enumerate(sents):
        # print(i)
        if i in content['images'].keys():
            # print("tttttt")
            for iimg in content['images'][i]:
                img_text=f"\n![{iimg[0]}]({iimg[1]})\n"
                newsents.append(img_text)
        newsents.append(sent+".")

    # print(newsents)
    return newsents




    pass

        # print("================================")
        # print(it)
        # print(image)
            # continue
    # for it in out:
    #     # print("================================")
    #     # print(it)
    #     item={"images":[],"text":''}
    #     if is_html:
    #         html=it
    #     else:
    #         html=Readability.markdown2Html(it)
    #     soup = BeautifulSoup(html,features="lxml")
    #     for ii,img in enumerate(soup.find_all('img')):

    #         img_info={
    #             "src":img.get("src"),
    #             "title":img.get("title"),
    #             "alt":img.get("alt"),
    #             # "width":img['width'],
    #             # "height":img['height']
    #             }
    #         item['images'].append(img_info)

    #     text=soup.get_text()
    #     item['text']=text
    #     yield item