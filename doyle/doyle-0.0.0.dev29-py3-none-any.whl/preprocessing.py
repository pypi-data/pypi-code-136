from .config import __statics__
from .utils import LogReporter
from .data_exploration import DataExplorer

import os
import re
import html
import numpy as np
import pandas as pd
import pythainlp
import glob
import gdown

from spellchecker import SpellChecker

from numbers import Number
from typing import (List, Dict, Sequence, Text, Union, Callable)
from .features import (
                        BaseFeature,
                        ImmutableFeature,
                        NumberFeature,
                        TextFeature,
                        ListFeature,
                        DictFeature,
                        CategoricalVariable,
                        ContinuousVariable
                        )

from fairseq.models.transformer import TransformerModel
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor
from sklearn.preprocessing import LabelEncoder, OneHotEncoder, OrdinalEncoder

def is_number(text: str) -> bool:
        try: 
            float(text)
            return True
        except: return False

def initial_th2en():
    if not os.path.exists(f"{__statics__}/SCB_1M+TBASE_th-en_newmm-moses_130000-130000_v1.0"):
        output = f"{__statics__}/SCB_1M+TBASE_th-en_newmm-moses_130000-130000_v1.0.zip"
        tmp_files = glob.glob(f"{output}*tmp")

        gdown.download(
            url="https://drive.google.com/file/d/166qsmRzsr7px39MeBO5xwBAbz3RSl6K4/view?usp=sharing",
            output=output,
            quiet=False, 
            fuzzy=True,
            resume=(len(tmp_files) > 0),
        )

        gdown.extractall(output)
        files = glob.glob(f"{output}*")
        for f in files:
            try: os.remove(f)
            except PermissionError as e:
                print(e)

def return_result(name: str, default_name: str, data: pd.Series, return_pandas: bool, cls: type, **cls_kw):
        if name is None: name = default_name
        data.name = name
        if return_pandas: return data
        return cls(data, name, **cls_kw)

class BasePreprocessor:
    default_return_class = BaseFeature

    @property
    def explorer(self): return self.__explorer

    @explorer.setter
    def explorer(self, new_explorer: DataExplorer): self.__explorer = new_explorer

    @property
    def original_dataframe(self): return self.explorer.original_dataframe

    @property
    def dataframe(self): return self.explorer.df

    @property
    def df(self): return self.dataframe

    @property
    def features(self): return self.explorer.features

    @property
    def features_name(self): return list(self.features.keys())

    def __init__(self, explorer: DataExplorer): 
        self.__explorer = explorer

    def __len__(self): return len(self.df)

    def __repr__(self): return f"{self.__class__.__name__} for " + self.explorer.__repr__()

    def __getitem__(self, item: str): return self.features[item]

    def validate_feature(self, feature_name: str) -> BaseFeature:
        assert self.has_feature(feature_name), f"there is not feature '{feature_name}'"
        if not self.validate_feature_type(feature_name):
            raise TypeError(f"'{feature_name}' must be {self.default_return_class}")

        return self.features[feature_name]

    def validate_feature_type(self, feature_name: str):
        return isinstance(self.features[feature_name], self.default_return_class)

    def has_feature(self, name: str): return self.explorer.has_feature(name)

    def process(
                self, 
                feature_name: str, 
                func: Callable, 
                name: str = None,
                return_pandas: bool = False,
                return_cls: bool = False,
                **func_param,
                ):
        target = self.validate_feature(feature_name)
        output = target.data.apply(lambda x: func(x, **func_param))
        cls_kw = dict()

        if return_cls:
            atypes = output.dropna().apply(lambda x: type(x)).unique()
            if all([ issubclass(atype, List) for atype in atypes ]): return_cls = ListFeature
            elif all([ issubclass(atype, Dict) for atype in atypes ]): return_cls = DictFeature
            elif all([ issubclass(atype, Number) for atype in atypes ]): return_cls = NumberFeature
            elif all([ issubclass(atype, Text) for atype in atypes ]): return_cls = TextFeature
            else: return_cls = self.default_return_class
            
        if hasattr(return_cls, "ctype"): cls_kw["ctype"] = target.ctype
        if hasattr(return_cls, "stype"): cls_kw["stype"] = target.atype
        return return_result(
                                name,
                                f"{target.name}__{func.__name__}",
                                output,
                                return_pandas,
                                return_cls,
                                **cls_kw
                                )

class Preprocessor(BasePreprocessor):
    default_return_class = ImmutableFeature

    def __init__(self, explorer: DataExplorer): 
        super().__init__(explorer)
        self.number = NumberPreprocessor(self.explorer)
        self.text = TextPreprocessor(self.explorer)

    def labels_encoding(self, feature_name: str, categories: Sequence = None, name: str = None, *, return_pandas: bool = False):
        if isinstance(categories, str) or isinstance(categories, Sequence):
            raise TypeError(f"categories must be instance of string or sequence, but got {type(categories)}")

        target = self.validate_feature(feature_name)
        if not issubclass(target.ctype, CategoricalVariable):
            LogReporter.error(f"{target.name}: only support encoding for categorical variable. got '{target.ctype}'")
            return None

        if categories is None and target.order_category is None:
            if name is None: name = f"{target.name}__label_encode"
            encoder = LabelEncoder().fit(target.unique)
            result = encoder.transform(target.notna)
            encoded = target.data.copy(deep=True)
            encoded[target.notna.index] = result
        else:
            if name is None: name = f"{target.name}__ordinal_encode"
            data = target.notna.to_numpy()
            if categories is None: encoder = OrdinalEncoder(categories=target.order_category)
            else: encoder = OrdinalEncoder(categories=categories)
            result = encoder.fit_transform(data.reshape(-1, 1)).ravel()
            encoded = target.data.copy(deep=True)
            encoded[target.notna.index] = result
            
        if return_pandas: return pd.DataFrame({name: encoded})
        return NumberFeature(encoded, name, ctype=CategoricalVariable, stype=target.stype)

    def one_hot_encoding(self, feature_name: str, name: str = None, *, return_pandas: bool = False):
        target = self.validate_feature(feature_name)
        if not issubclass(target.ctype, CategoricalVariable):
            LogReporter.error(f"{target.name}: only support encoding for categorical variable. got '{target.ctype}'")
            return None

        le = LabelEncoder().fit(target.unique)
        result = le.transform(target.notna)
        encoded = pd.DataFrame({ f"{target.name}" : target.data})
        encoded[f"{target.name}"][target.notna.index] = result

        encoder = OneHotEncoder(categories='auto', handle_unknown="ignore", sparse=False)
        result = encoder.fit_transform(encoded)
        result = pd.DataFrame(result, columns=le.classes_)

        if name is None: name = f"{target.name}__onehot"
        result.name = name
        if return_pandas: return result
        return  [ NumberFeature(
                        result[column],
                        f"{name}_{column}",
                        ctype=CategoricalVariable,
                        stype=target.stype
                    ) for column in result.columns ]

    def simple_impute(self, feature_name: str, impute_target: Union[str, Sequence] = "na", *, method: str ="auto", return_pandas: bool = False):
        
        if isinstance(impute_target, str):
            assert impute_target in ["na", "outlier"], \
                f"supported only 'na' or 'outlier' imputation, got {impute_target}"

            if impute_target == "na": 
                return self.na_simple_impute(feature_name, method=method, return_pandas=return_pandas)
            if impute_target == "outlier":
                return self.outlier_simple_impute(feature_name, method=method, return_pandas=return_pandas)
        elif isinstance(impute_target, Sequence):
            return self.index_simple_impute(feature_name, impute_target, method=method, return_pandas=return_pandas)

    def na_simple_impute(self, feature_name: str, *, method="auto", return_pandas: bool = False):
        assert method in ["auto", "mean", "mode"], f"supported method are ['auto', 'mean', 'mode'], but got {method}"

        target = self.validate_feature(feature_name)
        LogReporter.title(f"'{target.name}': NA imputation (method={method})")
        LogReporter.report(f"NA:NOTNA = {target.count_na}:{target.count_notna} ({target.na_percent}%:{target.notna_percent}%)")
        
        if target.count_notna == 0:
            LogReporter.error(f"{target.name}: there is no any NOTNA value")
            return None
        
        if target.na_percent > 0.1:
            LogReporter.warning(f"{target.name}: not recommend to use simple impute for feature which has NA value more than 10%")
        
        if method == "mode": return self.__mode_impute(target, target.na.index, f"{target.name}__na_mode_imputed", return_pandas=return_pandas)
        if method == "mean": return self.__mean_impute(target, target.na.index, f"{target.name}__na_mean_imputed", return_pandas=return_pandas)
        if method == "auto":
            if isinstance(target, NumberFeature) and target.ctype.is_symmetric(target): 
                return self.__mean_impute(target, target.na.index, f"{target.name}__na_mean_imputed", return_pandas=return_pandas)
            return self.__mode_impute(target, target.na.index, f"{target.name}__na_mode_imputed", return_pandas=return_pandas)

    def outlier_simple_impute(self, feature_name: str, *, method="auto", return_pandas: bool = False):
        assert method.lower() in ["auto", "mean", "mode"], f"supported method are ['auto', 'mean', 'mode'], but got {method}"

        target = self.validate_feature(feature_name)
        LogReporter.title(f"'{target.name}': outlier imputation (method={method})")
        LogReporter.report(f"detected outlier = {target.n_outlier} (target.outlier_percent%)")

        if target.n_outlier is None:
            LogReporter.error(f"{target.name}: can not detect outlier")
            return None

        if method == "mode": return self.__mode_impute(target, target.outlier.index, f"{target.name}__outlier_mode_imputed", return_pandas=return_pandas)
        if method == "mean": return self.__mean_impute(target, target.outlier.index, f"{target.name}__outlier_mean_imputed", return_pandas=return_pandas)
        if method == "auto":
            if isinstance(target, NumberFeature) and target.ctype.is_symmetric(target): 
                return self.__mean_impute(target, target.outlier.index, f"{target.name}__outlier_mean_imputed", return_pandas=return_pandas)
            return self.__mode_impute(target, target.outlier.index, f"{target.name}__outlier_mode_imputed", return_pandas=return_pandas)

    def index_simple_impute(self, feature_name: str, index: Sequence, *, method="auto", return_pandas: bool = False):
        assert method.lower() in ["auto", "mean", "mode"], f"supported method are ['auto', 'mean', 'mode'], but got {method}"

        target = self.validate_feature(feature_name)

        if target.count_notna == 0:
            LogReporter.error(f"{target.name}: there is no any NOTNA value")
            return None

        LogReporter.title(f"'{target.name}': imputation (method={method}) at specified index")
        LogReporter.report(f"lenght(index) = {len(index)} ({100*len(index)/len(target)}%)")

        if method == "mode": return self.__mode_impute(target, index, return_pandas=return_pandas)
        if method == "mean": return self.__mean_impute(target, index, return_pandas=return_pandas)
        if method == "auto":
            if isinstance(target, NumberFeature) and target.ctype.is_symmetric(target): 
                return self.__mean_impute(target, index, return_pandas=return_pandas)
            return self.__mode_impute(target, index, return_pandas=return_pandas)
    
    def __mode_impute(self, feature: ImmutableFeature, index: Sequence, name: str = None, *, return_pandas: bool = False):
        mode = feature.notna.mode().to_numpy()
        imputed_values = pd.Series(np.random.choice(mode, size=len(index)))
        imputed = feature.data.copy(deep=True)
        imputed[index] = imputed_values

        return return_result( name, 
                                f"{feature.name}__mode_imputed", 
                                imputed,
                                return_pandas,
                                feature.__class__,
                                ctype=feature.ctype, 
                                stype=feature.stype
                                )

    def __mean_impute(Self, feature: NumberFeature, index: Sequence, name: str = None, *, return_pandas: bool = False):
        if not isinstance(feature, NumberFeature):
            LogReporter.error(f"{feature.name}: not support mean imputation for class '{feature.__class__}'")
            return None

        imputed = feature.data.copy(deep=True)
        imputed[index] = feature.mean

        return return_result( name, 
                                f"{feature.name}__mean_imputed", 
                                imputed,
                                return_pandas,
                                feature.__class__,
                                ctype=feature.ctype, 
                                stype=feature.stype
                                )

    def knn_impute( self, 
                    depend_feature: str,
                    independ_features: Sequence[str],
                    impute_target: Union[str, Sequence] = "na",
                    name: str = None,
                    *,
                    k: int = 5,
                    metric: str = "minkowski",
                    return_pandas: bool = False,
                    na_strictness: bool = True,
                    **metric_params
                    ):
        self.validate_feature(depend_feature)
        for fname in independ_features: self.validate_feature(fname)
        assert isinstance(impute_target, Sequence) or impute_target in ["na", "outlier"], \
            f"impute_target must be 'na' or 'outlier' or sequence of index."

        LogReporter.title(f"'{depend_feature}': {k}-NN imputation for '{ impute_target if isinstance(impute_target, str) else 'specified index'}'")
        LogReporter.report(f"{len(independ_features)} independ features: {independ_features}")

        if impute_target == "na": index = self.features[depend_feature].na.index
        if impute_target == "outlier": index = self.features[depend_feature].outlier.index
        else: index = impute_target
        
        return self.__index_knn_impute(
                                depend_feature,
                                independ_features,
                                index,
                                name,
                                k=k,
                                metric=metric,
                                return_pandas=return_pandas,
                                na_strictness=na_strictness,
                                **metric_params)

    def __index_knn_impute(
                    self, 
                    depend_feature: str,
                    independ_features: Sequence[str],
                    index: Sequence, 
                    name: str = None, 
                    *,
                    k: int = 5,
                    metric: str = "minkowski",
                    return_pandas: bool = False,
                    na_strictness: bool = True,
                    **metric_params
                ):
        self.validate_feature(depend_feature)
        for fname in independ_features: self.validate_feature(fname)
        assert depend_feature not in independ_features, \
            f"dependent feature must not be in list of independent features"

        for fname in independ_features:
            _indend = self.features[fname]
            if _indend.count_na > 0:
                if na_strictness:
                    LogReporter.error(f"independent feature '{_indend.name}': independent feature must not contain NA values.")
                    LogReporter.report(f"you can set parameter 'na_strictness' as False (now is True) to use the rows which not include NA values for imputation.")
                    return None
                else: 
                    LogReporter.warning(f"independent feature '{_indend.name}': you may face to insufficient data problem for impute data.")
                    LogReporter.report(f"you can set parameter 'na_strictness' as True (now is False) to force all independent features to not include NA value.")
            
            if not isinstance(_indend, NumberFeature) and issubclass(_indend.ctype, ContinuousVariable):
                LogReporter.error(f"independent feature '{_indend.name}': not support imputation for not-categorical text features.")
                return None
        
        target = self.features[depend_feature]

        if len(index) == 0: return return_result( name, 
                                                f"{target.name}__not_imputed",
                                                target.data,
                                                return_pandas,
                                                target.__class__,
                                                ctype=target.ctype, 
                                                stype=target.stype
                                                )
        
        _features = list()
        for fname in independ_features:
            _indend = self.features[fname]
            if issubclass(_indend.ctype, CategoricalVariable):
                if _indend.is_ordinal():
                    _features.append(self.labels_encoding(_indend.name, return_pandas=True))
                else: 
                    _features.append(self.one_hot_encoding(_indend.name, return_pandas=True))
            elif isinstance(_indend, NumberFeature): _features.append(_indend.data)
            else: 
                LogReporter.error(f"{_indend.name}: not support imputation for class '{_indend.__class__}'")
                return None
        
        _features.append(pd.Series(target.data, name="target"))
        full_data = pd.concat(_features, axis=1)
        if not na_strictness:
            full_data = full_data[full_data.iloc[:, :-1].notna().all(axis=1)]
        
        imputeset = full_data.iloc[index, :-1]
        fitset = full_data.iloc[~full_data.index.isin(imputeset.index)]

        if issubclass(target.ctype, CategoricalVariable):
            imputer = KNeighborsClassifier(n_neighbors=k, metric=metric, metric_params=metric_params)
        elif issubclass(target.ctype, ContinuousVariable) and isinstance(target, NumberFeature):
            imputer = KNeighborsRegressor(n_neighbors=k, metric=metric, metric_params=metric_params)
        else:
            LogReporter.error(f"{target.name}: support for only continuous numerical target variable or categorical target variable, but got '{target.ctype}' of '{target.__class__}'")
            return None

        imputer = imputer.fit(fitset.iloc[:, :-1], fitset.iloc[:, -1])
        impute_values = imputer.predict(imputeset)
        full_data["target"][imputeset.index] = impute_values
        imputed = full_data["target"]

        return return_result( name, 
                                f"{target.name}__{k}nn_imputed",
                                imputed,
                                return_pandas,
                                target.__class__,
                                ctype=target.ctype, 
                                stype=target.stype
                                )

class NumberPreprocessor(BasePreprocessor):
    default_return_class = NumberFeature

class TextPreprocessor(BasePreprocessor):
    default_return_class = TextFeature

    def validate_feature(self, feature_name: str) -> TextFeature:
        assert self.has_feature(feature_name), f"there is not feature '{feature_name}'"
        if not self.validate_feature_type(feature_name):
            raise TypeError("'{feature_name}' must be {self.default_return_class}")

        return self.features[feature_name]

    def to_number(self, feature_name: str, name: str = None, *, return_pandas: bool = False):
        target = self.validate_feature(feature_name)

        if self.is_all_number(target):
            cast_data = target.data.apply(lambda x: float(x) if isinstance(x, str) else x)
            return return_result( name, 
                                    f"{target.name}__text_to_number", 
                                    cast_data, 
                                    return_pandas, 
                                    NumberFeature,
                                    ctype=target.ctype, 
                                    stype=target.stype
                                    )

        LogReporter.error(f"{target.name}: can not cast to number.")
        return None

    def is_all_number(self, feature: TextFeature): 
        return feature.notna.apply(is_number).all()

    def lower(self, feature_name: str, name: str = None, *, return_pandas: bool = False):
        target = self.validate_feature(feature_name)
        lower = target.data.apply(lambda x: x.lower() if isinstance(x, str) else x)

        return return_result( name, 
                                f"{target.name}__lower", 
                                lower, 
                                return_pandas, 
                                target.__class__,
                                ctype=target.ctype, 
                                stype=target.stype
                                )

    def upper(self, feature_name: str, name: str = None, *, return_pandas: bool = False):
        target = self.validate_feature(feature_name)
        upper = target.data.apply(lambda x: x.upper() if isinstance(x, str) else x)

        return return_result( name, 
                                f"{target.name}__upper", 
                                upper, 
                                return_pandas, 
                                target.__class__,
                                ctype=target.ctype, 
                                stype=target.stype
                                )

    def en_spell_correcting(self, feature_name: str, name: str = None, *, return_pandas: bool = False, **checker_params):
        target = self.validate_feature(feature_name)
        corrector = SpellChecker(**checker_params)

        def correcting(word):
            correct_word = corrector.correction(word)
            return correct_word if corrector is not None else word

        def correcting_sentence(sentence):
            if not isinstance(sentence, str): return sentence
            segwords = re.findall("\w+", sentence)
            spliters = re.split("\w+", sentence)
            corrects = [ correcting(word) for word in segwords ]

            corrected = spliters[0]
            for word, split in zip(corrects, spliters[1:]):
                corrected += word + split
            
            return corrected

        output = target.data.apply(correcting_sentence)

        return return_result( name, 
                                f"{target.name}__en_spell_correct", 
                                output, 
                                return_pandas, 
                                target.__class__,
                                ctype=target.ctype, 
                                stype=target.stype
                                )

    def th_spell_correcting(self,
                            feature_name: str,
                            name: str = None,
                            *,
                            return_pandas: bool = False,
                            **tokenizer_params):
        target = self.validate_feature(feature_name)
        tokenizer = pythainlp.Tokenizer(**tokenizer_params)

        def correcting_sentence(sentence):
            if not isinstance(sentence, str): return sentence
            if pythainlp.util.countthai(sentence) == 0: return sentence
            token = tokenizer.word_tokenize(sentence)
            return "".join([ 
                            pythainlp.correct(word) if pythainlp.util.countthai(word) > 0 
                            else word 
                            for word in token
                            ])

        output = target.data.apply(correcting_sentence)
        return return_result( name, 
                                f"{target.name}__th_spell_correct", 
                                output, 
                                return_pandas, 
                                target.__class__,
                                ctype=target.ctype, 
                                stype=target.stype
                                )

    def th2en(self, 
                feature_name: str,
                name: str = None,
                *,
                return_pandas: bool = False):
        target = self.validate_feature(feature_name)
        tokenizer = pythainlp.Tokenizer(keep_whitespace=False)

        try: self.__th_en_translater
        except AttributeError:
            initial_th2en()
            model_base_dir = f'{__statics__}/SCB_1M+TBASE_th-en_newmm-moses_130000-130000_v1.0/models/'
            vocab_base_dir = f'{__statics__}/SCB_1M+TBASE_th-en_newmm-moses_130000-130000_v1.0/vocab/'
            self.__th_en_translater = TransformerModel.from_pretrained(
                                        model_name_or_path=model_base_dir,
                                        checkpoint_file='checkpoint.pt',
                                        data_name_or_path=vocab_base_dir,
                                        )

        def translate(text):
            if not isinstance(text, str): return text
            if pythainlp.util.countthai(text) == 0: return text
            if not text.endswith('.'): text += '.'
            tokenise = tokenizer.word_tokenize(text)
            tokenise = " ".join(tokenise)
            result = self.__th_en_translater.translate(tokenise)
            result = html.unescape(result)
            return result
        
        output = target.data.apply(translate)
        return return_result( name, 
                                f"{target.name}__th2en", 
                                output, 
                                return_pandas, 
                                target.__class__,
                                ctype=target.ctype, 
                                stype=target.stype
                                )

class ListPreprocessor(BasePreprocessor):
    default_return_class = ListFeature

class DictPreprocessor(BasePreprocessor):
    default_return_class = DictFeature