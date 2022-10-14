from sqlalchemy import create_engine


def open_connection(host="192.168.10.106", port="3306", user="root", passwd="root16313302", db="service_report_auth"):
    sql_connect = "mysql+pymysql://{0}:{1}@{2}:{3}/{4}".format(
        user, passwd, host, port, db)
    engine = create_engine(sql_connect, echo=False)
    con = engine.connect()
    return(con)