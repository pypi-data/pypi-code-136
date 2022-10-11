print ("""

from bertify import BERTify
import numpy as np
import pandas as pd
import nltk
import re
import os
import codecs
from sklearn import feature_extraction
import mpld3
from math import*

from six import string_types
from nltk.corpus import movie_reviews
from string import punctuation
from nltk.corpus import stopwords
from nltk import word_tokenize

from gensim.parsing.preprocessing import PorterStemmer, remove_stopwords
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

import gensim.downloader as api

import requests
from bs4 import BeautifulSoup

import matplotlib.pyplot as plt
%matplotlib inline
import seaborn as sns
import os

import lda
import lda.datasets

from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import LSTM, Dense, Dropout, Embedding, Masking, Bidirectional
from tensorflow.keras.optimizers import Adam
from tensorflow.keras import backend
import glob
import spacy
import tweepy

from bertopic import BERTopic
from sklearn.datasets import fetch_20newsgroups


from nltk.tokenize.toktok import ToktokTokenizer
import unicodedata

import numpy as np
import pandas as pd

from gensim.test.utils import datapath, get_tmpfile
from gensim.scripts.glove2word2vec import glove2word2vec
from gensim.models import KeyedVectors

from autoscraper import AutoScraper

from flair.embeddings import WordEmbeddings
from flair.embeddings import TransformerWordEmbeddings
from flair.data import Sentence
from scipy.spatial import distance


nltk.download('movie_reviews') # Downloading corpus
nltk.download('stopwords') # Downloading stopwords
nltk.download('punkt') # Downloading tokenizer


########################################################################################################################################################################
#BERTifying text

# English Embedding Extraction
en_bertify = BERTify(
    lang="en",
    last_four_layers_embedding=True
)

# bn_bertify.batch_size = 96

texts = ["how are you doing?", "I don't know about this.", "This is the most important thing."]
en_embeddings = en_bertify.embedding(texts) 
# shape of the returned matrix in this example 3x3072 (3 -> num. of texts, 3072 -> embedding dim.)


########################################################################################################################################################################
#BOW - Classification


import os
cwd = os.getcwd()
print(cwd)
import pandas as pd       
train = pd.read_csv("labeledTrainData.tsv", header=0,delimiter="\t", quoting=3)
train.shape
train.columns.values
print(train["review"][0])
from bs4 import BeautifulSoup
example1 = BeautifulSoup(train["review"][0])
​
print(example1.get_text())
print(train["review"][0])
import re
letters_only = re.sub("[^a-zA-Z]"," ",example1.get_text() )
print(letters_only)
lower_case = letters_only.lower() 
words = lower_case.split()
words
from nltk.corpus import stopwords
print(stopwords.words("english"))
words = [w for w in words if not w in stopwords.words("english")]
print(words)
from nltk.stem.porter import PorterStemmer
porter_stemmer = PorterStemmer()
porter_stemmer.stem('running')
from nltk.stem.lancaster import LancasterStemmer
lancaster_stemmer = LancasterStemmer()
porter_stemmer.stem('running')
from nltk.stem.porter import PorterStemmer
for idx,x in enumerate(words):
    porter_stemmer = PorterStemmer()
    words[idx]= porter_stemmer.stem(x)
print(words)
for idx, val in enumerate(words):
    print(idx, val)
#POS tagging demo
import nltk
nltk.download('tagsets')
nltk.download('wordnet')
text = nltk.word_tokenize("A sample example to test POS tagging with python")
print(text)
nltk.pos_tag(text)
 nltk.help.upenn_tagset('JJ')
nltk.help.upenn_tagset('NNP')
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
wordnet_lemmatizer = WordNetLemmatizer()
print(wordnet_lemmatizer.lemmatize('is', pos='v'))
print(wordnet_lemmatizer.lemmatize('better', pos='r'))
sent=" ".join(words)
print(sent)
def review_to_words( raw_review ):
    # Function to convert a raw review to a string of words
    # The input is a single string (a raw movie review), and 
    # the output is a single string (a preprocessed movie review)
    #
    # 1. Remove HTML
    review_text = BeautifulSoup(raw_review).get_text() 
    #
    # 2. Remove non-letters        
    letters_only = re.sub("[^a-zA-Z]", " ", review_text) 
    #
    # 3. Convert to lower case, split into individual words
    words = letters_only.lower().split()                             
    #
    # 4. In Python, searching a set is much faster than searching
    #   a list, so convert the stop words to a set
    stops = set(stopwords.words("english"))                  
    # 
    # 5. Remove stop words
    meaningful_words = [w for w in words if not w in stops]   
    #
    # 6. Join the words back into one string separated by space, 
    # and return the result.
    return( " ".join( meaningful_words ))  
clean_review = review_to_words( train["review"][0] )
print(clean_review)
# Get the number of reviews based on the dataframe column size
num_reviews = train["review"].size
​
# Initialize an empty list to hold the clean reviews
clean_train_reviews = []
​
# Loop over each review; create an index i that goes from 0 to the length
# of the movie review list 
for i in range( 0, num_reviews ):
    # Call our function for each one, and add the result to the list of
    # clean reviews
    clean_train_reviews.append( review_to_words( train["review"][i] ) )
clean_train_reviews[0]
clean_train_reviews[24000]
clean_train_reviews[1500]
print("Creating the bag of words...\n")
from sklearn.feature_extraction.text import CountVectorizer
​
# Initialize the "CountVectorizer" object, which is scikit-learn's
# bag of words tool.  
vectorizer = CountVectorizer(max_features = 5000) 
​
# fit_transform() does two functions: First, it fits the model
# and learns the vocabulary; second, it transforms our training data
# into feature vectors. The input to fit_transform should be a list of 
# strings.
train_data_features = vectorizer.fit_transform(clean_train_reviews)
​
# Numpy arrays are easy to work with, so convert the result to an 
# array
train_data_features = train_data_features.toarray()
print(train_data_features.shape)
# Take a look at the words in the vocabulary
vocab = vectorizer.get_feature_names()
print(vocab)
import numpy as np
​
# Sum up the counts of each vocabulary word
dist = np.sum(train_data_features, axis=0)
​
# For each, print the vocabulary word and the number of times it 
# appears in the training set
for tag, count in zip(vocab, dist):
    print(count, tag)
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score
import numpy as np
# Initialize a Random Forest classifier with 100 trees
forest = RandomForestClassifier(n_estimators = 100) 
# Fit the forest to the training set, using the bag of words as 
# features and the sentiment labels as the response variable
#
# This may take a few minutes to run
print("Training the random forest...")
forest = forest.fit( train_data_features, train["sentiment"] )
# random forest performance through cross vaidation 
print(forest)
print(np.mean(cross_val_score(forest,train_data_features,train["sentiment"],cv=10)))
# Read the test data
test = pd.read_csv("testData.tsv", header=0, delimiter="\t", \
                   quoting=3 )
​
# Verify that there are 25,000 rows and 2 columns
print(test.shape)
​
# Create an empty list and append the clean reviews one by one
num_reviews = len(test["review"])
clean_test_reviews = [] 
​
print("Cleaning and parsing the test set movie reviews...\n")
for i in range(0,num_reviews):
    if( (i+1) % 1000 == 0 ):
        print("Review %d of %d\n" % (i+1, num_reviews))
    clean_review = review_to_words( test["review"][i] )
    clean_test_reviews.append( clean_review )
​
# Get a bag of words for the test set, and convert to a numpy array
test_data_features = vectorizer.transform(clean_test_reviews)
test_data_features = test_data_features.toarray()
​
# Use the random forest to make sentiment label predictions
result = forest.predict(test_data_features)
print(result)
​
# Copy the results to a pandas dataframe with an "id" column and
# a "sentiment" column
output = pd.DataFrame( data={"id":test["id"], "sentiment":result} )
​
# Use pandas to write the comma-separated output file
output.to_csv( "Bag_of_Words_model.csv", index=False, quoting=3 )


########################################################################################################################################################################
#BOW - Clustering



import os
os.chdir("/home/sunil/Desktop/boww2v")
print (os.getcwd())
from bs4 import BeautifulSoup
#import two lists: titles, and synopses
titles = open('title_list.txt').read().split('\n')
#ensures that only the first 100 are read in
titles = titles[:100]
synopses_imdb = open('synopses_list_imdb.txt').read().split('\n BREAKS HERE')
synopses_imdb = synopses_imdb[:100]
​
synopses_clean_imdb = []
​
for text in synopses_imdb:
    text = BeautifulSoup(text, 'html.parser').getText()
    #strips html formatting and converts to unicode
    synopses_clean_imdb.append(text)
​
synopses_imdb = synopses_clean_imdb
synopses = []
​
for i in range(len(synopses_imdb)):
    item = synopses_imdb[i]
    synopses.append(item)
print len(synopses)
print len(titles)
print titles[2]
print synopses[2]
print titles[:10]
print synopses[0][:200]
stopwords = nltk.corpus.stopwords.words('english')
print stopwords[:10]
# load nltk's SnowballStemmer as variabled 'stemmer'
from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
# here I define a tokenizer and stemmer which returns the set of stems in the text that it is passed
def tokenize_and_stem(text):
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    stems = [stemmer.stem(t) for t in filtered_tokens]
    return stems
​
def tokenize_only(text):
    # first tokenize by sentence, then by word to ensure that punctuation is caught as it's own token
    tokens = [word.lower() for sent in nltk.sent_tokenize(text) for word in nltk.word_tokenize(sent)]
    filtered_tokens = []
    # filter out any tokens not containing letters (e.g., numeric tokens, raw punctuation)
    for token in tokens:
        if re.search('[a-zA-Z]', token):
            filtered_tokens.append(token)
    return filtered_tokens
#use extend so it's a big flat list of vocab
totalvocab_stemmed = []
totalvocab_tokenized = []
for i in synopses:
    allwords_stemmed = tokenize_and_stem(i) #for each item in 'synopses', tokenize/stem
    totalvocab_stemmed.extend(allwords_stemmed) #extend the 'totalvocab_stemmed' list
    
    allwords_tokenized = tokenize_only(i)
    totalvocab_tokenized.extend(allwords_tokenized)
totalvocab_stemmed[10]
totalvocab_tokenized[10]
from sklearn.feature_extraction.text import TfidfVectorizer
​
#define vectorizer parameters
tfidf_vectorizer = TfidfVectorizer(max_df=0.8, max_features=200000,
                                 min_df=0.2, stop_words='english',
                                 use_idf=True, tokenizer=tokenize_and_stem, ngram_range=(1,3))
​
%time tfidf_matrix = tfidf_vectorizer.fit_transform(synopses) #fit the vectorizer to synopses
​
print(tfidf_matrix.shape)
terms = tfidf_vectorizer.get_feature_names()
​
print terms
from sklearn.metrics.pairwise import cosine_similarity
dist = cosine_similarity(tfidf_matrix)
print dist
dist[8]
from sklearn.cluster import KMeans
​
num_clusters = 5
​
km = KMeans(n_clusters=num_clusters)
​
%time km.fit(tfidf_matrix)
​
clusters = km.labels_.tolist()
print clusters
films = { 'title': titles, 'synopsis': synopses, 'cluster': clusters}
​
frame = pd.DataFrame(films, index = [clusters] , columns = ['title', 'cluster'])
frame['cluster'].value_counts()



########################################################################################################################################################################
#cosine similarity

def square_rooted(x):
    return round(sqrt(sum([a*a for a in x])),3)
 
def cosine_similarity(x,y):
   numerator = sum(a*b for a,b in zip(x,y))
   denominator = square_rooted(x)*square_rooted(y)
   return round(numerator/float(denominator),3)
 
print cosine_similarity([3, 45, 7, 2], [2, 54, 13, 15])





########################################################################################################################################################################
#FacultyNotebook Session 2-v2



from nltk.corpus import movie_reviews
from nltk.corpus import movie_reviews
nltk.download('movie_reviews')
movie_reviews.fileids()
movie_reviews.categories()
print(movie_reviews.raw('neg/cv001_19502.txt')) # Example
category = []
review = []
for i in movie_reviews.fileids():
  category.append(i.split('/')[0])
  review.append(movie_reviews.raw(i))
data = pd.DataFrame()
data['Review'] = review
data['Category'] = category
data.head(5)
data[data['Category'] == 'pos'].head()
data.shape
​
Process the data
## Convert into lower case and remove special character
docs = data['Review'].str.lower().str.replace('[^a-z\s]', '')
​
## Remove stopwords
docs = docs.apply(remove_stopwords)
​
## Stemm the words
stemmer = PorterStemmer()
docs = stemmer.stem_documents(docs)
Data Processing and model building with Count Vectorizor
Data Processing with Count Vectorizor
## divide the dataset into train & test 
train_docs, test_docs = train_test_split(pd.Series(docs), test_size=0.2, random_state=1)
​
​
## Vectorize the words
vectorizer = CountVectorizer(min_df=10).fit(train_docs)
​
## Create vocabulary
vocab = vectorizer.get_feature_names()
​
## Vectorize train & test
train_dtm = vectorizer.transform(train_docs)
test_dtm = vectorizer.transform(test_docs)
​
## Prepare the target column for train & test
train_y = data.loc[train_docs.index, 'Category']
test_y = data.loc[test_docs.index, 'Category']
​
train_y.shape
## Visualize the vectorized independent train data
train_dtm
Check for the sparsity in the data
total_values = 1600 * 5248
non_zero = 309635 
zero_values = total_values - non_zero
sparsity = zero_values / total_values * 100
sparsity
model building after Count Vectorizor preprocessing
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
​
naive_bayes_model = MultinomialNB().fit(train_dtm, train_y)
test_y_pred = naive_bayes_model.predict(test_dtm)
from sklearn.metrics import accuracy_score, f1_score
print('Accuracy score: ', accuracy_score(test_y, test_y_pred))
print('F1 score: ', f1_score(test_y, test_y_pred, pos_label='neg'))
Data Processing and model building with Tfidf Vectorizor
Data Processing with Tfidf Vectorizor
## divide the dataset into train & test 
train_docs, test_docs = train_test_split(pd.Series(docs), test_size=0.2, random_state=1)
​
​
## Vectorize the words
vectorizer = TfidfVectorizer(min_df=10).fit(train_docs)
​
## Create vocabulary
vocab = vectorizer.get_feature_names()
​
## Vectorize train & test
train_dtm = vectorizer.transform(train_docs)
test_dtm = vectorizer.transform(test_docs)
​
## Prepare the target column for train & test
train_y = data.loc[train_docs.index, 'Category']
test_y = data.loc[test_docs.index, 'Category']
model building after Tfidf Vectorizor preprocessing
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
​
naive_bayes_model = MultinomialNB().fit(train_dtm, train_y)
test_y_pred = naive_bayes_model.predict(test_dtm)
from sklearn.metrics import accuracy_score, f1_score
print('Accuracy score: ', accuracy_score(test_y, test_y_pred))
print('F1 score: ', f1_score(test_y, test_y_pred, pos_label='neg'))
Sentiment Analysis using Rule Based algorithm
docs = data['Review']
docs.head()
import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
total_score = 0.5
compound_score = total_score / np.sqrt(np.square(total_score) + 15)
compound_score
print(analyzer.polarity_scores('i love tea'))
print(analyzer.polarity_scores('i LOVE tea'))
print(analyzer.polarity_scores('i LOVE tea!!!!'))
print(analyzer.polarity_scores('i very much LOVE tea!!!!'))
print(analyzer.polarity_scores('i very much LOVE tea!!!! :)'))
# Do not perform lower case conversion
# Do not remove stop words
# Do not remove special characters
# Do not perform stemming or lemmatization
When to use

if no labelled data available & if you have pos/neg lexicons for the language

When not to use

If lexicon list for your language, if it is not there If text data is already processed, try avoiding





########################################################################################################################################################################
#FakeNewsClassifierUsingLSTM

df=pd.read_csv('train.csv')
df.head()
###Drop Nan Values
df=df.dropna()
## Get the Independent Features
X=df.drop('label',axis=1)
## Get the Dependent features
y=df['label']
X.shape
y.shape
import tensorflow as tf
tf.__version__
from tensorflow.keras.layers import Embedding
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import Sequential
from tensorflow.keras.preprocessing.text import one_hot
from tensorflow.keras.layers import LSTM
from tensorflow.keras.layers import Dense
### Vocabulary size
voc_size=5000
Onehot Representation
messages=X.copy()
messages['title'][1]
messages.reset_index(inplace=True)
import nltk
import re
from nltk.corpus import stopwords
nltk.download('stopwords')
### Dataset Preprocessing
from nltk.stem.porter import PorterStemmer
ps = PorterStemmer()
corpus = []
for i in range(0, len(messages)):
    print(i)
    review = re.sub('[^a-zA-Z]', ' ', messages['title'][i])
    review = review.lower()
    review = review.split()
    
    review = [ps.stem(word) for word in review if not word in stopwords.words('english')]
    review = ' '.join(review)
    corpus.append(review)
corpus
onehot_repr=[one_hot(words,voc_size)for words in corpus] 
onehot_repr
Embedding Representation
sent_length=20
embedded_docs=pad_sequences(onehot_repr,padding='pre',maxlen=sent_length)
print(embedded_docs)
embedded_docs[0]
## Creating model
embedding_vector_features=40
model=Sequential()
model.add(Embedding(voc_size,embedding_vector_features,input_length=sent_length))
model.add(LSTM(100))
model.add(Dense(1,activation='sigmoid'))
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
print(model.summary())
len(embedded_docs),y.shape
import numpy as np
X_final=np.array(embedded_docs)
y_final=np.array(y)
X_final.shape,y_final.shape
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_final, y_final, test_size=0.33, random_state=42)
Model Training
### Finally Training
model.fit(X_train,y_train,validation_data=(X_test,y_test),epochs=10,batch_size=64)
Adding Dropout
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
y_pred = model.predict(X_test)
y_pred = np.round(y_pred).astype(int)
print(confusion_matrix(y_test,y_pred))
print(accuracy_score(y_test,y_pred))
from tensorflow.keras.layers import Dropout
## Creating model
embedding_vector_features=40
model=Sequential()
model.add(Embedding(voc_size,embedding_vector_features,input_length=sent_length))
model.add(Dropout(0.3))
model.add(LSTM(100))
model.add(Dropout(0.3))
model.add(Dense(1,activation='sigmoid'))
model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
### Finally Training
model.fit(X_train,y_train,validation_data=(X_test,y_test),epochs=10,batch_size=64)
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
y_pred = model.predict(X_test)
y_pred = np.round(y_pred).astype(int)
print(confusion_matrix(y_test,y_pred))
print(accuracy_score(y_test,y_pred))



########################################################################################################################################################################
#Glove

corpus = api.load('text8')
from gensim.models.word2vec import Word2Vec
model = Word2Vec(corpus)
print(model.wv.most_similar('tree'))
import json
info = api.info()
print(json.dumps(info, indent=4))
print(info.keys())
for corpus_name, corpus_data in sorted(info['corpora'].items()):
    print(
        '%s (%d records): %s' % (
            corpus_name,
            corpus_data.get('num_records', -1),
            corpus_data['description'][:40] + '...',
        )
    )
for model_name, model_data in sorted(info['models'].items()):
    print(
        '%s (%d records): %s' % (
            model_name,
            model_data.get('num_records', -1),
            model_data['description'][:40] + '...',
        )
    )
fake_news_info = api.info('fake-news')
print(json.dumps(fake_news_info, indent=4))
model = api.load("glove-wiki-gigaword-50")
model.most_similar("glass")
model['glass']
#Show a word embedding
print('King: ',model.get_vector('king'))
​
result = model.most_similar(positive=['woman', 'king'], negative=['man'], topn=1)
​
print('Most similar word to King + Woman: ', result)
model.most_similar(positive=['ate','speak'], negative=['eat'], topn=5)



########################################################################################################################################################################
#LDA.ipynb

X = lda.datasets.load_reuters()
X
vocab = lda.datasets.load_reuters_vocab()
vocab
titles = lda.datasets.load_reuters_titles()
titles
X.shape
len(titles)
len(vocab)
model = lda.LDA(n_topics=20, n_iter=1500, random_state=1)
model.fit(X)
topic_word = model.topic_word_ 
n_top_words = 8
for i, topic_dist in enumerate(topic_word):
    topic_words = np.array(vocab)[np.argsort(topic_dist)][:-(n_top_words+1):-1]
    print('Topic {}: {}'.format(i, ' '.join(topic_words)))
doc_topic = model.doc_topic_
for i in range(10):
    print("{} (top topic: {})".format(titles[i], doc_topic[i].argmax()))
    
    
########################################################################################################################################################################
#NLP basics
Basic text reading
import nltk # Import NLTK
from nltk.corpus import reuters # Import the Reuters corpus
nltk.download('reuters')
reuters.fileids() # List file-ids in the corpus
reuters.categories() # List news categories in the corpus
reuters.fileids(['wheat','rice']) # List file ids with either wheat or rice categories
# Some file ids may overlap as news covers multiple categories
# Let us see how many chars, words and sentences are in each file
nltk.download('punkt')
for fileid in reuters.fileids(['wheat','rice']):
    num_chars = len(reuters.raw(fileid))
    num_words = len(reuters.words(fileid))
    num_sents = len(reuters.sents(fileid))
    num_vocab = len(set(w.lower() for w in reuters.words(fileid)))
    print(fileid, " : ",num_chars, num_words, num_sents, num_vocab)
# Select one file for futher processing
​
fileid = 'test/15618'
​
reuters.raw(fileid) # See what is in the selected file
reuters.words(fileid) # See individual words in the selected file
# See sentences in the file. Notice the bracket within bracket for each sentence
​
reuters.sents(fileid) 
​
Pre-processing: lower case, tokenization, removing stop words, finding words
# See all the words in the file, lexicographically sorted
​
set(w.lower() for w in reuters.words(fileid))
#Remove stop words
nltk.download('stopwords')
from nltk.corpus import stopwords # Import stop words
wordList = [w for w in reuters.words(fileid) if w.lower() not in stopwords.words('english')]
wordList
#Tokenize
​
from nltk import word_tokenize # Tokenize the file, which is similar to getting words
tokens = word_tokenize(reuters.raw(fileid))
wordList = reuters.words(fileid)
​
tokens
# Check out the difference between tokens and words. Tokenization is more intelligence segmentation
​
wordList[12:20]
# Find position of a word
​
reuters.raw(fileid).find('MARKET')
Synonyms, PoS Tagging, Parsing: Chunking, Chinking, Syntax Trees
# Check out some synonyms
nltk.download('wordnet')
from nltk.corpus import wordnet as wn # See the list of synonyms
wn.synsets('trade')
wn.synset('trade.v.02').lemma_names() # Read one particular synonym
# Find text with similar context
​
text = nltk.Text(word.lower() for file_id in reuters.fileids(['wheat','rice']) for word in reuters.words(file_id))
text.similar('rice')
# See PoS of tokens (for some corpora, POS are already tagged in this corpus)
nltk.download('averaged_perceptron_tagger')
nltk.pos_tag(tokens)
# Parsing using regular expression with chunking (without chinking)
​
# We specify that noun phrase can have a determinant, adverb, gerund verb, or an adjective,
# but it must have a noun or a pronoun, e.g. "A fastly running beautiful deer..."
# The verb phrase should start with a verb, and then it can have anything.
​
pattern = NP: {<DT>?<RB.?>?<VBG>?<JJ.?>*(<NN.?>|<PRP.?>)+}
             VP: {<VB.?>+<.*>*}

​
mySentence = 'A fastly running beautiful deer skidded off the road'
​
myParser = nltk.RegexpParser(pattern)
myParsedSentence = myParser.parse(nltk.pos_tag(nltk.word_tokenize(mySentence)))
#myParsedSentence = myParser.parse(nltk.pos_tag(nltk.word_tokenize('The cat was going to eat bread but then he found a mouse')))
print(myParsedSentence)
# Displaying a parse (syntax) tree. 
# Install Ghostscript: In Anacodna prompt, type 'conda install -c conda-forge ghostscript' 
​
# This cell will not work in Google Colab
​
from IPython.display import display
​
display(myParsedSentence)
# Let us try another sentence with chunking (without chinking)
​
mySentence = 'I left to do my homework'
​
myParser = nltk.RegexpParser(pattern)
myParsedSentence = myParser.parse(nltk.pos_tag(nltk.word_tokenize(mySentence)))
print(myParsedSentence)
# This cell will not work in Google Colab
​
display(myParsedSentence)
# Parsing using regular expression with chunking and chinking (exclusion rule)
​
# Redefine pattern with chinking, to exclude "to do something"
pattern = NP: {<DT>?<RB.?>?<VBG>?<JJ.?>*(<NN.?>|<PRP.?>)+}
             VP: {<VB.?>+<.*>*}
                 }(<VBG>|(<TO><.*>*)){

​
mySentence = 'I left to do my homework'
​
myParser = nltk.RegexpParser(pattern)
myParsedSentence = myParser.parse(nltk.pos_tag(nltk.word_tokenize(mySentence)))
print(myParsedSentence)
# This cell will not work in Google Colab
​
display(myParsedSentence)
Context free grammar (CFG)
# Defining a grammar
from nltk import CFG
​
myGrammar = nltk.CFG.fromstring(
    S -> NP VP
    VP -> VB NP
    VP -> VB
    VP -> VB PRP
    NP -> DET NN
    
    VB -> "chased"|"ate"
    DET -> "another"|"the"
    NN -> "cat"|"rat"|"snake"
    PRP -> "it"
)
​
​
# Generating sentences from the defined grammar
​
from nltk.parse.generate import generate
​
for sent in generate(myGrammar):
    print(' '.join(sent))
Frequency of words, bi-grams, tri-grams
# Frequency Distribution of words
​
fdist = nltk.FreqDist(wordList)
​
fdist
# Some n-gram examples in NLTK
​
from nltk.util import ngrams
​
bigrams = ngrams(tokens,2) # A bigram is specified by 2, trigram by 3, etc.
for b in bigrams:
    print(b)
trigrams = ngrams(tokens,3) # A bigram is specified by 2, trigram by 3, etc.
for t in trigrams:
    print(t)
Stemming, lemmatization
# Comparing stemming and lemmatization
# Reading corpus and removing stop words
nltk.download('brown')
from nltk.corpus import brown
fileid = 'ck23'
​
from nltk.corpus import stopwords # Remove stop words
wordList = [w for w in brown.words(fileid) if w.lower() not in stopwords.words('english')]
​
import string # Remove punctuation
wordList = [w for w in wordList if w not in string.punctuation]
# COMPARE TWO STEMMERS
​
from nltk.stem import PorterStemmer
from nltk.stem import LancasterStemmer
porter = PorterStemmer()
lancaster = LancasterStemmer()
​
StemmersCompared = [word+' : '+porter.stem(word)+' : '+lancaster.stem(word) for word in wordList]
StemmersCompared
# Lemmatization compared to Stemming
​
from nltk.stem import WordNetLemmatizer
wordNet = WordNetLemmatizer()
​
StemmersCompared = [word+' : '+porter.stem(word)+' : '+lancaster.stem(word)+' : '+wordNet.lemmatize(word) for word in wordList]
StemmersCompared


########################################################################################################################################################################
#NLP-Session2 -Inclass_question-v2-1

Reading the data
Use the bbc-text dataset.

We will employ a text categorization dataset based on articles (mentioned in text column). Each article is assigned a specific captegory.

###Implement the code to load the dataset.(Hint: Use the pandas library to load the csv file.)

df = pd.read_csv('bbc-text.csv')
df
Check the number of articles in each category
df.category.value_counts()
###Create a variable called "docs" to convert each article report narrative to individual tokens.(Hint: Use regular expression based tokenizer.)

​
Proccessing the Data
## Convert into lower case and remove special character
df.text = df.text.str.replace('[^a-z\s#@]', '')
​
## Remove stopwords
df.text = df.text.apply(remove_stopwords)
​
## Stemm the words
stemmer = PorterStemmer()
df.text = stemmer.stem_documents(df.text)
df.shape
Data Processing and model building with count Vectorizor
Data Processing with count Vectorizor
## divide the dataset into train & test 
train_docs, test_docs = train_test_split(pd.Series(df.text), test_size=0.2, random_state=1)
​
​
## Vectorize the words
vectorizer = CountVectorizer(min_df=10).fit(train_docs)
​
## Create vocabulary
vocab = vectorizer.get_feature_names()
​
## Vectorize train & test
train_dtm = vectorizer.transform(train_docs)
test_dtm = vectorizer.transform(test_docs)
​
## Prepare the target column for train & test
train_y = df.loc[train_docs.index, 'category']
test_y = df.loc[test_docs.index, 'category']
​
train_y.shape
## Visualize the vectorized independent train data
train_dtm
df_train_dtm = pd.DataFrame(train_dtm.toarray(), index=train_docs.index, columns=vocab)
df_train_dtm
Check for the sparsity in the data
total_values = 1780*3504
non_zero = 193147 
zero_values = total_values - non_zero
sparsity = zero_values / total_values * 100
sparsity
Model building after count Vectorizor preprocessing(use SVM)
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
​
naive_bayes_model = MultinomialNB().fit(train_dtm, train_y)
test_y_pred_countvec = naive_bayes_model.predict(test_dtm)
​
from sklearn.metrics import accuracy_score, f1_score
print('Accuracy score: ', accuracy_score(test_y, test_y_pred_countvec))
print('F1 score: ', f1_score(test_y, test_y_pred_countvec, average='weighted'))
Data Processing and model building with Tfidf Vectorizor
Data Processing with Tfidf Vectorizor
## divide the dataset into train & test 
train_docs, test_docs = train_test_split(pd.Series(df.text), test_size=0.2, random_state=1)
​
​
## Vectorize the words
vectorizer = TfidfVectorizer(min_df=10).fit(train_docs)
​
## Create vocabulary
vocab = vectorizer.get_feature_names()
​
## Vectorize train & test
train_dtm = vectorizer.transform(train_docs)
test_dtm = vectorizer.transform(test_docs)
​
## Prepare the target column for train & test
train_y = df.loc[train_docs.index, 'category']
test_y = df.loc[test_docs.index, 'category']
Model building after Tfidf Vectorizor preprocessing(use SVM)
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
​
naive_bayes_model = MultinomialNB().fit(train_dtm, train_y)
test_y_pred_tfidf = naive_bayes_model.predict(test_dtm)
from sklearn.metrics import accuracy_score, f1_score
print('Accuracy score: ', accuracy_score(test_y, test_y_pred_tfidf))
print('F1 score: ', f1_score(test_y, test_y_pred_tfidf, average='weighted'))
​
Compare the imapct of two different types of vectorization technique in model performance
Draw the conclussion for model evaluations on different categories as well

from sklearn.metrics._classification import classification_report, confusion_matrix
from sklearn.metrics import plot_confusion_matrix, ConfusionMatrixDisplay
import seaborn as sns
TF-IDF vectorizer metrics
print("When vectorized using TF IDF vectorizer: ")
print('F1 score: ', classification_report(test_y, test_y_pred_tfidf))
​
​
cm = confusion_matrix(test_y, test_y_pred_tfidf, normalize='all')
cmd = ConfusionMatrixDisplay(cm, display_labels=['business','entertainment', 'politics', 'sport', 'tech'])
cmd.plot()
Count vectorizer metrics
print("When vectorized using Count vectorizer: ")
print('F1 score: ', classification_report(test_y, test_y_pred_countvec))
​
​
cm = confusion_matrix(test_y, test_y_pred_countvec, normalize='all')
cmd = ConfusionMatrixDisplay(cm, display_labels=['business','entertainment', 'politics', 'sport', 'tech'])
cmd.plot()
Conclusion
Although the F1 scores and Accuracy scores are identical from two different vectorizers, Count vectorizer has a relatively higher F1 score.


########################################################################################################################################################################
#countvector-tfidfvector.ipynb

from sklearn.feature_extraction.text import CountVectorizer
# list of text documents
text = ["The quick brown fox jumped over the lazy dog."]
# create the transform
vectorizer = CountVectorizer()
# tokenize and build vocab
vectorizer.fit(text)
# summarize
print(vectorizer.vocabulary_)
# encode document
vector = vectorizer.transform(text)
# summarize encoded vector
print(vector.shape)
print(type(vector))
print(vector.toarray())

# encode another document
text2 = ["the puppy"]
vector = vectorizer.transform(text2)
print(vector.toarray())

from sklearn.feature_extraction.text import TfidfVectorizer
# list of text documents
text = ["The quick brown fox jumped over the lazy dog.",
        "The dog.",
        "The fox"]
# create the transform
vectorizer = TfidfVectorizer()
# tokenize and build vocab
vectorizer.fit(text)
# summarize
print(vectorizer.vocabulary_)
print(vectorizer.idf_)
# encode document
vector = vectorizer.transform([text[0]])
# summarize encoded vector
print(vector.shape)
print(vector.toarray())

t=["NLP is interesting"]
output=vectorizer.transform(t) 
output.toarray()

########################################################################################################################################################################
#NLP_Session3_1_v1.ipynb

Section 1 :Web Scrapping on HTML page
Step 1 : Fetch the web page and convert the html page into text with the help of Python request library
# import the python request library to query a website
import requests
# specify the url we want to scrape from
Link = "https://en.wikipedia.org/wiki/COVID-19_pandemic_by_country_and_territory"
​
# convert the web page to text
Link_text = requests.get(Link).text
print(Link_text)
Step 2 : In order to fetch useful information, convert Link_text (which is of string data type) into BeautifulSoup object. Import BeautifulSoup library from bs4
# import BautifulSoup library to pull data out of HTML and XML files
from bs4 import BeautifulSoup
# to convert Link_text into a BeautifulSoup Object
soup = BeautifulSoup(Link_text, 'lxml')
print(soup)
Step 3 : With the help of the prettify() function, make the indentation proper
# make the indentation proper
print(soup.prettify())
Step 4 : To fetch the web page title, use soup.title
# To take a look at the title of the web page
print(soup.title)
Step 5 : We want only the string part of the title, not the tags
# Only the string not the tags
print(soup.title.string)
Step 6 : We can also explore tags in the soup object
# First <a></a> tag
soup.a
Step 7 : Explore all tags
# all the <a> </a> tags
soup.find_all('a')
Step 8 : Again, just the way we fetched title tags, we will fetch all table tags
# Fetch all the table tags
all_table = soup.find_all('table')
print(all_table)
Step 9 :Since our aim is to get the List of references from the wiki-page, we need to find out the table class name. Go to the webpage. Inspect the table by placing cursor over the table and inspect the element using ‘Shift+Q’.
​
​
Step 10 : Now, fetch all table tags with the class name ‘wikitable sortable’
# fetch all the table tags with class name="wikitable sortable"
our_table = soup.find('table', class_= 'wikitable plainrowheaders sortable mw-datatable covid19-countrynames')
​
print(our_table)
Step 11 : We can see that the information that we want to retrieve from the table has tags in them. So, find all the tags from table_links.
# In the table that we will fetch find the <a> </a>tags  
table_links = our_table.find_all('a')
print(table_links)
Step 12 : In order to put the title on a list, iterate over table_links and append the title using the get() function
# put the title into a list 
References = []
for links in table_links:
  References.append(links.get('title'))
print(References)
Step 13: Now that we have our required data in the form of a list, we will be using Python Pandas library to save the data in an Excel file. Before that, we have to convert the list into a DataFrame
# Convert the list into a dataframe 
import pandas as pd
df = pd.DataFrame(References)
print(df)
Step 14 : Explore different components of a table
article = soup.find('table' , class_ = 'wikitable plainrowheaders sortable mw-datatable covid19-countrynames')
​
#article = soup.find('div' , id = 'covid-19-pandemic-deatth-rates' , class_ = 'covid19-container-wrapper')
article.text
# 1. title
title = article.caption.find('div' , class_ = 'navbar-ct-mini')
print(title.text)
# 2. summary 
summary = article.text 
print(summary)
# 3. Link
link = article.tbody.a['href']
print(link)
Step 15: Use the following method to write data into an Excel file.
# To save the data into an excel file 
writer = pd.ExcelWriter('ref.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name='List')
writer.save()
Step 16: Just to make sure if the Excel workbook is saved or not, read the file using read_excel
# check if it’s done right or not
df1= pd.read_excel('ref.xlsx')
df1
Section 2 : Scrapping Amazon
import requests
Link = 'https://www.amazon.in/s?k=headphones&rh=n%3A1389401031&ref=nb_sb_noss_2'
​
Link_text = requests.get(Link).text
print(Link_text)
# import BautifulSoup library to pull data out of HTML and XML files
from bs4 import BeautifulSoup
# to convert Link_text into a BeautifulSoup Object
soup = BeautifulSoup(Link_text, 'lxml')
print(soup)
# Only the string not the tags
print(soup.title.string)
# 1. Price
title = soup.find('span', class_="a-price-whole")
print(title)
# 2. summary 
summary = soup.text 
print(summary)
​
import requests
from glob import glob
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from time import sleep
​
Link = 'https://www.amazon.in/s?k=headphones&rh=n%3A1389401031&ref=nb_sb_noss'
# http://www.networkinghowtos.com/howto/common-user-agent-list/
HEADERS = ({'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
            'Accept-Language': 'en-US, en;q=0.5'})
# imports a csv file with the url's to scrape
prod_tracker_URLS = Link
# fetch the url
page = requests.get(prod_tracker_URLS, headers=HEADERS)
page
page.content
# create the object that will contain all the info in the url
soup = BeautifulSoup(page.content, features="lxml")
soup
soup.find('title').string
print(soup.find(class_ ="a-price-whole").get_text().strip())
# Rating
soup.find(class_="a-icon-alt").get_text().strip()
## Auto filled informations
for i in soup.find_all('span', class_="a-size-base a-color-base a-text-bold", dir= 'auto'):
  print(i.string)
Section 3 : Retrieve data from News API
Part 1 : Installation
pip install newsapi-python
import requests 
from newsapi import NewsApiClient
import os
import tweepy as tw
import pandas as pd
Part 2 : Init
newsapi = NewsApiClient(api_key='8cfb35124315407c9af7d5ecc271a4de')
Part 3 : Headline
3.1 Headline with url
import requests
url = ('http://newsapi.org/v2/top-headlines?'
        'country=us&category=health&'
        'apiKey=8cfb35124315407c9af7d5ecc271a4de') # The direct URL to the article.
response = requests.get(url)
print(response.json())
response.json()['articles']
3.2 Headline with parameters
top_headlines = newsapi.get_top_headlines(q='COVID-19',   # Keywords or a phrase to search for.
                                          sources ='bKSBW The Central Coast',  #A comma-seperated string of identifiers for the news sources or blogs you want headlines from. Use the /sources endpoint to locate these programmatically or look at the sources index. Note: you can't mix this param with the country or category params.                                          
                                          #category='health',                                
                                          #country='us',
                                          language='en')
print(top_headlines)
3.3 Parameter explanation
Constants and allowed parameter values specified in the News API.

TOP_HEADLINES_URL = "https://newsapi.org/v2/top-headlines"
EVERYTHING_URL = "https://newsapi.org/v2/everything"
SOURCES_URL = "https://newsapi.org/v2/sources"

#: The 2-letter ISO 3166-1 code of the country you want to get headlines for.  If not specified,
#: the results span all countries.
countries = {
    "ae",
    "ar",
    "at",
    "au",
    "be",
    "bg",
    "br",
    "ca",
    "ch",
    "cn",
    "co",
    "cu",
    "cz",
    "de",
    "eg",
    "es",
    "fr",
    "gb",
    "gr",
    "hk",
    "hu",
    "id",
    "ie",
    "il",
    "in",
    "is",
    "it",
    "jp",
    "kr",
    "lt",
    "lv",
    "ma",
    "mx",
    "my",
    "ng",
    "nl",
    "no",
    "nz",
    "ph",
    "pk",
    "pl",
    "pt",
    "ro",
    "rs",
    "ru",
    "sa",
    "se",
    "sg",
    "si",
    "sk",
    "th",
    "tr",
    "tw",
    "ua",
    "us",
    "ve",
    "za",
    "zh",
}

#: The 2-letter ISO-639-1 code of the language you want to get articles for.  If not specified,
#: the results span all languages.
languages = {"ar", "en", "cn", "de", "es", "fr", "he", "it", "nl", "no", "pt", "ru", "sv", "se", "ud", "zh"}

#: The category you want to get articles for.  If not specified,
#: the results span all categories.
categories = {"business", "entertainment", "general", "health", "science", "sports", "technology"}

#: The order to sort article results in.  If not specified, the default is ``"publishedAt"``.
sort_method = {"relevancy", "popularity", "publishedAt"}
Part 4 : Everything
4.1 Everything with url
import requests
url = ('https://newsapi.org/v2/everything?'
        'q=apple&'
        'from=2020-12-15&'
        'to=2020-12-15&'
        'sortBy=popularity&'
        'apiKey=8cfb35124315407c9af7d5ecc271a4de') # The direct URL to the article.
response = requests.get(url)
print(response.json())
everything = response.json()['articles']
print(everything)
4.2 Everything with parameters
all_articles = newsapi.get_everything(q='apple',  # Keywords or a phrase to search for.
                                     # sources='Engadget',   #A comma-seperated string of identifiers for the news sources or blogs you want headlines from. Use the /sources endpoint to locate these programmatically or look at the sources index. Note: you can't mix this param with the country or category params.
                                     # domains='bbc.co.uk,techcrunch.com',   # A comma-seperated string of domains (eg bbc.co.uk, techcrunch.com, engadget.com) to restrict the search to.
                                      from_param='2020-12-15',   # A date and optional time for the oldest article allowed. This should be in ISO 8601 format (e.g. 2020-12-16 or 2020-12-16T11:03:47)
                                      to='2020-12-15',   # A date and optional time for the newest article allowed. This should be in ISO 8601 format (e.g. 2020-12-16 or 2020-12-16T11:03:47)
                                     # language='en',   # The 2-letter ISO-639-1 code of the language you want to get headlines for.
                                      sort_by='popularity',  # The order to sort the articles in. Possible options: relevancy, popularity, publishedAt
                                      page=2 )   #  Use this to page through the results if the total results found is greater than the page size.
                                      #apiKey = 8cfb35124315407c9af7d5ecc271a4de)
print(all_articles)
Part 5 : sources
5.1 Sources with url
import requests
url = ('https://newsapi.org/v2/sources?'
        'language=en&'
        'country=us&'
        'apiKey=8cfb35124315407c9af7d5ecc271a4de') # The direct URL to the article.
response = requests.get(url)
print(response.json())
5.1 Sources with parameters
# /v2/sources
sources = newsapi.get_sources(language='en',
          country='us')
print(sources)
In the overall sentiment , we acn see the statust is ok ; implies the available overrall content has a neutral sentiment.Let's verify the validity of the claim.
Now, we will perform a sentiment analysis and sentiment intesity test for the content.
Section 4 : Sentiment Analysis using Twiter data
everything
Part 1 : Convert the available content into a dataframe and remove the null data
AllContent = []
for i in range(len(everything)):
  #print(everything[i]['content'])
  AllContent.append(everything[i]['content'])
import pandas as pd
AllContent = pd.DataFrame(AllContent,columns = ['Content'])
AllContent
AllContent = AllContent.dropna(axis = 0, how = 'any')
AllContent
Part 2 : Assign the subjetivity response to the content
# TextBlob - Python library for processing textual data
from textblob import TextBlob
def getTextSubjectivity(txt):
    return TextBlob(txt).sentiment.subjectivity
getTextSubjectivity(AllContent['Content'][0])
Part 3 : Assign the polarity response to the content
def getTextPolarity(txt):
    return TextBlob(txt).sentiment.polarity
AllContent['Subjectivity'] = AllContent['Content'].transform(lambda x: getTextSubjectivity(str(x)))
AllContent['Subjectivity'] 
AllContent['Polarity'] = AllContent['Content'].transform(lambda x: getTextPolarity(str(x)))
AllContent['Polarity'] 
Part 4 : Assing sentiment to the content
# negative, nautral, positive analysis
def getTextAnalysis(a):
    if a < 0:
        return "Negative"
    elif a == 0:
        return "Neutral"
    else:
        return "Positive"
AllContent['Score'] = AllContent['Polarity'].apply(getTextAnalysis)
Part 5 : Assign Polarity to the entire content
positive = AllContent[AllContent['Score'] == 'Positive']
​
print(str(positive.shape[0]/(AllContent.shape[0])*100) + " % of positive tweets")
Part 6 : Visualize the frequency distribution of the sentiment on each content
import matplotlib.pyplot as plt
plt.figure(figsize = (10,5))
labels = AllContent.groupby('Score').count().index.values
​
values = AllContent.groupby('Score').size().values
​
plt.bar(labels, values)
Part 7 : Construct a complete vocabulary for the entire content
# WordCloud - Python linrary for creating image wordclouds
from wordcloud import WordCloud
words = str()
for content in AllContent['Content']:
  words = words + ' ' + content 
print(words)
Part 8 : Visualise the complete vocabulary as per their intensity over the entire content available
# Creating a word cloud
plt.figure(figsize=(10,10))
words = ' '.join([content for content in AllContent['Content']])
wordCloud = WordCloud(width=600, height=400).generate(words)
​
plt.imshow(wordCloud)
plt.show()

########################################################################################################################################################################
#NMT with Attention.ipynb

Libraries along with their versions used at the time of making notebook-
google 2.0.3

matplotlib 3.1.3

numpy 1.18.1

tensorflow 2.1.0

Neural machine translation with attention
Firstly, let's select TensorFlow version 2.x in colab

%tensorflow_version 2.x
import tensorflow as tf
tf.__version__
# Initialize the random number generator
import random
random.seed(0)
​
# Ignore the warnings
import warnings
warnings.filterwarnings("ignore")
Load the dataset
As we are using google colab, we need to mount the google drive to load the data file

from google.colab import drive
drive.mount('/content/drive/')
Add path to the file

path_to_file = '/content/drive/My Drive/NLP/mar.txt'
Let's convert unicode file to ascii

import unicodedata
​
# Converts the unicode file to ascii
def unicode_to_ascii(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn')
Preprocessing the sentence

import re
​
def preprocess_sentence(w):
    w = unicode_to_ascii(w.lower().strip())
    
    # creating a space between a word and the punctuation following it
    # eg: "he is a boy." => "he is a boy ." 
    # Reference:- https://stackoverflow.com/questions/3645931/python-padding-punctuation-with-white-spaces-keeping-punctuation
    w = re.sub(r"([?.!,¿])", r" \1 ", w)
    w = re.sub(r'[" "]+', " ", w)
    
    # replacing everything with space except (a-z, A-Z, ".", "?", "!", ",")
    #w = re.sub(r"[^a-zA-Z?.!,¿]+", " ", w) # COMMENT THIS LINE FOR NON-LATIN SCRIPTS SUCH AS MARATHI, HINDI ETC.
    
    w = w.rstrip().strip()
    
    # adding a start and an end token to the sentence
    # so that the model know when to start and stop predicting.
    w = '<start> ' + w + ' <end>'
    return w
Now let's define a function to create the dataset

# 1. Remove the accents
# 2. Clean the sentences
# 3. Return word pairs in the format: [ENGLISH, MARATHI]
def create_dataset(path, num_examples):
    lines = open(path, encoding='UTF-8').read().strip().split('\n')
    
    word_pairs = [[preprocess_sentence(w) for w in l.split('\t')]  for l in lines[:num_examples]]
    
    return word_pairs
Let's create data for 10 examples to visualize

create_dataset(path_to_file, num_examples=10)
Define a class to create a word -> index mapping

# This class creates a word -> index mapping (e.g,. "dad" -> 5) and vice-versa 
# (e.g., 5 -> "dad") for each language,
class LanguageIndex():
  def __init__(self, lang):
    self.lang = lang
    self.word2idx = {}
    self.idx2word = {}
    self.vocab = set()
    
    self.create_index()
    
  def create_index(self):
    for phrase in self.lang:
      self.vocab.update(phrase.split(' '))
    
    self.vocab = sorted(self.vocab)
    
    self.word2idx['<pad>'] = 0
    for index, word in enumerate(self.vocab):
      self.word2idx[word] = index + 1
    
    for word, index in self.word2idx.items():
      self.idx2word[index] = word
def max_length(tensor):
    return max(len(t) for t in tensor)
​
​
def load_dataset(path, num_examples):
    # creating cleaned input, output pairs
    pairs = create_dataset(path, num_examples)
​
    # index language using the class defined above    
    inp_lang = LanguageIndex(mr for en, mr in pairs)
    targ_lang = LanguageIndex(en for en, mr in pairs)
    
    # Vectorize the input and target languages
    
    # Other language sentences
    input_tensor = [[inp_lang.word2idx[s] for s in mr.split(' ')] for en, mr in pairs]
    
    # English sentences
    target_tensor = [[targ_lang.word2idx[s] for s in en.split(' ')] for en, mr in pairs]
    
    # Calculate max_length of input and output tensor
    # Here, we'll set those to the longest sentence in the dataset
    max_length_inp, max_length_tar = max_length(input_tensor), max_length(target_tensor)
    
    # Padding the input and output tensor to the maximum length
    input_tensor = tf.keras.preprocessing.sequence.pad_sequences(input_tensor, 
                                                                 maxlen=max_length_inp,
                                                                 padding='post')
    
    target_tensor = tf.keras.preprocessing.sequence.pad_sequences(target_tensor, 
                                                                  maxlen=max_length_tar, 
                                                                  padding='post')
    
    return input_tensor, target_tensor, inp_lang, targ_lang, max_length_inp, max_length_tar
# Try experimenting with the size of that dataset
num_examples = 30000
input_tensor, target_tensor, inp_lang, targ_lang, max_length_inp, max_length_targ = load_dataset(path_to_file, num_examples)
from sklearn.model_selection import train_test_split
​
# Creating training and validation sets using an 90-10 split
input_tensor_train, input_tensor_val, target_tensor_train, target_tensor_val = train_test_split(input_tensor, target_tensor, test_size=0.1)
​
# Show length
len(input_tensor_train), len(target_tensor_train), len(input_tensor_val), len(target_tensor_val)
BUFFER_SIZE = len(input_tensor_train)
BATCH_SIZE = 64
N_BATCH = BUFFER_SIZE//BATCH_SIZE
embedding_dim = 256
units = 1024
vocab_inp_size = len(inp_lang.word2idx)
vocab_tar_size = len(targ_lang.word2idx)
​
dataset = tf.data.Dataset.from_tensor_slices((input_tensor_train, target_tensor_train)).shuffle(BUFFER_SIZE)
dataset = dataset.batch(BATCH_SIZE, drop_remainder=True)
class Encoder(tf.keras.Model):
    def __init__(self, vocab_size, embedding_dim, enc_units, batch_sz):
        super(Encoder, self).__init__()
        self.batch_sz = batch_sz
        self.enc_units = enc_units
        self.embedding = tf.keras.layers.Embedding(vocab_size, embedding_dim)
        self.gru = tf.keras.layers.GRU(self.enc_units, 
                                    return_sequences=True, 
                                    return_state=True, 
                                    recurrent_initializer='glorot_uniform')
        
    def call(self, x, hidden):
        x = self.embedding(x)
        output, state = self.gru(x, initial_state = hidden)        
        return output, state
    
    def initialize_hidden_state(self):
        return tf.zeros((self.batch_sz, self.enc_units))
class Decoder(tf.keras.Model):
    def __init__(self, vocab_size, embedding_dim, dec_units, batch_sz):
        super(Decoder, self).__init__()
        self.batch_sz = batch_sz
        self.dec_units = dec_units
        self.embedding = tf.keras.layers.Embedding(vocab_size, embedding_dim)
        self.gru = tf.keras.layers.GRU(self.dec_units, 
                                    return_sequences=True, 
                                    return_state=True, 
                                    recurrent_initializer='glorot_uniform')
        
        self.fc = tf.keras.layers.Dense(vocab_size)
        
        # used for attention
        self.W1 = tf.keras.layers.Dense(self.dec_units)
        self.W2 = tf.keras.layers.Dense(self.dec_units)
        self.V = tf.keras.layers.Dense(1)
        
    def call(self, x, hidden, enc_output):
        # enc_output shape == (batch_size, max_length, hidden_size)
        
        # hidden shape == (batch_size, hidden size)
        # hidden_with_time_axis shape == (batch_size, 1, hidden size)
        # we are doing this to perform addition to calculate the score
        hidden_with_time_axis = tf.expand_dims(hidden, 1)
        
        # score shape == (batch_size, max_length, 1)
        # we get 1 at the last axis because we are applying tanh(FC(EO) + FC(H)) to self.V
        score = self.V(tf.nn.tanh(self.W1(enc_output) + self.W2(hidden_with_time_axis)))
        
        # attention_weights shape == (batch_size, max_length, 1)
        attention_weights = tf.nn.softmax(score, axis=1)
        
        # context_vector shape after sum == (batch_size, hidden_size)
        context_vector = attention_weights * enc_output
        context_vector = tf.reduce_sum(context_vector, axis=1)
        
        # x shape after passing through embedding == (batch_size, 1, embedding_dim)
        x = self.embedding(x)
        
        # x shape after concatenation == (batch_size, 1, embedding_dim + hidden_size)
        x = tf.concat([tf.expand_dims(context_vector, 1), x], axis=-1)
        
        # passing the concatenated vector to the GRU
        output, state = self.gru(x)
        
        # output shape == (batch_size * 1, hidden_size)
        output = tf.reshape(output, (-1, output.shape[2]))
        
        # output shape == (batch_size * 1, vocab)
        x = self.fc(output)
        
        return x, state, attention_weights
        
    def initialize_hidden_state(self):
        return tf.zeros((self.batch_sz, self.dec_units))
encoder = Encoder(vocab_inp_size, embedding_dim, units, BATCH_SIZE)
decoder = Decoder(vocab_tar_size, embedding_dim, units, BATCH_SIZE)
import numpy as np
​
def loss_function(real, pred):
  mask = 1 - np.equal(real, 0)
  loss_ = tf.nn.sparse_softmax_cross_entropy_with_logits(labels=real, logits=pred) * mask
  return tf.reduce_mean(loss_)
import os
optimizer = tf.optimizers.Adam()
​
checkpoint_dir = './training_checkpoints'
checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt")
checkpoint = tf.train.Checkpoint(optimizer=optimizer,
                                 encoder=encoder,
                                 decoder=decoder)
import time
​
EPOCHS = 10
​
for epoch in range(EPOCHS):
    start = time.time()
    
    hidden = encoder.initialize_hidden_state()
    total_loss = 0
    
    for (batch, (inp, targ)) in enumerate(dataset):
        loss = 0
        
        with tf.GradientTape() as tape:
            enc_output, enc_hidden = encoder(inp, hidden)
            
            dec_hidden = enc_hidden
            
            dec_input = tf.expand_dims([targ_lang.word2idx['<start>']] * BATCH_SIZE, 1)       
            
            # Teacher forcing - feeding the target as the next input
            for t in range(1, targ.shape[1]):
                # passing enc_output to the decoder
                predictions, dec_hidden, _ = decoder(dec_input, dec_hidden, enc_output)
                
                loss += loss_function(targ[:, t], predictions)
                
                # using teacher forcing
                dec_input = tf.expand_dims(targ[:, t], 1)
        
        batch_loss = (loss / int(targ.shape[1]))
        
        total_loss += batch_loss
        
        variables = encoder.variables + decoder.variables
        
        gradients = tape.gradient(loss, variables)
        
        optimizer.apply_gradients(zip(gradients, variables))
        
        if batch % 100 == 0:
            print('Epoch {} Batch {} Loss {:.4f}'.format(epoch + 1,
                                                         batch,
                                                         batch_loss.numpy()))
    # saving (checkpoint) the model every 2 epochs
    if (epoch + 1) % 2 == 0:
      checkpoint.save(file_prefix = checkpoint_prefix)
    
    print('Epoch {} Loss {:.4f}'.format(epoch + 1,
                                        total_loss / N_BATCH))
    print('Time taken for 1 epoch {} sec\n'.format(time.time() - start))
checkpoint.save(file_prefix = checkpoint_prefix)
def evaluate(sentence, encoder, decoder, inp_lang, targ_lang, max_length_inp, max_length_targ):
    attention_plot = np.zeros((max_length_targ, max_length_inp))
    
    sentence = preprocess_sentence(sentence)
​
    inputs = [inp_lang.word2idx[i] for i in sentence.split(' ')]
    inputs = tf.keras.preprocessing.sequence.pad_sequences([inputs], maxlen=max_length_inp, padding='post')
    inputs = tf.convert_to_tensor(inputs)
    
    result = ''
​
    hidden = [tf.zeros((1, units))]
    enc_out, enc_hidden = encoder(inputs, hidden)
​
    dec_hidden = enc_hidden
    dec_input = tf.expand_dims([targ_lang.word2idx['<start>']], 0)
​
    for t in range(max_length_targ):
        predictions, dec_hidden, attention_weights = decoder(dec_input, dec_hidden, enc_out)
        
        # storing the attention weigths to plot later on
        attention_weights = tf.reshape(attention_weights, (-1, ))
        attention_plot[t] = attention_weights.numpy()
​
        predicted_id = tf.argmax(predictions[0]).numpy()
​
        result += targ_lang.idx2word[predicted_id] + ' '
​
        if targ_lang.idx2word[predicted_id] == '<end>':
            return result, sentence, attention_plot
        
        # the predicted ID is fed back into the model
        dec_input = tf.expand_dims([predicted_id], 0)
​
    return result, sentence, attention_plot
import matplotlib.pyplot as plt
​
# function for plotting the attention weights
def plot_attention(attention, sentence, predicted_sentence):
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(1, 1, 1)
    ax.matshow(attention, cmap='viridis')
    
    fontdict = {'fontsize': 14}
    
    ax.set_xticklabels([''] + sentence, fontdict=fontdict, rotation=90)
    ax.set_yticklabels([''] + predicted_sentence, fontdict=fontdict)
​
    plt.show()
def translate(sentence, encoder, decoder, inp_lang, targ_lang, max_length_inp, max_length_targ):
    print('Input: {}'.format(sentence))
    result, sentence, attention_plot = evaluate(sentence, encoder, decoder, inp_lang, targ_lang, max_length_inp, max_length_targ)
        
    print('Input: {}'.format(sentence))
    print('Predicted translation: {}'.format(result))
    
    attention_plot = attention_plot[:len(result.split(' '))-1, :len(sentence.split(' '))-1]
    plot_attention(attention_plot, sentence.split(' '), result.split(' '))
# restoring the latest checkpoint in checkpoint_dir
checkpoint.restore(tf.train.latest_checkpoint(checkpoint_dir))
# translate('hace mucho frio aqui.', encoder, decoder, inp_lang, targ_lang, max_length_inp, max_length_targ)
# translate('esta es mi vida.', encoder, decoder, inp_lang, targ_lang, max_length_inp, max_length_targ)
# translate('trata de averiguarlo.', encoder, decoder, inp_lang, targ_lang, max_length_inp, max_length_targ)
translate('चांगला कॅमेरा आहे', encoder, decoder, inp_lang, targ_lang, max_length_inp, max_length_targ)
​



########################################################################################################################################################################
#POS tagging using LSTM.ipynb


Libraries along with their versions used at the time of making notebook-
google 2.0.3

nltk 3.2.5

numpy 1.18.1

pandas 0.25.3

tensorflow 2.1.0

Firstly, let's select TensorFlow version 2.x in colab

%tensorflow_version 2.x
import tensorflow
tensorflow.__version__
# Initialize the random number generator
import random
random.seed(0)
​
# Ignore the warnings
import warnings
warnings.filterwarnings("ignore")
Load the dataset
As we are using google colab, we need to mount the google drive to load the data file

from google.colab import drive
drive.mount('/content/drive/')
# IMPORT DATA
import pandas as pd
import numpy as np
​
data = pd.read_csv('/content/drive/My Drive/NLP/ner_dataset.csv', encoding='latin1')
data = data.fillna(method="ffill") # Deal with N/A
tags = list(set(data["POS"].values)) # Read POS values
tags # List of possible POS values
words = list(set(data["Word"].values))
words.append("DUMMY") # Add a dummy word to pad sentences.
# Code to read sentences
​
class ReadSentences(object): 
    
    def __init__(self, data):
        self.data = data
        self.empty = False
        agg_func = lambda s: [(w, p, t) for w, p, t in zip(s["Word"].values.tolist(),
                                                           s["POS"].values.tolist(),
                                                           s["Tag"].values.tolist())]
        self.grouped = self.data.groupby("Sentence #").apply(agg_func)
        self.sentences = [s for s in self.grouped]
sentences = ReadSentences(data).sentences # Read all sentences
# Convert words and tags into numbers
word2id = {w: i for i, w in enumerate(words)}
tag2id = {t: i for i, t in enumerate(tags)}
# Prepare input and output data
​
from tensorflow.keras.preprocessing.sequence import pad_sequences
max_len = 50
X = [[word2id[w[0]] for w in s] for s in sentences]
X = pad_sequences(maxlen=max_len, sequences=X, padding="post", value=len(words)-1)
y = [[tag2id[w[1]] for w in s] for s in sentences]
y = pad_sequences(maxlen=max_len, sequences=y, padding="post", value=tag2id["."])
# Convert output to one-hot bit
​
from tensorflow.keras.utils import to_categorical
y = [to_categorical(i, num_classes=len(tags)) for i in y]
y[0]
# Training and test split by sentences
​
from sklearn.model_selection import train_test_split
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.20)
from tensorflow.keras.models import Model
from tensorflow.keras.layers import LSTM, Embedding, Dense, TimeDistributed, Dropout, Bidirectional, Input
input = Input(shape=(max_len,)) # Input layer
model = Embedding(input_dim=len(words), output_dim=50, input_length=max_len)(input) # Word embedding layer
model = Dropout(0.1)(model) # Dropout
model = Bidirectional(LSTM(units=100, return_sequences=True, recurrent_dropout=0.1))(model) # Bi-directional LSTM layer
out = TimeDistributed(Dense(len(tags), activation="softmax"))(model)  # softmax output layer
model = Model(input, out) # Complete model
model.compile(optimizer="rmsprop", loss="categorical_crossentropy", metrics=["accuracy"]) # Compile with an optimizer
history = model.fit(X_tr, np.array(y_tr), batch_size=32, epochs=3, validation_split=0.1, verbose=1) # Train
# Demo test on one sample. See how it is mostly correct, but not 100%
​
i = 1213 # Some test sentence sample
p = model.predict(np.array([X_te[i]])) # Predict on it
p = np.argmax(p, axis=-1) # Map softmax back to a POS index
for w, pred in zip(X_te[i], p[0]): # for every word in the sentence
    print("{:20} -- {}".format(words[w], tags[pred])) # Print word and tag
import nltk
nltk.download('punkt')
from nltk import word_tokenize
​
sentence = nltk.word_tokenize('That was a nice jump')
X_Samp = pad_sequences(maxlen=max_len, sequences=[[word2id[word] for word in sentence]], padding="post", value=len(words)-1)
p = model.predict(np.array([X_Samp[0]])) # Predict on it
p = np.argmax(p, axis=-1) # Map softmax back to a POS index
for w, pred in zip(X_Samp[0], p[0]): # for every word in the sentence
    print("{:20} -- {}".format(words[w], tags[pred])) # Print word and tag
​

########################################################################################################################################################################
#POS tagging with NLTK.ipynb


Proprietary content. ©Great Learning. All Rights Reserved. Unauthorized use or distribution prohibited

import nltk
nltk.download('brown') # download the corous
nltk.download('averaged_perceptron_tagger') # Download the tagger
nltk.download('punkt') # download the tokenizer
text = nltk.word_tokenize("Walking is good for health.") # Let us tokenize a sentence
nltk.pos_tag(text) # Let us see its POS
text = nltk.Text(word.lower() for word in nltk.corpus.brown.words()) # Make lower case
text.similar('kid') # Should be nouns like people
text.similar('run') # Should be verbs like 'walk'
text.similar('on') # Should be prepositions
text.similar('cricket') # Should be either games or insects
nltk.pos_tag(nltk.word_tokenize('cricket')) # Should be noun
nltk.pos_tag(nltk.word_tokenize("Do you want to jump")) # Let us see if 'jump' is verb
nltk.pos_tag(nltk.word_tokenize("That was a nice jump")) # Let us see if 'jump' is now noun
​

########################################################################################################################################################################
#POS-NER-WORDCLOUD-WORDHISTOGRAM-NGRAMS-SENTIMENT.ipynb
s
 os.getcwd()
print(cwd)
importhttp://localhost:8888/notebooks/Desktop/GreatLearning/NLP/All_Notebooks/POS-NER-WORDCLOUD-WORDHISTOGRAM-NGRAMS-SENTIMENT.ipynb#s os
cwd = os.getcwd()
print(cwd)
import pandas as pd       
train = pd.read_csv("labeledTrainData.tsv", header=0,delimiter="\t", quoting=3)
from bs4 import BeautifulSoup
import re
import nltk
from nltk.corpus import stopwords
def review_to_words( raw_review ):
    # Function to convert a raw review to a string of words
    # The input is a single string (a raw movie review), and 
    # the output is a single string (a preprocessed movie review)
    #
    # 1. Remove HTML
    review_text = BeautifulSoup(raw_review).get_text() 
    #
    # 2. Remove non-letters        
    letters_only = re.sub("[^a-zA-Z]", " ", review_text) 
    #
    # 3. Convert to lower case, split into individual words
    words = letters_only.lower().split()                             
    #
    # 4. In Python, searching a set is much faster than searching
    #   a list, so convert the stop words to a set
    stops = set(stopwords.words("english"))                  
    # 
    # 5. Remove stop words
    meaningful_words = [w for w in words if not w in stops]   
    #
    # 6. Join the words back into one string separated by space, 
    # and return the result.
    return( " ".join( meaningful_words ))  
# Get the number of reviews based on the dataframe column size
num_reviews = train["review"].size
​
# Initialize an empty list to hold the clean reviews
clean_train_reviews = []
​
# Loop over each review; create an index i that goes from 0 to the length
# of the movie review list 
for i in range( 0, num_reviews ):
    # Call our function for each one, and add the result to the list of
    # clean reviews
    clean_train_reviews.append( review_to_words( train["review"][i] ) )
clean_train_reviews_str=""
for i in range( 0, num_reviews ):
    clean_train_reviews_str+=clean_train_reviews[i]
clean_train_reviews_str
document_tokens = clean_train_reviews_str.split(" ")
document_tokens
print('No. of tokens in entire corpus:', len(document_tokens))
tokens_freq = pd.Series(document_tokens).value_counts()
tokens_freq
df_tokens = tokens_freq.to_frame('frequency')
df_tokens
import matplotlib.pyplot as plt
plt.figure(figsize=(24,5))
df_tokens['frequency'].head(25).plot.bar()
plt.xticks(fontsize = 20)
from wordcloud import WordCloud
wc = WordCloud( collocations=False, background_color='white').generate(clean_train_reviews_str)
plt.figure(figsize=(20,5))
plt.imshow(wc)
plt.axis('off');
import spacy
nlp = spacy.load('en_core_web_sm', parse=True, tag=True, entity=True)
teststr = 'nat geo release special edition magazine shoot oneplus pro national geographic reveal cover upcoming special edition magazine shoot oneplus pro notably image magazine shoot smartphone oneplus pro whole camera bag pocket allow us able shoot whole magazine issue smartphone say photographer krystle wright'
sentence_nlp = nlp(teststr)
# POS tagging with Spacy 
spacy_pos_tagged = [(word, word.tag_, word.pos_) for word in sentence_nlp]
pd.DataFrame(spacy_pos_tagged, columns=['Word', 'POS tag', 'Tag type'])
teststr='Uber falls below $ 70bn value on 1st trading day, CEO blames trade war. Uber ended its first day of trading with a market cap of $69.7 billion , below its last private valuation of $76 billion. CEO Dara Khosrowshahi PERSON said US - China trade tensions played a role in the stocks weak performance, adding, You cant pick when you go public. Uber priced its IPO at $45 per share, valuing the company at $75.5 billion'
sentence_nlp = nlp(teststr)
# print named entities in article
print([(word, word.ent_type_) for word in sentence_nlp if word.ent_type_])
from spacy import displacy
# visualize named entities
displacy.render(sentence_nlp, style='ent', jupyter=True)
# noun chunks
doc = nlp(u'Is it a rational decision? The cat and the dog , Morgan Stanley, sleep in the basket, Fidelity Investments near the door, Soviet Union is a Democratic country.')
for np in doc.noun_chunks:
    print(np.text)
from nltk.tokenize import sent_tokenize, word_tokenize
​
data = "All work and no play makes jack a dull boy, all work and no play"
print(word_tokenize(data))
data = "All work and no play makes jack dull boy. All work and no play makes jack a dull boy."
print(sent_tokenize(data))
from textblob import TextBlob
blob = TextBlob('Great Learning is a great platform to learn data science')
for ngram in blob.ngrams(2):
    print (ngram)
for ngram in blob.ngrams(3):
    print (ngram)
print (blob)
blob.sentiment
​

########################################################################################################################################################################
#regular expressions.ipynb

Regular Expressions
Regular expressions is a concept used to search for patterns in string text.

This is a univerisal concept for any programming language or text editing program.

We're going to learn the concepts while we learn the syntax for python.

The goal of regular expressions is to be able to search for a specific type of text inside of a string. If we have a form on our webpage where we ask for email addresses, can we check whether the inputted string actually follows the form of an email? some letters or numbers or special characters, then an @ sign then some more letters numbers or special characters then a . then a few more letters

import re
​
text_to_search = '''
abcdefghijklmnopqurtuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
1234567890
123abc
​
Hello HelloHello
​
MetaCharacters (Need to be escaped):
. ^ $ * + ? { } [ ] \ | ( )
​
utexas.edu
​
321-555-4321
123.555.1234
​
daniel-mitchell@utexas.edu
​
Mr. Johnson
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T
'''
​
​
​
Searching literals
pattern = re.compile(r'abc')
matches = pattern.finditer(text_to_search)
for mat in matches:
    print(mat)
print(text_to_search[69:72])
pattern = re.compile(r'cba')
matches = pattern.finditer(text_to_search)
for mat in matches:
    print(mat)
Searching special characters
pattern = re.compile(r'.')
matches = pattern.finditer(text_to_search)
for mat in matches:
    print(mat)
pattern = re.compile(r'\.')
matches = pattern.finditer(text_to_search)
for mat in matches:
    print(mat)
pattern = re.compile(r'\d')
matches = pattern.finditer(text_to_search)
for mat in matches:
    print(mat)
pattern = re.compile(r'\D')
matches = pattern.finditer(text_to_search)
for mat in matches:
    print(mat)
pattern = re.compile(r'\d\w')
matches = pattern.finditer(text_to_search)
for mat in matches:
    print(mat)
pattern = re.compile(r'\d\s')
matches = pattern.finditer(text_to_search)
for mat in matches:
    print(mat)
Word boundary
# Hello HelloHello
pattern = re.compile(r'Hello')
matches = pattern.finditer(text_to_search)
for mat in matches:
    print(mat)
pattern = re.compile(r'Hello\b')
matches = pattern.finditer(text_to_search)
for mat in matches:
    print(mat)
pattern = re.compile(r'\bHello\b')
matches = pattern.finditer(text_to_search)
for mat in matches:
    print(mat)
pattern = re.compile(r'\BHello\b')
matches = pattern.finditer(text_to_search)
for mat in matches:
    print(mat)
pattern = re.compile(r'\b\d')
matches = pattern.finditer(text_to_search)
for mat in matches:
    print(mat)
pattern = re.compile(r'^\s')
matches = pattern.finditer(text_to_search)
for mat in matches:
    print(mat)
Character sets
pattern = re.compile(r'[123]\w')
matches = pattern.finditer(text_to_search)
for mat in matches:
    print(mat)
pattern = re.compile(r'[a-z][a-z]')
matches = pattern.finditer(text_to_search)
for mat in matches:
    print(mat)
pattern = re.compile(r'[a-zA-Z0-9][a-zA-z-]')
matches = pattern.finditer(text_to_search)
for mat in matches:
    print(mat)
pattern = re.compile(r'[a-zA-Z][^a-zA-z]')
matches = pattern.finditer(text_to_search)
for mat in matches:
    print(mat)
Character groups
pattern = re.compile(r'(abc|edu|texas)\b')
matches = pattern.finditer(text_to_search)
for mat in matches:
    print(mat)
pattern = re.compile(r'([A-Z]|llo)[a-zA-z]')
matches = pattern.finditer(text_to_search)
for mat in matches:
    print(mat)
Quantifiers
pattern = re.compile(r'Mr\.?\s[A-Z]')
matches = pattern.finditer(text_to_search)
for mat in matches:
    print(mat)
pattern = re.compile(r'Mr\.?\s[A-Z][a-z]*')
matches = pattern.finditer(text_to_search)
for mat in matches:
    print(mat)
pattern = re.compile(r'M(s|rs)\.?\s[A-Z][a-z]*')
matches = pattern.finditer(text_to_search)
for mat in matches:
    print(mat)
pattern = re.compile(r'\d{3}[.-]\d{3}[.-]\d{4}')
matches = pattern.finditer(text_to_search)
for mat in matches:
    print(mat)
pattern = re.compile(r'[a-zA-Z0-9_]+\.[a-z]{3}')
matches = pattern.finditer(text_to_search)
for mat in matches:
    print(mat)
pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
matches = pattern.finditer(text_to_search)
for mat in matches:
    print(mat)
Accessing information in the Match object
​
pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]{2,4}')
matches = pattern.finditer(text_to_search)
for mat in matches:
    print(mat.span(0))
    print(mat.group(0))
    print(text_to_search[mat.span(0)[0]:mat.span(0)[1]])
    
    
​
urls = r'''
https://www.google.com
http://yahoo.com
https://www.whitehouse.gov
https://craigslist.org
'''
pattern = re.compile(r'https?://(www\.)?\w+\.\w+')
matches = pattern.finditer(urls)
for mat in matches:
    print(mat)
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.finditer(urls)
for mat in matches:
    print(mat.group(2)+mat.group(3))
pattern = re.compile(r'https?://(www\.)?(\w+)(\.\w+)')
matches = pattern.finditer(urls)
for mat in matches:
    print(mat.group(0))
    print(urls[mat.span(2)[0]:mat.span(2)[1]]+urls[mat.span(3)[0]:mat.span(3)[1]])

########################################################################################################################################################################
#S3-TakeHome-solution.ipynb

Import the packages
import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
​
%matplotlib inline
2.Data retrieval
2.1. Parse the https://www.ndtv.com/india url and find oout the topic of category in the url.
url = 'https://www.ndtv.com/india'
news_data = []
news_category = url.split('/')
news_category
news_category = news_category[-1]
​
2.2. Fetch the news-article , news-headline & news-category of the url
data = requests.get(url)
data.content
soup = BeautifulSoup(data.content, 'html.parser')
news_articles = [{'news_headline': headline.find('a')['title'],
                  'news_article': article.string,
                  'news_category': news_category} 
                 for headline, article in zip(soup.find_all('h2',class_ = ['nstory_header']), 
                                              soup.find_all('div',class_ = ['nstory_intro']))]
news_data.extend(news_articles)
news_data
2.3. Prepare a dataframe with news-headline, news-article & news-category
df = pd.DataFrame(news_data)
df = df[['news_headline', 'news_article', 'news_category']]
df.head(3)
2.4.Prepare user defined function to extract data (news-headline, news-article & news-category) from ndtv.com (from the technology, sports, world categories) and store it in a dataframe
urls_list = ['https://www.ndtv.com/india',
             'https://www.ndtv.com/world-news',
             'https://www.ndtv.com/cities']
def datasetPrepare(urls_list):
    news_data = []
    for url in urls_list:
        news_category = url.split('/')[-1]
        data = requests.get(url)
        soup = BeautifulSoup(data.content, 'html.parser')
        news_articles = [{'news_headline': headline.find('a')['title'], 'news_article': article.string, 'news_category': news_category} 
                 for headline, article in zip(soup.find_all('h2',class_ = ['nstory_header']), soup.find_all('div',class_ = ['nstory_intro']))]
        news_data.extend(news_articles) 
    df =  pd.DataFrame(news_data)
    df = df[['news_headline', 'news_article', 'news_category']]
    return df    
news_df = datasetPrepare(urls_list)
news_df.info()
news_df.head(5)
news_df.news_category.value_counts()
3.Text Wrangling and Pre-processing
import spacy
import nltk
from nltk.tokenize.toktok import ToktokTokenizer
import re
import unicodedata
nlp = spacy.load('en')
nltk.download('stopwords')
tokenizer = ToktokTokenizer()
stopword_list = nltk.corpus.stopwords.words('english')
stopword_list.remove('no')
stopword_list.remove('not')
3.1.Remove HTML tags
def strip_html_tags(text):
    soup = BeautifulSoup(text, "html.parser")
    stripped_text = soup.get_text()
    return stripped_text
​
strip_html_tags('<html><h2>Some important text</h2></html>')
3.2.Remove accented characters
def remove_accented_chars(text):
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    return text
​
remove_accented_chars('Sómě Áccěntěd těxt')
3.3.Remove special characters
def remove_special_characters(text, remove_digits=False):
    pattern = r'[^a-zA-z0-9\s]' if not remove_digits else r'[^a-zA-z\s]'
    text = re.sub(pattern, '', text)
    return text
remove_special_characters("Well this was fun! What do you think? 123#@!", remove_digits=True)
3.4.Text lemmatization
def lemmatize_text(text):
    text = nlp(text)
    text = ' '.join([word.lemma_ if word.lemma_ != '-PRON-' else word.text for word in text])
    return text
lemmatize_text("My system keeps crashing! his crashed yesterday, ours crashes daily")
3.5.Text stemming
def simple_stemmer(text):
    ps = nltk.porter.PorterStemmer()
    text = ' '.join([ps.stem(word) for word in text.split()])
    return text
​
simple_stemmer("My system keeps crashing his crashed yesterday, ours crashes daily")
3.6.Remove stopwords
def remove_stopwords(text, is_lower_case=False):
    tokens = tokenizer.tokenize(text)
    tokens = [token.strip() for token in tokens]
    if is_lower_case:
        filtered_tokens = [token for token in tokens if token not in stopword_list]
    else:
        filtered_tokens = [token for token in tokens if token.lower() not in stopword_list]
    filtered_text = ' '.join(filtered_tokens)    
    return filtered_text
​
remove_stopwords("The, and, if are stopwords, computer is not")
3.7.Building a text normalizer
def normalize_corpus(corpus, html_stripping=True, contraction_expansion=True,
                     accented_char_removal=True, text_lower_case=True, 
                     text_lemmatization=True, special_char_removal=True, 
                     stopword_removal=True, remove_digits=True):
    
    normalized_corpus = []
    # normalize each document in the corpus
    for doc in corpus:
        # strip HTML
        if html_stripping:
            doc = strip_html_tags(doc)
        # remove accented characters
        if accented_char_removal:
            doc = remove_accented_chars(doc)
        # lowercase the text    
        if text_lower_case:
            doc = doc.lower()
        # remove extra newlines
        doc = re.sub(r'[\r|\n|\r\n]+', ' ',doc)
        # lemmatize text
        if text_lemmatization:
            doc = lemmatize_text(doc)
        # remove special characters and\or digits    
        if special_char_removal:
            # insert spaces between special characters to isolate them    
            special_char_pattern = re.compile(r'([{.(-)!}])')
            doc = special_char_pattern.sub(" \\1 ", doc)
            doc = remove_special_characters(doc, remove_digits=remove_digits)  
        # remove extra whitespace
        doc = re.sub(' +', ' ', doc)
        # remove stopwords
        if stopword_removal:
            doc = remove_stopwords(doc, is_lower_case=text_lower_case)
            
        normalized_corpus.append(doc)
        
    return normalized_corpus
3.8.Pre-process and normalize news articles
news_df['full_text'] = news_df["news_headline"].map(str)+ '. ' + news_df["news_article"]
news_df['clean_text'] = normalize_corpus(news_df['full_text'])
norm_corpus = list(news_df['clean_text'])
news_df.iloc[1][['full_text', 'clean_text']].to_dict()
Save the news articles
news_df.to_csv('news.csv', index=False, encoding='utf-8')
Read the data
news_df = pd.read_csv('/content/news.csv')
3.9.Tagging Parts of Speech
corpus = normalize_corpus(news_df['full_text'], text_lower_case=False, 
                          text_lemmatization=False, special_char_removal=False)
​
sentence = str(news_df.iloc[1].news_headline)
sentence_nlp = nlp(sentence)
spacy_pos_tagged = [(word, word.tag_, word.pos_) for word in sentence_nlp]
pd.DataFrame(spacy_pos_tagged, columns=['Word', 'POS tag', 'Tag type'])
nltk.download('punkt')
nltk.download('maxent_treebank_pos_tagger')
nltk.download('averaged_perceptron_tagger')
nltk_pos_tagged = nltk.pos_tag(sentence.split())
pd.DataFrame(nltk_pos_tagged, columns=['Word', 'POS tag'])
3.10.Named Entity Recognition
sentence = str(news_df.iloc[1].full_text)
sentence
sentence_nlp = nlp(sentence)
sentence_nlp
print([(word, word.ent_type_) for word in sentence_nlp if word.ent_type_])
named_entities = []
for sentence in corpus:
    temp_entity_name = ''
    temp_named_entity = None
    sentence = nlp(sentence)
    for word in sentence:
        term = word.text 
        tag = word.ent_type_
        if tag:
            temp_entity_name = ' '.join([temp_entity_name, term]).strip()
            temp_named_entity = (temp_entity_name, tag)
        else:
            if temp_named_entity:
                named_entities.append(temp_named_entity)
                temp_entity_name = ''
                temp_named_entity = None
​
entity_frame = pd.DataFrame(named_entities, 
                            columns=['Entity Name', 'Entity Type'])
top_entities = (entity_frame.groupby(by=['Entity Name', 'Entity Type'])
                           .size()
                           .sort_values(ascending=False)
                           .reset_index().rename(columns={0 : 'Frequency'}))
top_entities.T.iloc[:,:15]
top_entities = (entity_frame.groupby(by=['Entity Type'])
                           .size()
                           .sort_values(ascending=False)
                           .reset_index().rename(columns={0 : 'Frequency'}))
top_entities.T.iloc[:,:15]
4.Emotion and Sentiment Analysis
pip install afinn
from afinn import Afinn
af = Afinn()
sentiment_scores = [af.score(article) for article in corpus]
sentiment_category = ['positive' if score > 0 
                          else 'negative' if score < 0 
                              else 'neutral' 
                                  for score in sentiment_scores]
df = pd.DataFrame([list(news_df['news_category']), sentiment_scores, sentiment_category]).T
df.columns = ['news_category', 'sentiment_score', 'sentiment_category']
df['sentiment_score'] = df.sentiment_score.astype('float')
df.groupby(by=['news_category']).describe()
f, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 4))
sp = sns.stripplot(x='news_category', y="sentiment_score",  hue='news_category', data=df, ax=ax1)
bp = sns.boxplot(x='news_category', y="sentiment_score", hue='news_category', data=df, palette="Set2", ax=ax2)
t = f.suptitle('Visualizing News Sentiment', fontsize=14)
fc = sns.factorplot(x="news_category", hue="sentiment_category", 
                    data=df, kind="count", 
                    palette={"negative": "#FE2020", 
                             "positive": "#BADD07", 
                             "neutral": "#68BFF5"})
df.news_category.unique()
pos_idx = df[(df.news_category=='world-news') & (df.sentiment_score == df[(df.news_category=='world-news')].sentiment_score.max())].index[0]
neg_idx = df[(df.news_category=='world-news') & (df.sentiment_score == df[(df.news_category=='world-news')].sentiment_score.min())].index[0]
print('Most Negative world-news Article:', news_df.iloc[neg_idx][['news_article']][0])
print()
print('Most Positive world-news Article:', news_df.iloc[pos_idx][['news_article']][0])
df1 = df[df.news_category=='cities']
pd.unique(df1.sentiment_score)
pos_idx = df[(df.news_category=='cities') & (df.sentiment_score == df[(df.news_category=='cities')].sentiment_score.max())].index[0]
neg_idx = df[(df.news_category=='cities') & (df.sentiment_score == df[(df.news_category=='cities')].sentiment_score.min())].index[0]
​
print('Most Negative cities News Article:', news_df.iloc[neg_idx][['news_article']][0])
print()
print('Most Positive cities News Article:', news_df.iloc[pos_idx][['news_article']][0])
from textblob import TextBlob
sentiment_scores_tb = [round(TextBlob(article).sentiment.polarity, 3) for article in news_df['clean_text']]
sentiment_category_tb = ['positive' if score > 0 
                             else 'negative' if score < 0 
                                 else 'neutral' 
                                     for score in sentiment_scores_tb]
df = pd.DataFrame([list(news_df['news_category']), sentiment_scores_tb, sentiment_category_tb]).T
df.columns = ['news_category', 'sentiment_score', 'sentiment_category']
df['sentiment_score'] = df.sentiment_score.astype('float')
df.groupby(by=['news_category']).describe()
df.head()
fc = sns.factorplot(x="news_category", hue="sentiment_category", 
                    data=df, kind="count", 
                    palette={"negative": "#FE2020", 
                             "positive": "#BADD07", 
                             "neutral": "#68BFF5"})
from sklearn.metrics import confusion_matrix
true_labels=sentiment_category
predicted_labels=sentiment_category_tb
confusion_matrix(true_labels, predicted_labels)
plt.figure(figsize = (5,5))
conf = pd.DataFrame(confusion_matrix(true_labels, predicted_labels),
            index = ['negative', 'neutral', 'positive'],
                  columns = ['negative', 'neutral', 'positive'])
sns.heatmap(conf, annot=True)

########################################################################################################################################################################
#S3_Inclass_question_without_Scraping.ipynb

Read the data(news.csv)
news_df = pd.read_csv("news.csv")
news_df.head()
news_df.news_category.value_counts()
Tag Parts of Speech
# Text preprocessing:
​
nlp = spacy.load('en_core_web_sm')
nltk.download('stopwords')
tokenizer = ToktokTokenizer()
stopword_list = nltk.corpus.stopwords.words('english')
stopword_list.remove('no')
stopword_list.remove('not')
def strip_html_tags(text):
    soup = BeautifulSoup(text, "html.parser")
    stripped_text = soup.get_text()
    return stripped_text
​
def remove_accented_chars(text):
    text = unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')
    return text
​
def remove_special_characters(text, remove_digits=False):
    pattern = r'[^a-zA-z0-9\s]' if not remove_digits else r'[^a-zA-z\s]'
    text = re.sub(pattern, '', text)
    return text
​
def lemmatize_text(text):
    text = nlp(text)
    text = ' '.join([word.lemma_ if word.lemma_ != '-PRON-' else word.text for word in text])
    return text
​
def simple_stemmer(text):
    ps = nltk.porter.PorterStemmer()
    text = ' '.join([ps.stem(word) for word in text.split()])
    return text 
​
def remove_stopwords(text, is_lower_case=False):
    tokens = tokenizer.tokenize(text)
    tokens = [token.strip() for token in tokens]
    if is_lower_case:
        filtered_tokens = [token for token in tokens if token not in stopword_list]
    else:
        filtered_tokens = [token for token in tokens if token.lower() not in stopword_list]
    filtered_text = ' '.join(filtered_tokens)    
    return filtered_text
​
def normalize_corpus(corpus, html_stripping=True, contraction_expansion=True,
                     accented_char_removal=True, text_lower_case=True, 
                     text_lemmatization=True, special_char_removal=True, 
                     stopword_removal=True, remove_digits=True):
    
    normalized_corpus = []
    # normalize each document in the corpus
    for doc in corpus:
        # strip HTML
        if html_stripping:
            doc = strip_html_tags(doc)
        # remove accented characters
        if accented_char_removal:
            doc = remove_accented_chars(doc)
        # lowercase the text    
        if text_lower_case:
            doc = doc.lower()
        # remove extra newlines
        doc = re.sub(r'[\r|\n|\r\n]+', ' ',doc)
        # lemmatize text
        if text_lemmatization:
            doc = lemmatize_text(doc)
        # remove special characters and\or digits    
        if special_char_removal:
            # insert spaces between special characters to isolate them    
            special_char_pattern = re.compile(r'([{.(-)!}])')
            doc = special_char_pattern.sub(" \\1 ", doc)
            doc = remove_special_characters(doc, remove_digits=remove_digits)  
        # remove extra whitespace
        doc = re.sub(' +', ' ', doc)
        # remove stopwords
        if stopword_removal:
            doc = remove_stopwords(doc, is_lower_case=text_lower_case)
            
        normalized_corpus.append(doc)
        
    return normalized_corpus
corpus = normalize_corpus(news_df['full_text'], text_lower_case=False, 
                          text_lemmatization=False, special_char_removal=False)
​
sentence = str(news_df.iloc[1].news_headline)
sentence_nlp = nlp(sentence)
spacy_pos_tagged = [(word, word.tag_, word.pos_) for word in sentence_nlp]
pd.DataFrame(spacy_pos_tagged, columns=['Word', 'POS tag', 'Tag type'])
nltk.download('punkt')
nltk.download('maxent_treebank_pos_tagger')
nltk.download('averaged_perceptron_tagger')
​
nltk_pos_tagged = nltk.pos_tag(sentence.split())
pd.DataFrame(nltk_pos_tagged, columns=['Word', 'POS tag'])
​
​
Named Entity Recognition
Identify the named entities for the first news article.

sentence = str(news_df.iloc[2].full_text)
sentence
sentence_nlp = nlp(sentence)
sentence_nlp
print([(word, word.ent_type_) for word in sentence_nlp if word.ent_type_])
​
named_entities = []
for sentence in corpus:
    temp_entity_name = ''
    temp_named_entity = None
    sentence = nlp(sentence)
    for word in sentence:
        term = word.text 
        tag = word.ent_type_
        if tag:
            temp_entity_name = ' '.join([temp_entity_name, term]).strip()
            temp_named_entity = (temp_entity_name, tag)
        else:
            if temp_named_entity:
                named_entities.append(temp_named_entity)
                temp_entity_name = ''
                temp_named_entity = None
​
entity_frame = pd.DataFrame(named_entities, 
                            columns=['Entity Name', 'Entity Type'])
top_entities = (entity_frame.groupby(by=['Entity Name', 'Entity Type'])
                           .size()
                           .sort_values(ascending=False)
                           .reset_index().rename(columns={0 : 'Frequency'}))
top_entities.T.iloc[:,:15]
top_entities = (entity_frame.groupby(by=['Entity Type'])
                           .size()
                           .sort_values(ascending=False)
                           .reset_index().rename(columns={0 : 'Frequency'}))
top_entities.T.iloc[:,:15]
Emotion and Sentiment Analysis
Perform sentiment analyis on all the news articles.

from afinn import Afinn
​
af = Afinn()
sentiment_scores = [af.score(article) for article in corpus]
​
sentiment_category = ['positive' if score > 0 
                          else 'negative' if score < 0 
                              else 'neutral' 
                                  for score in sentiment_scores]
df = pd.DataFrame([list(news_df['news_category']), sentiment_scores, sentiment_category]).T
​
df.columns = ['news_category', 'sentiment_score', 'sentiment_category']
df['sentiment_score'] = df.sentiment_score.astype('float')
df.groupby(by=['news_category']).describe()
​
f, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 4))
sp = sns.stripplot(x='news_category', y="sentiment_score",  hue='news_category', data=df, ax=ax1)
bp = sns.boxplot(x='news_category', y="sentiment_score", hue='news_category', data=df, palette="Set2", ax=ax2)
t = f.suptitle('Visualizing News Sentiment', fontsize=14)
fc = sns.catplot(x="news_category", hue="sentiment_category", 
                    data=df, kind="count", 
                    palette={"negative": "#FE2020", 
                             "positive": "#BADD07", 
                             "neutral": "#68BFF5"})
news_df.news_category.unique()
​
pos_idx = df[(df.news_category=='technology') & (df.sentiment_score == df[(df.news_category=='technology')].sentiment_score.max())].index[0]
​
neg_idx = df[(df.news_category=='technology') & (df.sentiment_score == df[(df.news_category=='technology')].sentiment_score.min())].index[0]
​
df
print('Most Negative technology Article:', news_df.iloc[neg_idx][['news_article']][0])
print()
print('Most Positive technology Article:', news_df.iloc[pos_idx][['news_article']][0])
df1 = df[df.news_category=='technology']
pd.unique(df1.sentiment_score)
pos_idx = df[(df.news_category=='technology') & (df.sentiment_score == df[(df.news_category=='technology')].sentiment_score.max())].index[0]
neg_idx = df[(df.news_category=='technology') & (df.sentiment_score == df[(df.news_category=='technology')].sentiment_score.min())].index[0]
​
print('Most Negative cities News Article:', news_df.iloc[neg_idx][['news_article']][0])
print()
print('Most Positive cities News Article:', news_df.iloc[pos_idx][['news_article']][0])
Using text blob library: (Approach 2)
from textblob import TextBlob
​
sentiment_scores_tb = [round(TextBlob(article).sentiment.polarity, 3) for article in news_df['clean_text']]
​
sentiment_category_tb = ['positive' if score > 0 
                             else 'negative' if score < 0 
                                 else 'neutral' 
                                     for score in sentiment_scores_tb]
df = pd.DataFrame([list(news_df['news_category']), sentiment_scores_tb, sentiment_category_tb]).T
df.columns = ['news_category', 'sentiment_score', 'sentiment_category']
df['sentiment_score'] = df.sentiment_score.astype('float')
df.groupby(by=['news_category']).describe()
df.head()
​
fc = sns.catplot(x="news_category", hue="sentiment_category", 
                    data=df, kind="count", 
                    palette={"negative": "#FE2020", 
                             "positive": "#BADD07", 
                             "neutral": "#68BFF5"})
from sklearn.metrics import confusion_matrix
true_labels=sentiment_category
predicted_labels=sentiment_category_tb
confusion_matrix(true_labels, predicted_labels)
plt.figure(figsize = (5,5))
conf = pd.DataFrame(confusion_matrix(true_labels, predicted_labels),
            index = ['negative', 'neutral', 'positive'],
                  columns = ['negative', 'neutral', 'positive'])
sns.heatmap(conf, annot=True, cmap='vlag')

########################################################################################################################################################################
#S4 - TakeHome Solutions.ipynb

Text generation using a RNN
Given a sequence of words from this data, train a model to predict the next word in the sequence. Longer sequences of text can be generated by calling the model repeatedly.

Libraries used in this notebook along with their version:

google 2.0.3

numpy 1.18.3

tensorflow 2.2.0rc3

sklearn 0.0

import tensorflow
tensorflow.__version__
Mount your Google Drive

from google.colab import drive
drive.mount('/content/drive/')
import os
os.chdir('/content/drive/MyDrive/My_NLP/Session 3/')
Import Keras and other libraries
import glob
​
from sklearn.utils import shuffle
import numpy as np
​
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import LSTM, Dense, Dropout, Embedding, Masking, Bidirectional
from tensorflow.keras.optimizers import Adam
from tensorflow.keras import backend
Download data
Data is collected from http://www.gutenberg.org

Go to this link to download the collected data https://github.com/partoftheorigin/text-generation-datasets/tree/master/oscar_wilde

Load the Oscar Wilde dataset
Store all the ".txt" file names in a list

import zipfile
zip_ref = zipfile.ZipFile("/content/drive/MyDrive/My_NLP/Session 3/data.zip", 'r')
zip_ref.extractall("/content/drive/MyDrive/My_NLP/Session 3/tmp")
zip_ref.close()
filelist = glob.glob("/content/drive/MyDrive/My_NLP/Session 3/tmp/data/*.txt")
Read the data
Read contents of every file from the list and append the text in a new list

text_data = []
for file in filelist:
    with open(file, "r") as file:
      text_data.append(file.read())
Process the text
Initialize and fit the tokenizer

tokenizer = Tokenizer()
tokenizer.fit_on_texts(text_data)
Vectorize the text
Before training, we need to map strings to a numerical representation. Create two lookup tables: one mapping words to numbers, and another for numbers to words.

word_idx = tokenizer.word_index #Last is the key
idx_word = tokenizer.index_word
Get the word count for every word and also get the total number of words.

word_counts = tokenizer.word_counts
num_words = len(word_counts)
Convert text to sequence of numbers

sequences = tokenizer.texts_to_sequences(text_data)
Generate Features and Labels
features = []
labels = []
​
training_length = 50
# Iterate through the sequences of tokens
for seq in sequences:
    # Create multiple training examples from each sequence
    for i in range(training_length, training_length+300):
        # Extract the features and label
        extract = seq[i - training_length: i - training_length + 20]
​
        # Set the features and label
        features.append(extract[:-1])
        labels.append(extract[-1])
The prediction task
Given a word, or a sequence of words, what is the most probable next word? This is the task we're training the model to perform. The input to the model will be a sequence of words, and we train the model to predict the output—the following word at each time step.

Since RNNs maintain an internal state that depends on the previously seen elements, given all the words computed until this moment, what is the next word?

Generate training and testing data
from sklearn.utils import shuffle
import numpy as np
​
features, labels = shuffle(features, labels, random_state=1)
​
# Decide on number of samples for training
train_end = int(0.75 * len(labels))
​
train_features = np.array(features[:train_end])
valid_features = np.array(features[train_end:])
​
train_labels = labels[:train_end]
valid_labels = labels[train_end:]
​
# Convert to arrays
X_train, X_valid = np.array(train_features), np.array(valid_features)
​
# Using int8 for memory savings
y_train = np.zeros((len(train_labels), num_words), dtype=np.int8)
y_valid = np.zeros((len(valid_labels), num_words), dtype=np.int8)
​
# One hot encoding of labels
for example_index, word_index in enumerate(train_labels):
    y_train[example_index, word_index] = 1
​
for example_index, word_index in enumerate(valid_labels):
    y_valid[example_index, word_index] = 1
This is just to check the features and labels

for i, sequence in enumerate(X_train[:1]):
    text = []
    for idx in sequence:
        text.append(idx_word[idx])
        
    print('Features: ' + ' '.join(text)+'\n')
    print('Label: ' + idx_word[np.argmax(y_train[i])] + '\n')
Build The Model
Use keras.Sequential to define the model. For this simple example three layers are used to define our model:

keras.layers.Embedding: The input layer. A trainable lookup table that will map the numbers of each character to a vector with embedding_dim dimensions;
keras.layers.LSTM: A type of RNN with size units=rnn_units (You can also use a GRU layer here.)
keras.layers.Dense: The output layer, with num_words outputs.
model = Sequential()
​
# Embedding layer
model.add(
    Embedding(
        input_dim=num_words,
        output_dim=100,
        weights=None,
        trainable=True))
​
# Recurrent layer
model.add(
    LSTM(
        64, return_sequences=False, dropout=0.1,
        recurrent_dropout=0.1))
​
# Fully connected layer
model.add(Dense(64, activation='relu'))
​
# Dropout for regularization
model.add(Dropout(0.5))
​
# Output layer
model.add(Dense(num_words, activation='softmax'))
​
# Compile the model
model.compile(
    optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
​
model.summary()
For each word the model looks up the embedding, runs the LSTM one timestep with the embedding as input, and applies the dense layer to generate logits predicting the log-liklihood of the next word.

Train the model
h = model.fit(X_train, y_train, epochs = 1, batch_size = 100, verbose = 1)
Save Model
# save the model to file
model.save('./tmp/data/model_1000epochs.h5')
If you have already trained the model and saved it, you can load a pretrained model
1
# load the model
2
model = load_model('./tmp/data/model_1000epochs.h5')
Note: After loading the model run model.fit() to continue training form there, if required.
model.fit(X_train, y_train, batch_size=50, epochs=500)
Evaluation
print(model.evaluate(X_train, y_train, batch_size = 20))
print('\nModel Performance: Log Loss and Accuracy on validation data')
print(model.evaluate(X_valid, y_valid, batch_size = 20))
Generate text
seed_length=50
new_words=50
diversity=1
n_gen=1
​
import random
​
# Choose a random sequence
seq = random.choice(sequences)
​
# print seq
​
# Choose a random starting point
seed_idx = random.randint(0, len(seq) - seed_length - 10)
# Ending index for seed
end_idx = seed_idx + seed_length
​
gen_list = []
​
for n in range(n_gen):
    # Extract the seed sequence
    seed = seq[seed_idx:end_idx]
    original_sequence = [idx_word[i] for i in seed]
    generated = seed[:] + ['#']
​
    # Find the actual entire sequence
    actual = generated[:] + seq[end_idx:end_idx + new_words]
        
    # Keep adding new words
    for i in range(new_words):
​
        # Make a prediction from the seed
        preds = model.predict(np.array(seed).reshape(1, -1))[0].astype(np.float64)
​
  
        # Softmax
        preds = preds / sum(preds)
​
        # Choose the next word
        probas = np.random.multinomial(1, preds, 1)[0]
​
        next_idx = np.argmax(probas)
​
        # New seed adds on old word
        #             seed = seed[1:] + [next_idx]
        seed += [next_idx]
        generated.append(next_idx)
    # Showing generated and actual abstract
    n = []
​
    for i in generated:
        n.append(idx_word.get(i, '< --- >'))
​
    gen_list.append(n)
​
a = []
​
for i in actual:
    a.append(idx_word.get(i, '< --- >'))
​
a = a[seed_length:]
​
gen_list = [gen[seed_length:seed_length + len(a)] for gen in gen_list]
​
print('Original Sequence: \n'+' '.join(original_sequence))
print("\n")
# print(gen_list)
print('Generated Sequence: \n'+' '.join(gen_list[0][1:]))
# print(a)
​



########################################################################################################################################################################
#S4_Faculty_Notebook_nlp (1).ipynb
Text generation using a RNN
1.Goal
Given a word, or a sequence of words, what is the most probable next word? This is the task we're training the model to perform. The input to the model will be a sequence of words, and we train the model to predict the output—the following word at each time step.

Since RNNs maintain an internal state that depends on the previously seen elements, given all the words computed until this moment, what is the next word?

Libraries used in this notebook along with their version:

google 2.0.3

numpy 1.18.3

tensorflow 2.4.1

sklearn 0.0

Given a sequence of words from this data, train a model to predict the next word in the sequence. Longer sequences of text can be generated by calling the model repeatedly.

import tensorflow
tensorflow.__version__
Mount your Google Drive

from google.colab import drive
drive.mount('/content/drive/')
import os
os.chdir('/content/drive/MyDrive/My_NLP/Session 4/FNB/')
2.Import Keras and other libraries
import glob
​
from sklearn.utils import shuffle
import numpy as np
​
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import LSTM, Dense, Dropout, Embedding, Masking, Bidirectional
from tensorflow.keras.optimizers import Adam
from tensorflow.keras import backend
3.Download data
Data is collected from http://www.gutenberg.org

Load the Tagore dataset
Store all the ".txt" file names in a list

import zipfile
zip_ref = zipfile.ZipFile("/content/drive/MyDrive/My_NLP/Session 4/FNB/Tagore.zip", 'r')
zip_ref.extractall("/content/drive/MyDrive/My_NLP/Session 4/FNB/Tagore")
zip_ref.close()
filelist = glob.glob("/content/drive/MyDrive/My_NLP/Session 4/FNB/Tagore/data/*.txt")
Read the data
Read contents of every file from the list and append the text in a new list

text_data = []
for file in filelist:
    with open(file, "r") as file:
      text_data.append(file.read())
4.Process the text
Initialize and fit the tokenizer

tokenizer = Tokenizer()
tokenizer.fit_on_texts(text_data)
Vectorize the text
Before training, we need to map strings to a numerical representation. Create two lookup tables: one mapping words to numbers, and another for numbers to words.

word_idx = tokenizer.word_index #Last is the key
idx_word = tokenizer.index_word
Get the word count for every word and also get the total number of words.

word_counts = tokenizer.word_counts
num_words = len(word_counts)
Convert text to sequence of numbers

sequences = tokenizer.texts_to_sequences(text_data)
Generate Features and Labels
features = []
labels = []
​
training_length = 50
# Iterate through the sequences of tokens
for seq in sequences:
    # Create multiple training examples from each sequence
    for i in range(training_length, training_length+300):
        # Extract the features and label
        extract = seq[i - training_length: i - training_length + 20]
​
        # Set the features and label
        features.append(extract[:-1])
        labels.append(extract[-1])
The prediction task
5.Generate training and testing data
from sklearn.utils import shuffle
import numpy as np
​
features, labels = shuffle(features, labels, random_state=1)
​
# Decide on number of samples for training
train_end = int(0.75 * len(labels))
​
train_features = np.array(features[:train_end])
valid_features = np.array(features[train_end:])
​
train_labels = labels[:train_end]
valid_labels = labels[train_end:]
​
# Convert to arrays
X_train, X_valid = np.array(train_features), np.array(valid_features)
​
# Using int8 for memory savings
y_train = np.zeros((len(train_labels), num_words), dtype=np.int8)
y_valid = np.zeros((len(valid_labels), num_words), dtype=np.int8)
​
# One hot encoding of labels
for example_index, word_index in enumerate(train_labels):
    y_train[example_index, word_index] = 1
​
for example_index, word_index in enumerate(valid_labels):
    y_valid[example_index, word_index] = 1
This is just to check the features and labels

for i, sequence in enumerate(X_train[:1]):
    text = []
    for idx in sequence:
        text.append(idx_word[idx])
        
    print('Features: ' + ' '.join(text)+'\n')
    print('Label: ' + idx_word[np.argmax(y_train[i])] + '\n')
6.Build The Model
Use keras.Sequential to define the model. For this simple example three layers are used to define our model:

keras.layers.Embedding: The input layer. A trainable lookup table that will map the numbers of each character to a vector with embedding_dim dimensions;
keras.layers.LSTM: A type of RNN with size units=rnn_units (You can also use a GRU layer here.)
keras.layers.Dense: The output layer, with num_words outputs.
model = Sequential()
​
# Embedding layer
model.add(
    Embedding(
        input_dim=num_words,
        output_dim=100,
        weights=None,
        trainable=True))
​
# Recurrent layer
model.add(
    LSTM(
        64, return_sequences=False, dropout=0.1,
        recurrent_dropout=0.1))
​
# Fully connected layer
model.add(Dense(64, activation='relu'))
​
# Dropout for regularization
model.add(Dropout(0.5))
​
# Output layer
model.add(Dense(num_words, activation='softmax'))
​
# Compile the model
model.compile(
    optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
​
model.summary()
For each word the model looks up the embedding, runs the LSTM one timestep with the embedding as input, and applies the dense layer to generate logits predicting the log-liklihood of the next word.

7.Train the model
h = model.fit(X_train, y_train, epochs = 1, batch_size = 100, verbose = 1)
8.Save Model
# save the model to file
model.save('./Tagore/data/model_1000epochs.h5')
If you have already trained the model and saved it, you can load a pretrained model
1
# load the model
2
model = load_model('./Tagore/data/model_1000epochs.h5')
Note: After loading the model run model.fit() to continue training form there, if required.
model.fit(X_train, y_train, batch_size=50, epochs=1000)
9.Evaluation
print(model.evaluate(X_train, y_train, batch_size = 20))
print('\nModel Performance: Log Loss and Accuracy on validation data')
print(model.evaluate(X_valid, y_valid, batch_size = 20))
10.Generate text
seed_length=20
new_words=20
diversity=1
n_gen=1
​
import random
​
# Choose a random sequence
seq = random.choice(sequences)
​
# print seq
​
# Choose a random starting point
seed_idx = random.randint(0, len(seq) - seed_length - 10)
# Ending index for seed
end_idx = seed_idx + seed_length
​
gen_list = []
​
for n in range(n_gen):
    # Extract the seed sequence
    seed = seq[seed_idx:end_idx]
    original_sequence = [idx_word[i] for i in seed]
    generated = seed[:] + ['#']
​
    # Find the actual entire sequence
    actual = generated[:] + seq[end_idx:end_idx + new_words]
        
    # Keep adding new words
    for i in range(new_words):
​
        # Make a prediction from the seed
        preds = model.predict(np.array(seed).reshape(1, -1))[0].astype(np.float64)
​
  
        # Softmax
        preds = preds / sum(preds)
​
        # Choose the next word
        probas = np.random.multinomial(1, preds, 1)[0]
​
        next_idx = np.argmax(probas)
​
        # New seed adds on old word
        #             seed = seed[1:] + [next_idx]
        seed += [next_idx]
        generated.append(next_idx)
    # Showing generated and actual abstract
    n = []
​
    for i in generated:
        n.append(idx_word.get(i, '< --- >'))
​
    gen_list.append(n)
​
a = []
​
for i in actual:
    a.append(idx_word.get(i, '< --- >'))
​
a = a[seed_length:]
​
gen_list = [gen[seed_length:seed_length + len(a)] for gen in gen_list]
​
print('Original Sequence: \n'+' '.join(original_sequence))
print("\n")
# print(gen_list)
print('Generated Sequence: \n'+' '.join(gen_list[0][1:]))
# print(a)


########################################################################################################################################################################
#S4_Faculty_Notebook_nlp.ipynb

Text generation using a RNN
1.Goal
Given a word, or a sequence of words, what is the most probable next word? This is the task we're training the model to perform. The input to the model will be a sequence of words, and we train the model to predict the output—the following word at each time step.

Since RNNs maintain an internal state that depends on the previously seen elements, given all the words computed until this moment, what is the next word?

Libraries used in this notebook along with their version:

google 2.0.3

numpy 1.18.3

tensorflow 2.4.1

sklearn 0.0

Given a sequence of words from this data, train a model to predict the next word in the sequence. Longer sequences of text can be generated by calling the model repeatedly.

import tensorflow
tensorflow.__version__
Mount your Google Drive

from google.colab import drive
drive.mount('/content/drive/')
import os
os.chdir('/content/drive/MyDrive/My_NLP/Session 4/FNB/')
2.Import Keras and other libraries
import glob
​
from sklearn.utils import shuffle
import numpy as np
​
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import LSTM, Dense, Dropout, Embedding, Masking, Bidirectional
from tensorflow.keras.optimizers import Adam
from tensorflow.keras import backend
3.Download data
Data is collected from http://www.gutenberg.org

Load the Tagore dataset
Store all the ".txt" file names in a list

import zipfile
zip_ref = zipfile.ZipFile("/content/drive/MyDrive/My_NLP/Session 4/FNB/Tagore.zip", 'r')
zip_ref.extractall("/content/drive/MyDrive/My_NLP/Session 4/FNB/Tagore")
zip_ref.close()
filelist = glob.glob("/content/drive/MyDrive/My_NLP/Session 4/FNB/Tagore/data/*.txt")
Read the data
Read contents of every file from the list and append the text in a new list

text_data = []
for file in filelist:
    with open(file, "r") as file:
      text_data.append(file.read())
4.Process the text
Initialize and fit the tokenizer

tokenizer = Tokenizer()
tokenizer.fit_on_texts(text_data)
Vectorize the text
Before training, we need to map strings to a numerical representation. Create two lookup tables: one mapping words to numbers, and another for numbers to words.

word_idx = tokenizer.word_index #Last is the key
idx_word = tokenizer.index_word
Get the word count for every word and also get the total number of words.

word_counts = tokenizer.word_counts
num_words = len(word_counts)
Convert text to sequence of numbers

sequences = tokenizer.texts_to_sequences(text_data)
Generate Features and Labels
features = []
labels = []
​
training_length = 50
# Iterate through the sequences of tokens
for seq in sequences:
    # Create multiple training examples from each sequence
    for i in range(training_length, training_length+300):
        # Extract the features and label
        extract = seq[i - training_length: i - training_length + 20]
​
        # Set the features and label
        features.append(extract[:-1])
        labels.append(extract[-1])
The prediction task
5.Generate training and testing data
from sklearn.utils import shuffle
import numpy as np
​
features, labels = shuffle(features, labels, random_state=1)
​
# Decide on number of samples for training
train_end = int(0.75 * len(labels))
​
train_features = np.array(features[:train_end])
valid_features = np.array(features[train_end:])
​
train_labels = labels[:train_end]
valid_labels = labels[train_end:]
​
# Convert to arrays
X_train, X_valid = np.array(train_features), np.array(valid_features)
​
# Using int8 for memory savings
y_train = np.zeros((len(train_labels), num_words), dtype=np.int8)
y_valid = np.zeros((len(valid_labels), num_words), dtype=np.int8)
​
# One hot encoding of labels
for example_index, word_index in enumerate(train_labels):
    y_train[example_index, word_index] = 1
​
for example_index, word_index in enumerate(valid_labels):
    y_valid[example_index, word_index] = 1
This is just to check the features and labels

for i, sequence in enumerate(X_train[:1]):
    text = []
    for idx in sequence:
        text.append(idx_word[idx])
        
    print('Features: ' + ' '.join(text)+'\n')
    print('Label: ' + idx_word[np.argmax(y_train[i])] + '\n')
6.Build The Model
Use keras.Sequential to define the model. For this simple example three layers are used to define our model:

keras.layers.Embedding: The input layer. A trainable lookup table that will map the numbers of each character to a vector with embedding_dim dimensions;
keras.layers.LSTM: A type of RNN with size units=rnn_units (You can also use a GRU layer here.)
keras.layers.Dense: The output layer, with num_words outputs.
model = Sequential()
​
# Embedding layer
model.add(
    Embedding(
        input_dim=num_words,
        output_dim=100,
        weights=None,
        trainable=True))
​
# Recurrent layer
model.add(
    LSTM(
        64, return_sequences=False, dropout=0.1,
        recurrent_dropout=0.1))
​
# Fully connected layer
model.add(Dense(64, activation='relu'))
​
# Dropout for regularization
model.add(Dropout(0.5))
​
# Output layer
model.add(Dense(num_words, activation='softmax'))
​
# Compile the model
model.compile(
    optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
​
model.summary()
For each word the model looks up the embedding, runs the LSTM one timestep with the embedding as input, and applies the dense layer to generate logits predicting the log-liklihood of the next word.

7.Train the model
h = model.fit(X_train, y_train, epochs = 1, batch_size = 100, verbose = 1)
8.Save Model
# save the model to file
model.save('./Tagore/data/model_1000epochs.h5')
If you have already trained the model and saved it, you can load a pretrained model
1
# load the model
2
model = load_model('./Tagore/data/model_1000epochs.h5')
Note: After loading the model run model.fit() to continue training form there, if required.
model.fit(X_train, y_train, batch_size=50, epochs=1000)
9.Evaluation
print(model.evaluate(X_train, y_train, batch_size = 20))
print('\nModel Performance: Log Loss and Accuracy on validation data')
print(model.evaluate(X_valid, y_valid, batch_size = 20))
10.Generate text
seed_length=20
new_words=20
diversity=1
n_gen=1
​
import random
​
# Choose a random sequence
seq = random.choice(sequences)
​
# print seq
​
# Choose a random starting point
seed_idx = random.randint(0, len(seq) - seed_length - 10)
# Ending index for seed
end_idx = seed_idx + seed_length
​
gen_list = []
​
for n in range(n_gen):
    # Extract the seed sequence
    seed = seq[seed_idx:end_idx]
    original_sequence = [idx_word[i] for i in seed]
    generated = seed[:] + ['#']
​
    # Find the actual entire sequence
    actual = generated[:] + seq[end_idx:end_idx + new_words]
        
    # Keep adding new words
    for i in range(new_words):
​
        # Make a prediction from the seed
        preds = model.predict(np.array(seed).reshape(1, -1))[0].astype(np.float64)
​
  
        # Softmax
        preds = preds / sum(preds)
​
        # Choose the next word
        probas = np.random.multinomial(1, preds, 1)[0]
​
        next_idx = np.argmax(probas)
​
        # New seed adds on old word
        #             seed = seed[1:] + [next_idx]
        seed += [next_idx]
        generated.append(next_idx)
    # Showing generated and actual abstract
    n = []
​
    for i in generated:
        n.append(idx_word.get(i, '< --- >'))
​
    gen_list.append(n)
​
a = []
​
for i in actual:
    a.append(idx_word.get(i, '< --- >'))
​
a = a[seed_length:]
​
gen_list = [gen[seed_length:seed_length + len(a)] for gen in gen_list]
​
print('Original Sequence: \n'+' '.join(original_sequence))
print("\n")
# print(gen_list)
print('Generated Sequence: \n'+' '.join(gen_list[0][1:]))
# print(a)

########################################################################################################################################################################
#S4_Inclass_Practice_Exercise_2.ipynb

Text generation using a RNN
Given a sequence of words from this data, train a model to predict the next word in the sequence. Longer sequences of text can be generated by calling the model repeatedly.

Mount your Google Drive

import tensorflow
from google.colab import drive
drive.mount('/content/drive')
import os
os.chdir('/content/drive/MyDrive/Colab Notebooks/NLP/')
Import Keras and other libraries
import glob
​
from sklearn.utils import shuffle
import numpy as np
​
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import LSTM, Dense, Dropout, Embedding, Masking, Bidirectional
from tensorflow.keras.optimizers import Adam
from tensorflow.keras import backend
Download data
Reference: Data is collected from http://www.gutenberg.org

For the lab purpose, you can load the dataset provided by Great Learning

Load the William Shakespeare dataset
Store all the ".txt" file names in a list

import zipfile
zip_ref = zipfile.ZipFile("/content/drive/MyDrive/Colab Notebooks/NLP/data-3.zip", 'r')
zip_ref.extractall("/content/drive/MyDrive/Colab Notebooks/NLP/")
zip_ref.close()
Read the data
Read contents of every file from the list and append the text in a new list

files = glob.glob("/content/drive/MyDrive/Colab Notebooks/NLP/dat/*.txt")
data = []
for file in files:
    with open(file, "r") as file:
      data.append(file.read())
len(data)
Process the text
Initialize and fit the tokenizer

new_tokenizer = Tokenizer()
new_tokenizer.fit_on_texts(data)
Vectorize the text
Before training, we need to map strings to a numerical representation. Create two lookup tables: one mapping words to numbers, and another for numbers to words.

word_index = new_tokenizer.word_index
index_word = new_tokenizer.index_word
Get the word count for every word and also get the total number of words.

word_count = new_tokenizer.word_counts
len_word = len(word_count)
len_word
Convert text to sequence of numbers

sequences = new_tokenizer.texts_to_sequences(data)
Generate Features and Labels
feature_list = []
label_list = []
​
train_length = 50
for seq in sequences:
    for i in range(train_length, train_length+300):
        extract = seq[i - train_length: i - train_length + 20]
        feature_list.append(extract[:-1])
        label_list.append(extract[-1])
The prediction task
Given a word, or a sequence of words, what is the most probable next word? This is the task we're training the model to perform. The input to the model will be a sequence of words, and we train the model to predict the output—the following word at each time step.

Since RNNs maintain an internal state that depends on the previously seen elements, given all the words computed until this moment, what is the next word?

Generate training and testing data
from sklearn.utils import shuffle
import numpy as np
​
features, labels = shuffle(feature_list, label_list, random_state=1)
​
# Decide on number of samples for training
train_end = int(0.75 * len(labels))
​
train_features = np.array(features[:train_end])
valid_features = np.array(features[train_end:])
​
train_labels = labels[:train_end]
valid_labels = labels[train_end:]
​
# Convert to arrays
X_train, X_valid = np.array(train_features), np.array(valid_features)
​
# Using int8 for memory savings
y_train = np.zeros((len(train_labels), len_word), dtype=np.int8)
y_valid = np.zeros((len(valid_labels), len_word), dtype=np.int8)
​
# One hot encoding of labels
for example_index, word_index in enumerate(train_labels):
    y_train[example_index, word_index] = 1
​
for example_index, word_index in enumerate(valid_labels):
    y_valid[example_index, word_index] = 1
This is just to check the features and labels

for i, sequence in enumerate(X_train[:1]):
    text = []
    for idx in sequence:
        text.append(index_word[idx])
        
    print('Features: ' + ' '.join(text)+'\n')
    print('Label: ' + index_word[np.argmax(y_train[i])] + '\n')
Build The Model
Use keras.Sequential to define the model. For this simple example three layers are used to define our model:

keras.layers.Embedding: The input layer. A trainable lookup table that will map the numbers of each character to a vector with embedding_dim dimensions;
keras.layers.LSTM: A type of RNN with size units=rnn_units (You can also use a GRU layer here.)
keras.layers.Dense: The output layer, with num_words outputs.
new_model = Sequential()
​
# Embedding layer
new_model.add(
    Embedding(
        input_dim=len_word,
        output_dim=100,
        weights=None,
        trainable=True))
​
# Recurrent layer
new_model.add(
    LSTM(
        64, return_sequences=False, dropout=0.1,
        recurrent_dropout=0.1))
​
# Fully connected layer
new_model.add(Dense(64, activation='relu'))
​
# Dropout for regularization
new_model.add(Dropout(0.5))
​
# Output layer
new_model.add(Dense(len_word, activation='softmax'))
​
# Compile the model
new_model.compile(
    optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
​
new_model.summary()
For each word the model looks up the embedding, runs the LSTM one timestep with the embedding as input, and applies the dense layer to generate logits predicting the log-liklihood of the next word.

Train the model
h = new_model.fit(X_train, y_train, epochs = 1, batch_size = 100, verbose = 1)
Save Model
new_model.save('./dat/model_new_1.h5')
If you have already trained the model and saved it, you can load a pretrained model
saved_model = load_model('./dat/model_new_1.h5')
Note: After loading the model run model.fit() to continue training form there, if required.
saved_model.fit(X_train, y_train, batch_size=50, epochs=500)
Evaluation
print(saved_model.evaluate(X_train, y_train, batch_size = 20))
print('\nModel Performance: Log Loss and Accuracy on validation data')
print(saved_model.evaluate(X_valid, y_valid, batch_size = 20))
Generate text
seed_length=50
new_words=50
diversity=1
n_gen=1
​
import random
​
# Choose a random sequence
seq = random.choice(sequences)
​
# print seq
​
# Choose a random starting point
seed_idx = random.randint(0, len(seq) - seed_length - 10)
# Ending index for seed
end_idx = seed_idx + seed_length
​
gen_list = []
​
for n in range(n_gen):
    # Extract the seed sequence
    seed = seq[seed_idx:end_idx]
    original_sequence = [index_word[i] for i in seed]
    generated = seed[:] + ['#']
​
    # Find the actual entire sequence
    actual = generated[:] + seq[end_idx:end_idx + new_words]
        
    # Keep adding new words
    for i in range(new_words):
​
        # Make a prediction from the seed
        preds = saved_model.predict(np.array(seed).reshape(1, -1))[0].astype(np.float64)
​
  
        # Softmax
        preds = preds / sum(preds)
​
        # Choose the next word
        probas = np.random.multinomial(1, preds, 1)[0]
​
        next_idx = np.argmax(probas)
​
        # New seed adds on old word
        #             seed = seed[1:] + [next_idx]
        seed += [next_idx]
        generated.append(next_idx)
    # Showing generated and actual abstract
    n = []
​
    for i in generated:
        n.append(index_word.get(i, '< --- >'))
​
    gen_list.append(n)
​
a = []
​
for i in actual:
    a.append(index_word.get(i, '< --- >'))
​
a = a[seed_length:]
​
gen_list = [gen[seed_length:seed_length + len(a)] for gen in gen_list]
​
print('Original Sequence: \n'+' '.join(original_sequence))
print("\n")
# print(gen_list)
print('Generated Sequence: \n'+' '.join(gen_list[0][1:]))
# print(a)


########################################################################################################################################################################
#S5_Inclass_question_1.ipynb

Proprietary content. ©Great Learning. All Rights Reserved. Unauthorized use or distribution prohibited

Source: https://www.tensorflow.org/tutorials/text/nmt_with_attention<br>
 license: Apache License 2.0
Libraries along with their versions used at the time of making notebook-
google 2.0.3

matplotlib 3.1.3

numpy 1.18.1

tensorflow 2.1.0

Neural machine translation with attention
Install the packages
Firstly, let's select TensorFlow version 2.x in colab

import tensorflow as tf
1.Load the dataset
As we are using google colab, we need to mount the google drive to load the data file

import random
random.seed(23)
​
# Ignore the warnings
import warnings
warnings.filterwarnings("ignore")
Add path to the file

from google.colab import drive
drive.mount('/content/drive/')
Let's convert unicode file to ascii

path_to_file = '/content/drive/MyDrive/Colab Notebooks/mar.txt'
import unicodedata
def unicode_to_ascii(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn')
2.Preprocessing the sentence
import re
​
def preprocess_sentence(w):
    w = unicode_to_ascii(w.lower().strip())
    w = re.sub(r"([?.!,¿])", r" \1 ", w)
    w = re.sub(r'[" "]+', " ", w)
    w = w.rstrip().strip()
    w = '<start> ' + w + ' <end>'
    return w
Now let's define a function to create the dataset

def create_dataset(path, num_examples):
    lines = open(path, encoding='UTF-8').read().strip().split('\n')
    
    word_pairs = [[preprocess_sentence(w) for w in l.split('\t')]  for l in lines[:num_examples]]
    
    return word_pairs
Let's create data for 10 examples to visualize

create_dataset(path_to_file, num_examples=10)
Define a class to create a word -> index mapping

class LanguageIndex():
  def __init__(self, lang):
    self.lang = lang
    self.word2idx = {}
    self.idx2word = {}
    self.vocab = set()
    
    self.create_index()
    
  def create_index(self):
    for phrase in self.lang:
      self.vocab.update(phrase.split(' '))
    
    self.vocab = sorted(self.vocab)
    
    self.word2idx['<pad>'] = 0
    for index, word in enumerate(self.vocab):
      self.word2idx[word] = index + 1
    
    for word, index in self.word2idx.items():
      self.idx2word[index] = word
Define a function load_dataset to read and process the data

def max_length(tensor):
    return max(len(t) for t in tensor)
​
​
def load_dataset(path, num_examples):
    pairs = create_dataset(path, num_examples)
    inp_lang = LanguageIndex(mr for en, mr in pairs)
    targ_lang = LanguageIndex(en for en, mr in pairs)
    input_tensor = [[inp_lang.word2idx[s] for s in mr.split(' ')] for en, mr in pairs]
    
    target_tensor = [[targ_lang.word2idx[s] for s in en.split(' ')] for en, mr in pairs]
    
    max_length_inp, max_length_tar = max_length(input_tensor), max_length(target_tensor)
    
    input_tensor = tf.keras.preprocessing.sequence.pad_sequences(input_tensor, 
                                                                 maxlen=max_length_inp,
                                                                 padding='post')
    
    target_tensor = tf.keras.preprocessing.sequence.pad_sequences(target_tensor, 
                                                                  maxlen=max_length_tar, 
                                                                  padding='post')
    
    return input_tensor, target_tensor, inp_lang, targ_lang, max_length_inp, max_length_tar
Load the data

num_examples = 30000
input_tensor, target_tensor, inp_lang, targ_lang, max_length_inp, max_length_targ = load_dataset(path_to_file, num_examples)
Split the data into train and test

from sklearn.model_selection import train_test_split
​
​
input_tensor_train, input_tensor_val, target_tensor_train, target_tensor_val = train_test_split(input_tensor, target_tensor, test_size=0.1)
​
​
len(input_tensor_train), len(target_tensor_train), len(input_tensor_val), len(target_tensor_val)
Consider the dataset into different batches

BUFFER_SIZE = len(input_tensor_train)
BATCH_SIZE = 64
N_BATCH = BUFFER_SIZE//BATCH_SIZE
embedding_dim = 256
units = 1024
vocab_inp_size = len(inp_lang.word2idx)
vocab_tar_size = len(targ_lang.word2idx)
​
dataset = tf.data.Dataset.from_tensor_slices((input_tensor_train, target_tensor_train)).shuffle(BUFFER_SIZE)
dataset = dataset.batch(BATCH_SIZE, drop_remainder=True)
3.Define an Encoder function
class Encoder(tf.keras.Model):
    def __init__(self, vocab_size, embedding_dim, enc_units, batch_sz):
        super(Encoder, self).__init__()
        self.batch_sz = batch_sz
        self.enc_units = enc_units
        self.embedding = tf.keras.layers.Embedding(vocab_size, embedding_dim)
        self.gru = tf.keras.layers.GRU(self.enc_units, 
                                    return_sequences=True, 
                                    return_state=True, 
                                    recurrent_initializer='glorot_uniform')
        
    def call(self, x, hidden):
        x = self.embedding(x)
        output, state = self.gru(x, initial_state = hidden)        
        return output, state
    
    def initialize_hidden_state(self):
        return tf.zeros((self.batch_sz, self.enc_units))
4.Define a Decoder function
class Decoder(tf.keras.Model):
    def __init__(self, vocab_size, embedding_dim, dec_units, batch_sz):
        super(Decoder, self).__init__()
        self.batch_sz = batch_sz
        self.dec_units = dec_units
        self.embedding = tf.keras.layers.Embedding(vocab_size, embedding_dim)
        self.gru = tf.keras.layers.GRU(self.dec_units, 
                                    return_sequences=True, 
                                    return_state=True, 
                                    recurrent_initializer='glorot_uniform')
        
        self.fc = tf.keras.layers.Dense(vocab_size)
        
        
        self.W1 = tf.keras.layers.Dense(self.dec_units)
        self.W2 = tf.keras.layers.Dense(self.dec_units)
        self.W3 = tf.keras.layers.Dense(self.dec_units)
        self.W4 = tf.keras.layers.Dense(self.dec_units)
​
        self.V = tf.keras.layers.Dense(1)
        
    def call(self, x, hidden, enc_output):
​
        hidden_with_time_axis = tf.expand_dims(hidden, 1)
        
        score = self.V(tf.nn.tanh(self.W1(enc_output) + self.W2(hidden_with_time_axis)))
        
        attention_weights = tf.nn.softmax(score, axis=1)
        
        context_vector = attention_weights * enc_output
        context_vector = tf.reduce_sum(context_vector, axis=1)
        
        x = self.embedding(x)
        
        x = tf.concat([tf.expand_dims(context_vector, 1), x], axis=-1)
        
        output, state = self.gru(x)
        
        output = tf.reshape(output, (-1, output.shape[2]))
        
        x = self.fc(output)
        
        return x, state, attention_weights
        
    def initialize_hidden_state(self):
        return tf.zeros((self.batch_sz, self.dec_units))
encoder = Encoder(vocab_inp_size, embedding_dim, units, BATCH_SIZE)
decoder = Decoder(vocab_tar_size, embedding_dim, units, BATCH_SIZE)
5.Define the loss function
import numpy as np
​
def loss_function(real, pred):
  mask = 1 - np.equal(real, 0)
  loss_ = tf.nn.sparse_softmax_cross_entropy_with_logits(labels=real, logits=pred) * mask
  return tf.reduce_mean(loss_)
6.Compile encoder-decoder-loss function
Show the loss for different epochs and different batches

import os
optimizer = tf.optimizers.Adam()
​
checkpoint_dir = './training_checkpoints'
checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt")
checkpoint = tf.train.Checkpoint(optimizer=optimizer,
                                 encoder=encoder,
                                 decoder=decoder)
import time
​
EPOCHS = 50
​
for epoch in range(EPOCHS):
    start = time.time()
    
    hidden = encoder.initialize_hidden_state()
    total_loss = 0
    
    for (batch, (inp, targ)) in enumerate(dataset):
        loss = 0
        
        with tf.GradientTape() as tape:
            enc_output, enc_hidden = encoder(inp, hidden)
            
            dec_hidden = enc_hidden
            
            dec_input = tf.expand_dims([targ_lang.word2idx['<start>']] * BATCH_SIZE, 1)       
            
​
            for t in range(1, targ.shape[1]):
​
                predictions, dec_hidden, _ = decoder(dec_input, dec_hidden, enc_output)
                
                loss += loss_function(targ[:, t], predictions)
                
​
                dec_input = tf.expand_dims(targ[:, t], 1)
        
        batch_loss = (loss / int(targ.shape[1]))
        
        total_loss += batch_loss
        
        variables = encoder.variables + decoder.variables
        
        gradients = tape.gradient(loss, variables)
        
        optimizer.apply_gradients(zip(gradients, variables))
        
        if batch % 100 == 0:
            print('Epoch {} Batch {} Loss {:.4f}'.format(epoch + 1,
                                                         batch,
                                                         batch_loss.numpy()))
​
    if (epoch + 1) % 2 == 0:
      checkpoint.save(file_prefix = checkpoint_prefix)
    
    print('Epoch {} Loss {:.4f}'.format(epoch + 1,
                                        total_loss / N_BATCH))
    print('Time taken for 1 epoch {} sec\n'.format(time.time() - start))
checkpoint.save(file_prefix = checkpoint_prefix)
7.Defie an evaluation function
Using the sentence, encoder, decoder define an evaluate function

def evaluate(sentence, encoder, decoder, inp_lang, targ_lang, max_length_inp, max_length_targ):
    attention_plot = np.zeros((max_length_targ, max_length_inp))
    
    sentence = preprocess_sentence(sentence)
​
    inputs = [inp_lang.word2idx[i] for i in sentence.split(' ')]
    inputs = tf.keras.preprocessing.sequence.pad_sequences([inputs], maxlen=max_length_inp, padding='post')
    inputs = tf.convert_to_tensor(inputs)
    
    result = ''
​
    hidden = [tf.zeros((1, units))]
    enc_out, enc_hidden = encoder(inputs, hidden)
​
    dec_hidden = enc_hidden
    dec_input = tf.expand_dims([targ_lang.word2idx['<start>']], 0)
​
    for t in range(max_length_targ):
        predictions, dec_hidden, attention_weights = decoder(dec_input, dec_hidden, enc_out)
        
​
        attention_weights = tf.reshape(attention_weights, (-1, ))
        attention_plot[t] = attention_weights.numpy()
​
        predicted_id = tf.argmax(predictions[0]).numpy()
​
        result += targ_lang.idx2word[predicted_id] + ' '
​
        if targ_lang.idx2word[predicted_id] == '<end>':
            return result, sentence, attention_plot
        
​
        dec_input = tf.expand_dims([predicted_id], 0)
​
    return result, sentence, attention_plot
8.Define a function for plotting the weights
import matplotlib.pyplot as plt
​
def plot_attention(attention, sentence, predicted_sentence):
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(1, 1, 1)
    ax.matshow(attention, cmap='viridis')
    
    fontdict = {'fontsize': 14}
    
    ax.set_xticklabels([''] + sentence, fontdict=fontdict, rotation=90)
    ax.set_yticklabels([''] + predicted_sentence, fontdict=fontdict)
​
    plt.show()
9.Define a translate function
Using evaluate function define a function translate which will translate a Marathi sentence into English.

def translate(sentence, encoder, decoder, inp_lang, targ_lang, max_length_inp, max_length_targ):
    print('Input: {}'.format(sentence))
    result, sentence, attention_plot = evaluate(sentence, encoder, decoder, inp_lang, targ_lang, max_length_inp, max_length_targ)
        
    print('Input: {}'.format(sentence))
    print('Predicted translation: {}'.format(result))
    
    attention_plot = attention_plot[:len(result.split(' '))-1, :len(sentence.split(' '))-1]
    plot_attention(attention_plot, sentence.split(' '), result.split(' '))
checkpoint.restore(tf.train.latest_checkpoint(checkpoint_dir))
translate('এটি একটি খুব গুরুত্বপূর্ণ শিক্ষা', encoder, decoder, inp_lang, targ_lang, max_length_inp, max_length_targ)

########################################################################################################################################################################
#S5_TakeHome--v1.ipynb

Proprietary content. ©Great Learning. All Rights Reserved. Unauthorized use or distribution prohibited

Source: https://www.tensorflow.org/tutorials/text/nmt_with_attention<br>
 license: Apache License 2.0
Libraries along with their versions used at the time of making notebook-
google 2.0.3

matplotlib 3.1.3

numpy 1.18.1

tensorflow 2.1.0

Neural machine translation with attention
Install the packages
Firstly, let's select TensorFlow version 2.x in colab

%tensorflow_version 2.x
import tensorflow as tf
tf.__version__
# Initialize the random number generator
import random
random.seed(0)
​
# Ignore the warnings
import warnings
warnings.filterwarnings("ignore")
1.Load the dataset
As we are using google colab, we need to mount the google drive to load the data file

from google.colab import drive
drive.mount('/content/drive/')
Add path to the file

path_to_file = '/content/drive/MyDrive/My_NLP/Session 3/Takehome/ben.txt'
Let's convert unicode file to ascii

import unicodedata
​
# Converts the unicode file to ascii
def unicode_to_ascii(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
        if unicodedata.category(c) != 'Mn')
2.Preprocessing the sentence
import re
​
def preprocess_sentence(w):
    w = unicode_to_ascii(w.lower().strip())
    
    # creating a space between a word and the punctuation following it
    # eg: "he is a boy." => "he is a boy ." 
    # Reference:- https://stackoverflow.com/questions/3645931/python-padding-punctuation-with-white-spaces-keeping-punctuation
    w = re.sub(r"([?.!,¿])", r" \1 ", w)
    w = re.sub(r'[" "]+', " ", w)
    
    # replacing everything with space except (a-z, A-Z, ".", "?", "!", ",")
    #w = re.sub(r"[^a-zA-Z?.!,¿]+", " ", w) # COMMENT THIS LINE FOR NON-LATIN SCRIPTS SUCH AS MARATHI, HINDI ETC.
    
    w = w.rstrip().strip()
    
    # adding a start and an end token to the sentence
    # so that the model know when to start and stop predicting.
    w = '<start> ' + w + ' <end>'
    return w
Now let's define a function to create the dataset

# 1. Remove the accents
# 2. Clean the sentences
# 3. Return word pairs in the format: [ENGLISH, MARATHI]
def create_dataset(path, num_examples):
    lines = open(path, encoding='UTF-8').read().strip().split('\n')
    
    word_pairs = [[preprocess_sentence(w) for w in l.split('\t')]  for l in lines[:num_examples]]
    
    return word_pairs
Let's create data for 10 examples to visualize

create_dataset(path_to_file, num_examples=10)
Define a class to create a word -> index mapping

# This class creates a word -> index mapping (e.g,. "dad" -> 5) and vice-versa 
# (e.g., 5 -> "dad") for each language,
class LanguageIndex():
  def __init__(self, lang):
    self.lang = lang
    self.word2idx = {}
    self.idx2word = {}
    self.vocab = set()
    
    self.create_index()
    
  def create_index(self):
    for phrase in self.lang:
      self.vocab.update(phrase.split(' '))
    
    self.vocab = sorted(self.vocab)
    
    self.word2idx['<pad>'] = 0
    for index, word in enumerate(self.vocab):
      self.word2idx[word] = index + 1
    
    for word, index in self.word2idx.items():
      self.idx2word[index] = word
Define a function load_dataset to read and process the data

def max_length(tensor):
    return max(len(t) for t in tensor)
​
​
def load_dataset(path, num_examples):
    # creating cleaned input, output pairs
    pairs = create_dataset(path, num_examples)
​
    # index language using the class defined above    
    inp_lang = LanguageIndex(mr for en, mr in pairs)
    targ_lang = LanguageIndex(en for en, mr in pairs)
    
    # Vectorize the input and target languages
    
    # Other language sentences
    input_tensor = [[inp_lang.word2idx[s] for s in mr.split(' ')] for en, mr in pairs]
    
    # English sentences
    target_tensor = [[targ_lang.word2idx[s] for s in en.split(' ')] for en, mr in pairs]
    
    # Calculate max_length of input and output tensor
    # Here, we'll set those to the longest sentence in the dataset
    max_length_inp, max_length_tar = max_length(input_tensor), max_length(target_tensor)
    
    # Padding the input and output tensor to the maximum length
    input_tensor = tf.keras.preprocessing.sequence.pad_sequences(input_tensor, 
                                                                 maxlen=max_length_inp,
                                                                 padding='post')
    
    target_tensor = tf.keras.preprocessing.sequence.pad_sequences(target_tensor, 
                                                                  maxlen=max_length_tar, 
                                                                  padding='post')
    
    return input_tensor, target_tensor, inp_lang, targ_lang, max_length_inp, max_length_tar
Load the data

# Try experimenting with the size of that dataset
num_examples = 30000
input_tensor, target_tensor, inp_lang, targ_lang, max_length_inp, max_length_targ = load_dataset(path_to_file, num_examples)
Split the data into train and test

from sklearn.model_selection import train_test_split
​
# Creating training and validation sets using an 90-10 split
input_tensor_train, input_tensor_val, target_tensor_train, target_tensor_val = train_test_split(input_tensor, target_tensor, test_size=0.1)
​
# Show length
len(input_tensor_train), len(target_tensor_train), len(input_tensor_val), len(target_tensor_val)
Consider the dataset into different batches

BUFFER_SIZE = len(input_tensor_train)
BATCH_SIZE = 64
N_BATCH = BUFFER_SIZE//BATCH_SIZE
embedding_dim = 256
units = 1024
vocab_inp_size = len(inp_lang.word2idx)
vocab_tar_size = len(targ_lang.word2idx)
​
dataset = tf.data.Dataset.from_tensor_slices((input_tensor_train, target_tensor_train)).shuffle(BUFFER_SIZE)
dataset = dataset.batch(BATCH_SIZE, drop_remainder=True)
3.Define an Encoder function
class Encoder(tf.keras.Model):
    def __init__(self, vocab_size, embedding_dim, enc_units, batch_sz):
        super(Encoder, self).__init__()
        self.batch_sz = batch_sz
        self.enc_units = enc_units
        self.embedding = tf.keras.layers.Embedding(vocab_size, embedding_dim)
        self.gru = tf.keras.layers.GRU(self.enc_units, 
                                    return_sequences=True, 
                                    return_state=True, 
                                    recurrent_initializer='glorot_uniform')
        
    def call(self, x, hidden):
        x = self.embedding(x)
        output, state = self.gru(x, initial_state = hidden)        
        return output, state
    
    def initialize_hidden_state(self):
        return tf.zeros((self.batch_sz, self.enc_units))
4.Define a Decoder function
class Decoder(tf.keras.Model):
    def __init__(self, vocab_size, embedding_dim, dec_units, batch_sz):
        super(Decoder, self).__init__()
        self.batch_sz = batch_sz
        self.dec_units = dec_units
        self.embedding = tf.keras.layers.Embedding(vocab_size, embedding_dim)
        self.gru = tf.keras.layers.GRU(self.dec_units, 
                                    return_sequences=True, 
                                    return_state=True, 
                                    recurrent_initializer='glorot_uniform')
        
        self.fc = tf.keras.layers.Dense(vocab_size)
        
        # used for attention
        self.W1 = tf.keras.layers.Dense(self.dec_units)
        self.W2 = tf.keras.layers.Dense(self.dec_units)
        self.W3 = tf.keras.layers.Dense(self.dec_units)
        self.W4 = tf.keras.layers.Dense(self.dec_units)
​
        self.V = tf.keras.layers.Dense(1)
        
    def call(self, x, hidden, enc_output):
        # enc_output shape == (batch_size, max_length, hidden_size)
        
        # hidden shape == (batch_size, hidden size)
        # hidden_with_time_axis shape == (batch_size, 1, hidden size)
        # we are doing this to perform addition to calculate the score
        hidden_with_time_axis = tf.expand_dims(hidden, 1)
        
        # score shape == (batch_size, max_length, 1)
        # we get 1 at the last axis because we are applying tanh(FC(EO) + FC(H)) to self.V
        score = self.V(tf.nn.tanh(self.W1(enc_output) + self.W2(hidden_with_time_axis)))
        
        # attention_weights shape == (batch_size, max_length, 1)
        attention_weights = tf.nn.softmax(score, axis=1)
        
        # context_vector shape after sum == (batch_size, hidden_size)
        context_vector = attention_weights * enc_output
        context_vector = tf.reduce_sum(context_vector, axis=1)
        
        # x shape after passing through embedding == (batch_size, 1, embedding_dim)
        x = self.embedding(x)
        
        # x shape after concatenation == (batch_size, 1, embedding_dim + hidden_size)
        x = tf.concat([tf.expand_dims(context_vector, 1), x], axis=-1)
        
        # passing the concatenated vector to the GRU
        output, state = self.gru(x)
        
        # output shape == (batch_size * 1, hidden_size)
        output = tf.reshape(output, (-1, output.shape[2]))
        
        # output shape == (batch_size * 1, vocab)
        x = self.fc(output)
        
        return x, state, attention_weights
        
    def initialize_hidden_state(self):
        return tf.zeros((self.batch_sz, self.dec_units))
encoder = Encoder(vocab_inp_size, embedding_dim, units, BATCH_SIZE)
decoder = Decoder(vocab_tar_size, embedding_dim, units, BATCH_SIZE)
5.Define the loss function
import numpy as np
​
def loss_function(real, pred):
  mask = 1 - np.equal(real, 0)
  loss_ = tf.nn.sparse_softmax_cross_entropy_with_logits(labels=real, logits=pred) * mask
  return tf.reduce_mean(loss_)
import os
optimizer = tf.optimizers.Adam()
​
checkpoint_dir = './training_checkpoints'
checkpoint_prefix = os.path.join(checkpoint_dir, "ckpt")
checkpoint = tf.train.Checkpoint(optimizer=optimizer,
                                 encoder=encoder,
                                 decoder=decoder)
6.Compile encoder-decoder-loss function
Show the loss for different epochs and different batches

import time
​
EPOCHS = 50
​
for epoch in range(EPOCHS):
    start = time.time()
    
    hidden = encoder.initialize_hidden_state()
    total_loss = 0
    
    for (batch, (inp, targ)) in enumerate(dataset):
        loss = 0
        
        with tf.GradientTape() as tape:
            enc_output, enc_hidden = encoder(inp, hidden)
            
            dec_hidden = enc_hidden
            
            dec_input = tf.expand_dims([targ_lang.word2idx['<start>']] * BATCH_SIZE, 1)       
            
            # Teacher forcing - feeding the target as the next input
            for t in range(1, targ.shape[1]):
                # passing enc_output to the decoder
                predictions, dec_hidden, _ = decoder(dec_input, dec_hidden, enc_output)
                
                loss += loss_function(targ[:, t], predictions)
                
                # using teacher forcing
                dec_input = tf.expand_dims(targ[:, t], 1)
        
        batch_loss = (loss / int(targ.shape[1]))
        
        total_loss += batch_loss
        
        variables = encoder.variables + decoder.variables
        
        gradients = tape.gradient(loss, variables)
        
        optimizer.apply_gradients(zip(gradients, variables))
        
        if batch % 100 == 0:
            print('Epoch {} Batch {} Loss {:.4f}'.format(epoch + 1,
                                                         batch,
                                                         batch_loss.numpy()))
    # saving (checkpoint) the model every 2 epochs
    if (epoch + 1) % 2 == 0:
      checkpoint.save(file_prefix = checkpoint_prefix)
    
    print('Epoch {} Loss {:.4f}'.format(epoch + 1,
                                        total_loss / N_BATCH))
    print('Time taken for 1 epoch {} sec\n'.format(time.time() - start))
checkpoint.save(file_prefix = checkpoint_prefix)
7.Defie an evaluation function
Using the sentence, encoder, decoder define an evaluate function

def evaluate(sentence, encoder, decoder, inp_lang, targ_lang, max_length_inp, max_length_targ):
    attention_plot = np.zeros((max_length_targ, max_length_inp))
    
    sentence = preprocess_sentence(sentence)
​
    inputs = [inp_lang.word2idx[i] for i in sentence.split(' ')]
    inputs = tf.keras.preprocessing.sequence.pad_sequences([inputs], maxlen=max_length_inp, padding='post')
    inputs = tf.convert_to_tensor(inputs)
    
    result = ''
​
    hidden = [tf.zeros((1, units))]
    enc_out, enc_hidden = encoder(inputs, hidden)
​
    dec_hidden = enc_hidden
    dec_input = tf.expand_dims([targ_lang.word2idx['<start>']], 0)
​
    for t in range(max_length_targ):
        predictions, dec_hidden, attention_weights = decoder(dec_input, dec_hidden, enc_out)
        
        # storing the attention weigths to plot later on
        attention_weights = tf.reshape(attention_weights, (-1, ))
        attention_plot[t] = attention_weights.numpy()
​
        predicted_id = tf.argmax(predictions[0]).numpy()
​
        result += targ_lang.idx2word[predicted_id] + ' '
​
        if targ_lang.idx2word[predicted_id] == '<end>':
            return result, sentence, attention_plot
        
        # the predicted ID is fed back into the model
        dec_input = tf.expand_dims([predicted_id], 0)
​
    return result, sentence, attention_plot
8.Define a function for plotting the weights
import matplotlib.pyplot as plt
​
# function for plotting the attention weights
def plot_attention(attention, sentence, predicted_sentence):
    fig = plt.figure(figsize=(10,10))
    ax = fig.add_subplot(1, 1, 1)
    ax.matshow(attention, cmap='viridis')
    
    fontdict = {'fontsize': 14}
    
    ax.set_xticklabels([''] + sentence, fontdict=fontdict, rotation=90)
    ax.set_yticklabels([''] + predicted_sentence, fontdict=fontdict)
​
    plt.show()
9.Define a translate function
Using evaluate function define a function translate which will translate a Bengali sentence into English.

def translate(sentence, encoder, decoder, inp_lang, targ_lang, max_length_inp, max_length_targ):
    print('Input: {}'.format(sentence))
    result, sentence, attention_plot = evaluate(sentence, encoder, decoder, inp_lang, targ_lang, max_length_inp, max_length_targ)
        
    print('Input: {}'.format(sentence))
    print('Predicted translation: {}'.format(result))
    
    attention_plot = attention_plot[:len(result.split(' '))-1, :len(sentence.split(' '))-1]
    plot_attention(attention_plot, sentence.split(' '), result.split(' '))
# restoring the latest checkpoint in checkpoint_dir
checkpoint.restore(tf.train.latest_checkpoint(checkpoint_dir))
translate('এটি একটি খুব গুরুত্বপূর্ণ শিক্ষা', encoder, decoder, inp_lang, targ_lang, max_length_inp, max_length_targ)
########################################################################################################################################################################
#Scrapping_BeautifulSoup.ipynb
s
import os
os.chdir('/home/sunil/Desktop/GL/NLP/Session3')
import requests
from bs4 import BeautifulSoup
  
URL = "http://www.values.com/inspirational-quotes"
r = requests.get(URL)
  
soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
print(soup)
print(soup.prettify())
quotes=[]  # a list to store quotes
   
table = soup.find('div', attrs = {'id':'all_quotes'})
table.prettify()
count=0
for row in table.find_all_next('div', attrs = {'class': 'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
    print(row)
    print(count)
    count=count+1
    if(count>2):
        break
    #quote = {}
    #quote['theme'] = row.h5.text
    #quote['url'] = row.a['href']
    #quote['img'] = row.img['src']
    #quote['lines'] = row.img['alt'].split(" #")[0]
    #quote['author'] = row.img['alt'].split(" #")[1]
    #quotes.append(quote)
row.h5
row.h5.text
row.a
row.a['href']
row.img
row.img['src']
row.img['alt'].split(" #")[0]
for row in table.find_all_next('div', attrs = {'class': 'col-6 col-lg-3 text-center margin-30px-bottom sm-margin-30px-top'}):
    quote = {}
    quote['theme'] = row.h5.text
    quote['lines'] = row.img['alt'].split(" #")[0]
    quotes.append(quote)
import csv
filename = 'inspirational_quotes.csv'
with open(filename, 'w', newline='') as f:
    w = csv.DictWriter(f,['theme','lines'])
    w.writeheader()
    for quote in quotes:
        w.writerow(quote)

########################################################################################################################################################################
#Sentiment Analysis using LSTM.ipynb

Libraries along with their versions used at the time of making notebook-
google 2.0.3

numpy 1.18.1

pandas 0.25.3

tensorflow 2.1.0

Firstly, let's select TensorFlow version 2.x in colab

%tensorflow_version 2.x
import tensorflow
tensorflow.__version__
# Initialize the random number generator
import random
random.seed(0)
​
# Ignore the warnings
import warnings
warnings.filterwarnings("ignore")
Load the dataset
As we are using google colab, we need to mount the google drive to load the data file

from google.colab import drive
drive.mount('/content/drive/')
set project path

project_path = '/content/drive/My Drive/NLP/'
import pandas as pd
​
data = pd.read_csv( project_path + 'Sentiment.csv')
# Keeping only the neccessary columns
data = data[['text','sentiment']]
import re
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
​
data = data[data.sentiment != "Neutral"]
data['text'] = data['text'].apply(lambda x: x.lower())
data['text'] = data['text'].apply((lambda x: re.sub('[^a-zA-z0-9\s]','',x)))
​
print(data[ data['sentiment'] == 'Positive'].size)
print(data[ data['sentiment'] == 'Negative'].size)
​
for idx,row in data.iterrows():
    row[0] = row[0].replace('rt',' ')
    
vocabSize = 2000
tokenizer = Tokenizer(num_words=vocabSize, split=' ')
tokenizer.fit_on_texts(data['text'].values)
X = tokenizer.texts_to_sequences(data['text'].values)
X = pad_sequences(X)
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Embedding, LSTM, SpatialDropout1D
​
embed_dim = 128
lstm_out = 196
​
model = Sequential()
model.add(Embedding(vocabSize, embed_dim,input_length = X.shape[1]))
model.add(SpatialDropout1D(0.4))
model.add(LSTM(lstm_out, dropout=0.2, recurrent_dropout=0.2))
model.add(Dense(2,activation='softmax'))
model.compile(loss = 'categorical_crossentropy', optimizer='adam',metrics = ['accuracy'])
print(model.summary())
from sklearn.model_selection import train_test_split
​
Y = pd.get_dummies(data['sentiment']).values
X_train, X_test, Y_train, Y_test = train_test_split(X,Y, test_size = 0.15, random_state = 42)
print(X_train.shape,Y_train.shape)
print(X_test.shape,Y_test.shape)
batch_size = 32
model.fit(X_train, Y_train, epochs = 10, batch_size=batch_size, verbose = 2)
score,acc = model.evaluate(X_test, Y_test, verbose = 2, batch_size = batch_size)
print("score: %.2f" % (score))
print("acc: %.2f" % (acc))
import numpy as np
​
pos_cnt, neg_cnt, pos_correct, neg_correct = 0, 0, 0, 0
​
for x in range(len(X_test)):
    
    result = model.predict(X_test[x].reshape(1,X_test.shape[1]),batch_size=1,verbose = 2)[0]
   
    if np.argmax(result) == np.argmax(Y_test[x]):
        if np.argmax(Y_test[x]) == 0:
            neg_correct += 1
        else:
            pos_correct += 1
       
    if np.argmax(Y_test[x]) == 0:
        neg_cnt += 1
    else:
        pos_cnt += 1
​
print("pos_acc", pos_correct/pos_cnt*100, "%")
print("neg_acc", neg_correct/neg_cnt*100, "%")
twt = ['He is a lazy person.']
#vectorizing the tweet by the pre-fitted tokenizer instance
twt = tokenizer.texts_to_sequences(twt)
#padding the tweet to have exactly the same shape as `embedding_2` input
twt = pad_sequences(twt, maxlen=28, dtype='int32', value=0)
print(twt)
sentiment = model.predict(twt,batch_size=1,verbose = 2)[0]
if(np.argmax(sentiment) == 0):
    print("negative")
elif (np.argmax(sentiment) == 1):
    print("positive")
########################################################################################################################################################################
#Session2_TakeHome_sol_v1.ipynb

We cannot work with the text data in machine learning so we need to convert them into numerical vectors, As a part of this practice exercise you will implement different techniques to do the same.

In this notebook we are going to understand some basic text cleaning steps and techniques for encoding text data. We are going to learn about

Understanding the data - See what's data is all about. what should be considered for cleaning for data (Punctuations , stopwords etc..).
Basic Cleaning -We will see what parameters need to be considered for cleaning of data (like Punctuations , stopwords etc..) and its code.
Techniques for Encoding - All the popular techniques that are used for encoding that I personally came across.
Bag of Words
Binary Bag of Words
Bigram, Ngram
TF-IDF( Term Frequency - Inverse Document Frequency)
Word2Vec
Emotion and Sentiment analysis
Import Libraries
Libraries used in this notebook along with their version:

google 2.0.3

nltk 3.2.5

numpy 1.18.3

pandas 1.0.3

from google.colab import drive
drive.mount('/content/drive')
import numpy as np                                  #for large and multi-dimensional arrays
import pandas as pd                                 #for data manipulation and analysis
import nltk                                         #Natural language processing tool-kit
import re
from sklearn.decomposition import PCA
from matplotlib import pyplot
%matplotlib inline
from six import string_types
from string import punctuation
​
from nltk.corpus import stopwords                   #Stopwords corpus
from nltk.stem import PorterStemmer                 # Stemmer
from nltk import word_tokenize
from nltk.tokenize import RegexpTokenizer
​
from sklearn.feature_extraction.text import CountVectorizer          #For Bag of words
from sklearn.feature_extraction.text import TfidfVectorizer          #For TF-IDF
1.Understanding the data
We will employ a text categorization dataset based on Reviews. Each article is assigned a specific captegory.

Implement the code to load the dataset.(Hint: Use the pandas library to load the csv file.)

# Solution
import pandas as pd
df = pd.read_csv('/content/drive/MyDrive/My_NLP/Session 1/Takehome/bbc-text.csv')
# Sanity check: Your output should look like the below
df.head()
Create a function called "complaint_to_words" to store each consumer complaint narrative .
# Solution
complaint_to_words = df['text']  
2.Basic Cleaning
2.1.Tokenize
We will use the above function here to create a list of list that will store each complaint tokenized into separate words.(Hint: Use regular expression based tokenizer.)

data_list = list()
for comp in complaint_to_words:
    data_list.append(RegexpTokenizer('\w+').tokenize(comp))
print(data_list[:3]) # Example
for file_id in data_list[:3]:
  print(file_id)
2.2.Lower Case
low=[]
for line in data_list:
  lines = list(map(lambda x : x.lower(),line))
  low.append(lines) 
print(low[:3])
2.3.Removing Stopwords
Converting all words to lowercase and removing punctuations and html tags if any

Stemming- Converting the words into their base word or stem word ( Ex - tastefully, tasty, these words are converted to stem word called 'tasti'). This reduces the vector dimension because we dont consider all similar words

Stopwords - Stopwords are the unnecessary words that even if they are removed the sentiment of the sentence dosent change.

Ex - This pasta is so tasty ==> pasta tasty ( This , is, so are stopwords so they are removed)

To see all the stopwords see the below code cell.

2.3.1.Removing Punctuation
nltk.download('punkt')
# Remove Punctuation
  
#stop_words = set(stopwords.words('english')) 
puncList = [";",":","!","?","/","\\",",","#","@","$","&",")","(","\""]
​
#word_tokens = word_tokenize(text_tokens) 
​
Punc_filtered_sentence = [] 
​
for lines in low:
  punc = []
  for w in lines: 
      if w not in puncList: 
          punc.append(w) 
  Punc_filtered_sentence.append(punc)
​
print(len(low[0])) 
print(len(Punc_filtered_sentence[0])) 
print(low[0])
print(Punc_filtered_sentence[0])
2.3.2.Removing the Stop Words
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
print(stopwords.words('english'))
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
    
stop_words = set(stopwords.words('english')) 
    
filtered_sentence = [] 
​
for lines in Punc_filtered_sentence:
  word = []
  for w in lines: 
      if w not in stop_words: 
          word.append(w) 
  filtered_sentence.append(word)
​
print(len(Punc_filtered_sentence[0])) 
print(len(filtered_sentence[0])) 
print(Punc_filtered_sentence[0])
print(filtered_sentence[0])
2.4.Stemming & Lemitization
2.4.1.Stemming
from nltk.stem import PorterStemmer
#create an object of class PorterStemmer
porter = PorterStemmer()
# Stemming
​
stemmed=[]
for line in filtered_sentence:
  lines = list(map(lambda x : porter.stem(x),line))
  stemmed.append(lines) 
print(len(filtered_sentence[0])) 
print(len(stemmed[0])) 
print(filtered_sentence[0]) 
print(stemmed[0])
2.4.2.Lemitization
from nltk.stem import LancasterStemmer
lancaster=LancasterStemmer()
# Lemitization
​
lemmitized=[]
for line in stemmed:
  lines = list(map(lambda x : lancaster.stem(x),line))
  lemmitized.append(lines) 
print(len(stemmed[0])) 
print(len(lemmitized[0])) 
print(stemmed[0]) 
print(lemmitized[0])
2.5.PoS
nltk.download('averaged_perceptron_tagger')
nltk.pos_tag(lemmitized[0])
final_X = stemmed
print(final_X[1])
sent = []
for row in final_X:
    sequ = ''
    for word in row:
        sequ = sequ + ' ' + word
    sent.append(sequ)
​
final_X = sent
print(final_X[1])
Save the data
data = pd.DataFrame()
data['category'] = list(df['category'])
data['Text'] = final_X
print(data)
data.to_csv('S1TakeHome.csv', index=False, encoding='utf-8')
Load the data
data = pd.read_csv('/content/S1TakeHome.csv')
data
We will employ a text categorization dataset based on BBC articles. Each article is assigned a specific captegory.

Implement the code to load the dataset.(Hint: Use the pandas library to load the csv file.)

# Sanity check: Your output should look like the below
data.head()
3.Techniques for Encoding
Techniques for Encoding

BAG OF WORDS

In BoW we construct a dictionary that contains set of all unique words from our text review dataset.The frequency of the word is counted here. if there are d unique words in our dictionary then for every sentence or review the vector will be of length d and count of word from review is stored at its particular location in vector. The vector will be highly sparse in such case.

Ex. pasta is tasty and pasta is good

[0]....[1]............[1]...........[2]..........[2]............[1].......... <== Its vector representation ( remaining all dots will be represented as zeroes)

[a]..[and].....[good].......[is].......[pasta]....[tasty]....... <==This is dictionary .

Using scikit-learn's CountVectorizer we can get the BoW and check out all the parameters it consists of, one of them is max_features =5000 it tells about to consider only top 5000 most frequently repeated words to place in a dictionary. so our dictionary length or vector length will be only 5000

BINARY BAG OF WORDS

In binary BoW, we dont count the frequency of word, we just place 1 if the word appears in the review or else 0. In CountVectorizer there is a parameter binary = true this makes our BoW to binary BoW.

final_X = data['Text']
###Create a function called "count_vect" to convert each review text to individual tokens.

# Here we use the CountVectorizer from sklearn to create bag of words
count_vect = CountVectorizer(max_features=5000)
bow_data = count_vect.fit_transform(final_X)
print(bow_data[1])
Drawbacks of BoW/ Binary BoW

Our main objective in doing these text to vector encodings is that similar meaning text vectors should be close to each other, but in some cases this may not possible for Bow

For example, if we consider two reviews This pasta is very tasty and This pasta is not tasty after stopwords removal both sentences will be converted to pasta tasty so both giving exact same meaning.

The main problem is here we are not considering the front and back words related to every word, here comes Bigram and Ngram techniques.

3.1.N-gram
3.1.1.BI-GRAM BOW
Considering pair of words for creating dictionary is Bi-Gram , Tri-Gram means three consecutive words so as NGram.

CountVectorizer has a parameter ngram_range if assigned to (1,2) it considers Bi-Gram BoW

But this massively increases our dictionary size

final_B_X = final_X
count_vect = CountVectorizer(ngram_range=(1,2))
Bigram_data = count_vect.fit_transform(final_B_X)
print(Bigram_data[1])
3.2.TF-IDF
Term Frequency - Inverse Document Frequency it makes sure that less importance is given to most frequent words and also considers less frequent words.

Term Frequency is number of times a particular word(W) occurs in a review divided by totall number of words (Wr) in review. The term frequency value ranges from 0 to 1.

Inverse Document Frequency is calculated as log(Total Number of Docs(N) / Number of Docs which contains particular word(n)). Here Docs referred as Reviews.

TF-IDF is TF * IDF that is (W/Wr)*LOG(N/n)

Using scikit-learn's tfidfVectorizer we can get the TF-IDF.

So even here we get a TF-IDF value for every word and in some cases it may consider different meaning reviews as similar after stopwords removal. so to over come we can use BI-Gram or NGram.

final_tf = final_X
tf_idf = TfidfVectorizer(max_features=5000)
tf_data = tf_idf.fit_transform(final_tf)
print(tf_data[1])
We will use the above function here to create a list of list that will store each complaint tokenized into separate words.

data_list = list()
for comp in data['Text']:
    data_list.append(RegexpTokenizer('\w+').tokenize(comp))
3.3.Word2Vec
Next step is to import the Word2Vec model from gensim.

Gensim is a free to use python library. It provides APIs to solve various problems relating to natural language processing. It is fast, scalable and robust.

In this practice exercise we will train our own Word2Vec model using gensim Word2Vec API. Objectives of this practice exercise are,

Train your word2vec word embedding model.
Visualize trained word embedding model using principal component analysis.
First step will be to load the corpus, clean it and tokenize it.

Libraries used in this notebook along with their version:

google 2.0.3

matplotlib 3.2.1

numpy 1.18.3

pandas 1.0.3

from gensim.models import Word2Vec
Create your own model using the data_list defined above and gensim Word2Vec API.
(Hint: https://radimrehurek.com/gensim/models/word2vec.html)

# Solution
model = Word2Vec(stemmed, min_count=1, size=100)
# Loading the vectors for each word in varaible "x"
x = model[model.wv.vocab]
Use PCA algorithm from sklearn to convert high dimesnional word embeddings to two diemnsions and save them in the variable "results".
# Solution
pca = PCA(n_components=2)
result = pca.fit_transform(x)
Visualizing the word embeddings.

pyplot.figure(figsize = (20, 10))
pyplot.scatter(result[40:80, 0], result[40:80, 1])
words = list(model.wv.vocab)
for i, word in enumerate(words[40:80]):
    pyplot.annotate(word, xy=(result[40 + i, 0], result[40 + i, 1]))
pyplot.show()
sentence = str(data['Text'][1])
sentence
sentence_nlp = sentence
sentence_nlp
nltk.download('maxent_treebank_pos_tagger')
nltk.download('averaged_perceptron_tagger')
4.Emotion and Sentiment Analysis
pip install afinn
from afinn import Afinn
af = Afinn()
sentiment_scores = [af.score(article) for article in data['Text']]
sentiment_category = ['positive' if score > 3 
                          else 'negative' if score < 3 
                              else 'neutral' 
                                  for score in sentiment_scores]
df = pd.DataFrame([list(data['category']), sentiment_scores, sentiment_category]).T
df.columns = ['category', 'sentiment_score', 'sentiment_category']
df['sentiment_score'] = df.sentiment_score.astype('float')
df.groupby(by=['category']).describe()
import matplotlib.pyplot as plt
import seaborn as sns
f, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 4))
sp = sns.stripplot(x='category', y="sentiment_score",  hue='sentiment_category', data=df, ax=ax1)
bp = sns.boxplot(x='category', y="sentiment_score", hue='sentiment_category', data=df, palette="Set2", ax=ax2)
t = f.suptitle('Visualizing Sentiment', fontsize=14)
fc = sns.factorplot(x="category", hue="sentiment_category", 
                    data=df, kind="count", 
                    palette={"negative": "#FE2020", 
                             "positive": "#BADD07", 
                             "neutral": "#68BFF5"})
pos_idx = df[(df.category=='tech') & (df.sentiment_score == df[(df.category=='tech')].sentiment_score.max())].index[0]
neg_idx = df[(df.category=='tech') & (df.sentiment_score == df[(df.category=='tech')].sentiment_score.min())].index[0]
neg_idx
print('Most Negative Tech Article:', data['Text'][neg_idx])
​
print()
print('Most Positive Tech Article:', data['Text'][pos_idx])
df1 = df[df.category=='politics']
pd.unique(df1.sentiment_score)
pos_idx = df[(df.category=='politics') & (df.sentiment_score == 5)].index[0]
neg_idx = df[(df.category=='politics') & (df.sentiment_score == 30.)].index[0]
​
print('Most Negative political Article:', data.iloc[neg_idx][['Text']][0])
print()
print('Most Positive political Article:', data.iloc[pos_idx][['Text']][0])
from textblob import TextBlob
sentiment_scores_tb = [round(TextBlob(article).sentiment.polarity, 3) for article in data['Text']]
sentiment_category_tb = ['positive' if score > 0 
                             else 'negative' if score < 0 
                                 else 'neutral' 
                                     for score in sentiment_scores_tb]
df = pd.DataFrame([list(data['category']), sentiment_scores_tb, sentiment_category_tb]).T
df.columns = ['category', 'sentiment_score', 'sentiment_category']
df['sentiment_score'] = df.sentiment_score.astype('float')
df.groupby(by=['category']).describe()
df.head()
fc = sns.factorplot(x="category", hue="sentiment_category", 
                    data=df, kind="count", 
                    palette={"negative": "#FE2020", 
                             "positive": "#BADD07", 
                             "neutral": "#68BFF5"})
from sklearn.metrics import confusion_matrix
true_labels=sentiment_category
predicted_labels=sentiment_category_tb
confusion_matrix(true_labels, predicted_labels)
plt.figure(figsize = (5,5))
conf = pd.DataFrame(confusion_matrix(true_labels, predicted_labels),
            index = ['negative', 'neutral', 'positive'],
                  columns = ['negative', 'neutral', 'positive'])
sns.heatmap(conf, annot=True)

########################################################################################################################################################################
#Session_1--solution--TakeHome--v1.ipynb

.Install the required packages
import nltk
from six import string_types
from nltk.corpus import reuters
from string import punctuation
from nltk.corpus import stopwords
from nltk import word_tokenize
import numpy as np
​
nltk.download('reuters') # Downloading corpus
nltk.download('stopwords') # Downloading stopwords
nltk.download('punkt') # Downloading tokenizer
from google.colab import drive
drive.mount('/content/drive')
from google.colab import drive
drive.mount('/content/drive')
from nltk.tokenize import RegexpTokenizer
from sklearn.decomposition import PCA
from matplotlib import pyplot
%matplotlib inline
import numpy as np
import re
2.Reading the data
We will employ a text categorization dataset based on Reviews. Each article is assigned a specific captegory. ###Implement the code to load the dataset.(Hint: Use the pandas library to load the csv file.)

# Solution
import pandas as pd
df = pd.read_csv('/content/drive/MyDrive/My_NLP/Session 0/TakeHome/Reviews.csv')
# Sanity check: Your output should look like the below
df.head()
Create a function called "complaint_to_words" to store each consumer complaint narrative.
# Solution
complaint_to_words = df['Text']  
3.Proccessing the Data
We will use the above function here to create a list of list that will store each complaint tokenized into separate words.(Hint: Use regular expression based tokenizer.)

3.1.Tokenize
data_list = list()
for comp in complaint_to_words:
    data_list.append(RegexpTokenizer('\w+').tokenize(comp))
print(data_list[:3]) # Example
for file_id in data_list[:3]:
  print(file_id)
#word = []
#for file_id in df['Text']:
#    words = word_tokenize(file_id)
#    word.extend(words)
#print(word)
3.2.Lower Case
low=[]
for line in data_list:
  lines = list(map(lambda x : x.lower(),line))
  low.append(lines) 
print(low[:3])
3.3.Removing Stopwords
3.3.1.Removing Punctuation
nltk.download('punkt')
# Remove Punctuation
  
#stop_words = set(stopwords.words('english')) 
puncList = [";",":","!","?","/","\\",",","#","@","$","&",")","(","\""]
​
#word_tokens = word_tokenize(text_tokens) 
​
Punc_filtered_sentence = [] 
​
for lines in low:
  punc = []
  for w in lines: 
      if w not in puncList: 
          punc.append(w) 
  Punc_filtered_sentence.append(punc)
​
print(len(low[0])) 
print(len(Punc_filtered_sentence[0])) 
print(low[0])
print(Punc_filtered_sentence[0])
3.3.2.Removing the Stop Words
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
print(stopwords.words('english'))
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize 
    
stop_words = set(stopwords.words('english')) 
    
filtered_sentence = [] 
​
for lines in Punc_filtered_sentence:
  word = []
  for w in lines: 
      if w not in stop_words: 
          word.append(w) 
  filtered_sentence.append(word)
​
print(len(Punc_filtered_sentence[0])) 
print(len(filtered_sentence[0])) 
print(Punc_filtered_sentence[0])
print(filtered_sentence[0])
3.4.Stemming & Lemitization
3.4.1.Stemming
from nltk.stem import PorterStemmer
#create an object of class PorterStemmer
porter = PorterStemmer()
# Stemming
​
stemmed=[]
for line in filtered_sentence:
  lines = list(map(lambda x : porter.stem(x),line))
  stemmed.append(lines) 
print(len(filtered_sentence[0])) 
print(len(stemmed[0])) 
print(filtered_sentence[0]) 
print(stemmed[0])
3.4.2.Lemitization
from nltk.stem import LancasterStemmer
lancaster=LancasterStemmer()
# Lemitization
​
lemmitized=[]
for line in stemmed:
  lines = list(map(lambda x : lancaster.stem(x),line))
  lemmitized.append(lines) 
print(len(stemmed[0])) 
print(len(lemmitized[0])) 
print(stemmed[0]) 
​
print(lemmitized[0])
3.5.PoS
nltk.download('averaged_perceptron_tagger')
nltk.pos_tag(lemmitized[0])
3.6.Create a word vocabulary
Voc = []
for line in lemmitized:
  Voc.extend(line)
print(Voc[:20])
4.TF & IDF
4.1.TF
from six import string_types
 
def word_tf(word, token): 
    return float(token.count(word)) / len(token)
 
def tf_idf(word, token): 
    if word not in word_index:
        return .0
    return word_tf(word, token) * word_idf[word_index[word]]
word_tf('town',Voc)
4.2.IDF
# build the vocabulary in one pass
vocabulary = set(Voc)
word_index = {w: index for index, w in enumerate(vocabulary)}
​
VOCABULARY_SIZE = len(vocabulary)
DOCUMENTS_COUNT = len(complaint_to_words)
 
print(VOCABULARY_SIZE, DOCUMENTS_COUNT)
import numpy as np
word_doc_count = np.zeros(VOCABULARY_SIZE)
​
for word in Voc : 
  indexes = [word_index[word]] 
  word_doc_count[indexes] += 1.0
​
print(word_doc_count) 
​
word_idf = np.log(DOCUMENTS_COUNT / (1 + word_doc_count).astype(float))
​
print(word_idf[word_index['town']])
print(word_idf[word_index['dog']])
4.3.TF & IDF¶
def tf_idf(word, token): 
    if word not in word_index:
        return .0
    return word_tf(word, token) * word_idf[word_index[word]]
tf_idf('town',Voc)


########################################################################################################################################################################
#Session_1-v2.ipynb

Reading the data
from nltk.corpus import reuters
print(reuters.raw('test/15000')) # Example
import zipfile
with zipfile.ZipFile('/root/nltk_data/corpora/reuters.zip', 'r') as zip_ref:
    zip_ref.extractall('/root/nltk_data/corpora/')
print(reuters.raw('test/15000')) # Example
reuters.fileids()
Collecting document
document = []
for file_id in reuters.fileids():
    document.append(reuters.raw(file_id))
document[:3]
import pandas as pd
document = pd.Series(document)
Proccessing the Data
Lower Case
document = document.str.lower()
Removing Punctuation
document = document.str.replace('[^a-z\s#@]', '')
document[2]
## Remove '\n'
document = document.str.replace('\n', '')
document[2]
Tokenize
document_tokens = document.str.split(' ')
tokens_all = []
for tokens in document_tokens:
    tokens_all.extend(tokens)
print('No. of tokens in entire corpus:', len(tokens_all))
Bag of words analysis
tokens_freq = pd.Series(tokens_all).value_counts()
tokens_freq
## Remove ''
tokens_freq = pd.Series(tokens_all).value_counts().drop([''])
tokens_freq
Remove Stpoword
Collect Common Stopwords
import nltk # natural language tool kit
nltk.download('stopwords')
print(stopwords)
common_stopwords = nltk.corpus.stopwords.words('english')
len(common_stopwords)
Collect Customized Stopwords
custom_stopwords = ['amp', 'rt']
Combine all stopwords
all_stopwords = np.hstack([common_stopwords, custom_stopwords])
len(all_stopwords)
Remove
## Convert all toens into DataFrame
df_tokens = pd.DataFrame(tokens_freq).reset_index().rename(columns={'index': 'token', 0: 'frequency'})
df_tokens
​
## Remove all stopwords
df_tokens = df_tokens[~df_tokens['token'].isin(all_stopwords)]
df_tokens
Bar Chart of Bag f Words
import matplotlib.pyplot as plt
plt.figure(figsize=(24,5))
df_tokens.set_index('token')['frequency'].head(25).plot.bar()
plt.xticks(fontsize = 20)
Wordclouds
from wordcloud import WordCloud
​
docs_strings = ' '.join(document)
len(docs_strings)
wc = WordCloud( collocations=False, background_color='white', stopwords=all_stopwords).generate(docs_strings)
plt.figure(figsize=(20,5))
plt.imshow(wc)
plt.axis('off');
​
Vectorization
from nltk.corpus import movie_reviews
nltk.download('movie_reviews')
movie_reviews.fileids()
movie_reviews.categories()
print(movie_reviews.raw('neg/cv001_19502.txt')) # Example
category = []
review = []
for i in movie_reviews.fileids():
  category.append(i.split('/')[0])
  review.append(movie_reviews.raw(i))
data = pd.DataFrame()
data['Review'] = review
data['Category'] = category
data.head(5)
data[data['Category'] == 'pos'].head()
data.shape
docs = data['Review'].str.lower().str.replace('[^a-z\s]', '')
​
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import train_test_split
​
train_docs, test_docs = train_test_split(docs, test_size=0.2, random_state=1)
​
stopwords = nltk.corpus.stopwords.words('english')
stopwords.remove('not')
vectorizer = CountVectorizer(stop_words=stopwords).fit(train_docs)
​
vocab = vectorizer.get_feature_names()
len(vocab)
twig vocabulary size
## min_df --> retain the token which appears atlead 10 times 
​
vectorizer = CountVectorizer(stop_words=stopwords, min_df=10).fit(train_docs)
​
vocab = vectorizer.get_feature_names()
len(vocab)
vocab[:100]
Document Term Matrix
train_dtm = vectorizer.transform(train_docs)
test_dtm = vectorizer.transform(test_docs)
train_dtm
test_dtm
df_train_dtm = pd.DataFrame(train_dtm.toarray(), index=train_docs.index, columns=vocab)
df_test_dtm = pd.DataFrame(test_dtm.toarray(), index=test_docs.index, columns=vocab)
df_train_dtm.head(6)
Stemming
from gensim.parsing.preprocessing import PorterStemmer, remove_stopwords
stemmer = PorterStemmer()
docs = data['Review'].str.lower().str.replace('[^a-z\s]', '')
docs = docs.apply(remove_stopwords)
docs = stemmer.stem_documents(docs)
train_docs, test_docs = train_test_split(pd.Series(docs), test_size=0.2, random_state=1)
​
​
vectorizer = CountVectorizer(min_df=10).fit(train_docs)
vocab = vectorizer.get_feature_names()
​
train_dtm = vectorizer.transform(train_docs)
test_dtm = vectorizer.transform(test_docs)
len(vocab)
df_train_dtm = pd.DataFrame(train_dtm.toarray(), index=train_docs.index, columns=vocab)
df_test_dtm = pd.DataFrame(test_dtm.toarray(), index=test_docs.index, columns=vocab)
df_train_dtm.head()
TF-IDF
vectorizer = TfidfVectorizer(min_df=5).fit(train_docs)
vocab = vectorizer.get_feature_names()
​
train_dtm_tfidf = vectorizer.transform(train_docs)
test_dtm_tfidf = vectorizer.transform(test_docs)
​
df_train_dtm_tfidf = pd.DataFrame(train_dtm_tfidf.toarray(), index=train_docs.index, columns=vocab)
df_train_dtm_tfidf.head()
N-Gram ( Bi-gram , Tri-gram )
Bi-gram
vectorizer = CountVectorizer(min_df=10, ngram_range=(2,2)).fit(train_docs)
vocab = vectorizer.get_feature_names()
vocab[:5]
Tri-gram
vectorizer = CountVectorizer(min_df=10, ngram_range=(3,3)).fit(train_docs)
vocab = vectorizer.get_feature_names()
vocab[:5]
​
vectorizer = CountVectorizer(min_df=5, ngram_range=(1,3)).fit(train_docs)
vocab = vectorizer.get_feature_names()
vocab[:5]
Lemmitization & PoS tagging
import spacy
nlp = spacy.load("en_core_web_sm")
​
doc = data['Review'].iloc[0]
​
proc_doc = nlp(doc)
for token in proc_doc:
    print(token, '|', token.lemma_, '|', token.pos_)
Label tagging
for token in proc_doc.ents:
    print(token, token.label_)


########################################################################################################################################################################
#Session_1_question_Inclass_v2-1.ipynb
Import the packages
import nltk
from six import string_types
from nltk.corpus import reuters
from string import punctuation
from nltk.corpus import stopwords
from nltk import word_tokenize
import numpy as np
​
nltk.download('stopwords') # Downloading stopwords
nltk.download('punkt') # Downloading tokenizer
nltk.download('reuters') # Downloading corpus
nltk.download('stopwords') # Downloading stopwords
nltk.download('punkt') # Downloading tokenizer
from gensim.parsing.preprocessing import PorterStemmer, remove_stopwords
​
# from google.colab import drive
# drive.mount('/content/drive')
from nltk.tokenize import RegexpTokenizer
from sklearn.decomposition import PCA
from matplotlib import pyplot
%matplotlib inline
import numpy as np
import re
Reading the data
We will employ a text categorization dataset based on Reviews. Each article is assigned a specific captegory. ###Implement the code to load the dataset.(Hint: Use the pandas library to load the csv file.)

# Solution
import pandas as pd
df = pd.read_csv('bbc-text.csv')
# Sanity check: Your output should look like the below
df.head()
###Create a variable called "Report" to convert each article report narrative to individual tokens.(Hint: Use regular expression based tokenizer.)

​
Proccessing the Data
# docs = df.copy()
Lower Case
docs = df['text'].str.lower()
Removing Punctuation & Stopwords
Removing Punctuation
df.text = df.text.str.replace('[^a-z\s#@]', '')
​
Removing stopwords
df.text = df.text.apply(remove_stopwords)
Stemming
stemmer = PorterStemmer()
df.text = stemmer.stem_documents(df.text)
Lemmitization
import spacy
nlp = spacy.load("en_core_web_sm")
​
doc = docs[0]
​
proc_doc = nlp(doc)
for token in proc_doc:
    print(token, '|', token.lemma_)
Tokenize
document_tokens = df.text.str.split(' ')
tokens_all = []
for tokens in document_tokens:
    tokens_all.extend(tokens)
print('No. of tokens in entire corpus:', len(tokens_all))
Bag of words analysis
tokens_freq = pd.Series(tokens_all).value_counts()
tokens_freq
tokens_freq = pd.Series(tokens_all).value_counts()
tokens_freq
import nltk 
nltk.download('stopwords')
common_stopwords = nltk.corpus.stopwords.words('english')
custom_stopwords = ['amp', 'rt']
all_stopwords = np.hstack([common_stopwords, custom_stopwords])
df_tokens = pd.DataFrame(tokens_freq).reset_index().rename(columns={'index': 'token', 0: 'frequency'})
df_tokens
# Removal of stop words
df_tokens = df_tokens[~df_tokens['token'].isin(all_stopwords)]
df_tokens
Bar Chart of Bag f Words
import matplotlib.pyplot as plt
plt.figure(figsize=(24,5))
df_tokens.set_index('token')['frequency'].head(25).plot.bar()
plt.xticks(fontsize = 20)
Wordclouds
from wordcloud import WordCloud
​
docs_strings = ' '.join(df.text.str.replace('\n', ''))
len(docs_strings)
wc = WordCloud( collocations=False, background_color='white', stopwords=all_stopwords).generate(docs_strings)
plt.figure(figsize=(20,5))
plt.imshow(wc)
plt.axis('off');
Vectorization
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.model_selection import train_test_split
​
train_docs, test_docs = train_test_split(df.text, test_size=0.2, random_state=1)
​
stopwords = nltk.corpus.stopwords.words('english')
stopwords.remove('not')
vectorizer = CountVectorizer(stop_words=stopwords).fit(train_docs)
​
vocab = vectorizer.get_feature_names()
len(vocab)
twig vocabulary size
​
vectorizer = CountVectorizer(stop_words=stopwords, min_df=10).fit(train_docs)
​
vocab = vectorizer.get_feature_names()
len(vocab)
vocab[:40]
Document Term Matrix
train_dtm = vectorizer.transform(train_docs)
test_dtm = vectorizer.transform(test_docs)
train_dtm
test_dtm
df_train_dtm = pd.DataFrame(train_dtm.toarray(), index=train_docs.index, columns=vocab)
df_test_dtm = pd.DataFrame(test_dtm.toarray(), index=test_docs.index, columns=vocab)
df_train_dtm.head()
TF & IDF
​
TF
import scipy.sparse as sp
import pandas as pd 
​
vectorizer = TfidfVectorizer(norm=None) 
X = vectorizer.fit_transform(train_docs)
features = vectorizer.get_feature_names()
n = len(features)
inverse_idf = sp.diags(1/vectorizer.idf_,
                       offsets=0,
                       shape=(n, n),
                       format='csr',
                       dtype=np.float64).toarray()
​
pd.DataFrame(X*inverse_idf, 
            columns=features)
TF-IDF
vectorizer = TfidfVectorizer(min_df=5).fit(train_docs)
vocab = vectorizer.get_feature_names()
​
train_dtm_tfidf = vectorizer.transform(train_docs)
test_dtm_tfidf = vectorizer.transform(test_docs)
​
df_train_dtm_tfidf = pd.DataFrame(train_dtm_tfidf.toarray(), index=train_docs.index, columns=vocab)
df_train_dtm_tfidf.head()
N-Gram ( Bi-gram , Tri-gram )
Bi-gram
vectorizer = CountVectorizer(min_df=10, ngram_range=(2,2)).fit(train_docs)
vocab = vectorizer.get_feature_names()
vocab[:5]
Tri-gram
vectorizer = CountVectorizer(min_df=10, ngram_range=(3,3)).fit(train_docs)
vocab = vectorizer.get_feature_names()
vocab[:5]
PoS tagging
import spacy
nlp = spacy.load("en_core_web_sm")
​
doc = df['text'].iloc[0]
​
proc_doc = nlp(doc)
for token in proc_doc:
    print(token, '|', token.pos_)
Label tagging
for token in proc_doc.ents:
    print(token, token.label_)
​

########################################################################################################################################################################
#text generation with GPT2.ipynb

from transformers import pipeline, set_seed
generator = pipeline('text-generation', model='gpt2')
set_seed(42)
 generator("Jack and Jill,", max_length=300)
 generator("Jack and Jill", max_length=500, num_return_sequences=5)
 
########################################################################################################################################################################
#TFIDF example.ipynb
Proprietary content. ©Great Learning. All Rights Reserved. Unauthorized use or distribution prohibited

import nltk
nltk.download('reuters') # Downloading corpus
nltk.download('stopwords') # Downloading stopwords
nltk.download('punkt') # Downloading tokenizer
from nltk.corpus import reuters
print(reuters.raw('test/15000')) # Example
from string import punctuation
from nltk.corpus import stopwords
from nltk import word_tokenize
 
stop_words = stopwords.words('english') + list(punctuation)
 
def tokenize(text):
    words = word_tokenize(text)
    words = [w.lower() for w in words]
    return [w for w in words if w not in stop_words and not w.isdigit()]
# build the vocabulary in one pass
vocabulary = set()
for file_id in reuters.fileids():
    words = tokenize(reuters.raw(file_id))
    vocabulary.update(words)
 
vocabulary = list(vocabulary)
word_index = {w: index for index, w in enumerate(vocabulary)}
 
VOCABULARY_SIZE = len(vocabulary)
DOCUMENTS_COUNT = len(reuters.fileids())
 
print(VOCABULARY_SIZE, DOCUMENTS_COUNT)
import numpy as np
​
word_doc_count = np.zeros(VOCABULARY_SIZE)
for file_id in reuters.fileids():
    words = set(tokenize(reuters.raw(file_id)))
    indexes = [word_index[word] for word in words]
    word_doc_count[indexes] += 1.0
 
word_idf = np.log(DOCUMENTS_COUNT / (1 + word_doc_count).astype(float))
​
print(word_idf[word_index['town']])
print(word_idf[word_index['jewelry']])
print(word_idf[word_index['sales']])
from six import string_types
 
def word_tf(word, document): 
    return float(document.count(word)) / len(document)
 
def tf_idf(word, document):
    document = tokenize(document)
 
    if word not in word_index:
        return .0
 
    return word_tf(word, document) * word_idf[word_index[word]]
print(tf_idf('jewelry', reuters.raw('test/15000')))
from sklearn.feature_extraction.text import TfidfVectorizer
 
tfidf = TfidfVectorizer(stop_words=stop_words, tokenizer=tokenize, vocabulary=vocabulary)
 
# Fit the TfIdf model
tfidf.fit([reuters.raw(file_id) for file_id in reuters.fileids()])
 
# Transform a document into TfIdf coordinates
X = tfidf.transform([reuters.raw('test/15000')])
print(tf_idf('jewelry', reuters.raw('test/15000')))

########################################################################################################################################################################
#topic modelling with BERT.ipynb

from bertopic import BERTopic
from sklearn.datasets import fetch_20newsgroups
 
docs = fetch_20newsgroups(subset='all',  remove=('headers', 'footers', 'quotes'))['data']
​
topic_model = BERTopic()
topics, probs = topic_model.fit_transform(docs)
docs
topic_model.get_topic(0)
topic_model.get_topic_info()
topic_model.visualize_topics()

########################################################################################################################################################################
#tweepy code.ipynb

import tweepy
​
# Variables that contains the credentials to access Twitter API
ACCESS_TOKEN = 'your_access_token'
ACCESS_SECRET = 'your_access_secret'
CONSUMER_KEY = 'your_consumer_key'
CONSUMER_SECRET = 'your_consumer_secret'
​
​
# Setup access to API
def connect_to_twitter_OAuth():
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
​
    api = tweepy.API(auth)
    return api
​
​
# Create API object
api = connect_to_twitter_OAuth()
# tweets from my stream
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
# tweets from a specific user
trump_tweets = api.user_timeline('realdonaldtrump')
for tweet in trump_tweets:
    print(tweet.text)
# fuction to extract data from tweet object
def extract_tweet_attributes(tweet_object):
    # create empty list
    tweet_list =[]
    # loop through tweet objects
    for tweet in tweet_object:
        tweet_id = tweet.id # unique integer identifier for tweet
        text = tweet.text # utf-8 text of tweet
        favorite_count = tweet.favorite_count
        retweet_count = tweet.retweet_count
        created_at = tweet.created_at # utc time tweet created
        source = tweet.source # utility used to post tweet
        reply_to_status = tweet.in_reply_to_status_id # if reply int of orginal tweet id
        reply_to_user = tweet.in_reply_to_screen_name # if reply original tweetes screenname
        retweets = tweet.retweet_count # number of times this tweet retweeted
        favorites = tweet.favorite_count # number of time this tweet liked
        # append attributes to list
        tweet_list.append({'tweet_id':tweet_id, 
                          'text':text, 
                          'favorite_count':favorite_count,
                          'retweet_count':retweet_count,
                          'created_at':created_at, 
                          'source':source, 
                          'reply_to_status':reply_to_status, 
                          'reply_to_user':reply_to_user,
                          'retweets':retweets,
                          'favorites':favorites})
    # create dataframe   
    df = pd.DataFrame(tweet_list, columns=['tweet_id',
                                           'text',
                                           'favorite_count',
                                           'retweet_count',
                                           'created_at',
                                           'source',
                                           'reply_to_status',
                                           'reply_to_user',
                                           'retweets',
                                           'favorites'])
    return df
​
​
df = extract_tweet_attributes(trump_tweets)

########################################################################################################################################################################
#Untitled.ipynb
import gensim.downloader as api
wv = api.load('word2vec-google-news-300')
for index, word in enumerate(wv.index_to_key):
    if index == 10:
        break
    print(f"word #{index}/{len(wv.index_to_key)} is {word}")
vec_king = wv['king']
vec_cameroon = wv['cameroon']
pairs = [
    ('car', 'minivan'),   # a minivan is a kind of car
    ('car', 'bicycle'),   # still a wheeled vehicle
    ('car', 'airplane'),  # ok, no wheels, but still a vehicle
    ('car', 'cereal'),    # ... and so on
    ('car', 'communism'),
]
for w1, w2 in pairs:
    print('%r\t%r\t%.2f' % (w1, w2, wv.similarity(w1, w2)))
print(wv.most_similar(positive=['car', 'minivan'], topn=5))
print(wv.doesnt_match(['fire', 'water', 'land', 'sea', 'air', 'car']))


########################################################################################################################################################################
#Webscraping - Autoscraper.ipynb
a
from autoscraper import AutoScraper
url = 'https://inshorts.com/en/read/'
category = ["Britney regains control of her personal life as 13-year conservatorship terminated"]
scrape = AutoScraper()
final = scrape.build(url, category)
print(final)
url1='https://www.reddit.com/r/gameofthrones/'
category1 = ["https://www.reddit.com/r/gameofthrones/comments/p3fec8/spoilers_join_us_on_discord_for_trivia_starting/"]
final1 = scrape.build(url1, category1)
print(final1)

########################################################################################################################################################################
#word2vec pretrained.ipynb

import gensim.downloader as api
wv = api.load('word2vec-google-news-300')
wv.vocab
wv.vectors
vec_king = wv['king']
vec_king
vec_cameroon = wv['cameroon']
pairs = [
    ('car', 'minivan'),   # a minivan is a kind of car
    ('car', 'bicycle'),   # still a wheeled vehicle
    ('car', 'airplane'),  # ok, no wheels, but still a vehicle
    ('car', 'cereal'),    # ... and so on
    ('car', 'communism'),
]
for w1, w2 in pairs:
    print('%r\t%r\t%.2f' % (w1, w2, wv.similarity(w1, w2)))
print(wv.most_similar(positive=['car', 'minivan'], topn=5))
print(wv.doesnt_match(['fire', 'water', 'land', 'sea', 'air', 'car']))


########################################################################################################################################################################
#Word2Vec.ipynb
As we are using google colab, we need to mount the google drive to load the data file

from google.colab import drive
drive.mount('/content/drive/')
from gensim.test.utils import datapath, get_tmpfile
from gensim.models import KeyedVectors # Gensim contains word2vec models and processing tools
​
path = '/content/drive/My Drive/'
​
glove_file = datapath(path + 'glove.6B.50d.txt') # This is a GloVe model
tmp_file = get_tmpfile(path + 'word2vec.glove.6B.50d.txt')
​
from gensim.scripts.glove2word2vec import glove2word2vec
glove2word2vec(glove_file, tmp_file)  # Converting the GloVe file into a Word2Vec file
model = KeyedVectors.load_word2vec_format(tmp_file)
# Check out what the embedding looks like
​
wordEmbed = model['cat']
print(wordEmbed.shape)
print(wordEmbed)
# What happens if a word it out of the dictionary?
​
word = 'Amit'
if word in model:
    print('{0} is in the model'.format(word))
else:
    print('{0} is NOT in the model'.format(word))
# Most like
​
print(model.most_similar(positive=['boy']))
# Most like X but unlike Y
​
print(model.most_similar(positive=['boy', 'girl'], negative=['man']))
print(model.doesnt_match("boy girl car man".split()))
print(model.similarity('shark', 'man'))
model.similar_by_vector(model['king'] - model['queen'] + model['woman'])
print(model.most_similar(positive=['king', 'woman'], negative=['queen']))
print(model.most_similar(positive=['king', 'woman'], negative=['queen']))
print(model.most_similar(positive=['cricket']))
Type Markdown and LaTeX: 𝛼2


########################################################################################################################################################################
#Word2Vec_vs_BERT.ipynb

Glove Embeddings Example
glove_embedding = WordEmbeddings('glove')
Sentence 1
sentence_1 = Sentence('apple released iphone 12 pro max in 2020')
glove_embedding.embed(sentence_1)
for token in sentence_1:
    print(token)
    print(token.embedding)
    print("\n")
sentence_1[0]
sentence_1[0].embedding
sentence_1[0].embedding.shape
Sentence 2
sentence_2 = Sentence('an apple a day keeps the doctor away')
glove_embedding.embed(sentence_2)
for token in sentence_2:
    print(token)
    print(token.embedding)
    print("\n")
sentence_2[1]
sentence_2[1].embedding
sentence_2[1].embedding.shape
Glove Distance between the same word
glove_dst = distance.euclidean(np.array(sentence_1[0].embedding), 
                               np.array(sentence_2[1].embedding))
print("Distance between apple embeddings for Glove = {}".format(glove_dst))
Bert Embeddings
bert_embedding = TransformerWordEmbeddings('bert-base-multilingual-cased')
bert_embedding.embed(sentence_1)
for token in sentence_1:
    print(token)
    print(token.embedding)
sentence_1[0]
sentence_1[0].embedding
sentence_1[0].embedding.shape
bert_embedding.embed(sentence_2)
​
for token in sentence_2:
    print(token)
    print(token.embedding)
sentence_2[1]
sentence_2[1].embedding
sentence_2[1].embedding.shape
bert_dst = distance.euclidean(np.array(sentence_1[0].embedding), 
                               np.array(sentence_2[1].embedding))
print("Distance between apple embeddings for Glove = {}".format(bert_dst))
​
########################################################################################################################################################################
#Word2VecSentiment_Analysis.ipynb


Importing libraries
​
import numpy as np
import pandas as pd
# BeautifulSoup is used to remove html tags from the text
from bs4 import BeautifulSoup 
import re # For regular expressions
​
# Stopwords can be useful to undersand the semantics of the sentence.
# Therefore stopwords are not removed while creating the word2vec model.
# But they will be removed  while averaging feature vectors.
from nltk.corpus import stopwords
# This function converts a text to a sequence of words.
def review_wordlist(review, remove_stopwords=False):
    # 1. Removing html tags
    review_text = BeautifulSoup(review).get_text()
    # 2. Removing non-letter.
    review_text = re.sub("[^a-zA-Z]"," ",review_text)
    # 3. Converting to lower case and splitting
    words = review_text.lower().split()
    # 4. Optionally remove stopwords
    if remove_stopwords:
        stops = set(stopwords.words("english"))     
        words = [w for w in words if not w in stops]
    
    return(words)
# word2vec expects a list of lists.
# Using punkt tokenizer for better splitting of a paragraph into sentences.
​
import nltk.data
#nltk.download('popular')
​
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
# This function splits a review into sentences
def review_sentences(review, tokenizer, remove_stopwords=False):
    # 1. Using nltk tokenizer
    raw_sentences = tokenizer.tokenize(review.strip())
    sentences = []
    # 2. Loop for each sentence
    for raw_sentence in raw_sentences:
        if len(raw_sentence)>0:
            sentences.append(review_wordlist(raw_sentence,\
                                            remove_stopwords))
​
    # This returns the list of lists
    return sentences
import os
os.chdir('/home/sunil/Desktop/GL/NLP/Session1')
import pandas as pd       
train = pd.read_csv("labeledTrainData.tsv", header=0,delimiter="\t", quoting=3)
sentences = []
print("Parsing sentences from training set")
for review in train["review"]:
    sentences += review_sentences(review, tokenizer)
train['review'][0]
sentences
# Importing the built-in logging module
import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
# Creating the model and setting values for the various parameters
num_features = 300  # Word vector dimensionality
min_word_count = 40 # Minimum word count
num_workers = 4     # Number of parallel threads
context = 10        # Context window size
downsampling = 1e-3 # (0.001) Downsample setting for frequent words
​
# Initializing the train model
from gensim.models import word2vec
print("Training model....")
model = word2vec.Word2Vec(sentences,\
                          workers=num_workers,\
                          size=num_features,\
                          min_count=min_word_count,\
                          window=context,
                          sample=downsampling)
​
# To make the model memory efficient
model.init_sims(replace=True)
​
# Saving the model for later use. Can be loaded using Word2Vec.load()
model_name = "300features_40minwords_10context"
model.save(model_name)
# Few tests: This will print the odd word among them 
model.wv.doesnt_match("man woman dog child kitchen".split())
model.wv.doesnt_match("france england germany berlin".split())
# This will print the most similar words present in the model
model.wv.most_similar("man")
model.wv.most_similar("awful")
# This will give the total number of words in the vocabolary created from this dataset
model.wv.syn0.shape
model.wv.vocab
# Function to average all word vectors in a paragraph
def featureVecMethod(words, model, num_features):
    # Pre-initialising empty numpy array for speed
    featureVec = np.zeros(num_features,dtype="float32")
    nwords = 0
    
    #Converting Index2Word which is a list to a set for better speed in the execution.
    index2word_set = set(model.wv.index2word)
    
    for word in  words:
        if word in index2word_set:
            nwords = nwords + 1
            featureVec = np.add(featureVec,model[word])
    
    # Dividing the result by number of words to get average
    featureVec = np.divide(featureVec, nwords)
    return featureVec
# Function for calculating the average feature vector
def getAvgFeatureVecs(reviews, model, num_features):
    counter = 0
    reviewFeatureVecs = np.zeros((len(reviews),num_features),dtype="float32")
    for review in reviews:
        # Printing a status message every 1000th review
        if counter%1000 == 0:
            print("Review %d of %d"%(counter,len(reviews)))
            
        reviewFeatureVecs[counter] = featureVecMethod(review, model, num_features)
        counter = counter+1
        
    return reviewFeatureVecs
# Calculating average feature vector for training set
clean_train_reviews = []
for review in train['review']:
    clean_train_reviews.append(review_wordlist(review, remove_stopwords=True))
    
trainDataVecs = getAvgFeatureVecs(clean_train_reviews, model, num_features)
# Read the test data
test = pd.read_csv("testData.tsv", header=0, delimiter="\t", \
                   quoting=3 )
# Calculating average feature vactors for test set     
clean_test_reviews = []
for review in test["review"]:
    clean_test_reviews.append(review_wordlist(review,remove_stopwords=True))
    
testDataVecs = getAvgFeatureVecs(clean_test_reviews, model, num_features)
# Fitting a random forest classifier to the training data
from sklearn.ensemble import RandomForestClassifier
forest = RandomForestClassifier(n_estimators = 100)
    
print("Fitting random forest to training data....")    
forest = forest.fit(trainDataVecs, train["sentiment"])
print(np.mean(cross_val_score(forest,trainDataVecs,train["sentiment"],cv=10)))
# Predicting the sentiment values for test data and saving the results in a csv file 
result = forest.predict(testDataVecs)
output = pd.DataFrame(data={"id":test["id"], "sentiment":result})
output.to_csv( "output.csv", index=False, quoting=3 )

""")