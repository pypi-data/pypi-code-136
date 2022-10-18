from mlops_validators.metrics import SparkTwoDistMetrics, TwoDistMetrics
from mlops_validators.tables import SparkValidationTable
import pyspark.sql.functions as f

class SparkTargetKolmogorovSmirnovStatistic(TwoDistMetrics):
    
    def __init__(self, **kwargs):        
        self.cumsum_label =  kwargs.get("cumsum_label", "_cumsum")                
        if not isinstance(self.cumsum_label, str):
            raise ValueError("The cumsum_label must be a string.")        
        kwargs["df"] = kwargs.get("df_validation", None)                     
        kwargs["feature_A"] = kwargs.get("feature", None)                     
        kwargs["feature_B"] = kwargs.get("target", None) 
        kwargs["feature_B_remove_missing"] = True        
        self.validator = SparkValidationTable(**kwargs)      
        self.minimal_columns = []                                                     
        self.df_metric = None            

    def __classify_ks_statistic(self):
        conditions = f.when((f.col("metric_value") >= 0) & (f.col("metric_value") <= 0.2), "low")\
                      .when((f.col("metric_value") > 0.2) & (f.col("metric_value") <= 0.3), "low")\
                      .when((f.col("metric_value") > 0.3) & (f.col("metric_value") <= 0.4), "low")\
                      .when((f.col("metric_value") > 0.4) & (f.col("metric_value") <= 0.5), "acceptable")\
                      .when((f.col("metric_value") > 0.5) & (f.col("metric_value") <= 0.6), "good")\
                      .when((f.col("metric_value") > 0.6) & (f.col("metric_value") <= 0.7), "very good")\
                      .when((f.col("metric_value") > 0.7) & (f.col("metric_value") <= 1), "suspicious")\
                      .otherwise("undefined")
        return conditions

    def get_metric_name(self):
        return "SparkTargetKolmogorovSmirnovStatistic"

    def get_metric_table(self, minimal_table=True):
        if minimal_table:            
            return self.df_metric.select(self.minimal_columns)
        else:
            return self.df_metric
        
    def get_metric(self):           
        ks = self.df_metric.agg(f.max("diff").alias("metric_value"))            
        ks = ks.withColumn("feature", f.lit(self.validator.feature_A))      
        ks = ks.withColumn("metric_name", f.lit("target_ks_statistic"))
        ks = ks.withColumn("result", self.__classify_ks_statistic())
        return ks.select(["feature", "metric_name", "metric_value", "result"])     
    
    def fit(self, **kwargs):
        kwargs["calculate_percents"] = True
        self.validator.fit(**kwargs)        
        dist_labels = self.validator.get_values_percentage_columns()                                     
        dist_A_label, dist_B_label = dist_labels[0], dist_labels[1]
        self.df_metric = SparkTwoDistMetrics.ks(self.validator.get_frequency_table(), dist_A_label, dist_B_label, cumsum_label=self.cumsum_label)                
        self.df_metric = self.df_metric.withColumn("feature", f.lit(self.validator.feature_A))        
        self.minimal_columns = ["feature", self.validator.buckets_label, dist_A_label, dist_B_label, "diff"]
        return self