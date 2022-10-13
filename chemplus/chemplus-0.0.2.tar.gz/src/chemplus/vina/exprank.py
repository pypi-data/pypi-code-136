import pandas as pd
import numpy as np
from scipy.stats import percentileofscore

def get_exprank_df(df, vina_col="pKd_vina", nn2_col="pKd_nn2", rf4_col="pKd_rf4", reverse=True):
    df = df.copy(deep=True)
    if reverse:
        sign = -1
    else:
        sign = 1
    df["Vina percentile"] = df[vina_col].apply( lambda x: percentileofscore(sign * df[vina_col], sign * x))
    df["NNScore2 percentile"] = df[nn2_col].apply( lambda x: percentileofscore(sign * df[nn2_col], sign * x))
    df["RF-Score4 percentile"] = df[rf4_col].apply( lambda x: percentileofscore(sign * df[rf4_col], sign * x))
    
    sigma_vina = 10
    sigma_rf4 = 10
    sigma_nn2 = 10
    max_rank_regulator = 5
    # 100 / sigma_sf / max_rank_regulator = max_rank
    df["ECR"] = df[["Vina percentile", "NNScore2 percentile", "RF-Score4 percentile"]].apply(lambda x: np.exp(-x[0] / max_rank_regulator /sigma_vina) / sigma_vina + np.exp(-x[1] / max_rank_regulator / sigma_rf4) / sigma_rf4 + np.exp(-x[2] / max_rank_regulator / sigma_nn2) / sigma_nn2, axis=1)
    return df.sort_values(by="ECR", ascending=False).reset_index()#drop=True)