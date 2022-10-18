#%% load module
import sys
sys.path.append(r"D:\az_git_folder\azdsdr\src")

#%% 
from azdsdr.readers import DremioReader
username    = "anzhu@microsoft.com"
token       = "deXyT5YhSQS5d74OfHsfpv+VOAwCkn2giWJbBmCODba8mxbfB5S4P0+oGcZxMQ=="
dr          = DremioReader(username=username,token=token)

dr = DremioReader(username=username,token=token)

#%% run another test
query_sql   = """SELECT * FROM Azure.PPE."vw_customer_azure_monthlyusage " LIMIT 10"""
r           = dr.run_sql(query_sql)
display(r)

#%% 
sql = '''
select 
    * 
from 
    BizApps.PROD."vw_customer_powerapps_portalusage"
limit 10
'''
r = dr.run_sql(sql)
display(r)

#%% test Kusto Reader
from azdsdr.readers import KustoReader

cluster = "https://cgadataout.kusto.windows.net"
db      = "AIPDD_Usage"
kr = KustoReader(cluster=cluster,db=db)

#%% 
kql = '''
cluster('Cgadataout').database('Starlight').FACT_ACR_Publish
| where 1==1
    and DIM_DateId < 20220901
    and DIM_DateId > 20210701
    and DIM_ACRAdjustmentTypeId == -686078934765504679
| summarize  
    ACR_sum = round(sum(ACR),0)
    by DIM_DateId
| order by DIM_DateId asc
'''
r = kr.run_kql(kql)
display(r)
r.plot()

#%% public sample 
from azdsdr.readers import KustoReader

cluster = "https://help.kusto.windows.net"
db      = "Samples"
kr = KustoReader(cluster=cluster,db=db)

#%% 
kql = "StormEvents | take 10"
r = kr.run_kql(kql)
display(r)

#%% test scope
# cosmos wiki: https://mscosmos.visualstudio.com/CosmosWiki/_wiki/wikis/Cosmos.wiki/3095/Pyscope-Code-Sample
import sys
sys.path.append(r"F:\az_git_folder\azdsdr\src")
from azdsdr.readers import CosmosReader

scope_exe_path      = r"D:\tools\ScopeSDK\Scope.exe"
scope_script        = "pa_daily_makers.script"
vc_path             = r"vc://cosmos11/AzureInsights.analytics"
account             = r"anzhu@microsoft.com"

cr                  = CosmosReader(scope_exe_path,account,vc_path)

#%% cosmos delete file test
file_path = "/users/anzhu/scope_query_temp.ss"
cr.delete_file_from_cosmos(file_path)

#%% run scope script
output_str = cr.run_scope(scope_script)
cr.check_job_status(output_str)

#%% download file from cosmos
source = "/users/anzhu/daily_makers.ss"
target = "./data/daily_makers.csv"

cr.download_file_as_csv(source,target)

#%% 
u_sql = '''
// Module references        
MODULE @"/shares/AzureAnalytics.Prod/Sdk/AzureAnalytics1.5.module" AS AzureAnalytics;   // Production location
   
#DECLARE cloudName                   string   = "public";
#DECLARE WorkloadEnvironment         string   = "Prod";

#DECLARE startDateTime string = "2022-09-07T00:00:00"; //DateTime.Parse("2020/09/25"); 
#DECLARE endDateTime string = "2022-09-13T00:00:00"; //DateTime.Parse("2020/09/26"); 

// Set the user details version. 
// This is the suffix added to the PowerApps.Telemetry.ActiveDailyUserDetailsV# (where # is the userDetailsVersion) 
// When the details version changes, just change it here!
#DECLARE userDetailsVersion string = "2";

#IF (@WorkloadEnvironment != "Prod")   
    #DECLARE prefixEntity string = @WorkloadEnvironment;
#ELSE
    #DECLARE prefixEntity string = "";
#ENDIF

#IF (@cloudName.ToLower() != "public")   // This is only for the current rest of world. When RoW migrates to Blueshift then the code will always be: prefixEntity = @prefixEntity+"."+ @cloudName;
    #IF (@prefixEntity != "")
    	#SET prefixEntity = @prefixEntity+"."+ @cloudName;
    #ELSE
    	#SET prefixEntity = @cloudName;
    #ENDIF
#ENDIF 

#IF (@prefixEntity != "")
        #DECLARE dailyActiveUserDetailsInputEntity string  = @prefixEntity+".PowerApps.Telemetry.ActiveDailyUserDetailsV" + @userDetailsVersion;   
#ELSE
        #DECLARE dailyActiveUserDetailsInputEntity string  = "PowerApps.Telemetry.ActiveDailyUserDetailsV" + @userDetailsVersion;
#ENDIF
        
AzureAnalytics.Initialize(entity = @dailyActiveUserDetailsInputEntity); 

curr_activeUser =    
    SELECT 
        TOP 10000
         activeUserDate     AS activeUserDate
        ,TenantID           AS TenantID
        ,TenantCountryCode  AS TenantCountryCode
        ,UserID             AS UserID
        ,UserIDType         AS UserIDType
        ,clientSessionId    AS clientSessionId
        ,eventPersona       AS eventPersona
        ,applicationType    AS applicationType
        ,userLicense        AS userLicense                
        ,applicationId      AS applicationId
        ,DeviceType         AS DeviceType
        ,deviceMake         AS deviceMake
        ,browserName        AS browserName
        ,OSType             AS OSType  
        ,JoinDate           AS JoinDate
        FROM 
        (AzureAnalytics.LoadStream
            (
                 startDateTime  = @startDateTime
                ,endDateTime    = @endDateTime
                ,entity         = @dailyActiveUserDetailsInputEntity
            )
        );

OUTPUT curr_activeUser
TO SSTREAM @output;
'''
r = cr.scope_query(scope_script=u_sql)
display(r)


#%% kusto ingest
import sys
sys.path.append(r"F:\az_git_folder\azdsdr\src")
import azdsdr.readers as dsdr
import importlib
importlib.reload(dsdr)
from azdsdr.readers import KustoReader

cluster         = "https://cgadataout.kusto.windows.net"
db              = "CGAWorkArea"
ingest_cluster  = r"https://ingest-cgadataout.kusto.windows.net"
kr              = KustoReader(cluster=cluster,db=db,ingest_cluster_str=ingest_cluster)

#%%
kql = '''
pa_makers_test | take 10
'''
r = kr.run_kql(kql)
display(r)

#%% ingest data 
import pandas as pd
target_table = 'pa_makers_test'
df = pd.read_csv("temp_query_data.csv")
kr.upload_to_kusto(target_table,df)

#%%
target_table = 'pa_makers_test'
kr.check_table_data(target_table)

#%% BLob test
import sys
sys.path.append(r"F:\az_git_folder\azdsdr\src")
from azdsdr.readers import AzureBlobReader

connect_str         = "DefaultEndpointsProtocol=https;AccountName=cedssparkstorage;AccountKey=AK054WvhVssGGpmGyLiZ8em5FhzQ6z6UmloFE6DM5dXQN2iJ30pP9x0jard+BCITJNVZU6JqTWO+EYCLw0zoxg==;EndpointSuffix=core.windows.net"
container           = "andrewzhu"
abr = AzureBlobReader(blob_conn_str=connect_str,container_name=container)

#%% blob upload test
import time
blob_file_path      = r'powerapps_data/pa_daily_temp.csv'
local_csv_path      = r'data/scope_query_temp.csv'
s = time.time()
abr.upload_file_chunks(blob_file_path=blob_file_path,local_file_path=local_csv_path)
print('done, use time',(time.time() -s))


#%% download test
blob_file_path = 'temp_query_data.csv'
local_file_path = 'test.csv'
abr.download_file(blob_file_path,local_file_path)


#%% upload test
#sas_token = abr.get_blob_sas_url()
# the working version:
# https://cedssparkstorage.blob.core.windows.net/andrewzhu/temp_query_data.csv?sv=2021-04-10&st=2022-10-05T04%3A29%3A18Z&se=2023-01-06T05%3A29%3A00Z&sr=b&sp=r&sig=sHWYA4IAyuRUGYS611aO0vXcijZD%2FY0WqwjzCPtzq0U%3D
# sas token: 
# se=2023-01-13T17%3A12%3A22Z&sp=r&sv=2021-08-06&ss=b&srt=o&sig=sWxAukkF7p%2B3DhfyNTkrfAQKSC5NxWsaMM8xbLD82L4%3D
url = r'''https://cedssparkstorage.blob.core.windows.net/andrewzhu/temp_query_data.csv?se=2023-01-13T17%3A12%3A22Z&sp=r&sv=2021-08-06&ss=b&srt=o&sig=sWxAukkF7p%2B3DhfyNTkrfAQKSC5NxWsaMM8xbLD82L4%3D'''

#%% test get blob sas url
blob_file_path = 'temp_query_data.csv'
url = abr.get_blob_sas_url(blob_file_path)
print(url)

#%% upload file test 
blob_file_path = 'upload_test.csv'
local_file_path = 'temp_query_data_2.csv'
abr.upload_file(blob_file_path=blob_file_path,local_file_path=local_file_path)
print('done')

#%% delete blob file test
blob_file_path = 'upload_test.csv'
abr.delete_blob_file(blob_file_path)
print('done')

#%% test kusto table exist
table_name = 'pa_makers_test2'
r = kr.is_table_exist(table_name)
print(r)

#%% test kusto delete
table_name = 'pa_makers_test'
output_str = kr.drop_table(table_name)
print(output_str)


#%% test create table from csv
kusto_table_name = 'pa_makers_test'
csv_file_path = 'temp_query_data.csv'
folder = 'anzhu/test'
r = kr.create_table_from_csv(kusto_table_name,csv_file_path,kusto_folder=folder)
print(r)


#%% cosmos delete file test
