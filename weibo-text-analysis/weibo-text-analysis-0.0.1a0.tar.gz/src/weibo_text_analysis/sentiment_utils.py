import numpy as np

list_unique_emoji=[]

happy_emoji=['good','中国赞','打call','鼓掌','赞','笑而不语','笑cry','哈哈','加油','给力','鲜花','太开心','微笑','心','太阳','笑哈哈','偷乐','嘻嘻','喵喵','给你小心心','耶','音乐','赞啊',
             '偷笑','可爱','送花花','哇','爱你' ,'愛你','好爱哦','锦鲤','好喜欢','微笑趣泡','喜','机智','棒棒糖','牛哞哞','烟花','贊','鮮花','亲亲','掌宝爱心','星星','礼物','給力','哆啦A梦微笑',
             '带感','太陽','ali笑','贊啊','太開心','奥克耶','666','贏牛奶','酷','顶'
             ]

sad_emoji=[
    '允悲','费解','求饶','泪','苦涩','悲伤','伤心','抓狂','失望','抱抱','蠟燭','怒','哼','怒骂','生病','鄙视','疑问','可怜','裂开','傻眼','酸','跪了','衰','困','哆啦A夢害怕','打脸',
    '捂脸','吃惊','淚','委屈','怒罵','哈欠','打臉','白眼','弱','睡','阴险'
           ]
print(sad_emoji)

neutral_emoji=[
    '思考','并不简单','围观','ok','举手'
]

def sentiment_emoji(list_emoji):
    list_all_emoji=happy_emoji+sad_emoji+neutral_emoji
    if len(list_emoji)==0:
        return 0,0,0
    N=0
    happy=0
    sad=0
    neutral=0
    for emoji in list_emoji:
        e=emoji.replace("[","").replace("]","")
        if e in happy_emoji:
            happy+=1
        if e in sad_emoji:
            sad+=1
        if e in neutral_emoji:
            neutral+=1
        if e in list_all_emoji:
            N+=1
    if N==0:
        return 0,0,0
    return round(happy/N,4),round(sad/N,4),round(neutral/N,4)

def get_mean_emoji_sentiment(s_happy,s_sad,s_neutral):
    if s_happy>s_sad and s_happy>s_neutral:
        return 2
    if s_sad>s_happy and s_sad>s_neutral:
        return 0
    return 1

def get_mean_emoji_sentiment_revised(s_happy,s_sad,s_neutral):
    if s_happy>s_sad and s_happy>s_neutral:
        return 1+s_happy
    if s_sad>s_happy and s_sad>s_neutral:
        return 1-s_sad
    return 1

def get_avg_sentiment_revised(s_text,s_happy,s_sad,s_neutral):
    r_text=s_text*1.0/2
    r_emoji=get_mean_emoji_sentiment_revised(s_happy,s_sad,s_neutral)*1.0/2
    return (r_text+r_emoji)*1.0/2

def get_avg_sentiment(s_text,s_happy,s_sad,s_neutral):
    r_text=s_text*1.0/2
    r_emoji=get_mean_emoji_sentiment(s_happy,s_sad,s_neutral)*1.0/2
    return (r_text+r_emoji)*1.0/2

def get_sentiment_for_a_comment(text,list_emoji,sw1=None):
    global sw
    if sw1!=None:
        sw=sw1
    list_unique_emoji=[]
    for emoji in list_emoji:
        if emoji not in list_unique_emoji:
            list_unique_emoji.append(emoji)
    s_happy, s_sad, s_neutral = sentiment_emoji(list_unique_emoji)
    # text = comment['text']
    text_sentiment = sw.sentiment_chinese(text)
    s_text_sum = 0
    for l in text_sentiment:
        v = l["sentiment"]
        s_text_sum += int(v)
    s_text = s_text_sum * 1.0 / len(text_sentiment)
    avg_sentiment = get_avg_sentiment(s_text, s_happy, s_sad, s_neutral)
    return avg_sentiment

def get_weibo_sentiment(weibo_id,list_comments,list_emoji):
    list_emoji_new=[]
    for l_emoji in list_emoji:
        l_new=[]
        for l in l_emoji:
            if l!="":
                l_new.append(l.replace("[","").replace("]",""))
        list_emoji_new.append(l_new)
    list_comments_new=[]
    for c in list_comments:
        if c.strip()!="":
            list_comments_new.append(c)
    list_s=[]
    list_data=[]
    for idx,c in enumerate(list_comments_new):
        score=get_sentiment_for_a_comment(c,list_emoji_new[idx])
        list_s.append(score)
        list_data.append({
            "weibo_id":weibo_id,
            "comment":c,
            "emoji":";".join(list_emoji_new[idx]),
            "score":score
        })
    mean_user_sentiment = round(np.mean(list_s), 4)
    for idx,k in enumerate(list_data):
        list_data[idx]["mean_score"]=mean_user_sentiment
    return mean_user_sentiment,list_data

