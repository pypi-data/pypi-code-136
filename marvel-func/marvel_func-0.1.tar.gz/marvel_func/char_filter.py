# filter_func function is used to filter out required characters from dataframe according to filter condition
# filter_func requires dataframe of marvel_characters as an argument

class filter:

    def filter_func(self, df):
        column_name = input(
            "Enter valid column name of dataframe from (char_id,events, series, stories, comics):")
        op_type = int(
            input("Enter operation type ( 1 -'>',2-'<',3-'==',4- '>=',5- '<='):"))
        value = int(input("Enter value for the filter:"))
        filter_data = {
            1: lambda df, column_name, value: df[df[column_name] > value],
            2: lambda df, column_name, value: df[df[column_name] < value],
            3: lambda df, column_name, value: df[df[column_name] == value],
            4: lambda df, column_name, value: df[df[column_name] >= value],
            5: lambda df, column_name, value: df[df[column_name] <= value]
        }
        return filter_data[op_type](df, column_name, value)

# filter_func returns filtered dataframe of marvel characters
