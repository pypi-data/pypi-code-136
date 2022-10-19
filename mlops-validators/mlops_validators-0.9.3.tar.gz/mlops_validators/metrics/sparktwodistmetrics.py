import sys
import pyspark.sql.functions as f
from pyspark.sql.window import Window
from scipy.stats import norm

class SparkTwoDistMetrics:
    
    @classmethod
    def kl_div(self, df, dist_A_label, dist_B_label):
        df = df.withColumn("kl_div", f.col(dist_B_label) * f.log(f.col(dist_B_label) / f.col(dist_A_label)))
        return df

    @classmethod
    def psi(self, df, dist_A_label, dist_B_label):
        df = df.withColumn("psi", (f.col(dist_B_label) - f.col(dist_A_label)) * f.log(f.col(dist_B_label) / f.col(dist_A_label)))
        return df
        
    @classmethod
    def chi2(self, df, dist_A_label, dist_B_label):
        df = df.withColumn("chi2", f.pow(f.col(dist_B_label)-f.col(dist_A_label), 2) / f.col(dist_A_label)) 
        return df    
    
    @classmethod
    def proportion_test(self, df, dist_A_label, dist_B_label, dist_B_total_label, dist_prob=0.95):
        inv_norm = norm.ppf(dist_prob)        
        df = df.withColumn("std", f.sqrt(f.col(dist_A_label) * (1-f.col(dist_A_label))) / f.col(dist_B_total_label))
        df = df.withColumn("interval", inv_norm * f.col("std"))
        df = df.withColumn("lower_band", f.col(dist_A_label) - f.col("interval"))
        df = df.withColumn("upper_band", f.col(dist_A_label) + f.col("interval"))  
        df = df.withColumn("result", f.when(f.col(dist_B_label).between(f.col("lower_band"), f.col("upper_band")), "ok")
                                      .when(f.col(dist_B_label) < f.col("lower_band"), "underestimated")
                                      .when(f.col(dist_B_label) > f.col("upper_band"), "overestimated")
                                      .otherwise("undefined"))
        return df
    
    @classmethod
    def iv(self, df, dist_P_label, dist_N_label):
        df = df.withColumn("rr", f.col(dist_P_label) / f.col(dist_N_label))    
        df = df.withColumn("woe", f.log(f.col("rr")))
        df = df.withColumn("iv", (f.col(dist_P_label) - f.col(dist_N_label)) * f.col("woe")) 
        return df    
    
    @classmethod
    def ks(self, df, dist_A_label, dist_B_label, cumsum_label="_cumsum"):
        dist_A_cumsum = f.sum(df[dist_A_label]).over(Window.partitionBy().orderBy().rowsBetween(-sys.maxsize, 0))
        dist_B_cumsum = f.sum(df[dist_B_label]).over(Window.partitionBy().orderBy().rowsBetween(-sys.maxsize, 0))
        dist_A_label_cumsum = dist_A_label+cumsum_label
        dist_B_label_cumsum = dist_B_label+cumsum_label
        df = df.withColumn(dist_A_label_cumsum, dist_A_cumsum)
        df = df.withColumn(dist_B_label_cumsum, dist_B_cumsum)
        df = df.withColumn("diff", f.abs(f.col(dist_A_label_cumsum)-f.col(dist_B_label_cumsum)))
        return df