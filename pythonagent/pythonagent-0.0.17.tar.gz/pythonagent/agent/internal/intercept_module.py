

from pythonagent.agent.probes import frameworks, http, sql, logging, mongodb, cache, Instrumentation, elasticdb

BT = (
    # Entry points
    ('flask', frameworks.intercept_flask),
    ('django.core.handlers.wsgi', frameworks.intercept_django_wsgi_handler),
    ('django.core.handlers.base', frameworks.intercept_django_base_handler),
    ('bottle', frameworks.intercept_bottle),
    ('tornado.web', frameworks.intercept_tornado_web),
    ('cherrypy', frameworks.intercept_cherrypy),
    ('pyramid', frameworks.intercept_pyramid),
    ('falcon', frameworks.intercept_falcon),
    # HTTP exit calls
    ('httplib', http.intercept_httplib),
    ('http.client', http.intercept_httplib),
    ('urllib3', http.intercept_urllib3),
    ('requests', http.intercept_requests),
    ('tornado.httpclient', http.intercept_tornado_httpclient),
    #('boto.https_connection', http.intercept_boto),

    # Logging
    # ('logging', logging.intercept_logging),

    # SQL exit calls
    ('psycopg2', sql.psycopg2.intercept_psycopg2_connection),
    ('pymysql.connections', sql.pymysql.intercept_pymysql_connections),
    ('mysql.connector.connection', sql.mysql_connector.intercept_mysql_connector_connection),
    ('MySQLdb.connections', sql.mysqldb.intercept_MySQLdb_connection),

    # MongoDB
    ('pymongo', mongodb.intercept_pymongo),
    ('elasticsearch',elasticdb.intercept_elastic),

    #dynamo
    ('botocore.client', sql.dynamodb.intercept_dynamodb),
    ('botocore.endpoint', sql.botocores3.intercept_s3),
    #    #REDIS
    ('redis.connection', cache.intercept_redis),
)
