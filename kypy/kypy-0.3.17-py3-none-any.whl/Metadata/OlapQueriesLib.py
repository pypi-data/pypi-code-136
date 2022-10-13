"""
At this time (11/2021), it doesn't seem like Kyvos' ODBC interace implements:

pyodbc.columns(table='iowa_liquor_sales')
pyodbc.foreignKeys

Both of those

But the XMLA export has more information required for OLAPy stuff anyway.
"""
from pandas.core.frame import DataFrame
import pandas as pd
import os

from .. import KyvosLib as ky # Import from parent directory.


group_by_columns = {
    "hash":{"Type":"string"},
    "cube":{"Type":"string"},
    "server":{"Type":"string"},
    "schema":{"Type":"string"},
    "attribute":{"Type":"string"},
    "repr":{"Type":"string"}
}

measures_columns = {
    "hash":{"Type":"string"},
    "cube":{"Type":"string"},
    "server":{"Type":"string"},
    "schema":{"Type":"string"},
    "metric":{"Type":"string"},
    "alias":{"Type":"string"},
    "class":{"Type":"string"},
    "repr":{"Type":"string"}
}

where_columns = {
    "hash":{"Type":"string"},
    "cube":{"Type":"string"},
    "server":{"Type":"string"},
    "schema":{"Type":"string"},
    "attribute":{"Type":"string"},
    "alias":{"Type":"string"},
    "value":{"Type":"string"},
    "class":{"Type":"string"},
    "repr":{"Type":"string"}
}

metadata_dir = ky.EnvVar.get_var("KYVOS_OLAP_QUERIES")
query_def_ext = ".json"

def olap_queries():
    """ Return an aggregated lists of saves OlapQueryDef objects.

    Returns a DataFrame each for measures, where, and group_by
    """


    querylist = [
        f.replace(query_def_ext,"") 
        for f in os.listdir(metadata_dir) 
        if f.endswith(query_def_ext)
    ]

    def row_template(obj)->dict:
        return {"hash":qd.hash,"class":obj.class_name if hasattr(itm,"class_name") else None,"schema":qd.cube.cubeSchema,"server":qd.cube.dsn,"cube":qd.cube.cubeName,"repr":repr(obj)}

    dfmeasures = pd.DataFrame(columns=list(measures_columns.keys()))
    dfwhere = pd.DataFrame(columns=list(where_columns.keys()))
    dfgroup_by = pd.DataFrame(columns=list(group_by_columns.keys()))
    for qd_name in querylist:
        print(qd_name)
        qd = ky.OlapQueryDef.load_from_JSON(qd_name)
        for itm in qd.measure_array:
            row = row_template(itm)
            row.update({"metric":itm.metric if hasattr(itm,"metric") else None})
            row.update({"alias":itm.alias if hasattr(itm,"alias") else None})
            dfmeasures = dfmeasures.append(row, ignore_index=True)
            
        for itm in qd.where_array:
            row = row_template(itm)
            row.update({"attribute":itm.attribute if hasattr(itm,"attribute") else None})
            row.update({"value":itm.value if hasattr(itm,"value") else None})
            row.update({"alias":itm.alias if hasattr(itm,"alias") else None})
            dfwhere = dfwhere.append(row, ignore_index=True)

        for itm in qd.group_by_array:
            row = row_template(itm)
            row.update({"attribute":itm})
            dfgroup_by = dfgroup_by.append(row, ignore_index=True)
            
    return (dfmeasures, dfwhere,dfgroup_by)


