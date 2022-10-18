import pyspark.sql.functions as f

class SparkFeatureMetricProfile:

    def __init__(self, validators=[], include_timestamp=False, **kwargs):        
        if not isinstance(validators, list):
            raise ValueError("The validators must be a list.") 
        elif len(validators) < 1:
            raise ValueError("At least one validator must be informed in validators list.")         
        self.profile_validators = []
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
        for validator in validators:
            self.profile_validators.append(validator(**kwargs))

    def get_flatten_metrics(self):
        return self.df_flat_metrics

    def get_profiles(self):
        return self.profile_validators

    def flat_metrics(self):
        self.df_flat_metrics = self.profile_validators[0].get_metric()
        for profile_validator in self.profile_validators[1:]:
            self.df_flat_metrics = self.df_flat_metrics.unionByName(profile_validator.get_metric(), allowMissingColumns=True)
        if self._include_timestamp:
            self.df_flat_metrics = self.df_flat_metrics.withColumn("timestamp", self.timestamp)
        return self.df_flat_metrics

    def fit(self, **kwargs):
        for profile_validator in self.profile_validators:
            profile_validator.fit(**kwargs)


