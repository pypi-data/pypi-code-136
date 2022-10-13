import clr
import pandas as pd

clr.AddReference('System.Data')

from System import Data, Decimal
from System.Data import DataSet
from System.Data import DataTable
from System.Data import DataColumn
from System.Data import DataRow

def TableToDataFrame(dt):
    ''' Convert DataTable type to DataFrame type '''
    colTempCount = 0
    dic = {}
    while (colTempCount < dt.Columns.Count):
        li = []
        rowTempCount = 0
        column = dt.Columns[colTempCount]
        colName = column.ColumnName
        typeName = column.DataType.Name
        while (rowTempCount < dt.Rows.Count):
            result = dt.Rows[rowTempCount][colTempCount]
            if typeName == 'Decimal':
                li.append(Decimal.ToDouble(result))
            else:
                li.append(result)
            rowTempCount = rowTempCount + 1

        colTempCount = colTempCount + 1
        dic.setdefault(colName, li)

    df = pd.DataFrame(dic)
    return (df)

    def DataFrameToDic(df):
        ''' Convert DataFrame data type to dictionary type '''
        dic = df.to_dict(' list ' )
        return dic