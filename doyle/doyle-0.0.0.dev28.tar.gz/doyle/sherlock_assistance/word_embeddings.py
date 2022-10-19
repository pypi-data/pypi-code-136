# original is sherlock/features/word_embeddings.py
import sys
from .. import config #
from . import initial_sherlock_necessary
import re
import nltk
import numpy as np
import pandas as pd

import random
import string
import itertools
from tqdm import tqdm
from scipy import stats
from typing import Union
from copy import deepcopy
from nltk.corpus import stopwords
from collections import OrderedDict

from gensim.models.doc2vec import Doc2Vec

try:
    from sherlock.features.helpers import CHARACTERS_TO_CHECK
    from sherlock.features.stats_helper import compute_stats
except ImportError as e:
    print(f'''
to install sherlock you can run: 'pip install -e git+https://github.com/mitmedialab/sherlock-project.git#egg=sherlock'
or 
>> from sherlock_assistance import sherlock_installing
>> sherlock_installing()
**if you run in IPython Notebook restart kernel to re-import after install the package**
''')
    sys.exit(e)

nltk.download("punkt")
nltk.download("stopwords")

initial_sherlock_necessary()

class SherlockWordEmbeddings:

    NUMBER_PATTERN = re.compile(r"[0-9]")
    TEXT_PATTERN = re.compile(r"[a-zA-Z]")
    WORD_PATTERN = re.compile(r"[\w+]")
    STOPWORDS_ENGLISH = stopwords.words("english")
    SPECIAL_CHARACTERS_PATTERN = re.compile(r'[!@#$%^&*(),.?":{}|<>]')
    CHARACTERS_TO_CHECK = ( [c for c in string.printable if c not in ('\n', '\v', '\r', '\t', '\\', '^')] + ['\\', '^'] )

    def __init__(self, 
                num_embeddings = 50, 
                vec_dim = 400, 
                word_vectors_path = f"{config.__statics__}/sherlock_files/glove.6B.50d.txt",
                model_path = None
                ):
        
        self.word_to_embedding = dict()

        word_vectors_file = open(word_vectors_path, "r", encoding="utf-8")
        for word in word_vectors_file:
            term, vector = word.strip().split(" ", 1)
            vector = list(map(float, vector.split(" ")))

            self.word_to_embedding[term] = vector
        
        word_vectors_file.close()

        self.num_embeddings = num_embeddings
        self.vec_dim = vec_dim

        if model_path is None: 
            model_path =  f"{config.__statics__}/sherlock_files/par_vec_trained_{self.vec_dim}.pkl"

        self.model = Doc2Vec.load(model_path)
        self.model.delete_temporary_training_data(keep_doctags_vectors=True, keep_inference=True)

    def tokenise(self, values):
        joined = " ".join(s for s in values if len(s) >= 2)
        filtered = "".join( e for e in joined if e.isalnum() or e.isspace() or e == "'" ).lower()

        return [ word for word in nltk.word_tokenize(filtered) if len(word) >= 2 and word not in self.STOPWORDS_ENGLISH ]

    def extract_word_embeddings_features(self, col_values: list, features: OrderedDict):
        embeddings = list()
        features = deepcopy(features)

        for col_value in map(str.lower, col_values):
            if col_value in self.word_to_embedding:
                embeddings.append(self.word_to_embedding.get(col_value))
            else:
                embeddings_to_all_words = [ self.word_to_embedding.get(w) for w in col_value.split(' ') if w in self.word_to_embedding ]

                n = len(embeddings_to_all_words)

                if n == 1:
                    embeddings.append(embeddings_to_all_words[0])
                elif n > 1:
                    mean_of_word_embeddings = np.mean(embeddings_to_all_words, dtype=float, axis=0)
                    embeddings.append(mean_of_word_embeddings)

        n_rows = len(embeddings)

        if n_rows == 0:
            for i in range(self.num_embeddings):
                features['word_embedding_avg_' + str(i)] = np.nan
                features['word_embedding_std_' + str(i)] = np.nan
                features['word_embedding_med_' + str(i)] = np.nan
                features['word_embedding_mode_' + str(i)] = np.nan

            features['word_embedding_feature'] = 0
        else: 
            if n_rows > 1:
                embeddings_T = np.transpose(embeddings)
                mean_embeddings = np.mean(embeddings_T, axis=1)
                std_embeddings = np.std(embeddings_T, axis=1)
                med_embeddings = np.median(embeddings_T, axis=1)
                mode_embeddings = stats.mode(embeddings_T, axis=1).mode.reshape(-1)
            else:
                mean_embeddings = med_embeddings = mode_embeddings = embeddings[0]
                std_embeddings = np.zeros(self.num_embeddings)

            for i, e in enumerate(mean_embeddings):
                features['word_embedding_avg_' + str(i)] = e
                features['word_embedding_std_' + str(i)] = std_embeddings[i]
                features['word_embedding_med_' + str(i)] = med_embeddings[i]
                features['word_embedding_mode_' + str(i)] = mode_embeddings[i]

            features['word_embedding_feature'] = 1

        return features

    def extract_bag_of_characters_features(self, col_values: list, features: OrderedDict):
        # Create a set of unique chars from the string vectors to quickly test whether to perform expensive
        # processing for any given char
        char_set = set(''.join(col_values))
        features = deepcopy(features)

        for c in CHARACTERS_TO_CHECK:
            value_feature_name = f'n_[{c}]'

            if c in char_set:
                counts = [ s.count(c) for s in col_values]
                has_any = any(counts)
            else:
                has_any = False

            if has_any:
                _any = 1
                _all = 1 if all(counts) else 0
                _mean, _variance, _skew, _kurtosis, _min, _max, _sum = compute_stats(counts)
                _median = np.median(counts)

                features[value_feature_name + '-agg-any'] = _any
                features[value_feature_name + '-agg-all'] = _all
                features[value_feature_name + '-agg-mean'] = _mean
                features[value_feature_name + '-agg-var'] = _variance
                features[value_feature_name + '-agg-min'] = _min
                features[value_feature_name + '-agg-max'] = _max
                features[value_feature_name + '-agg-median'] = _median
                features[value_feature_name + '-agg-sum'] = _sum
                features[value_feature_name + '-agg-kurtosis'] = _kurtosis
                features[value_feature_name + '-agg-skewness'] = _skew
            else:
                features[value_feature_name + '-agg-any'] = 0
                features[value_feature_name + '-agg-all'] = 0
                features[value_feature_name + '-agg-mean'] = 0
                features[value_feature_name + '-agg-var'] = 0
                features[value_feature_name + '-agg-min'] = 0
                features[value_feature_name + '-agg-max'] = 0
                features[value_feature_name + '-agg-median'] = 0
                features[value_feature_name + '-agg-sum'] = 0
                features[value_feature_name + '-agg-kurtosis'] = -3
                features[value_feature_name + '-agg-skewness'] = 0

        return features

    def count_pattern_in_cells(self, values: list, pat):
        return [len(re.findall(pat, s)) for s in values]

    def count_pattern_in_cells_with_non_zero_count(self, values: list, pat):
        cell_counts = [len(re.findall(pat, s)) for s in values]

        return sum(1 for c in cell_counts if c > 0), cell_counts

    def extract_bag_of_words_features(self, col_values: list, features: OrderedDict, n_val):
        if not n_val: return features
        features = deepcopy(features)

        # Entropy of column
        freq_dist = nltk.FreqDist(col_values)
        probs = [freq_dist.freq(l) for l in freq_dist]
        features["col_entropy"] = - sum(p * np.log2(p) for p in probs)

        # Fraction of cells with unique content
        num_unique = len(set(col_values))
        features["frac_unique"] = num_unique / n_val

        # Fraction of cells with numeric content -> frac text cells doesn't add information
        numeric_cell_nz_count, numeric_char_counts = self.count_pattern_in_cells_with_non_zero_count(
            col_values, self.NUMBER_PATTERN
        )
        text_cell_nz_count, text_char_counts = self.count_pattern_in_cells_with_non_zero_count(
            col_values, self.TEXT_PATTERN
        )

        features["frac_numcells"] = numeric_cell_nz_count / n_val
        features["frac_textcells"] = text_cell_nz_count / n_val

        # Average + std number of numeric tokens in cells
        features["avg_num_cells"] = np.mean(numeric_char_counts)
        features["std_num_cells"] = np.std(numeric_char_counts)

        # Average + std number of textual tokens in cells
        features["avg_text_cells"] = np.mean(text_char_counts)
        features["std_text_cells"] = np.std(text_char_counts)

        # Average + std number of special characters in each cell
        spec_char_counts = self.count_pattern_in_cells(col_values, self.SPECIAL_CHARACTERS_PATTERN)

        features["avg_spec_cells"] = np.mean(spec_char_counts)
        features["std_spec_cells"] = np.std(spec_char_counts)

        # Average number of words in each cell
        word_counts = self.count_pattern_in_cells(col_values, self.WORD_PATTERN)

        features["avg_word_cells"] = np.mean(word_counts)
        features["std_word_cells"] = np.std(word_counts)

        features["n_values"] = n_val

        lengths = [len(s) for s in col_values]
        n_none = sum(1 for _l in lengths if _l == 0)

        has_any = any(lengths)

        if has_any:
            _any = 1
            _all = 1 if all(lengths) else 0
            _mean, _variance, _skew, _kurtosis, _min, _max, _sum = compute_stats(lengths)
            _median = np.median(lengths)

            features["length-agg-any"] = _any
            features["length-agg-all"] = _all
            features["length-agg-mean"] = _mean
            features["length-agg-var"] = _variance
            features["length-agg-min"] = _min
            features["length-agg-max"] = _max
            features["length-agg-median"] = _median
            features["length-agg-sum"] = _sum
            features["length-agg-kurtosis"] = _kurtosis
            features["length-agg-skewness"] = _skew
        else:
            features["length-agg-any"] = 0
            features["length-agg-all"] = 0
            features["length-agg-mean"] = 0
            features["length-agg-var"] = 0
            features["length-agg-min"] = 0
            features["length-agg-max"] = 0
            features["length-agg-median"] = 0
            features["length-agg-sum"] = 0
            features["length-agg-kurtosis"] = -3
            features["length-agg-skewness"] = 0

        features["none-agg-has"] = 1 if n_none > 0 else 0
        features["none-agg-percent"] = n_none / n_val
        features["none-agg-num"] = n_none
        features["none-agg-all"] = 1 if n_none == n_val else 0

        return features

    def transform(self, data: Union[pd.DataFrame, pd.Series], n_samples = 1000):
        output = list()

        for raw_sample in data:
            n_values = len(raw_sample)

            if n_samples > n_values:
                n_samples = n_values

            random.seed(13)
            raw_sample = random.sample(raw_sample, k=n_samples)

            features = OrderedDict()
            features = self.extract_bag_of_characters_features(raw_sample, features)
            features = self.extract_word_embeddings_features(raw_sample, features)
            features = self.extract_bag_of_words_features(raw_sample, features, n_samples)

            # TODO use data_no_null version?
            features = self.infer_paragraph_embeddings_features(raw_sample, features)
            
            output.append(dict(features))
        
        return pd.DataFrame(output)

    def infer_paragraph_embeddings_features(self, col_values: list, features: OrderedDict):
        # Resetting the random seed before inference keeps the inference vectors deterministic. Gensim uses random values
        # in the inference process, so setting the seed just beforehand makes the inference repeatable.
        # https://github.com/RaRe-Technologies/gensim/issues/447

        # To make the inference repeatable across runtime launches, we also need to set PYTHONHASHSEED
        # prior to launching the execution environment (i.e. jupyter notebook).  E.g. export PYTHONHASHSEED=13
        # See above Github thread for more information.
        features = deepcopy(features)
        self.model.random.seed(13)

        tokens = self.tokenise(col_values)

        # Infer paragraph vector for data sample.
        inferred = self.model.infer_vector(tokens, steps=20, alpha=0.025)

        for idx, value in enumerate(inferred):
            features["par_vec_" + str(idx)] = value

        return features