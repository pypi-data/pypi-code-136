from mlops_validators.tables import SparkTrainValidationTable
from mlops_validators.metrics import SparkTwoDistMetrics, TwoDistMetrics
import pyspark.sql.functions as f

class SparkFeatureKullbackLeiblerDivergence(TwoDistMetrics):
  
    def __init__(self, **kwargs):        
        self.shift_distributions = kwargs.get("shift_distributions", False)         
        if not isinstance(self.shift_distributions, bool):
            raise ValueError("The shift_distributions must be a bool.")        
        kwargs["target"] = None        
        self.validator = SparkTrainValidationTable(**kwargs)
        self.minimal_columns = []   
        self.df_metric = None

    def get_metric_name(self):
        return "SparkFeatureKullbackLeiblerDivergence"

    def get_metric_table(self, minimal_table=True):
        if minimal_table:            
            return self.df_metric.select(self.minimal_columns)
        else:
            return self.df_metric
    
    def get_metric(self):      
        kl_div = self.df_metric.agg(f.sum("kl_div").alias("metric_value"))
        kl_div = kl_div.withColumn("feature", f.lit(self.validator.feature_A))
        kl_div = kl_div.withColumn("metric_name", f.lit("feature_total_kl_div"))      
        kl_div = kl_div.withColumn("result", f.lit("undefined"))  
        return kl_div.select(["feature", "metric_name", "metric_value", "result"])           
    
    def fit(self, **kwargs):
        kwargs["calculate_percents"] = True
        self.validator.fit(**kwargs)      
        train_label, validation_label = self.validator.get_values_percentage_columns()
        if self.shift_distributions:
            train_label, validation_label = validation_label, train_label
        self.df_metric = SparkTwoDistMetrics.kl_div(self.validator.train_validation_table, train_label, validation_label)                 
        self.df_metric = self.df_metric.withColumn("feature", f.lit(self.validator.feature_A))        
        self.minimal_columns = ["feature", self.validator.buckets_label, train_label, validation_label, "kl_div"]
        return self