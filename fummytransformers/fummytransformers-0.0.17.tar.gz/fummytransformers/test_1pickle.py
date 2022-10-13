from fummytransformers import files

p = files.load_pickle("/Users/xiaoou/Documents/data/output_stanza/lemmas_article/frwac_articles_2270000_lemmas_article.pickle")
print(len(p))
print(p[0])

# files.load_pickle("tokens_sentences/frwac_articles_10000_tokens_sentences.pickle")