from tkitAutoRewriter import AutoReWrite, SentenceClassification,auto_cut_markdown,auto_cut_paragraph,back2text
# from tkitAutoRewriter.diff import similar_diff_qk_ratio
# from tkitAutoRewriter.api import get_markdown_images_format,rewriter_by_summary
# from tkitAutoRewriter.text_tilling import auto_text_tilling
# from tkitreadability import tkitReadability
import re


# html="""
# <section class="mb4 px3 body"><p>Pyoderma is a bacterial infection of the skin that is generally uncommon in cats. Lesions and pustules (inflamed pus-filled swelling) on the skin, and in some cases partial hair loss, often characterize the infection. Treatment is typically given on an outpatient basis and prognosis is good.</p>
# <p>
# <img decoding="async" alt=" Pyoderma Is A Bacterial Infection Of The Skin That Is Generally Uncommon In Cats" src="https://fast.maomihezi.com/api/v1/thumbnail?widthPx=500&amp;heightPx=300&amp;shavePx=0&amp;fill=True&amp;smartCrop=True&amp;responseType=Binary&amp;openInBrowser=True&amp;fileUri=https%3A%2F%2Fs3.maomihezi.com%2Fpet%2Ffull%2Fb2d560364e8888fcf502fdbf11636fe7ccc3e365.jpg" class="i-amphtml-fill-content i-amphtml-replaced-content">
# Cats have a higher risk of developing an infection when they have a fungal infection or an endocrine disease such as hyperthyroidism. In most cases, the condition will be examined on a superficial basis and treated accordingly. In the event that the pyoderma appears to be deeper in the cat</p><p>The infection typically responds favorably to medical treatment. Treatment is generally done on an outpatient basis and will involve external (topical) medications, as well as antibiotics for the infection. An antibiotic treatment regimen is generally prescribed for more than a month to ensure that the entire infection is eliminated.<img decoding="async" alt=" Pyoderma Is A Bacterial Infection Of The Skin That Is Generally Uncommon In Cats" src="https://fast.maomihezi.com/api/v1/thumbnail?widthPx=500&amp;heightPx=300&amp;shavePx=0&amp;fill=True&amp;smartCrop=True&amp;responseType=Binary&amp;openInBrowser=True&amp;fileUri=https%3A%2F%2Fs3.maomihezi.com%2Fpet%2Ffull%2Fb2d560364e8888fcf502fdbf11636fe7ccc3e365.jpg" class="i-amphtml-fill-content i-amphtml-replaced-content">
# Cats have a higher risk of developing an infection when they have a fungal infection or an endocrine disease such as hyperthyroidism. In most cases, the condition will be examined on a superficial basis and treated accordingly. In the event that the pyoderma appears to be deeper in the cat</p><p>The infection typically responds favorably to medical treatment. Treatment is generally done on an outpatient basis and will involve external (topical) medications, as well as antibiotics for the infection. An antibiotic treatment regimen is generally prescribed for more than a month to ensure that the entire infection is eliminated.</p></section>


# """


def auto_optimize_content(html,is_html=True,api='http://192.168.1.18:3017',**kwargs):
    """自动对内容进行优化处理
    """
    # print("--")
    pre_input=auto_cut_paragraph(html,is_html=is_html)
    # print(pre_input)
    ar = AutoReWrite(api=api,
                    api_sbert_host="http://192.168.1.18:3016")

    text=" ".join(pre_input['sents'])
    out=ar.auto_optimize_content(text.replace("\n", ""))

    try:
        out_text=out['results'][0][0][0]['generated_text']
        # print(out_text)
        pre_input['sents']=out_text.split(".")
        newsents=back2text(pre_input)
        # print("\n".join(newsents))
        out_text=" ".join(newsents)
        # print(out_text)
        return out_text
    except Exception as e:
        return None
        pass


