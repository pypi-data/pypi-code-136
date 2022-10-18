import numpy as np
from scipy.stats import norm

class PandasTwoDistMetrics:

    @classmethod
    def kl_div(self, df, dist_A_label, dist_B_label):
        df["kl_div"] = df[dist_B_label] / np.log(df[dist_B_label] / df[dist_A_label])
        df.replace([np.inf, -np.inf], np.nan, inplace=True)
        return df
    
    @classmethod
    def psi(self, df, dist_A_label, dist_B_label):
        df["psi"] = (df[dist_B_label] - df[dist_A_label]) * np.log(df[dist_B_label] / df[dist_A_label])
        df.replace([np.inf, -np.inf], np.nan, inplace=True)
        return df
    
    @classmethod
    def chi2(self, df, dist_A_label, dist_B_label):
        df["chi2"] = np.power(df[dist_B_label] - df[dist_A_label], 2) / df[dist_A_label]
        df.replace([np.inf, -np.inf], np.nan, inplace=True)
        return df 
    
    @classmethod
    def proportion_test(self, df, dist_A_label, dist_B_label, dist_B_total_label, dist_prob=0.95):
        inv_norm = norm.ppf(dist_prob)
        df["std"] = np.sqrt(df[dist_A_label] * (1-df[dist_A_label]))/ df[dist_B_total_label]      
        df["interval"] = inv_norm * df["std"]
        df["lower_band"] = df[dist_A_label] - df["interval"]
        df["upper_band"] = df[dist_A_label] + df["interval"]  
        df["result"] = df[dist_B_label].where(df[dist_B_label].between(df["lower_band"], df["upper_band"]), "ok",
                                  df[dist_B_label].where(df[dist_B_label] < df["lower_band"], "underestimated",
                                  df[dist_B_label].where(df[dist_B_label] > df["upper_band"], "overestimated", "undefined")))
        df.replace([np.inf, -np.inf], np.nan, inplace=True)
        return df
    
    @classmethod
    def iv(self, df, dist_P_label, dist_N_label):
        df["rr"] = df[dist_P_label] / df[dist_N_label]
        df["woe"] = np.log(df["rr"])
        df["iv"] = (df[dist_P_label] - df[dist_N_label]) * df["woe"] 
        df.replace([np.inf, -np.inf], np.nan, inplace=True)
        return df    
    
    @classmethod
    def ks(self, df, dist_A_label, dist_B_label, cumsum_label="_cumsum"):
        dist_A_cumsum = df[dist_A_label].cumsum()
        dist_B_cumsum = df[dist_B_label].cumsum()
        dist_A_label_cumsum = dist_A_label+cumsum_label
        dist_B_label_cumsum = dist_B_label+cumsum_label
        df[dist_A_label_cumsum] = dist_A_cumsum
        df[dist_B_label_cumsum] = dist_B_cumsum
        df["diff"] = np.abs(df[dist_A_label_cumsum] - df[dist_B_label_cumsum])
        df.replace([np.inf, -np.inf], np.nan, inplace=True)
        return df