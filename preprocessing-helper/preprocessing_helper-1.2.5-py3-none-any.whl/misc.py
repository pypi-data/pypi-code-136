import logging
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
from typing import Any, Callable, List
import re
# List all files in a database
# List all files matching a certain pattern


logger = logging.getLogger("preprocessing_helper")

def flatten_mutli_index(input_df_cols:List)->List:
    """Flattens a hierachichal pandas index

    Args:
        input_df_cols (List): List type object of hierachical indices

    Returns:
        List: Flatten list of indexes where the index names are concatonated 
        by _
    """
    input_df_cols = [re.sub("_$", "", '_'.join(col).strip()) 
                     for col in input_df_cols]
    return input_df_cols
    

def pd_safe_merge(input_df_1:pd.DataFrame, input_df_2:pd.DataFrame, *args, 
                  raise_exception:bool=False, **kwargs)->pd.DataFrame:
    """Wrapper for pandas merge but raises a warning (and optionally an 
    exception) when the row counts have been altered by the merge

    Args:
        input_df_1 (pd.DataFrame): Input dataframe whichh requires merging. 
        This dataframe will be used as the basis for the row counts
        input_df_2 (pd.DataFrame): Input dataframe whichh requires merging. 
        raise_exception (bool, optional): Indicator determining whether an 
        exception should be raised if the row counts don't match. Defaults to 
        False.

    Raises:
        Exception: Raised when the row counts don't match and raise_exception 
        is True

    Returns:
        pd.DataFrame: pandas data frame with input_df_1 and input_df_2 joined
    """
    pre_join_shape = input_df_1.shape[0]
    out_df = pd.merge(input_df_1, input_df_2, *args, **kwargs)
    if pre_join_shape != out_df.shape[0]:
        warn_msg = "Join has altered the shape of input_df_1."
        logger.warning(warn_msg)
        info_msg = "input_df_1 shape: {}, input_df_2 shape: {}, out_df shape: {}".format(
            input_df_1.shape[0], input_df_2.shape[0], out_df.shape[0])
        logger.info(info_msg)
        if raise_exception:
            raise Exception(warn_msg+" "+info_msg)
    else:
        pass
    return out_df


def flatten_lst(input_lst:List[Any], recursive:bool=True)->List[Any]:
    """Function for flattening a list containing lists

    Args:
        input_lst (List[Any]): Input list to flatten
        recursive (bool, optional): If true the function will recursively 
        flatten lists within the input list else only the first layer of lists
        will be flattened. Defaults to True.

    Returns:
        List[Any]: A flattened version of the input_lst
    """
    output_lst = []
    for sub_lst in input_lst:
        if isinstance(sub_lst, list):
            if recursive:
                sub_lst = flatten_lst(sub_lst)
            output_lst = output_lst + sub_lst
        else:
            output_lst.append(sub_lst)
    return output_lst


def pd_agg_percentile(n:int, nan:str="ignore")->Callable:
    """Function to generate percentile values in the pandas aggregate function
    us as follows:
        column.agg([np.sum, np.mean, np.std, np.median,
                     np.var, np.min, np.max, percentile(50), percentile(95)])

    Args:
        n (int): Integer between 0 and 100, defining the percentile of interest
        nan (str, optional): Option to "ignore" nans or "include" nans. If 
        "include" is selected and nans are present, the percentile_ will return 
        nans. Defaults to "ignore".

    Returns:
        Callable: Chosen percentile function, with name based on the percentile 
        of interest. This can then be evaluated in the pandas agg function
    """
    fnk_lkp = {
        "include":np.percentile,
        "ignore":np.nanpercentile
    }
    def percentile_(x):
        return fnk_lkp[nan](x, n)
    percentile_.__name__ = 'percentile_%s' % n
    return percentile_


def get_prop_hist(df_hist:pd.DataFrame, bins:int, grp_var:str, trgt_var:str, 
                  sv_dir=None, sv_nm="", shw_plt=False) -> None:
    """Generates histogram plot of values as proportions

    Args:
        df_hist (pd.DataFrame): Dataframe containing values to aggregate. Must 
        contain at least grp_var and trgt_var columns
        bins (int): Number of bins to use
        grp_var (str): Variable to group over
        trgt_var (str): Variable to aggregate
        sv_dir (_type_, optional): Save directory for the file. 
        Defaults to None.
        sv_nm (str, optional): Additional information for title and file name. 
        Defaults to "".
        shw_plt (bool, optional): Option to display the plot. Defaults to False.
    """
    df_hist["bins"] = pd.cut(df_hist[trgt_var], bins=bins)
    unq_cat_vals = df_hist["bins"].drop_duplicates().sort_values()
    cat_map = {key:value for key, value 
               in zip(unq_cat_vals, range(0, len(unq_cat_vals)))}
    df_hist["bins"] = df_hist["bins"].map(cat_map)
    df_hist_grp = df_hist.groupby(by=[grp_var, "bins"], as_index=False).size()
    df_hist_grp["ttl_size"] = df_hist_grp.groupby(by=[grp_var]).transform("sum")
    df_hist_grp["size"] = df_hist_grp["size"]/df_hist_grp["ttl_size"]
    ttl = "Histogram of {}values split by {}".format(sv_nm, grp_var)
    for i in df_hist_grp[grp_var].unique():
        tmp_df = df_hist_grp[df_hist_grp[grp_var] == i]
        plt.bar(tmp_df["bins"], tmp_df["size"], label=i, alpha=0.5)
    plt.legend()
    plt.title(ttl)
    if sv_dir:
        plt.savefig(os.path.join(sv_dir, ttl))
    if shw_plt:
        plt.show()

def pd_col_opt_slct(df:pd.DataFrame, sub_str_lst:List[str])->List[str]:
    """Function to select columns from a pandas dataframe based on whether they 
    contain one of the substrings found in the list sub_str_lst

    Args:
        df (pd.DataFrame): Dataframe over which to select columns
        sub_str_lst (List[str]): List of substrings to look for

    Returns:
        List[str]: List of column names containing one of the substrings found
        in the list sub_str_lst
    """
    sub_str_regex = "|".join(sub_str_lst)
    slct_cols = list(df.columns[df.columns.str.contains(sub_str_regex)])
    return slct_cols