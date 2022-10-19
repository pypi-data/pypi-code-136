from mlops_validators.tables import SparkTrainValidationTable
from mlops_validators.metrics import SparkTwoDistMetrics, TwoDistMetrics
import matplotlib.pyplot as plt
import pyspark.sql.functions as f

class SparkFeatureChi2Statistic(TwoDistMetrics):
        
    def __init__(self, **kwargs):
        kwargs["target"] = None        
        self.validator = SparkTrainValidationTable(**kwargs)        
        self.minimal_columns = []

    @classmethod
    def print_formula(self):    
        formula = r'\chi^2 = \sum_{{i = 1}}^{{n}}\frac{{({0}^i-{1}^i)^2}}{{{0}^i}}'.format("x_{t}", "x_{v}")
        ax = plt.axes() 
        ax.set_xticks([])
        ax.set_yticks([])
        plt.text(0.3, 0.4,'$%s$' %formula, size=30);    

    def get_metric_name(self):
        return "SparkFeatureChi2Statistic"

    def get_metric_table(self, minimal_table=True):                
        if minimal_table:            
            return self.df_metric.select(self.minimal_columns)
        else:
            return self.df_metric
    
    def get_metric(self):                
        chi2 = self.df_metric.agg(f.sum("chi2").alias("metric_value"))        
        chi2 = chi2.withColumn("feature", f.lit(self.validator.feature_A))
        chi2 = chi2.withColumn("metric_name", f.lit("feature_chi2_statistic"))      
        chi2 = chi2.withColumn("result", f.lit("undefined"))  
        return chi2.select(["feature", "metric_name", "metric_value", "result"])
    
    def fit(self, **kwargs):
        kwargs["calculate_percents"] = True
        self.validator.fit(**kwargs)                                                       
        train_label, validation_label = self.validator.get_values_percentage_columns()        
        self.df_metric = SparkTwoDistMetrics.chi2(self.validator.train_validation_table, train_label, validation_label)            
        self.df_metric = self.df_metric.withColumn("feature", f.lit(self.validator.feature_A))         
        self.minimal_columns = ["feature", self.validator.buckets_label, train_label, validation_label, "chi2"]           
        return self  