from mlops_validators.profiles import SparkFeatureMetricProfile
import pyspark.sql.functions as f

class SparkDatasetMetricProfile:

    def __init__(self, features=[], validators=[], include_timestamp=False, **kwargs):        
        self.features = features
        if not isinstance(self.features, list):
            raise ValueError("The features must be a list.") 
        elif len(self.features) < 1:
            raise ValueError("At least one feature must be informed in features list.")            

        self.validators = validators
        if not isinstance(self.validators, list):
            raise ValueError("The validators must be a list.") 
        elif len(self.validators) < 1:
            raise ValueError("At least one validator must be informed in validators list.") 

        self.include_timestamp = include_timestamp
        self._include_timestamp = True
        if isinstance(self.include_timestamp, bool):
            if self.include_timestamp:
                self.timestamp = f.current_timestamp()
            else:
                self._include_timestamp = False            
        elif isinstance(self.include_timestamp, str):
            self.timestamp = f.to_timestamp(f.lit(self.include_timestamp))            
        else:
            self.timestamp = self.include_timestamp        

        bins = kwargs.get("bins", False)         
        if isinstance(bins, dict):
            self._bins = {feature: bins.get(feature, False) for feature in features}
        else:            
            self._bins = {feature: bins for feature in features}                                    

        self._feature_profiles = {}
        for feature in self.features: 
            kwargs["feature"] = feature
            kwargs["bins"] = self._bins[feature]
            self._feature_profiles[feature] = SparkFeatureMetricProfile(validators=self.validators, **kwargs)        

    def flat_profile(self, i):
        self.df_flat_profiles = self._feature_profiles[self.features[0]].get_profiles()[i].get_metric_table()
        for feature in self.features[1:]:
            self.df_flat_profiles = self.df_flat_profiles.unionByName(self._feature_profiles[feature].get_profiles()[i].get_metric_table(), allowMissingColumns=True)
        if self._include_timestamp:
            self.df_flat_profiles = self.df_flat_profiles.withColumn("timestamp", self.timestamp)
        return self.df_flat_profiles

    def get_flatten_metrics(self):
        return self.df_flat_metrics

    def flat_metrics(self):
        self.df_flat_metrics = self._feature_profiles[self.features[0]].flat_metrics()
        for feature in self.features[1:]:
            self.df_flat_metrics = self.df_flat_metrics.unionByName(self._feature_profiles[feature].flat_metrics(), allowMissingColumns=True)
        if self._include_timestamp:
            self.df_flat_metrics = self.df_flat_metrics.withColumn("timestamp", self.timestamp)
        return self.df_flat_metrics        

    def fit(self, **kwargs):
        for feature in self.features:
            self._feature_profiles[feature].fit(**kwargs)

    