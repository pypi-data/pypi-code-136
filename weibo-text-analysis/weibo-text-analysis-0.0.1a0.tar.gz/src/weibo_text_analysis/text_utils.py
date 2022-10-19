import collections
import jieba

def remove_weibo_tags(str):
    str = re.sub(
        re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', re.DOTALL), '',
        str)
    pattern = re.compile(r'#[^#]*#', re.S)
    result = pattern.sub('', str)
    return result

def extract_emoji(str):
    result=re.findall(r"\[([\w+]+)\]", str)
    list_r=[]
    for r in result:
        if r not in list_r:
            list_r.append(f"[{r}]")
    return list_r

def sort_dict_by_value(dict_reposts,reverse=True):
    dict_reposts = collections.OrderedDict(sorted(dict_reposts.items(), key=lambda t: t[1],reverse=reverse))
    return dict_reposts

def sort_dict_by_key(dict_reposts,reverse=True):
    dict_reposts = collections.OrderedDict(sorted(dict_reposts.items(), key=lambda t: t[0],reverse=reverse))
    return dict_reposts

def extract_label(str):
    result=re.findall(r"【(.+)】", str)
    list_r=[]
    for r in result:
        if r not in list_r:
            list_r.append(f"{r}")
    return list_r

def remove_emoji(str):
    pattern = re.compile(r"\[[\w+]+\]", re.S)
    result = pattern.sub('', str)
    return result

def remove_label(str):
    pattern = re.compile(r"【(.+)】", re.S)
    result = pattern.sub('', str)
    return result

def remove_at_someone(str):
    pattern = re.compile(r"\B(@[\w\d_]+)[\s]?", re.S)
    result = pattern.sub('', str)
    return result

def get_plain_text(s):
    return remove_emoji(remove_weibo_tags(remove_label(remove_at_someone(s))))

def simple_word_segmentation(str):
    seg_list = jieba.cut(str, cut_all=False)
    r_list=[]
    for w in seg_list:
        if w.strip()=="":
            continue
        r_list.append(w.strip())
    return r_list

import re
def clean_text(rgx_list, text):
    new_text = text
    for rgx_match in rgx_list:
        new_text = re.sub(rgx_match, '', new_text)
    return new_text

def clean_weibo_text(text):
    text = clean_text(['#(.*)#', '【(.*)】',"@(\w*)\s*"], text)

    text = text.replace("【", "")
    text = text.replace("】", "")
    text = text.replace("展开c", "")
    text = text.replace("​", "")
    text=text.replace("？","")
    text=text.replace(" ","")
    text = text.strip()
    return text

def extract_at_someone(str):
    result=re.findall(r'\B(@[\w\d_]+)[\s]?', str)
    list_r=[]
    for r in result:
        if r not in list_r:
            list_r.append(f"{r}")
    return list_r

if __name__=="__main__":
    weibo_text='@北京12345 #随手拍北京蓝天[超话]#  #北京的枫叶红了# [围观]你好！【天气很好】'
    print(extract_label(weibo_text))
    print(extract_emoji(weibo_text))
    print(extract_at_someone(weibo_text))
    print(get_plain_text(weibo_text).strip())