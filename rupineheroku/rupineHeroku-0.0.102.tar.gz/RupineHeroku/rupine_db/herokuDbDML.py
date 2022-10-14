from datetime import datetime
from RupineHeroku.rupine_db import herokuDbAccess
from psycopg2 import sql
import json

def POST(connection, schema, tableName:str, data:dict, onConflict:bool=False, uniqueColumnNamesForConflict:str='id'):
    # TODO: Check if any column is not nullable that does not appear in data. Return ERROR in this case
    data['created_at'] = int(datetime.now().timestamp())
    data['modified_at'] = int(datetime.now().timestamp())
    columns = data.keys()
    onConflictString = ''
    if onConflict:
        onConflictString = 'ON CONFLICT ({}) DO NOTHING'.format(uniqueColumnNamesForConflict)
    queryString = "INSERT INTO {{}}.{} ({}) VALUES ({}) {};".format(tableName,', '.join(columns),','.join(['%s']*len(columns)),onConflictString)

    params = []
    for key in data:
        if type(data[key]) == dict or type(data[key]) == list:
            params.append(json.dumps(data[key]))
        else:
            params.append(data[key])

    query = sql.SQL(queryString).format(sql.Identifier(schema))
    result = herokuDbAccess.insertDataIntoDatabase(query, params, connection)    
    return result

def POST_BULK(connection, schema, tableName:str, data:list, byCopy = True, onConflict:bool=False, uniqueColumnNamesForConflict:str='id'):
    '''
    data must be list of diictionaries. Key is column name according to database!
    '''
    query = sql.SQL('SELECT column_name,data_type FROM information_schema.columns WHERE table_schema = %s AND table_name = %s')
    res = herokuDbAccess.fetchDataInDatabase(query, [schema,tableName], connection)
    columns = []
    template = []
    for row in res:
        if row[0] in data[0]:
            columns.append(row[0])
            if row[1] == 'json':
                template.append('%s::json')
            else:
                template.append('%s')
    template = '(' + ','.join(template) + ')' 

    newData = []
    for item in data:
        item['created_at'] = int(datetime.now().timestamp())
        item['modified_at'] = int(datetime.now().timestamp())
        # TODO: Check if any column is not nullable that does not appear in data. Return ERROR in this case
        newItem = []
        for column in columns:
            if column in item:
                if type(item[column]) == dict or type(item[column]) == list:
                    if byCopy:
                        newItem.append(json.dumps(item[column]).encode('utf8'))
                    else:
                        newItem.append(json.dumps(item[column]))
                elif type(item[column]) == str:
                    if byCopy:
                        newItem.append(str(item[column]).encode('utf8'))
                    else:
                        newItem.append(item[column])
                else:
                    newItem.append(item[column])
            else:
                newItem.append(None)
        newData.append(newItem)

    if byCopy and not onConflict:
        result = herokuDbAccess.insertBulkDataIntoDatabaseByCopyManager('.'.join([schema,tableName]),columns,newData,connection)  
    else:
        onConflictString = ''
        if onConflict:
            onConflictString = 'ON CONFLICT ({}) DO NOTHING'.format(uniqueColumnNamesForConflict)
        queryString = "INSERT INTO {{}}.{} ({}) VALUES %s {};".format(tableName,', '.join(columns),onConflictString)
        query = sql.SQL(queryString).format(sql.Identifier(schema))
        result = herokuDbAccess.insertBulkDataIntoDatabase(query,template,newData,connection)
    return result

def PUT(connection, schema, updates:dict, tableName:str, conditions:dict={}):
    updates['modified_at'] = int(datetime.now().timestamp())
    sqlTemplateEqual = "{} = %s"
    sqlTemplateIn = "{} IN ({})"
    setArray = []
    conditionArray = []
    params = []
    for key in updates.keys():
        setArray.append(sqlTemplateEqual.format(key))
        if type(updates[key]) == dict or type(updates[key]) == list:
            params.append(json.dumps(updates[key]))
            
        else:
            params.append(updates[key])
    
    for key in conditions.keys():
        if type(conditions[key]) == list:
            conditionArray.append(sqlTemplateIn.format(key,','.join(['%s'] * len(conditions[key]))))
            for item in conditions[key]:
                params.append(item) 
        else:
            conditionArray.append(sqlTemplateEqual.format(key))
            params.append(conditions[key]) 
    
    if len(conditionArray) == 0:
        queryString = "UPDATE {{}}.{} SET {}".format(tableName,', '.join(setArray))
    else:
        queryString = "UPDATE {{}}.{} SET {} WHERE 1=1 AND {}".format(tableName,', '.join(setArray),' AND '.join(conditionArray))
    query = sql.SQL(queryString).format(sql.Identifier(schema))
    herokuDbAccess.insertDataIntoDatabase(query, params, connection)    
    return None

def PUT_BULK(connection, schema, updates:list, tableName:str, conditionColumns:list=['id']):
    '''
    updates must be list of dictionaries (with equal keys!). Key is column name according to database!
    conditionColumns must be in updates!
    '''
    query = sql.SQL('SELECT column_name,data_type FROM information_schema.columns WHERE table_schema = %s AND table_name = %s')
    res = herokuDbAccess.fetchDataInDatabase(query, [schema,tableName], connection)
    columns = ['modified_at']
    for row in res:
        if row[0] in updates[0]:
            columns.append(row[0])


    newData = []
    for item in updates:
        item['modified_at'] = int(datetime.now().timestamp())
        # TODO: Check if any column is not nullable that does not appear in data. Return ERROR in this case
        newItem = []
        for column in columns:
            if column in item:
                if type(item[column]) == dict or type(item[column]) == list:
                    newItem.append(json.dumps(item[column]).encode('utf8'))
                elif type(item[column]) == str:
                    newItem.append(str(item[column]).encode('utf8'))
                else:
                    newItem.append(item[column])
            else:
                newItem.append(None)
        newData.append(newItem)

    setArray = []
    conditionArray = []

    for col in conditionColumns:
        if col not in columns:
            return {
                'error': 1,
                'msg': 'at least one columnn in conditionColumns is not in updates'
            }
        conditionArray.append("t.{} = tmp.{}".format(col,col))
    for col in columns:
        if col not in conditionColumns:
            setArray.append("{} = tmp.{}".format(col,col))
    
    tmpTableName = schema + '_tmp_' + tableName
    queryString = "UPDATE {{}}.{} AS t SET {} FROM {} tmp WHERE 1=1 AND {}".format(tableName,', '.join(setArray),tmpTableName,' AND '.join(conditionArray))

    query = sql.SQL(queryString).format(sql.Identifier(schema))

    result = herokuDbAccess.updatetBulkDataInDatabaseByCopyManager(schema,tableName,columns,newData,query,connection)   
    return result

def SELECT(connection, schema, columns:list, tableName:str, conditions:dict={}):
    if columns == [] or columns == ['*']:
        query = sql.SQL('SELECT column_name FROM information_schema.columns WHERE table_schema = %s AND table_name = %s')
        res = herokuDbAccess.fetchDataInDatabase(query, [schema,tableName], connection)
        columns = []
        for row in res:
            columns.append(row[0])
    
    sqlTemplateEqual = "{} = %s"
    sqlTemplateIn = "{} IN ({})"
    sqlTemplateNotIn = "{} NOT IN ({})"
    sqlTemplateIsNull = "{} IS NULL"
    sqlTemplateIsNotNull = "{} IS NOT NULL"

    sqlTemplateLt = "{} < %s"
    sqlTemplateLte = "{} <= %s"
    sqlTemplateGt = "{} > %s"
    sqlTemplateGte = "{} >= %s"
    conditionArray = []
    params = []
    for key in conditions.keys():
        conditionColumnName = key
        if type(conditions[key]) == dict:
            conditionValue = conditions[key]['value']
            if 'alias' in conditions[key]:
                conditionColumnName = conditions[key]['alias']
            sqlTemplate = None
            if conditions[key]['operator'] == 'lt':
                sqlTemplate = sqlTemplateLt
            elif conditions[key]['operator'] == 'lte':
                sqlTemplate = sqlTemplateLte
            elif conditions[key]['operator'] == 'gt':
                sqlTemplate = sqlTemplateGt
            elif conditions[key]['operator'] == 'gte':
                sqlTemplate = sqlTemplateGte
            elif conditions[key]['operator'] == 'not in':
                sqlTemplate = sqlTemplateNotIn
            elif conditions[key]['operator'] == 'in':
                sqlTemplate = sqlTemplateIn
            elif conditions[key]['operator'] == 'is not':
                sqlTemplate = sqlTemplateIsNotNull
        else:
            conditionValue = conditions[key]
            if conditionValue is None:
                sqlTemplate = sqlTemplateIsNull
            else:
                sqlTemplate = sqlTemplateEqual
        
        
        if type(conditionValue) == list:
            if sqlTemplate is None or sqlTemplate not in (sqlTemplateIn,sqlTemplateNotIn):
                conditionArray.append(sqlTemplateIn.format(conditionColumnName,','.join(['%s'] * len(conditionValue))))
            else:
                conditionArray.append(sqlTemplate.format(conditionColumnName,','.join(['%s'] * len(conditionValue))))
            for item in conditionValue:
                params.append(item) 
        else:
            conditionArray.append(sqlTemplate.format(conditionColumnName))
            if conditionValue is not None:
                params.append(conditionValue) 
   
    if len(conditionArray) == 0:
        queryString = "SELECT {} FROM {{}}.{}".format(', '.join(columns),tableName)
    else:
        queryString = "SELECT {} FROM {{}}.{} WHERE 1=1 AND {}".format(', '.join(columns),tableName,' AND '.join(conditionArray))
    query = sql.SQL(queryString).format(sql.Identifier(schema))
    res = herokuDbAccess.fetchDataInDatabase(query, params, connection)    

    if res == None:
        return []
    
    result = []
    for row in res:
        resultDict = {}
        for idx,item in enumerate(row):
            resultDict[columns[idx]] = item
        result.append(resultDict)
    return result

def SELECT_FUNCTION(connection, schema,functionName,functionParameter:list,columns:list=[]):
    '''
    See PostGreSQL Function get_return_columns_of_function for supported RETURN TYPES
    '''
    if columns == [] or columns == ['*']:
        queryString = 'SELECT column_name, arg_type, col_num FROM {}.get_return_columns_of_function(%s,%s)'
        query = sql.SQL(queryString).format(sql.Identifier(schema))
        # query = sql.SQL('SELECT t.column_name, t.arg_type::regtype::text, t.col_num FROM pg_proc p LEFT JOIN pg_namespace pn ON p.pronamespace = pn.oid \
        #                 CROSS JOIN UNNEST(proargnames, proargmodes, proallargtypes) WITH ORDINALITY AS t(column_name, arg_mode, arg_type, col_num) \
        #                 WHERE p.proname = %s AND pn.nspname = %s AND t.arg_mode = \'t\' ORDER BY t.col_num')
        res = herokuDbAccess.fetchDataInDatabase(query, [functionName,schema], connection)
        if res == None:
            return []
        
        columns = []
        for row in res:
            columns.append(row[0])
    queryString = "SELECT {} FROM {{}}.{}({})".format(', '.join(columns),functionName,','.join(['%s']*len(functionParameter)))
    query = sql.SQL(queryString).format(sql.Identifier(schema))
    res = herokuDbAccess.fetchDataInDatabase(query, functionParameter, connection)    

    if res == None:
        return []
    
    result = []
    for row in res:
        resultDict = {}
        for idx,item in enumerate(row):
            resultDict[columns[idx]] = item
        result.append(resultDict)
    return result

# import os
# from dotenv import load_dotenv
# import herokuDbAccess as db
# import time
# import decimal

# load_dotenv()

# def convertToType(data,type):
#     if data is None:
#         return None
#     else:
#         return type(data)
# def assignDBResponse(res:tuple):
#     return {
#         'id':res[0],
#         'address':res[1],
#         'block_number':res[2],
#         'future_settlement_block':res[3],
#         'loan':convertToType(res[4],float),
#         'loan_token':res[5],
#         'loan_oracle_price':convertToType(res[6],float),
#         'loan_dex_price':convertToType(res[7],float),
#         'invest_type':res[8],
#         'sentiment':res[9],
#         'risk':convertToType(res[10],float),
#         'invest':convertToType(res[11],float),
#         'invest_token':res[12],
#         'invest_oracle_price':convertToType(res[13],float),
#         'invest_dex_price':convertToType(res[14],float),
#         'lp_pool_tokens':convertToType(res[15],float),
#     }

# if __name__ == '__main__':
#     connection = db.connect(
#         os.environ.get("HEROKU_GOD_USER"),
#         os.environ.get("HEROKU_GOD_PASSWORD"),
#         os.environ.get("HEROKU_HOST"),
#         os.environ.get("HEROKU_PORT"),
#         os.environ.get("HEROKU_DB")
#     )
#     conditions = {
#         'transaction_type': {
#             'operator': 'not in',
#             'value': ["auth","blub"]
#         },
#         'listaccounthistory_data': None,
#         'block_number_1': {
#             'alias': 'block_number',
#             'operator': 'gte',
#             'value': 1760000
#         },
#         'block_number_2': {
#             'alias': 'block_number',
#             'operator': 'lt',
#             'value': 1900000
#         }

#     }
#     #conditions = {'transaction_type': "auth"}
#     SELECT(connection,os.environ.get("ENVIRONMENT"),[],'dfi_blockchain_data',conditions)

#     r = POST_BULK(connection,'dbdev','testbulk',[{'number':2}],True)
#     print(r)
    #r = POST_BULK(connection,'dbdev','testbulk',[{'id':1,'t':'TSLA'}],True)
    #r = POST_BULK(connection,'dbdev','testbulk',[{'id':1,'t':'TSLA/v1'}],True)
    # d = {
    #     'id': '19488fdb3c264e181117ba8f764f486df43c1a25a29f5bef74f123a1eb665e13_6_-1_0_ARKK', 
    #     'txid': '19488fdb3c264e181117ba8f764f486df43c1a25a29f5bef74f123a1eb665e13', 
    #     'public_address': 'dRPF64SSDi5h9hpTx3KRWX5U86MByES34s', 
    #     'transaction_type': 'removepoolliquidity', 
    #     'block_number': 1610004, 
    #     'block_timestamp': 1644358131, 
    #     'tx_order': 6, 
    #     'vin': None, 
    #     'vout': 0, 
    #     'token_in': 'ARKK-DUSD', 
    #     'amount_in': 1343094801, 
    #     'share_address': 'dRPF64SSDi5h9hpTx3KRWX5U86MByES34s', 
    #     'token_out': 'ARKK', 
    #     'poolsymbols_route': None, 
    #     'max_price':decimal.Decimal(1000000000000002.00000000),
    #     'amount_out':135528499,
    #     'has_listaccounthistory_correction':'Y'
    # }
    # d = {
    #     'id': 'f',
    #     'txid': 't', 
    #     'public_address': 't', 
    #     'transaction_type': 't', 
    #     'block_number': 1, 
    #     'block_timestamp': 1, 
    #     'tx_order': 3, 
    #     'token_in': 't', 
    #     'share_address': 't',
    #     'max_price': decimal.Decimal(1000000000000002.00000000),
    #     'poolsymbols_route': {'here': 1, 'is': {'a': ['deep','json']}},
    #     'has_listaccounthistory_correction':'Y'}
    # r = POST_BULK(connection,'dbdev','testbulk',[d],False,True)
    # print(r)
    # r = PUT_BULK(connection,'dbdev',[{
    #     'id': 1,
    #     'number':decimal.Decimal('1000000000000000.00000000')
    # }],'testbulk')
    # print(r)
#     start = time.time()
    
#     for i in range(10,20):
#         data = {
#             'id': i,
#             'number':i+20
#         }
#         updates = {
#             'number':i+200
#         }
#         conditions = {
#             'id': i
#         }
#         #r= POST(connection,'dbdev','testbulk',data,True,'id')
#         r = PUT(connection,'dbdev',updates,'testbulk',conditions)
#         print(r)

#     end = time.time()
#     print(end - start)

#     start = time.time()
#     data = []
#     for i in range(1,10):
#         item = {
#             'id': i,
#             'number':i+200
#         }
#         data.append(item)
#     #r = POST_BULK(connection,'dbdev','testbulk',data,False,True,'id')
#     r = PUT_BULK(connection,'dbdev',data,'testbulk')
#     print(r)

#     end = time.time()
#     print(end - start)

    



#     data =  {'id': '30772bccd4b4e747b588e100c375242b8971d72c69871eb77fabfe478b7f43a6_4_-1_0', 'txid': '30772bccd4b4e747b588e100c375242b8971d72c69871eb77fabfe478b7f43a6', 'public_address': 'N/A', 'transaction_type': 'setgovheight', 'block_number': 2103358, 'block_timestamp': 1659194237, 'tx_order': 4, 'vin': None, 'vout': 0, 'value': 0, 
#         'data': {
#             'attributes': [
#                 {'unknown': 1, 'type': 'p', 'typeId': 17, 'key': 'a', 'keyId': 1, 'value': 29270000},
#                 {'unknown': 1, 'type': 'p', 'typeId': 101, 'key': 'b', 'keyId': 1, 'value': 29270000},
#                 {'unknown': 1, 'type': 'p', 'typeId': 102, 'key': 'b', 'keyId': 1, 'value': 29270000}
#             ],
#         'height': 2105280, 'hex': None, 'name': 'setgovheight'}}
#     updates = data.copy()
#     updates.pop('id',None)
#     PUT(connection,os.environ.get("ENVIRONMENT"),updates,'dfi_transaction',{'id':data['id']})
#     #dfi_dex_calc_preparation_by_timestamp
#     #dfi_dex_tx_get_all_by_timestamp
#     SELECT_FUNCTION(connection,'dbdev','dfi_dex_tx_get_all_by_timestamp',[0, 1659183422])
#     data = {
#             'context':'TEST',
#             'key':'TEST2',
#             'description':'',
#             'flag':'Y',
#         }
#     POST(connection,os.environ.get("ENVIRONMENT"),'dfi_control',data)
    # print(SELECT(connection,'dbdev',[],'dfi_transaction',{}))
    # print(PUT(connection,'dbdev',{'transaction_type': 'BAR'},'dfi_transaction',{'block_number': 2056337,'public_address':'8bL7jZe2Nk5EhqFA6yuf8HPre3M6eewkqj'}))
    # print(PUT(connection,'dbdev',{'transaction_type': 'BAR'},'dfi_transaction'))
# #     data = {
# #         'id': '1',
#         'txid':'sdg',
#         'public_address':'sdjkl',
#         'transaction_type':'skjlfd',
#         'block_number':1,
#         'block_timestamp':2,
#         'tx_order':1,
#         'vin':1,
#         'vout':0,
#         'data':{'some':'data','and':1}
#     }

    #    id varchar(255) not null
    # ,  varchar(255) not null
    # ,  varchar(255) not null 
    # ,  varchar(255) not null
    # ,  integer not null
    # ,  integer not null
    # ,  integer not null
    # ,  integer
    # ,  integer
    # ,  json
    #print(POST(connection,'dbdev','dfi_transaction',data,True))
#     data = {
#         'id':"bla",
#         'key':"TSLA-DUSD",
#         'block_number':123,
#         'block_timestamp':456,
#         'pool_reserve':390.1,
#         'reserve_a':4.5,
#         'reserve_b':6.5,
#         'dex_price':0.12
#     }
#     postDFIDEX(connection,'dbdev',data)
#     print(getlatestDEXBlock(connection,'dbdev','TSLA-DUSD'))
#     res = getOracleRecordForTimestamp(connection,'prod','PYPL',1652344775)
#     print(res)
#     print(len(res))
#     res = putDFIBotcontrol(connection,'stage','dfi1','N')
#     print(res)
    # data = {
    #     'id':'1003718-tf1q6qj52ykxlf6halmx0g32gaumuuptactwgrqh23-MSFT',
    #     'address':'tf1q6qj52ykxlf6halmx0g32gaumuuptactwgrqh23',
    #     'expected_roi':13,
    #     'is_active':'N',
    #     'waiting_for_loan_payback':'Y'
    # } 
#     putDFIBotEventROI(connection,os.environ.get("ENVIRONMENT"),data)
#     changeDFIBotEventStatus(connection,os.environ.get("ENVIRONMENT"),data)
    # print(getTokenRisk(connection,'prod',1,1,1,True))
    # data = {
    #     'id':'dfi1-123-TSLA',
    #     'address':'dfi1',
    #     'is_active':'Y' 
    # }
    # changeDFIBotEventStatus(connection,'stage',data)

    # trades = getDFIBotEvents(connection,'stage','dfi1',True)
    # for t in trades:
    #     print(assignDBResponse(t))
