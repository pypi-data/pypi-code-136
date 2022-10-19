from mlops_validators.tables import SparkValidationTable
from mlops_validators.metrics import SparkTwoDistMetrics, TwoDistMetrics
import pyspark.sql.functions as f

class SparkFeatureInformationValue(TwoDistMetrics):  
    
    def __init__(self, **kwargs):            
        self.pos_value = kwargs.get("pos_value", "1")
        self.neg_value = kwargs.get("neg_value", "0")                
        if not isinstance(self.pos_value, str):
            raise ValueError("The pos_value must be a string.")
        if not isinstance(self.neg_value, str):
            raise ValueError("The neg_value must be a string.")                     
        kwargs["df"] = kwargs.get("df_validation", None)
        kwargs["feature_A"] = kwargs.get("feature", None)
        kwargs["feature_B"] = kwargs.get("target", None)
        kwargs["feature_B_remove_missing"] = True        
        self.validator = SparkValidationTable(**kwargs)        
        self.minimal_columns = []
        self.df_metric = None    

    def __classify_iv(self):
        conditions = f.when(f.col("metric_value") < 0.02, "not useful")\
                      .when((f.col("metric_value") >= 0.02) & (f.col("metric_value") <= 0.1), "weak")\
                      .when((f.col("metric_value") > 0.1) & (f.col("metric_value") <= 0.3), "medium")\
                      .when((f.col("metric_value") > 0.3) & (f.col("metric_value") <= 0.5), "strong")\
                      .when(f.col("metric_value") > 0.5, "suspicious")\
                      .otherwise("undefined")
        return conditions
    
    def get_metric_name(self):
        return "SparkFeatureInformationValue"

    def get_metric_table(self, minimal_table=True):
        if minimal_table:            
            return self.df_metric.select(self.minimal_columns)
        else:
            return self.df_metric    
    
    def get_metric(self):      
        iv = self.df_metric.agg(f.sum("iv").alias("metric_value"))              
        iv = iv.withColumn("feature", f.lit(self.validator.feature_A))      
        iv = iv.withColumn("metric_name", f.lit("feature_total_iv"))
        iv = iv.withColumn("result", self.__classify_iv())
        return iv.select(["feature", "metric_name", "metric_value", "result"])
    
    def fit(self, **kwargs):  
        kwargs["calculate_percents"] = True
        self.validator.fit(**kwargs)        
        pos_label = self.validator.map_percentage_columns[self.pos_value]
        neg_label = self.validator.map_percentage_columns[self.neg_value]        
        self.df_metric = SparkTwoDistMetrics.iv(self.validator.frequency_table, pos_label, neg_label)     
        self.df_metric = self.df_metric.withColumn("feature", f.lit(self.validator.feature_A))        
        self.minimal_columns = ["feature", self.validator.buckets_label, pos_label, neg_label, "rr", "woe", "iv"]
        return self 