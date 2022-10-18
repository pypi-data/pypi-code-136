from mlops_validators.tables import SparkTrainValidationTable
from mlops_validators.metrics import SparkTwoDistMetrics, TwoDistMetrics
import pyspark.sql.functions as f

class SparkFeaturePopulationStabilityIndex(TwoDistMetrics):
  
    def __init__(self, **kwargs):        
        kwargs["target"] = None        
        self.validator = SparkTrainValidationTable(**kwargs)  
        self.minimal_columns = []         
        self.df_metric = None        

    def __classify_psi(self):
        conditions = f.when(f.col("metric_value") < 0.1, "no change")\
                      .when((f.col("metric_value") >= 0.1) & (f.col("metric_value") <= 0.2), "slight change")\
                      .when(f.col("metric_value") > 0.2, "significant change")\
                      .otherwise("undefined")
        return conditions

    def get_metric_name(self):
        return "SparkFeaturePopulationStabilityIndex"

    def get_metric_table(self, minimal_table=True):
        if minimal_table:            
            return self.df_metric.select(self.minimal_columns)
        else:
            return self.df_metric
    
    def get_metric(self):                 
        psi = self.df_metric.agg(f.sum("psi").alias("metric_value"))            
        psi = psi.withColumn("feature", f.lit(self.validator.feature_A))      
        psi = psi.withColumn("metric_name", f.lit("feature_total_psi"))
        psi = psi.withColumn("result", self.__classify_psi())
        return psi.select(["feature", "metric_name", "metric_value", "result"])
    
    def fit(self, **kwargs):
        kwargs["calculate_percents"] = True
        self.validator.fit(**kwargs)      
        train_label, validation_label = self.validator.get_values_percentage_columns()
        self.df_metric = SparkTwoDistMetrics.psi(self.validator.train_validation_table, train_label, validation_label)         
        self.df_metric = self.df_metric.withColumn("feature", f.lit(self.validator.feature_A))        
        self.minimal_columns = ["feature", self.validator.buckets_label, train_label, validation_label, "psi"]
        return self