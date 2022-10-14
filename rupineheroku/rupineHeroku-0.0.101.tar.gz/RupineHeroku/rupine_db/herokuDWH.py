from RupineHeroku.rupine_db import herokuDbAccess
from psycopg2 import sql
from datetime import datetime
import pytz

def postAccountAddress(connection, schema, data):
    query = sql.SQL("INSERT INTO {}.dwh_address_account (chain_id,chain,account,public_address,context) VALUES (%s,%s,%s,%s,%s)").format(sql.Identifier(schema))
    params = (
        data['chain_id'],
        data['chain'],
        data['account'],
        data['public_address'],
        data['context'])
    result = herokuDbAccess.insertDataIntoDatabase(query, params, connection)    
    return result

def getAccountAddress(connection, schema, account=None, public_address=None, chain=None, chain_id=None):
    conditions = ""
    params = []
    if chain is None and chain_id is None:
        return []
    elif chain is not None:
        conditions = conditions + " AND t.chain = %s"
        params.append(chain)
    elif chain_id is not None:
        conditions = conditions + " AND t.chain_id = %s"
        params.append(chain_id)
    if account is not None:
        query = sql.SQL("SELECT account,public_address,context from {0}.dwh_address_account t WHERE 1=1 %s  AND account = %%s " % (conditions)).format(sql.Identifier(schema))
        params.append(account)
    elif public_address is not None:
        query = sql.SQL("SELECT account,public_address,context from {0}.dwh_address_account t WHERE 1=1 %s AND public_address = %%s" % (conditions)).format(sql.Identifier(schema))
        params.append(public_address)
    else:
        return []

    result = herokuDbAccess.fetchDataInDatabase(query, [*params], connection)  
    return result

def getUniqueTokenFromTransactions(connection, schema, public_address:str=None, chain_id:int=None):
    
    queryStrSend = "select distinct(amount_send_dwh_token_id) \
        FROM {}.dwh_transaction \
        WHERE amount_send_dwh_token_id is not NULL"

    queryStrRecv = "select distinct(amount_recv_dwh_token_id) \
        FROM {}.dwh_transaction \
        WHERE amount_recv_dwh_token_id is not NULL"

    params = []

    if chain_id:
        queryStrSend = queryStrSend + " AND chain_id=%s"
        queryStrRecv = queryStrRecv + " AND chain_id=%s"
        params.append(chain_id)

    if public_address:
        queryStrSend = queryStrSend + " AND public_address=%s"
        queryStrRecv = queryStrRecv + " AND public_address=%s"
        params.append(public_address)

    querySend = sql.SQL(queryStrSend).format(sql.Identifier(schema))
    queryRecv = sql.SQL(queryStrRecv).format(sql.Identifier(schema))

    resultSend = herokuDbAccess.fetchDataInDatabase(querySend, params, connection)    
    resultRecv = herokuDbAccess.fetchDataInDatabase(queryRecv, params, connection)    

    allResults = [*resultSend, *resultRecv]

    return allResults

def getUniqueAddress(connection, schema, chain_id:int=None):
    
    queryStr = "select distinct(public_address) \
        FROM {}.dwh_address_account"

    params = []

    if chain_id:
        queryStr = queryStr + " WHERE chain_id=%s"
        params.append(chain_id)

    query = sql.SQL(queryStr).format(sql.Identifier(schema))

    result = herokuDbAccess.fetchDataInDatabase(query, params, connection)    
    return result

def getLatestTx(connection, schema, public_address, min_timestamp):
    
    queryStr = "SELECT tx_timestamp, tx_from, amount_fee_value, amount_fee_dwh_token_id,  \
                        amount_send_value, amount_send_dwh_token_id, \
                        amount_recv_value, amount_recv_dwh_token_id  \
                FROM {}.dwh_transaction \
                WHERE public_address = %s AND tx_timestamp > %s \
                ORDER BY tx_timestamp DESC"
  
    query = sql.SQL(queryStr).format(sql.Identifier(schema))

    result = herokuDbAccess.fetchDataInDatabase(query, [public_address, min_timestamp], connection) 
    return result

def getTxSortedAsc(connection, schema, public_address_list):

    queryStr = "SELECT tx_timestamp, tx_from, amount_fee_value, amount_fee_dwh_token_id,  \
                        amount_send_value, amount_send_dwh_token_id, \
                        amount_recv_value, amount_recv_dwh_token_id  \
                FROM {}.dwh_transaction \
                WHERE public_address IN " + public_address_list + " \
                ORDER BY tx_timestamp ASC"

    query = sql.SQL(queryStr).format(sql.Identifier(schema))

    result = herokuDbAccess.fetchDataInDatabase(query, [], connection) 
    return result