from .config import __statics__
from .utils import LogReporter, FileReader
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

import copy
import pathlib
import numpy as np
import pandas as pd

from scipy import stats

from numbers import Number
from typing import List, Dict, Text, Union, NamedTuple

from sklearn.preprocessing import LabelEncoder

class Correlation(NamedTuple):
    '''
    description 
    ----------
    (class) Correlation: named tuple class contain result from bi-variate correlation

    import
    ---------
    dolye.data_exploration.Correlation

    attributes
    ----------
        strategy : str
            calculation strategy to find correlation
        correlation : float or None
            correlation between 2 features (None if 'not support' strategy)
        pvalue : float or None
            p-value (None if 'not support' strategy)
    '''
    strategy: str
    '''calculation strategy to find correlation'''
    correlation: Union[float, None]
    '''correlation between 2 features (None if 'not support' strategy)'''
    pvalue: Union[float, None]
    '''p-value (None if 'not support' strategy)'''

class DataExplorer:
    '''
    description 
    ----------
    (class) DataExplorer: doyle's data exploring class

    import
    ----------
    dolye.DataExplorer\n
    dolye.data_exploration.DataExplorer

    static method
    ----------
        explore_file(path : str) -> DataExplorer or list(DataExplore)
            read files from specified path then create DataExplorer instances for each read dataframe

    class method
    ----------
        dtype_indentify(__feature : BaseFeature) -> subclass(BaseFeature)
            convert BaseFeature instance to subclass of BaseFeature depend on its atomic type

        bi_variate(x : TextFeature or NumberFeature, y : TextFeature or NumberFeature) -> Correlation
            determine correlation between 2 features automatically
    '''
    
    @property
    def original_dataframe(self): 
        '''(read-only attribute) original dataframe'''
        return self.__ori_df

    @property
    def dataframe(self):
        '''(read-only attribute) dataframe consists of original columns and preprocessed columns'''
        try:
            features = { name: feature.data for name, feature in self.features.items() }
            return pd.DataFrame(features)
        except AttributeError:
            return self.original_dataframe.copy(deep=True)

    @property
    def df(self): 
        '''(read-only attribute) alias of dataframe'''
        return self.dataframe

    @property
    def path(self): 
        '''(read-only attribute) path to read file which contain data'''
        return self.__path

    @property
    def sheet(self): 
        '''(read-only attribute) sheet name in case of read file from excel file with multiple sheet'''
        return self.__sheet

    @property
    def features(self): 
        '''
        (read-only attribute) dictionary of features where; 
        - keys is columns name 
        - values is doyle's feature class
        '''
        return self.__features

    @property
    def features_name(self): 
        '''(read-only attribute) list of columns name'''
        return list(self.__features.keys())

    @staticmethod
    def explore_file(path: str):
        '''
        description 
        ----------
            (static method) read files from specified path then create DataExplorer instances for each read dataframe
        
        parameters 
        ----------
            path : str (positional)
                path to file or directory to read

        return
        ----------
            DataExplorer or list(DataExplorer)
                DataExplorer instance or list of DataExplorer instance for each file
        '''
        LogReporter.clear()
        dfs = FileReader.read_files(path)
        explorers: List[DataExplorer] = list()
        for path, df in dfs.items():
            if isinstance(df, dict):
                explorers.extend([DataExplorer(v, path, sheet) for sheet, v in df.items()])
            elif isinstance(df, pd.DataFrame): 
                explorers.append(DataExplorer(df, path))
        
        if len(explorers) == 1: return explorers[0]
        return explorers

    @classmethod
    def dtype_indentify(cls, feature: BaseFeature):
        '''
        description 
        ----------
            (static method) convert BaseFeature instance to subclass of BaseFeature depend on its atomic type

        parameters 
        ----------
            feature : BaseFeature (positional)
                feature to convert

        return
        ----------
            subclass(BaseFeature)
            - if atomic type is list : ListFeature
            - if atomic type is dict : DictFeature
            - if atomic type is number : NumberFeature
            - if atomic type is text : TextFeature
            - else : BaseFeature
        '''
        if feature.__class__ != BaseFeature: 
            raise TypeError(f"__feature must be excatly instance of BaseFeature, got {feature.__class__}")
        
        if issubclass(feature.atype, List): 
            # print(f"indentify {__feature.name} as list")
            return ListFeature.clone_parent(feature)
        if issubclass(feature.atype, Dict): 
            # print(f"indentify {__feature.name} as dict")
            return DictFeature.clone_parent(feature)
        if issubclass(feature.atype, Number): 
            # print(f"indentify {__feature.name} as number")
            return NumberFeature.clone_parent(feature)
        if issubclass(feature.atype, Text): 
            # print(f"indentify {__feature.name} as text")
            return TextFeature.clone_parent(feature)
        
        return feature

    @classmethod
    def __numeric_pearson_correlation(cls, data: pd.DataFrame):
        corr, pval = stats.pearsonr(data.iloc[:, 0], data.iloc[:, 1])
        return "pearson", corr, pval

    @classmethod
    def __numeric_spearman_correlation(cls, data: pd.DataFrame):
        corr, pval = stats.spearmanr(data.iloc[:, 0], data.iloc[:, 1], nan_policy="omit")
        return "spearman rank", corr, pval

    @classmethod
    def __cramers_v_correlation(cls, data: pd.DataFrame, correction = False):
        crosstab = pd.crosstab(data.iloc[:, 0], data.iloc[:, 1])
        chi2, pval, dof, expected = stats.chi2_contingency(crosstab, correction=correction)
        min_dim = min(crosstab.shape) - 1
        N = len(data)
        V = np.sqrt(chi2/(N * min_dim))
        return "cramer's v", V, pval, chi2, dof, expected

    @classmethod
    def __numeric_point_biserial_correlation(cls, data: pd.DataFrame):
        corr, pval = stats.pointbiserialr(data.iloc[:, 0], data.iloc[:, 1])
        return "point-biserial", corr, pval

    @classmethod
    def __numeric_bi_variate(cls, x: NumberFeature, y: NumberFeature):
        
        data = pd.concat([x.data, y.data], axis=1).dropna()
        if len(data) < 0.1 * len(x.data): 
            LogReporter.warning(f"number of notna data that intersect in both features is small than 10% of total (got {len(data)}), so result may not accurate.")

        # combination table
        # 0>  X  &  Y  
        # --------------
        # 1> con & con / pearson
        # 2> con & ord / spearman
        # 2> ord & con / spearman
        # 2> ord & ord / spearman
        # 3> nor & nor / cramers'v
        # 3> nor & ord / cramers'v
        # 3> ord & nor / cramers'v
        # 4> nor & con (binary) / .biserial
        # 4> con & nor (binary) / .biserial
        # 5> nor & con (non-binary) \ not support for now
        # 5> con & nor (non-binary) \ not support for now

        # both are continuous variable. (con&con)
        if issubclass(x.ctype, ContinuousVariable) and issubclass(y.ctype, ContinuousVariable):
            return Correlation(*cls.__numeric_pearson_correlation(data))
        # at least one variable is ordinal categorical variable. (con&ord, ord&con, ord&ord)
        if x.is_ordinal() and y.is_ordinal():
            return Correlation(*cls.__numeric_spearman_correlation(data))
        # both are norminal categorical variable. (nor&nor)
        if issubclass(x.ctype, CategoricalVariable) and issubclass(y.ctype, CategoricalVariable):
            name, corr, pval, _, _, _ = cls.__cramers_v_correlation(data)
            return Correlation(name, corr, pval)
        # one of both is binary. (nor&con, con&nor)
        if x.is_binary() or y.is_binary():
            return Correlation(*cls.__numeric_point_biserial_correlation(data))
        
        LogReporter.error("not support correlation between non-binary and continuous for now.")
        return Correlation("not support", None, None)

    @classmethod
    def __text_bi_variate(cls, x: TextFeature, y: TextFeature):
        
        data = pd.concat([x.data, y.data], axis=1).dropna()
        if len(data) < 0.1 * len(x.data): 
            LogReporter.warning(f"number of notna data that intersect in both features is small than 10% of total (got {len(data)}), so result may not accurate.")
        
        if issubclass(x.ctype, CategoricalVariable) and issubclass(y.ctype, CategoricalVariable):
            name, corr, pval, _, _, _ = cls.__cramers_v_correlation(data)
            return Correlation(name, corr, pval)

        LogReporter.error("only support correlation between categorical variables for now.")
        return Correlation("not support", None, None)

    @classmethod
    def bi_variate(cls, x: TextFeature or NumberFeature, y: TextFeature or NumberFeature):
        '''
        description 
        ----------
            (class method) determine correlation between 2 features automatically

        parameters 
        ----------
            x : TextFeature or NumberFeature (positional)
            y : TextFeature or NumberFeature (positional)

        return
        ----------
            Correlation(strategy : str, correlation : float, pvalue : float)
            - "pearson" : 2 numerical variables which are continuous
            - "spearman" : 2 ordinal categorical variables or continuous numerical and ordinal categorical
            - "cramer'v" : 2 categorical norminal variables
            - "point-biserial": binary variable and continuous numerical variable
            - "not support" : other cases
        '''
        if isinstance(x, NumberFeature) and isinstance(y, NumberFeature): 
            return cls.__numeric_bi_variate(x, y)
        
        if isinstance(x, TextFeature) and isinstance(y, TextFeature):
            return cls.__text_bi_variate(x, y)

        if isinstance(y, TextFeature) and issubclass(y.ctype, CategoricalVariable): x, y = y, x
        data = pd.concat([x.data, y.data], axis=1).dropna()

        if isinstance(x, TextFeature) and issubclass(x.ctype, CategoricalVariable):
            encode_x = LabelEncoder().fit_transform(data.iloc[:, 0])
            data.iloc[:, 0] = encode_x

            if issubclass(y.ctype, ContinuousVariable) and x.is_binary():
                return Correlation(*cls.__numeric_point_biserial_correlation(data))

            if issubclass(y.ctype, CategoricalVariable):
                name, corr, pval, _, _, _ = cls.__cramers_v_correlation(data)
                return Correlation(name, corr, pval)

        # if isinstance(y, TextFeature) and issubclass(y.ctype, CategoricalVariable): 
        #     encode_y = LabelEncoder().fit_transform(data.iloc[:, 1])
        #     data.iloc[:, 1] = encode_y

        #     if issubclass(x.ctype, ContinuousVariable) and y.is_binary():
        #         return cls.__numeric_point_biserial_correlation(data)
                
        #     if issubclass(x.ctype, CategoricalVariable):
        #         name, corr, pval, _, _, _ = cls.__cramers_v_correlation(data)
        #         return name, corr, pval

        LogReporter.error("only support correlation between continuous text variables or continuous and non-binary categorical variables for now.")
        return Correlation("not support", None, None)
        
    def __init__(self, df: pd.DataFrame, path: str or pathlib.PurePath = None, sheet_name: str = None):
        '''
        parameters 
        ----------
            df : DataFrame (positional)
                dataframe to explore
            path : str or pathlib.PurePath (optional)
                path to file that contain data in dataframe (default = None)
            sheet_name : str (optional)
                sheet name in case of read from excel file
        '''
        LogReporter.title(f"initial explorer for {path} ({sheet_name})")
        self.__ori_df = df.copy(deep=True)
        self.__path = path
        self.__sheet_name = sheet_name
        self.features_analysis()
    
    def __len__(self): return len(self.df)   
    
    def __repr__(self): 
        repr = f"\033[1mData Explorer of {self.__path}\033[0m"
        repr += f"({self.__sheet_name}) " if self.__sheet_name else " "
        repr += f": {len(self.__features)} features\n"
        repr += "\033[107m\033[30m\033[1m" + f"{'FEATURE':20}| {'ATYPE':>12} {'DTYPE':>12} {'CTYPE':>12} {'STYPE':>12} {'NA':>12} {'NA%':>12}" + "\033[0m\n"
        for feature in self.__features.values():
            repr += f"{feature.name:20}| {feature.atype.__name__:>12} {feature.label if feature.label else '':>12} "
            repr += f"{feature.ctype.label:>12} {feature.stype:>12} " if isinstance(feature, ImmutableFeature) and feature.ctype is not None else f"{' ':>12} {' ':>12} "
            repr += f"{feature.count_na:>12} {feature.na_percent * 100:>10.2f} %\n"
        return repr

    def __add__(self, other: Union[BaseFeature, List[BaseFeature]]):
        new = copy.deepcopy(self)
        if isinstance(other, list): new.extend_features(other)
        else: new.append_feature(other)
        return new

    def __iadd__(self, other: Union[BaseFeature, List[BaseFeature]]):
        if isinstance(other, list): self.extend_features(other)
        else: self.append_feature(other)
        return self

    def __getitem__(self, item: str):
        return self.features[item]

    def has_feature(self, name: str):
        '''if this instance include specified feature name'''
        return name in self.features_name

    def features_analysis(self):
        ''''''
        df = self.df
        self.__features: Dict[str, Union[NumberFeature, TextFeature, ListFeature, DictFeature, BaseFeature]] = dict()
        for column in df.columns:
            LogReporter.report(f"explore feature : {column}")
            feature = DataExplorer.dtype_indentify(BaseFeature(df[column], column))
            self.__features[column] = feature

    def bi_variate_analysis(self, x_feature_name: str, y_feature_name: str):
        assert self.has_feature(x_feature_name), f"there is not feature '{x_feature_name}'"
        assert self.has_feature(y_feature_name), f"there is not feature '{y_feature_name}'"
        x = self.features[x_feature_name]
        y = self.features[y_feature_name]
        return self.bi_variate(x, y)

    def pop_feature(self, feature_name: str):
        assert self.has_feature(feature_name), f"there is not feature '{feature_name}'"
        pop = self.__features[feature_name]
        del self.__features[feature_name]
        return pop

    def delete_feature(self, feature_name: str):
        assert self.has_feature(feature_name), f"there is not feature '{feature_name}'"
        del self.__features[feature_name]

    def append_feature(self, new_feature: BaseFeature):
        assert len(self) == len(new_feature), f"length of feature must be match to dataframe, expected {len(self)} but got {len(new_feature)}"
        f = copy.deepcopy(new_feature)
        _name, i = f.name, 0
        while self.has_feature(_name): _name = f"{f.name}__{i}"; i += 1
        f.name = _name
        
        if f.__class__ == BaseFeature: f = DataExplorer.dtype_indentify(f)
        self.__features[f.name] = f

    def add_features(self, *new_features: BaseFeature):
        assert all([len(self) == len(f) for f in new_features]), f"length of all features must be match to dataframe, expected {len(self)} but got [" + ", ".join([ f'\033[31m\033[1m{len(f)}\033[0m' if len(f) != len(self) else f'{len(f)}' for f in new_features]) + "]"
        for f in new_features: self.append_feature(f)
    
    def extend_features(self, new_features: List[BaseFeature]):
        self.add_features(*new_features)