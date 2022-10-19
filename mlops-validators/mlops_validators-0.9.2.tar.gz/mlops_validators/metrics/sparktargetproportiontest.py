from mlops_validators.tables import SparkTrainValidationTable
from mlops_validators.metrics import SparkTwoDistMetrics, TwoDistMetrics
import pyspark.sql.functions as f

class SparkTargetProportionTest(TwoDistMetrics):
    
    def __init__(self, **kwargs):                                   
        self.target_value = kwargs.get("target_value", "1")
        self.dist_prob = kwargs.get("dist_prob", 0.95)        
        if not isinstance(self.target_value, str):
            raise ValueError("The target_value must be a string.")
        if not isinstance(self.dist_prob, float):
            raise ValueError("The dist_prob must be a float.")            
        kwargs["feature_B_remove_missing"] = True                    
        self.validator = SparkTrainValidationTable(**kwargs)     
        self.minimal_columns = []                                      
        self.df_metric = None        

    def get_metric_name(self):
        return "SparkTargetProportionTest"

    def get_metric_table(self, minimal_table=True):        
        if minimal_table:            
            return self.df_metric.select(self.minimal_columns)
        else: 
            return self.df_metric        
    
    def get_metric(self): 
        prop_test = self.df_metric.agg(f.count(f.when(f.col("result") != "ok", 1).otherwise(0)).alias("metric_value"))              
        prop_test = prop_test.withColumn("feature", f.lit(self.validator.feature_A))      
        prop_test = prop_test.withColumn("metric_name", f.lit("target_proportion_test"))          
        prop_test = prop_test.withColumn("result", f.when(f.col("metric_value") > 0, "fail").otherwise("pass") )
        return prop_test.select(["feature", "metric_name", "metric_value", "result"])

    def fit(self, **kwargs):
        kwargs["calculate_proportions"] = True
        self.validator.fit(**kwargs)                            
        train_label = self.validator.map_proportion_columns[self.target_value]
        validation_label = self.validator.validation_table.map_proportion_columns[self.target_value]      
        self.df_metric = SparkTwoDistMetrics.proportion_test(self.validator.train_validation_table, train_label, validation_label, 
                                                             self.validator.validation_totals_label, dist_prob=self.dist_prob)       
        self.df_metric = self.df_metric.withColumn("feature", f.lit(self.validator.feature_A))        
        self.minimal_columns = ["feature", self.validator.buckets_label, train_label, validation_label, "result"]
        return self
 