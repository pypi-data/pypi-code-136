from ..config import __statics__
from ..utils import LogReporter
from ..sherlock_assistance.word_embeddings import SherlockWordEmbeddings
from ..sherlock_assistance.model import SherlockSemanticClassifier

import copy
import numpy as np
import pandas as pd
import pickle

from abc import ABC
from tqdm import tqdm

from numbers import Number
from numpy.typing import ArrayLike
from typing import List, Dict, Sequence, Text, Tuple

import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from statsmodels.stats.stattools import medcouple

CONF_RANGE = (30, 1500)
CAT_CON_CLASSIFY_COEF: List[float] = pickle.load(
    open(f"{__statics__}/category_variable_conf_30-1500_viznet_dataset_threshold.bin", "rb")
    )

ORDINAL_STYPE = (
    "age", "area", "birth date", "capacity", "depth", "elevation", "file size", "grades", "order", 
    "play", "range", "rank", "ranking", "sales", "weight", "year"
    )

def traoezoidal_area(X: ArrayLike, y: ArrayLike) -> float:
    X, y = np.array(X), np.array(y)
    h = (X.max() - X.min()) / len(X)
    return 0.5 * h * (2 * np.sum(y[1:-1]) + y[0] + y[-1])

def interquartile_range(X: ArrayLike) -> Tuple[float, float, float]:
    q3 = np.quantile(X, 0.75)
    q1 = np.quantile(X, 0.25)
    return q3 - q1, q1, q3

class RevisionFeatureMixin:
    
    @classmethod
    def clone_parent(cls, source):
        class_dtype = cls.__dict__[f'_{cls.__name__}__class_dtype']
        assert issubclass(cls, source.__class__), \
            f"class of source '{source}' must be super class of '{cls.__name__}'"
        assert issubclass(source.atype, class_dtype), \
            f"'{cls.__name__}' is not compatible to atomic type of source, expect subclass of '{class_dtype}' not '{source.atype}')"
        instance = object.__new__(cls)
        for name, value in source.__dict__.items():
            # prefix_len = len(f"_{source.__class__.__name__}")
            # LogReporter.warning(f"{name}, _{source.__class__.__name__}, _{cls.__name__}{name[prefix_len:]}, ")
            # LogReporter.warning("starts with: " + str(name.startswith(f"_{source.__class__.__name__}")))
            # if name.startswith(f"_{source.__class__.__name__}"):
            #     prefix_len = len(f"_{source.__class__.__name__}")
            #     name = f"_{cls.__name__}" + name[prefix_len:]
            # else: name = name
            instance.__setattr__(name, copy.deepcopy(value))
        instance.__after_init__()

        return instance

class BaseFeature:
    __atype_threshold = 0.6
    label = None
    __class_dtype = type(None)
    support_visualise_kw = ['na', 'notna']

    @property
    def data(self): return self.__data

    @property
    def name(self): return self.__name

    @name.setter
    def name(self, new_name: str):
        self.__name = new_name
        self.__data.name = self.__name

    @property
    def na(self): return self.__data[self.__data.isna()]

    @property
    def notna(self): 
        return self.__data[self.__data.notna()]

    @property
    def count_na(self): return len(self.na)

    @property
    def count_notna(self): return len(self.notna)

    @property
    def na_percent(self): return self.count_na / len(self)

    @property
    def notna_percent(self): return 1 - self.na_percent

    @property
    def atomic_types(self): 
        try: return self.__atomic_types 
        except: return None

    @property
    def atomic_freq(self):
        try: return self.__atomic_freq
        except: return None

    @property
    def atomic_percent(self):
        try: return self.__atomic_percent
        except: return None

    @property
    def atype(self): return self.__atype

    def visualise(self, ax: Axes = None, type = "na", **fig_kw):
        flag = False
        
        if ax is None:
            fig, ax = plt.subplots(nrows=1, ncols=1, **fig_kw)
            flag = True

        visualise_call = self.visual_switch(type)
        if visualise_call is None:
            LogReporter.error(f"do not support visualise type. got {type}\n{self.name} support visualise keywords: {self.support_visualise_kw}")
        else: visualise_call(ax=ax)

        if flag: return fig, ax

    def visual_switch(self, type):
        if type.lower() == "na" or type.lower() == "notna": return self.visualise_na

    def visualise_na(self, ax: Axes):
        data = [ self.count_na, self.count_notna ]
        labels = [ "NA", "NOT-NA" ]
        colors = [ "#222222", "#cc0000" ]

        def func(pct, allvals):
            absolute = int(np.round(pct/100.*np.sum(allvals)))
            return "{:.1f}%\n({:d})".format(pct, absolute)

        wedges, texts, autotexts = ax.pie(
                                            data, 
                                            autopct=lambda pct: func(pct, data),
                                            labels=labels,
                                            startangle=90,
                                            colors=colors,
                                            explode=(0, 0.1)
                                        )

        for i in range(len(wedges)):
            texts[i].set_color(wedges[i].get_facecolor())
            texts[i].set_fontweight(600)
            
        plt.setp(autotexts, color="w", size=8, weight="bold")
        ax.set_aspect("equal")
        ax.set_title(f"{self.name}: NA propotion")

    def validate_dtype(self):
        dtype = self.__getattribute__(f"_{self.__class__.__name__}__class_dtype")
        if dtype == type(None): return
        if not issubclass(self.atype, dtype):
            error_massage = f"class '{self.__class__.__name__}' not suitable to data's atomic type, got '{str(self.atype)}' (expect 'str({self.__class_dtype})') "
            if issubclass(self.atype, List): error_massage += f"suggest to use class 'ListFeature' instead"
            elif issubclass(self.atype, Dict): error_massage += f"suggest to use class 'DictFeature' instead"
            elif issubclass(self.atype, Number): error_massage += f"suggest to use class 'NumberFeature' instead"
            elif issubclass(self.atype, Text): error_massage += f"suggest to use class 'TextFeature' instead"
            else: error_massage += f"suggest to use class 'BaseFeature' instead"
            
            raise TypeError(error_massage)

    def info(self): return  f"\033[47m\033[30m{self.name} ({len(self)})\033[0m\n" + \
                                    f"notna     |{self.count_notna:>8} ({self.notna_percent * 100:>6.2f}%)\n" + \
                                    f"na        |{self.count_na:>8} ({self.na_percent * 100:>6.2f}%)\n"

    def __init__(self, data: pd.Series or np.array, name: str):
        if not isinstance(data, pd.Series):
            data = pd.Series(data, name=name)
        self.__data = data
        self.__name = name
        self.__atomic_analysis()
        self.validate_dtype()
        
    def __after_init__(self): pass

    def __len__(self): return len(self.data)

    def __repr__(self): return  f"{self.info()}\n" + \
                                f"data:\n{self.data.__repr__()}\n" + \
                                f"atype: {self.atype}"

    def __atomic_analysis(self):
        LogReporter.title(f"{self.name}: atomic type analysis")
        if self.count_notna > 0:
            self.__atomic_types = self.notna.apply(lambda x: type(x))
            self.__atomic_freq = self.__atomic_types.value_counts()
            self.__atomic_percent = self.__atomic_freq / self.count_notna
            if self.__atomic_percent.max() >= self.__atype_threshold:
                self.__atype = self.__atomic_freq.idxmax()
            else: self.__atype = type(None)
        else: self.__atype = type(None)

class ImmutableFeature(BaseFeature):
    cv = 5
    semantic_embedding = SherlockWordEmbeddings()
    semantic_classifier = SherlockSemanticClassifier()
    semantic_classifier.initialize_model_from_json(with_weights=True, model_id="sherlock")
    support_visualise_kw = BaseFeature.support_visualise_kw + \
        ['duplicate', 'distinct', 'frequency', 'unique-rate', 'boxplot', 'boxplot-frequency']

    @property
    def order_category(self): return self.__order_category

    @order_category.setter
    def order_category(self, new_order: Sequence):
        if new_order is not None:
            assert len(new_order) == len(np.unique(self.notna)), \
                f"length of order must be match to length of unique. got {len(new_order)} and {len(np.unique(self.notna))}"
            for xi, xj in zip(np.sort(new_order), np.sort(np.unique(self.notna))): assert xi == xj, f"got unknow value '{xi}'"
        self.__order_category = new_order

    @property
    def frequency(self): return self.__frequency

    @property
    def unique(self): return self.__unique

    @property
    def n_unique(self): return len(self.unique)

    @property
    def distinct(self): return self.__distinct

    @property
    def n_distinct(self): return len(self.distinct)

    @property
    def duplicate(self): return self.__duplicate

    @property
    def n_duplicate(self): return len(self.duplicate)

    @property
    def fqmean(self): return self.frequency.mean()

    @property
    def fqmedian(self): return self.frequency.median()

    @property
    def fqmode(self): return self.frequency.mode()

    @property
    def fqstd(self): return self.frequency.std()

    @property
    def fqmin(self): return self.frequency[self.frequency == self.frequency.min()]

    @property
    def fqmax(self): return self.frequency[self.frequency == self.frequency.max()]
    
    @property
    def fqskew(self): return self.frequency.skew()

    @property
    def fqkurt(self): return self.frequency.kurt()
    
    @property
    def category_threshold(self): 
        n = self.count_notna if self.count_notna < CONF_RANGE[1] else CONF_RANGE[1]
        n = n if n < max(self.n_unique * 2, 80) else max(self.n_unique * 2, 80)
        return CAT_CON_CLASSIFY_COEF[0]*n**2 + CAT_CON_CLASSIFY_COEF[1]*n + CAT_CON_CLASSIFY_COEF[2] 

    @property
    def ctype(self):
        try: return self.__ctype
        except AttributeError as e:
            self.__category_variable_analysis()
            return self.__ctype
    
    @property
    def stype(self):
        try: return self.__stype
        except AttributeError as e:
            self.__semantic_analysis()
            return self.__stype

    def visual_switch(self, type):
        type = type.lower()
        if type == "duplicate" or type == "distinct": return self.visualise_duplicate
        if type == "frequency": return self.visualise_frequency
        if type == "unique-rate": return self.visualise_unique_rate
        if type == "boxplot" or type == "boxplot-frequency": return self.visualise_boxplot
        # if type == "adjusted-boxplot": return self.visualise_adjust_boxplot
        # if type == "any-boxplot": return self.any_boxplot
        return super().visual_switch(type)
    
    def visualise_boxplot(self, ax: Axes):
        data = self.frequency.to_numpy()
        iqr, q1, q3 = interquartile_range(data)
        ax.boxplot(data, vert=False)
        ax.set_yticks([])
        ax.set_title(f"{self.name}: boxplot")
        ax.set_xlabel(f"{self.name}'s frequency")
        ax.legend([f"Q1 = {q1:g}, Q3 = {q3:g}, IQR = {iqr:g}"])

    def visualise_unique_rate(self, ax: Axes):
        n = self.count_notna if self.count_notna < CONF_RANGE[1] else CONF_RANGE[1]
        n = n if n < max(self.n_unique * 2, 80) else max(self.n_unique * 2, 80)
        __th = CAT_CON_CLASSIFY_COEF[0]*n**2 + CAT_CON_CLASSIFY_COEF[1]*n + CAT_CON_CLASSIFY_COEF[2]

        sample = self.notna.sample(n, random_state=0)
        sample = self.__sorted_by_frequency(sample)
        unique_rate = list()
        norm_X = list()
        unique = set()

        for i in range(n):
            unique.add(sample[i])
            unique_rate.append(len(unique)/(i + 1))
            norm_X.append(i/(n - 1))

        auc = traoezoidal_area(norm_X, unique_rate)
        ax.set_title(f"{self.name}: unique rate\nrandom {n} sample from {self.count_notna} data", multialignment='center')

        ax.plot(norm_X, unique_rate, label=f"AUC = {auc:.4f}")
        ax.hlines(__th, 0., 1, linestyles="--", colors='r', label=f"threshold_AUC({n}) = {__th}")

        ax.set_xbound(0., 1)
        ax.set_ybound(-0.1, 1.1)
        ax.set_xlabel("normalized x")
        ax.set_ylabel("unique rate")
        ax.legend()
        ax.grid()

    def visualise_frequency(self, ax: Axes):
        labels = [ f"{label}" for label in self.frequency.index ]
        fr_vc = self.frequency.values

        total = np.sum(fr_vc)
        stack, bounds = 0., [0.]
        for fr in fr_vc:
            stack += fr / total
            bounds.append(stack)
        bounds[-1] = 1.

        ax.set_title(f"{self.name}: frequency of each unique values\nthere are {len(self.frequency)} unique data", multialignment='center')
        
        ax.plot(labels, fr_vc, "o--", color="grey", alpha=0.3)
        ax.step(labels, fr_vc, where="post")

        ax.set_xticklabels(labels)
        ax.set_ylabel("frequency")

        cmap = mpl.cm.get_cmap("Purples")
        norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
        sm = mpl.cm.ScalarMappable(cmap=cmap, norm=norm)
        sm.set_array([])

        cbar = plt.colorbar(
            sm,
            ax=ax,
            spacing='proportional',
            orientation='horizontal',
            label=f'colorbar show the frequency propotion (%)',
        )

        for t in cbar.ax.get_xticklabels():
                t.set_fontsize(6)

    def visualise_duplicate(self, ax: Axes):
        data = [ self.n_distinct, self.n_duplicate ]
        labels = [ "distinct", "duplicate" ]
        colors = [ "#222222", "#8a2be2" ]

        def func(pct, allvals):
            absolute = int(np.round(pct/100.*np.sum(allvals)))
            return "{:.1f}%\n({:d})".format(pct, absolute)

        wedges, texts, autotexts = ax.pie(
                                            data, 
                                            autopct=lambda pct: func(pct, data),
                                            labels=labels,
                                            startangle=90,
                                            colors=colors,
                                            explode=(0, 0.1)
                                        )

        for i in range(len(wedges)):
            texts[i].set_color(wedges[i].get_facecolor())
            texts[i].set_fontweight(600)
            
        plt.setp(autotexts, color="w", size=8, weight="bold")
        ax.set_aspect("equal")
        ax.set_title(f"{self.name}: duplicate propotion")

    def fqquantile(self, qupper: float, qlower: float = 0.):
        upper = self.frequency.quantile(qupper)
        lower = self.frequency.quantile(qlower)
        return upper, lower, self.frequency[ (lower <= self.frequency) & (self.frequency <= upper) ]

    def is_binary(self):
        return self.n_unique == 2

    def is_ordinal(self):
        return self.order_category is not None

    def set_as_categorical(self):
        LogReporter.report(f"{self.name} is set as categorical variable.")
        self.__ctype = CategoricalVariable
    
    def set_as_continuous(self):
        LogReporter.report(f"{self.name} is set as continuous variable.")
        self.__ctype = ContinuousVariable

    def __init__(self, data: pd.Series or np.array, name: str, ctype = None, stype: str = None, order_category: Sequence = None):
        LogReporter.title(f"initialize: name = {name}, ctype = {ctype}, stype = {stype}, order_category = {order_category}")
        super().__init__(data, name)
        if order_category is not None:
            assert len(order_category) == len(np.unique(self.notna)), \
                f"length of order category must be match to length of unique. got {len(order_category)} and {len(np.unique(self.notna))}"
            for xi, xj in zip(np.sort(order_category), np.sort(np.unique(self.notna))): assert xi == xj, f"got unknow value '{xi}'"
            self.__ctype = CategoricalVariable
        else: self.__ctype = ctype
        self.__order_category = order_category
        self.__stype = stype
        print(self.__ctype, self.__stype)
        self.__after_init__()

    def __after_init__(self):
        # print("after initial")
        self.__proportion_analysis()
        try: self.__order_category
        except AttributeError: self.__order_category = None
        if self.ctype is None: self.__category_variable_analysis()
        if self.stype is None: self.__semantic_analysis()

    def info(self): return super().info() + \
                                        f"duplicate |{self.n_duplicate:>8} ({self.n_duplicate / self.n_unique * 100:>6.2f}%)\n" + \
                                        f"distinct  |{self.n_distinct:>8} ({self.n_distinct / self.n_unique * 100:>6.2f}%)\n" + \
                                        f"unique    |{self.n_unique:>8}\n" + \
                                        f"order     |{self.order_category if self.order_category is not None else None}\n"

    def __repr__(self): return super().__repr__() + f" ctype: {self.ctype.label if self.ctype is not None else 'none'}" + \
                                                    f" stype: {self.stype if self.stype is not None else 'none'}"

    def __proportion_analysis(self):
        LogReporter.title(f"{self.name}: proportion analysis")
        self.__frequency = self.notna.value_counts().sort_values(ascending=False)
        self.__distinct = self.__frequency[self.__frequency == 1].index.to_list()
        self.__duplicate = self.__frequency[~self.__frequency.index.isin(self.__distinct)].index.to_list()
        self.__unique = self.__frequency.index.to_list()

    def __sorted_by_frequency(self, sample):
        value_counts = pd.value_counts(sample).sort_values(ascending=False)
        return np.array([ key for key in value_counts.index for freq in range(value_counts[key]) ])

    def __category_variable_analysis(self):
        LogReporter.title(f"{self.name}: category variable type analysis")
        assert ImmutableFeature.cv % 2 == 1, "cv must be odd, got {ImmutableFeature.cv}"

        if self.count_notna < CONF_RANGE[0]: 
            LogReporter.warning(f"column '{self.name}' has amount of notna row less than lowest confidence range ({CONF_RANGE[0]}), got {self.count_notna}")
            self.__ctype = None
            return None
        
        n = self.count_notna if self.count_notna < CONF_RANGE[1] else CONF_RANGE[1]
        n = n if n < max(self.n_unique * 2, 80) else max(self.n_unique * 2, 80)
        __th = CAT_CON_CLASSIFY_COEF[0]*n**2 + CAT_CON_CLASSIFY_COEF[1]*n + CAT_CON_CLASSIFY_COEF[2]
        vote_continuous = 0

        for _ in range(ImmutableFeature.cv):
            sample = self.notna.sample(n)
            sample = self.__sorted_by_frequency(sample)
            unique_rate = list()
            norm_X = list()
            unique = set()

            for i in range(n):
                unique.add(sample[i])
                unique_rate.append(len(unique)/(i + 1))
                norm_X.append(i/n)

            auc = traoezoidal_area(norm_X, unique_rate)
            # print(f"{self.name}: AUC = {auc}")
            vote_continuous += -1 if auc <= __th else 1
        
        self.__ctype = CategoricalVariable if vote_continuous < 0 else ContinuousVariable
        LogReporter.report(f"classify {self.name} as {self.__ctype} vote result: {vote_continuous} with threshold = {__th} of {n} sample")
    
    def __semantic_analysis(self):
        LogReporter.title(f"{self.name}: semantic type analysis")
        data = self.notna.apply(str).tolist()
        features = self.semantic_embedding.transform(pd.Series([data]))
        predict = self.semantic_classifier.predict(features)
        self.__stype = predict[0].lower()

class NumberFeature(ImmutableFeature, RevisionFeatureMixin):
    __class_dtype = Number
    label = "number"
    support_visualise_kw = ImmutableFeature.support_visualise_kw +\
        ['boxplot-value']

    @property
    def mean(self): return self.notna.mean()

    @property
    def median(self): return self.notna.median()

    @property
    def mode(self): return self.notna.mode()

    @property
    def std(self): return self.notna.std()

    @property
    def min(self): return self.notna.min()

    @property
    def max(self): return self.notna.max()

    @property
    def skew(self): return self.notna.skew()

    @property
    def kurt(self): return self.notna.kurt()

    @property
    def outlier(self):
        lower, upper = self.ctype.outlier_analysis(self)
        if issubclass(self.ctype, CategoricalVariable): 
            outlier_idx = self.frequency[(self.frequency <= lower) | (self.frequency >= upper)].index
            return self.notna[self.notna.isin(outlier_idx)]
        elif issubclass(self.ctype, ContinuousVariable):
            return self.notna[(self.notna <= lower) | (self.notna >= upper)]
        
        return None

    @property
    def n_outlier(self):
        return len(self.outlier) if self.outlier is not None else None

    @property
    def outlier_percent(self):
        return self.n_outlier / len(self) if self.n_outlier is not None else None

    def is_ordinal(self):
        # TODO: other approachs for classify ordinal and norminal
        return self.stype in ORDINAL_STYPE or issubclass(self.ctype, ContinuousVariable) or self.order_category is not None

    def quantile(self, qupper: float, qlower: float = 0.):
        upper = self.notna.quantile(qupper)
        lower = self.notna.quantile(qlower)
        return upper, lower, self.notna[ (lower <= self.notna) & (self.notna <= upper) ]

    def info(self): return super().info() + \
                                f"\033[47m\033[30mvalue{' '*12}\033[0m\n" +\
                                f"mean      |{self.mean}\n" + \
                                f"median    |{self.median}\n" + \
                                f"mode      |{self.mode.values}\n" + \
                                f"min, max  |{self.min}, {self.max}\n" + \
                                f"std       |{self.std}\n"

    def visual_switch(self, type):
        type = type.lower()
        if type == "boxplot-value": return self.visualise_boxplot_value
        if type == "boxplot-frequency": return super().visualise_boxplot
        return super().visual_switch(type)

    def visualise_boxplot(self, ax: Axes):
        if issubclass(self.ctype, ContinuousVariable): self.visualise_boxplot_value(ax)
        else: super().visualise_boxplot(ax)

    def visualise_boxplot_value(self, ax: Axes):
        data = self.notna.to_numpy()
        iqr, q1, q3 = interquartile_range(data)
        ax.boxplot(data, vert=False)
        ax.set_yticks([])
        ax.set_title(f"{self.name}: boxplot")
        ax.set_xlabel(f"{self.name}'s values")
        ax.legend([f"Q1 = {q1:.4g}, Q3 = {q3:.4g}, IQR = {iqr:.4g}"])

    def visualise_frequency(self, ax: Axes):
        super().visualise_frequency(ax)

        if len(self.frequency) > 6:
            step = len(self.frequency) // 6
            loc = list(range(0, len(self.frequency), step))
            loc[-1] = len(self.frequency)
            ax.xaxis.set_major_locator(mpl.ticker.FixedLocator(loc))
            for t in ax.get_xticklabels():
                t.set_fontsize(8)

        ticklabels = list(ax.xaxis.get_ticklabels())
        @mpl.ticker.FuncFormatter
        def major_formatter(x, pos):
            l = ticklabels[pos].get_text()
            try: return f"{int(l):.3e}" if int(l) > 9999 else f"{int(l):g}"
            except: pass
            try: return f"{float(l):.3e}" if float(l) > 9999. or float(l) < 0.001 else f"{float(l):.3f}"
            except: return l

        ax.xaxis.set_major_formatter(major_formatter)

class TextFeature(ImmutableFeature, RevisionFeatureMixin):
    __class_dtype = Text
    label = 'text'

    @property
    def outlier(self):
        if issubclass(self.ctype, CategoricalVariable):
            lower, upper = CategoricalVariable.outlier_analysis(self)
            outlier_idx = self.frequency[(self.frequency <= lower) | (self.frequency >= upper)].index
            return self.notna[self.notna.isin(outlier_idx)]
        
        return None

    @property
    def n_outlier(self):
        return len(self.outlier) if self.outlier is not None else None

    @property
    def outlier_percent(self):
        return self.n_outlier / len(self) if self.n_outlier is not None else None

    def visualise_frequency(self, ax: Axes):
        super().visualise_frequency(ax)
        
        @mpl.ticker.FuncFormatter
        def major_formatter(x, pos):
            label = self.frequency.index[x]
            return label[:9] + '...' if len(label) > 12 else label

        ax.xaxis.set_major_formatter(major_formatter)
        if len(self.frequency) > 6:
            ax.xaxis.set_major_locator(mpl.ticker.FixedLocator([0, len(self.frequency) - 1]))

    def info(self): return super().info() + \
                                f"\033[47m\033[30mfrequency{' '*8}\033[00m\n" +\
                                f"mean      |{self.fqmean}\n" + \
                                f"median    |{self.fqmedian}\n" + \
                                f"std       |{self.fqstd}\n" + \
                                f"min       |{self.fqmin.index[0]} = {self.frequency.min()} ({len(self.fqmin)})\n" + \
                                f"max       |{self.fqmax.index[0]} = {self.frequency.max()} ({len(self.fqmax)})"

class ListFeature(BaseFeature, RevisionFeatureMixin):
    __class_dtype = List
    label = 'list'

    @property
    def members(self): 
        try: return self.__members
        except: return None

    @property
    def members_insight(self): 
        try: return self.__members_insight
        except: return None

    @property
    def row_len(self): return self.notna.apply(lambda x: len(x) if isinstance(x, list) else None)

    def __after_init__(self):
        self.members_analysis()

    def members_analysis(self):
        __members = list()
        for indx, value in tqdm(zip(self.notna.index, self.notna.values), f"{self.name}: members analysis\t", total=len(self.notna)):
            value = value if isinstance(value, list) else [value]
            __members.append(pd.Series(value, index=[ indx for _ in range(len(value)) ]))
        self.__members : pd.Series = pd.concat(__members, axis=0)
        members_insight = BaseFeature(self.__members, f"_{self.name}__members")
        
        if issubclass(members_insight.atype, Number):
            self.__members_insight = NumberFeature.clone_parent(members_insight)
        elif issubclass(members_insight.atype, Text):
            self.__members_insight = TextFeature.clone_parent(members_insight)
        else:
            self.__members_insight = members_insight

class DictFeature(BaseFeature, RevisionFeatureMixin):
    __class_dtype = Dict
    label = 'dictionary'
    
    @property
    def items(self):
        try: return self.__items
        except: return None

    @property
    def keys(self):
        try: return self.items.columns.to_numpy()
        except: return None

    @property
    def values(self):
        try: return self.items.values
        except: return None

    @property
    def items_insight(self):
        try: return self.__items_insight
        except: return None

    def __after_init__(self):
        # print("after initial")
        self.items_analysis()

    def items_analysis(self):
        __items = list()
        for value in tqdm(self.notna.values, f"{self.name}: items analysis\t"):
            if isinstance(value, dict):
                __items.append(pd.Series(value))
        self.__items = pd.concat(__items, axis=1).T
        self.__items_insight = dict()
        for _key in tqdm(self.__items.columns, f"{self.name}: keys analysis\t"):
            itmes_insight = BaseFeature(self.__items[_key], f"_{self.name}__{_key}")

            if issubclass(itmes_insight.atype, Number):
                self.__items_insight[_key] = NumberFeature.clone_parent(itmes_insight)
            elif issubclass(itmes_insight.atype, Text):
                self.__items_insight[_key] = TextFeature.clone_parent(itmes_insight)
            else: self.__items_insight[_key] = itmes_insight

class CategoricalVariable(ABC):
    label = "categorical"

    @classmethod
    def is_symmetric(cls, feature: ImmutableFeature):
        return np.abs(feature.fqskew) < 0.5

    @classmethod
    def IQR(cls, feature: ImmutableFeature):
        data = feature.frequency.to_numpy()
        iqr, q1, q3 = interquartile_range(data)

        return q1 - 1.5*iqr, q3 + 1.5*iqr

    @classmethod
    def adjusted_boxplot(cls, feature: ImmutableFeature):
        data = feature.frequency.to_numpy()
        iqr, q1, q3 = interquartile_range(data)
        mc = medcouple(data)

        return q1 - 1.5*np.exp(-3.5*mc)*iqr, q3 + 1.5*np.exp(4*mc)*iqr

    @classmethod
    def outlier_analysis(cls, feature: ImmutableFeature):
        if cls.is_symmetric(feature): return cls.IQR(feature)
        else: return cls.adjusted_boxplot(feature)

class ContinuousVariable(ABC):
    label = "continuous"

    @classmethod
    def is_symmetric(cls, feature: NumberFeature):
        return np.abs(feature.skew) < 0.5

    @classmethod
    def IQR(cls, feature: NumberFeature):
        data = feature.notna.to_numpy()
        iqr, q1, q3 = interquartile_range(data)

        return q1 - 1.5*iqr, q3 + 1.5*iqr

    @classmethod
    def adjusted_boxplot(cls, feature: NumberFeature):
        if feature.count_notna > 1e4:
            LogReporter.warning(f"medcouple require a O(N**2) space complexity and may not work for very large arrays. (got N={feature.count_notna})")
            LogReporter.warning(f"warning: so to avoid memory error use IQR for outlier detection instead.")
            return cls.IQR(feature)
        
        data = feature.notna.to_numpy()
        iqr, q1, q3 = interquartile_range(data)
        mc = medcouple(data)

        return q1 - 1.5*np.exp(-3.5*mc)*iqr, q3 + 1.5*np.exp(4*mc)*iqr

    @classmethod
    def outlier_analysis(cls, feature: NumberFeature):
        if cls.is_symmetric(feature): return cls.IQR(feature)
        else: return cls.adjusted_boxplot(feature)