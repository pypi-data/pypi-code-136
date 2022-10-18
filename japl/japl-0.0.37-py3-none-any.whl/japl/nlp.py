# NLP
from pandas import Series, DataFrame

# OS Manage
from itertools import chain
from pkg_resources import working_set
from os import system

def nlp(texts: Series, 
        lang:       str = "en",
        model:      str = "all",
        use_gpu:    bool = False):
    
    ACCEPTED_LANGS  = ["en", "es"]
    ACCEPTED_MODELS = ["all", "lemma", "sentiment"]

    assert lang in ACCEPTED_LANGS, "Language not accepted."
    assert model in ACCEPTED_MODELS, "Model not accepted."

    models = {
        "all": 'tokenize,mwt,pos,lemma',
        "lemma": 'tokenize,mwt,pos,lemma',
        "sentiment": 'tokenize, mwt, sentiment'
    }

    if isinstance(texts, Series):
        texts = texts.to_list()
    
    if not 'stanza' in list({pkg.key for pkg in working_set}):
        system("pip install stanza")

    from stanza import download as sdownload, Pipeline
    
    if model == "lemma" or model == "sentiment":
        
        sdownload(lang, package='ancora', processors=models.get(model), verbose=False)
        
        nlp = Pipeline(processors=models.get(model), lang=lang, use_gpu=use_gpu)
    
        return Series(list(map(lambda text: nlp(text), texts)))

    elif model == "all":
        
        sdownload(lang, package='ancora', processors=models.get("lemma"), verbose=False)

        data = DataFrame({"texts": texts})

        if not 'stop-words' in list({pkg.key for pkg in working_set}):
            system("pip install stop-words")
        from stop_words import get_stop_words

        if not 'dataprep' in list({pkg.key for pkg in working_set}):
            system("pip install dataprep")
        from dataprep.clean import clean_text

        stop_words = get_stop_words(lang)

        custom_pipeline = [
            {
                "operator": "lowercase"
            },
            {
                "operator": "remove_punctuation"
            },
            {
                "operator": "remove_stopwords", 
                 "parameters": 
                     {
                         "stopwords": {
                             *stop_words
                         }
                     }
            },
            {
                "operator": "remove_digits"
            },
            {
                "operator": "remove_urls"
            }
        ]

        data = clean_text(data, "texts", pipeline=custom_pipeline)
        
        # Lemmatization
        nlp = Pipeline(processors=models.get("lemma"), lang=lang, use_gpu=use_gpu)
        
        return Series(list(map(lambda text: " ".join(list(chain.from_iterable(list(map(lambda sent: list(map(lambda word: word.lemma,sent.words)), nlp(text).sentences))))), texts)))