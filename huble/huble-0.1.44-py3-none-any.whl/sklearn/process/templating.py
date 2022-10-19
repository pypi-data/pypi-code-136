def return_function(node):
    if node["data"]["value"] == "Remove NAN values":
        return remove_nan_values(node['data']['parameters'])
    elif node["data"]["value"] == "Replace NAN values":
        return replace_nan_values(node['data']['parameters'])
    elif node["data"]["value"] == "Dropping rows or columns":
        return drop_rows_columns(node['data']['parameters'])
    elif node["data"]["value"] == "Remove Outliers":
        return remove_outliers(node['data']['parameters'])
    elif node["data"]["value"] == "Drop Duplicates":
        return drop_duplicates(node['data']['parameters'])
    elif node["data"]["value"] == "Change Data Type":
        return change_data_type(node['data']['parameters'])
    elif node["data"]["value"] == "Round Data":
        return round_data(node['data']['parameters'])
    elif node["data"]["value"] == "Filter DataFrame":
        return filter_dataframe(node['data']['parameters'])
    elif node["data"]["value"] == "Truncate DataFrame":
        return truncate_dataframe(node['data']['parameters'])
    elif node["data"]["value"] == "Sort Values":
        return sort_values(node['data']['parameters'])
    elif node["data"]["value"] == "Transpose DataFrame":
        return transpose()
    elif node["data"]["value"] == "Min Max Scaler":
        return min_max_scale(node['data']['parameters'])
    elif node["data"]["value"] == "Max Abs Scaler":
        return max_abs_scale(node['data']['parameters'])
    elif node["data"]["value"] == "Robust Scaler":
        return robust_scale(node['data']['parameters'])
    elif node["data"]["value"] == "Standard Scaler":
        return standard_scale(node['data']['parameters'])
    elif node["data"]["value"] == "Normalization":
        return normalize(node['data']['parameters'])
    elif node["data"]["value"] == "Ordinal Encoding":
        return ordinal_encode(node['data']['parameters'])
    elif node["data"]["value"] == "One Hot Encoding":
        return one_hot_encode(node['data']['parameters'])

def remove_nan_values(params):
    subset=[]
    for i in range(len(params['subset'])):
        subset.append(params['subset'][i]['value'])
    parameters = {
        "axis": params["axis"],
        "how": params["how"],
        "inplace": params["inplace"],
        "subset": subset,
    }
    return f"data = huble.sklearn.remove_nan_values(data=data,parameters={parameters})"


def replace_nan_values(params):
    parameters = {
        "missing_values" : params['missing_values'], 
        "strategy" : params['strategy'],
        "fill_value" : params['fill_value'],
    }
    return f"data = huble.sklearn.replace_nan_values(data=data, column='{params['column']}', parameters={parameters})"

def drop_rows_columns(params):
    labels=[]
    for i in range(len(params['labels'])):
        labels.append(params['labels'][i]['value'])

    parameters = {
        "labels" : labels,
        "axis" : params['axis'],
        "inplace" : params['inplace'],
        "errors" : params['errors'],
    }
    return f"data = huble.sklearn.drop_rows_columns(data=data,parameters={parameters})"

def remove_outliers(params):
    return f"data = huble.sklearn.remove_outliers(data=data,columns='{params['columns']}')"

def drop_duplicates(params):
    subset=[]
    for i in range(len(params['subset'])):
        subset.append(params['subset'][i]['value'])
    parameters = {
        "subset" : subset, 
        "keep" : params['keep'],
        "inplace" : params['inplace'],
        "ignore_index" : params['ignore_index'],
    }
    return f"data = huble.sklearn.drop_duplicates(data=data,parameters={parameters})"


def change_data_type(params):
    parameters = {
        "dtype" : params['data type'], 
        "copy" : params['copy'], 
        "errors" : params['errors'],
    }
    return f"data = huble.sklearn.change_data_type(data=data,column={params['column']}, parameters={parameters})"


def round_data(params):
    parameters = {
        "decimals" : params['decimals'],
    }
    return f"data = huble.sklearn.round_data(data=data, parameters={parameters})"


def filter_dataframe(params):
    items=[]
    for i in range(len(params['items'])):
        items.append(params['items'][i]['value'])
    parameters = {
        "items" : items,
        "like" : params['like'],
        "axis" : params['axis'],
    }
    return f"data = huble.sklearn.filter_dataframe(data=data, parameters={parameters})"


def truncate_dataframe(params):
    parameters = {
        "before" : params['before'], 
        "after" : params['after'], 
        "copy" : params['copy'], 
        "axis" : params['axis'],
    }
    return f"data = huble.sklearn.truncate_datfarame(data=data, parameters={parameters})"


def sort_values(params):
    by=[]
    for i in range(len(params['by'])):
        by.append(params['by'][i]['value'])
    parameters = {
        "by" : by,
        "axis" : params['axis'],
        "ascending" : params['ascending'],
        "inplace" : params['inplace'],
        "kind" : params['kind'],
        "na_position" : params['na_position'],
        "ignore_index" : params['ignore_index'],
    }
    return f"data = huble.sklearn.sort_values(data=data, parameters={parameters})"


def transpose():
    return f"data = huble.sklearn.transpose(data=data)"


def min_max_scale(params):
    parameters = {
        "feature_range" : params['feature_range'], 
        "copy" : params['copy'], 
        "clip" : params['clip'],
    }
    return f"data = huble.sklearn.min_max_scalar(data=data, columns={params['columns']}, parameters={parameters})"


def max_abs_scale(params):
    parameters = {
        "copy" : params['copy'],
    }
    return f"data = huble.sklearn.max_abs_scalar(data=data, columns={params['columns']}, parameters={parameters})"


def robust_scale(params):
    columns=[]
    for i in range(len(params['column'])):
        columns.append(params['column'][i]['value'])
    parameters = {
        "with_centering" : params['with_centering'], 
        "with_scaling" : params['with_scaling'], 
        "copy" : params['copy'], 
        "unit_variance" : params['unit_variance'], 
        "quantile_range" : params['quantile_range'],
    }
    return f"data = huble.sklearn.robust_scalar(data=data, column={columns}, parameters={parameters})"


def standard_scale(params):
    parameters = {
        "copy" : params['copy'], 
        "with_mean" : params['with_mean'], 
        "with_std" : params['with_std'],
    }
    return f"data = huble.sklearn.standard_scalar(data=data, column={params['column']}, parameters={parameters})"


def normalize(params):
    parameters = {
        "X" : params['column'], 
        "norm" : params['norm'], 
        "copy" : params['copy'],
    }
    return f"data = huble.sklearn.normalize(data=data, parameters={parameters})"


def ordinal_encode(params):
    columns=[]
    for i in range(len(params['columns'])):
        columns.append(params['columns'][i]['value'])
    parameters = {
        "categories" : params['categories'], 
        "dtype" : params['dtype'], 
        "handle_unknown" : params['handle_unknown'], 
        "unknown_value" : params['unknown_value'], 
        "encoded_missing_value" : params['encoded_missing_value'],
    }
    return f"data = huble.sklearn.ordinal_encode(data=data, columns={columns}, parameters={parameters})"


def one_hot_encode(params):
    columns=[]
    for i in range(len(params['columns'])):
        columns.append(params['columns'][i]['value'])
    parameters = {
        "categories" : params['categories'], 
        "dtype" : params['dtype'], 
        "handle_unknown" : params['handle_unknown'], 
        "sparse" : params['sparse'], 
        "min_frequency" : params['min_frequency'], 
        "max_categories" : params['max_categories'],
    }
    return f"data = huble.sklearn.one_hot_encode(data=data, columns={columns}, parameters={parameters})"
