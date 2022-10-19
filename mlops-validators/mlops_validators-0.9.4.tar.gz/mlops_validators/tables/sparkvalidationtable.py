from functools import reduce
from operator import add
from pyspark.sql.window import Window
from pyspark.sql import DataFrame
from pyspark.ml.feature import QuantileDiscretizer
import pyspark.sql.functions as f

class SparkValidationTable:

    _comparators = {
        "right_closed_comparison" : lambda int1, int2, value: (value > int1, value <= int2),
        "left_closed_comparison" : lambda int1, int2, value: (value >= int1, value < int2),
        "open" : lambda int1, int2, value: (value > int1, value < int2),
        "closed" : lambda int1, int2, value: (value >= int1, value <= int2)
    }

    _comparators_str_rep = {
        "right_closed_comparison" : "a < x <= b, where x is the feature value and a is the first interval value and b the second.",
        "left_closed_comparison" : "a <= x < b, where x is the feature value and a is the first interval value and b the second.",
        "open" : "a < x < b, where x is the feature value and a is the first interval value and b the second.",
        "closed" : "a <= x <= b, where x is the feature value and a is the first interval value and b the second."
    }

    def __init__(self, **kwargs):
        self.df = kwargs.get("df", None)
        self._feature_A = self.feature_A = kwargs.get("feature_A", None)
        self.feature_B = kwargs.get("feature_B", None)
        self.feature_A_remove_missing = kwargs.get("feature_A_remove_missing", False)
        self.feature_B_remove_missing = kwargs.get("feature_B_remove_missing", False)
        self.bins = kwargs.get("bins", False)
        self.bins_by_quantiles = kwargs.get("bins_by_quantiles", True)
        self.sort_buckets = kwargs.get("sort_buckets" , True)
        self.frequency_label = kwargs.get("frequency_label", "value_")
        self.percentage_label = kwargs.get("percentage_label", "_percent")
        self.proportion_label = kwargs.get("proportion_label", "_proportion")
        self.frequency_totals_label = kwargs.get("frequency_totals_label", "totals")
        self.buckets_label = kwargs.get("buckets_label", "buckets")
        self.buckets_min_label = kwargs.get("buckets_min_label", "buckets_min")
        self.buckets_max_label = kwargs.get("buckets_max_label", "buckets_max")
        self.comparator = kwargs.get("comparator", "right_closed_comparison")
        self.frequency_table = None
        self.map_frequency_columns = {}
        self.map_percentage_columns = {}
        self.map_proportion_columns = {}             
        self._buckets_label = "bins" 
        self._has_calculated_totals = False

        if not isinstance(self.df, DataFrame):
            raise ValueError("The df must be a Spark DataFrame SQl instance.")

        if not isinstance(self.feature_A, str):
            raise ValueError("The feature_A must be a string.")
        elif self.feature_A not in self.df.columns:
            raise ValueError("The feature_A must be a column of the DataFrame df.")
                
        if not isinstance(self.feature_A_remove_missing, bool):
            raise ValueError("The feature_A_remove_missing must be a bool.")

        if self.feature_A_remove_missing:
            self.df = self.df.na.drop(subset=[self.feature_A]) if self.feature_A_remove_missing else self.df

        if not isinstance(self.feature_B_remove_missing, bool):
            raise ValueError("The feature_B_remove_missing must be a bool.")

        if self.feature_B == None:
            self._feature_B = "feature_B_count"
            self.df = self.df.withColumn(self._feature_B, f.lit(1))
        elif isinstance(self.feature_B, str):
            if self.feature_B not in self.df.columns:
                raise ValueError("The feature_B must be a column of the DataFrame df.")
            self._feature_B = self.feature_B
            self.df = self.df.na.drop(subset=[self.feature_B]) if self.feature_B_remove_missing else self.df
        else:
            raise ValueError("The feature_B must be either a string or None.")                

        if isinstance(self.bins, int) and not isinstance(self.bins, bool):
            if self.bins < 1:
                raise ValueError("The bins must be either an integer (>1), a list or False.")
        elif not isinstance(self.bins, bool) and not isinstance(self.bins, list):            
            raise ValueError("The bins must be either an integer (>1), a list or False.")
        
        if not isinstance(self.bins_by_quantiles, bool):
            raise ValueError("The bins_by_quantiles must be a bool.")

        if not isinstance(self.sort_buckets, bool):
            raise ValueError("The sort_buckets must be a bool.")

        if not isinstance(self.frequency_label, str):
            raise ValueError("The frequency_label must be a string.")
            
        if not isinstance(self.percentage_label, str):
            raise ValueError("The percentage_label must be a string.")
            
        if not isinstance(self.proportion_label, str):
            raise ValueError("The proportion_label must be a string.")
            
        if not isinstance(self.frequency_totals_label, str):
            raise ValueError("The frequency_totals_label must be a string.")
            
        if not isinstance(self.buckets_label, str):
            raise ValueError("The buckets_label must be a string.")
        
        if self.buckets_label == self._buckets_label:
            raise ValueError("The buckets_label can not be equal {}.".format(self._buckets_label))

        if not isinstance(self.buckets_min_label, str):
            raise ValueError("The buckets_min_label must be a string.")
        
        if not isinstance(self.buckets_max_label, str):
            raise ValueError("The buckets_max_label must be a string.")

        if not self.comparator in self._comparators.keys():
            raise ValueError("The comparator must be one of the following values: {}.".format(self._comparators.keys()))
    
    def __append_min_max(self, df_buckets, feature_A):        
        df_min_max = df_buckets.groupBy(feature_A).agg(f.min(self._feature_A).alias(self.buckets_min_label), 
                                                       f.max(self._feature_A).alias(self.buckets_max_label))        
        columns_select = self.frequency_table.columns + [self.buckets_min_label, self.buckets_max_label]
        key = self.frequency_table[self.buckets_label] == df_min_max[feature_A]
        self.frequency_table = self.frequency_table.join(df_min_max, key, how="left").select(columns_select)

    def __compile_cross_table(self, df_buckets, feature_A, feature_B):
        self.frequency_table = df_buckets.crosstab(feature_A, feature_B)                                  
        self.frequency_table = self.frequency_table.withColumnRenamed(self.frequency_table.columns[0], self.buckets_label)        
        # removing dots from column names that may cause errors during calculations in float features
        self.map_frequency_columns = {col : self.frequency_label+col.replace(".", "_") for col in self.frequency_table.columns if col != self.buckets_label}
        for col in self.map_frequency_columns:                 
            self.frequency_table = self.frequency_table.withColumnRenamed(col, self.map_frequency_columns[col])         
        types = dict(df_buckets.dtypes) 
        self.frequency_table = self.frequency_table.withColumn(self.buckets_label, f.col(self.buckets_label).cast(types[feature_A]))
        if self.calculate_bin_edges:
            self.__append_min_max(df_buckets, feature_A)
        if self.sort_buckets:
            self.frequency_table = self.frequency_table.sort(self.frequency_table[self.buckets_label])        
    
    def __compile_from_list_of_bins(self):
        intervals = self._comparators[self.comparator](self.bins[0], self.bins[1], self.df[self._feature_A]) 
        case = f.when((intervals[0] & intervals[1]), 1)
        for bucket in range(1, len(self.bins)-1):
            intervals = self._comparators[self.comparator](self.bins[bucket], self.bins[bucket+1], self.df[self._feature_A]) 
            case = case.when((intervals[0] & intervals[1]), bucket+1)        
        return self.df.withColumn(self._buckets_label, case).select([self._buckets_label, self._feature_A, self._feature_B])
    
    def __generate_table_from_list_of_bins(self):        
        df_buckets = self.__compile_from_list_of_bins()
        self.__compile_cross_table(df_buckets, self._buckets_label, self._feature_B)                
    
    def __generate_table_from_feature(self):
        df_buckets = self.df.select([self._feature_A, self._feature_B])        
        self.__compile_cross_table(df_buckets, self._feature_A, self._feature_B)
    
    def __compile_from_number_of_bins_by_quantiles(self):
        query = self.df.select(self._feature_A, self._feature_B)
        quantiles = QuantileDiscretizer(numBuckets=self.bins, inputCol=self._feature_A, outputCol=self._buckets_label, relativeError=0.01, handleInvalid="error")
        quantiles = quantiles.fit(query)
        query = quantiles.setHandleInvalid("skip").transform(query)
        query = query.withColumn(self._buckets_label, f.col(self._buckets_label)+1)
        query = query.withColumn(self._buckets_label, f.col(self._buckets_label).cast("long"))
        return query

    def __compile_from_number_of_bins_by_ntile(self):
        ntile = f.ntile(self.bins).over(Window.orderBy(f.col(self._feature_A)))
        query = self.df.select(f.when(f.col(self._feature_A).isNotNull(), ntile).alias(self._buckets_label), self._feature_A, self._feature_B)        
        return query 

    def __compile_from_number_of_bins(self): 
        if self.bins_by_quantiles:
            return self.__compile_from_number_of_bins_by_quantiles()
        else:
            return self.__compile_from_number_of_bins_by_ntile()
    
    def __generate_table_from_number_of_bins(self):
        df_buckets = self.__compile_from_number_of_bins()        
        self.__compile_cross_table(df_buckets, self._buckets_label, self._feature_B)
        
    def __calculate_percents(self):        
        self.map_percentage_columns = {col : self.frequency_label+col.replace(".", "_")+self.percentage_label for col in self.map_frequency_columns}
        for col in self.map_frequency_columns:                        
            col_sum = self.frequency_table.agg(f.sum(self.map_frequency_columns[col])).first()[0]                        
            self.frequency_table = self.frequency_table.withColumn(self.map_percentage_columns[col], 
                                                       f.col(self.map_frequency_columns[col]) / col_sum)                    
    
    def __calculate_totals(self):        
        self.frequency_table = self.frequency_table.withColumn(self.frequency_totals_label, 
                                                   reduce(add, [f.col(self.map_frequency_columns[col]) for col in self.map_frequency_columns]))   
        self._has_calculated_totals = True

    def __calculate_proportions(self):
        if not self._has_calculated_totals:
            self.__calculate_totals()
        self.map_proportion_columns = {col : self.frequency_label+col.replace(".", "_")+self.proportion_label for col in self.map_frequency_columns}
        for col in self.map_frequency_columns:
            self.frequency_table = self.frequency_table.withColumn(self.map_proportion_columns[col], 
                                                       f.col(self.map_frequency_columns[col]) / f.col(self.frequency_totals_label))
    
    def get_values_frequency_columns(self):
        return list(self.map_frequency_columns.values())
            
    def get_map_frequency_columns(self):
        return self.map_frequency_columns
    
    def get_values_percentage_columns(self):
        return list(self.map_percentage_columns.values())
    
    def get_map_percentage_columns(self):        
        return self.map_percentage_columns
    
    def get_values_proportion_columns(self):
        return list(self.map_proportion_columns.values())
    
    def get_map_proportion_columns(self):        
        return self.map_proportion_columns        
    
    def get_comparator_str_rep(self):
        return self._comparators_str_rep[self.comparator]

    def get_frequency_table(self):
        return self.frequency_table

    def fit(self, calculate_percents=False, calculate_totals=False, calculate_bin_edges=False, calculate_proportions=False):
        if not isinstance(calculate_percents, bool):
            raise ValueError("The calculate_percents must be a bool.")
        if not isinstance(calculate_totals, bool):
            raise ValueError("The calculate_totals must be a bool.")
        if not isinstance(calculate_bin_edges, bool):
            raise ValueError("The calculate_bin_edges must be a bool.")
        if not isinstance(calculate_proportions, bool):
            raise ValueError("The calculate_proportions must be a bool.")
        self.calculate_bin_edges = calculate_bin_edges
        if isinstance(self.bins, list):
            self.__generate_table_from_list_of_bins()               
        elif isinstance(self.bins, bool):                                    
            self.__generate_table_from_feature()
        elif isinstance(self.bins, int):
            self.__generate_table_from_number_of_bins()
        if calculate_percents:
            self.__calculate_percents() 
        if calculate_totals:
            self.__calculate_totals()  
        if calculate_proportions:
            self.__calculate_proportions()
        return self