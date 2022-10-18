import pandas as pd

from pyplattsapi import plattsapicore

api_name = "WORLD REFINERY DATABASE"
runs_api = f"{plattsapicore.api_url}/odata/refinery-data/v2/Runs"


def get_runs(filter:str, field:str=None, groupBy:str=None):
    params = {
        "$filter": filter,
        "pageSize": 1000,
        "groupBy": groupBy,

    }
    res = plattsapicore.generic_odata_call(api=runs_api, api_name=api_name, params=params)

    qmap = { 1: 1, 2: 4, 3: 7, 4: 10 }
    res.index = res.apply(lambda x: pd.to_datetime(f"{x.Year}-{qmap.get(x.Quarter)}-1"), 1)
    res.index.name = "date"
    return res



#
# def getMarginsbyType(type: str):
#     Historical_data_URL = f"https://api.platts.com/odata/refinery-data/v2/Margins?&pageSize=1000&$expand=*"
#     df5 = pd.DataFrame()
#     while Historical_data_URL != "NaN":
#         time.sleep(1)  # api can only accept 2 requests per second and 5000 per day
#         data_request = requests.get(url=f"{Historical_data_URL}", headers=Headers_ref)
#         data = data_request.json()
#         df2 = pd.json_normalize(data).reset_index(drop=True)
#         x = df2["value"].iloc[0]
#         df3 = pd.json_normalize(x).reset_index(drop=True)
#         df3 = df3.drop_duplicates()
#         df5 = df5.append(df3, ignore_index=False)
#         try:
#             Historical_data_URL = df2[f"@odata.nextLink"].iloc[0]
#         except:
#             Historical_data_URL = "NaN"
#             continue
#     df5 = df5[df5["MarginType.Name"] == type]
#     df5 = df5.reset_index()
#     return df5
#
#
# def getCountryCapacityChangesTimeSeries(country: str):
#     Historical_data_URL = f"https://api.platts.com/odata/refinery-data/v2/capacity?$select=*&$expand=*&pageSize=1000&$filter=Refinery/Country/Name eq '{country}'"
#     df5 = pd.DataFrame()
#     while Historical_data_URL != "NaN":
#         time.sleep(1)  # api can only accept 2 requests per second and 5000 per day
#         data_request = requests.get(url=f"{Historical_data_URL}", headers=Headers_sup)
#         data = data_request.json()
#         df2 = pd.json_normalize(data).reset_index(drop=True)
#         x = df2["value"].iloc[0]
#         df3 = pd.json_normalize(x).reset_index(drop=True)
#         df3 = df3.drop_duplicates()
#         df3["Date"] = df3[["Year", "Quarter"]].apply(
#             lambda row: "-Q".join(row.values.astype(str)), axis=1
#         )
#         df4 = df3[["Refinery.Name", "Mbcd", "Mmtcd", "Mmtcy", "Date"]]
#         df4 = df4.groupby(["Date", "Refinery.Name"]).sum()
#         df4 = df4.reset_index()
#         df4["Date"] = pd.to_datetime(df4["Date"])
#         df5 = df5.append(df4, ignore_index=False)
#         try:
#             Historical_data_URL = df2[f"@odata.nextLink"].iloc[0]
#         except:
#             Historical_data_URL = "NaN"
#             continue
#     df4.columns = ["Date", "Refinery", "Mbdc", "Mmtcd", "Mmtcy"]
#     df5 = df4.groupby(["Date"]).sum()
#     df6 = df5.reset_index()
#     return df6
