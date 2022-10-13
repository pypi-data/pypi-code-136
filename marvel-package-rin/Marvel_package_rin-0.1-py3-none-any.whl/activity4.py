def filter_func(df, col_name, filter_cond, value):
    col_name = str(col_name)
    value = int(value)
    if filter_cond == 'g':
        print(df[df[col_name] > value])
    elif filter_cond == 'l':
         print(df[df[col_name] < value])
    else:
        print(df[df[col_name] == value])