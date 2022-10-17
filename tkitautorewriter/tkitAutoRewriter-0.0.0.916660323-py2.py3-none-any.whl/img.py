import re


def get_markdown_images(text):
    """
    从markdown中提取图片

    :param text:
    :return:
    """
    image_arr = re.findall(r'(?:!\[(.*?)\]\((.*?)\))', text)  # 提最述与rul
    # image_arr = re.findall(r'!\[(.*)\]\((.+)\)', text)  # 提最述与rul

    # print("image_arr", image_arr)
    return image_arr
def get_markdown_images_format(text):
    """
    对markdown图片进行分割，在图片标签前后添加两个换行

    :param text:
    :return: []
    """
    # image_arr = re.findall(r'(?:!\[(.*?)\]\((.*?)\))', text)  # 提最述与rul
    for it in re.findall(r'(?:!\[(.*?)\))', text):
        text=text.replace("!["+it+")","\n\n!["+it+")\n\n")
    items=[]
    images_list=[]
    for it in text.split("\n"):
        if len(it) >0:
            it=it.strip().replace(" .",'.').replace(" !",'!').replace(" ;",';').replace(" ?",'?').replace(":.",":")
            image_arr = re.findall(r'(?:!\[(.*?)\]\((.*?)\))', it)
            if len(image_arr) > 0:
                images_list.append(image_arr)
            else:
                images_list.append(None)

            items.append(it.strip())
    # print("image_arr", image_arr)
    # return "\n".join(items)
    return items,images_list