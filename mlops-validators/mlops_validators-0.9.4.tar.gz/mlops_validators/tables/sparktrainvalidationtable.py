from mlops_validators.tables import SparkValidationTable

class SparkTrainValidationTable(SparkValidationTable):
                     
    def __init__(self, **kwargs):  
        self.df_train = kwargs["df"] = kwargs.get("df_train", None)
        self.feature = kwargs["feature_A"] = kwargs.get("feature", None)
        self.target = kwargs["feature_B"] = kwargs.get("target", None)
        self.train_frequency_label = kwargs["frequency_label"] = kwargs.get("train_frequency_label", "train_value_")
        self.train_totals_label = kwargs["frequency_totals_label"] = kwargs.get("train_totals_label", "train_total")
        self.train_buckets_min_label = kwargs["buckets_min_label"] = kwargs.get("train_buckets_min_label", "train_buckets_min")
        self.train_buckets_max_label = kwargs["buckets_max_label"] = kwargs.get("train_buckets_max_label", "train_buckets_max") 
        self.train_buckets_label = kwargs["buckets_label"] = kwargs.get("train_buckets_label", "train_buckets")
        super().__init__(**kwargs) 

        self.df_validation = kwargs["df"] = kwargs.get("df_validation", None)
        self.validation_frequency_label = kwargs["frequency_label"] = kwargs.get("validation_frequency_label", "validation_value_")
        self.validation_totals_label = kwargs["frequency_totals_label"] = kwargs.get("validation_totals_label", "validation_total")      
        self.validation_buckets_min_label = kwargs["buckets_min_label"] = kwargs.get("validation_buckets_min_label", "validation_buckets_min")
        self.validation_buckets_max_label = kwargs["buckets_max_label"] = kwargs.get("validation_buckets_max_label", "validation_buckets_max")
        self.validation_buckets_label = kwargs["buckets_label"] = kwargs.get("validation_buckets_label", "validation_buckets")
        self.validation_table = SparkValidationTable(**kwargs)      
        
        if self.train_frequency_label == self.validation_frequency_label:
            raise ValueError("The train_frequency_label can not be equal to validation_frequency_label.")
        if self.train_totals_label == self.validation_totals_label:
            raise ValueError("The train_totals_label can not be equal to validation_totals_label.")
        if not (self.feature in self.df_train.columns and self.feature in self.df_validation.columns):
            raise ValueError("The feature must be in df_train and df_validation DataFrames.")
        if isinstance(self.target, str):
            if not (self.target in self.df_train.columns and self.feature in self.df_validation.columns):
                raise ValueError("The target must be in df_train and df_validation DataFrames.")      
        self.validation_frequency_table = None         
        self.train_validation_table = None  

    def __merge_maps(self, map_one, map_two):
        keys = map_one.keys() | map_two.keys()
        merged_maps = {key: [map_one.get(key,"")] + [map_two.get(key,"")] for key in keys}
        return merged_maps

    def get_frequency_table(self):
        return self.train_validation_table
    
    def get_map_frequency_columns(self):
        return self.__merge_maps(self.map_frequency_columns, self.validation_table.map_frequency_columns)

    def get_values_frequency_columns(self):
        return super().get_values_frequency_columns() + self.validation_table.get_values_frequency_columns()

    def get_map_proportion_columns(self):
        return self.__merge_maps(self.map_proportion_columns, self.validation_table.map_proportion_columns)

    def get_values_proportion_columns(self):
        labels = super().get_values_proportion_columns() + self.validation_table.get_values_proportion_columns()
        return labels

    def get_map_percentage_columns(self):
        return self.__merge_maps(self.map_percentage_columns, self.validation_table.map_percentage_columns)

    def get_values_percentage_columns(self):
        labels = super().get_values_percentage_columns() + self.validation_table.get_values_percentage_columns()
        return labels
    
    def fit(self, **kwargs):
        super().fit(**kwargs)                           
        self.validation_frequency_table = self.validation_table.fit(**kwargs).get_frequency_table()               
        select_columns = self.frequency_table.columns + self.validation_frequency_table.columns                
        key = self.frequency_table[self.train_buckets_label] == self.validation_frequency_table[self.validation_buckets_label]            
        self.train_validation_table = self.frequency_table.join(self.validation_frequency_table, key, how="fullouter").select(select_columns)        
        self.train_validation_table = self.train_validation_table.sort(self.train_buckets_label) 
        return self