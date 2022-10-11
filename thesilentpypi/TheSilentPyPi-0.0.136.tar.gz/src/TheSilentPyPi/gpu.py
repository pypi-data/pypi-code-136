#try block for termux
try:
    from selenium import webdriver
    from selenium.webdriver.common.by import *
    from selenium.webdriver.firefox.service import *
    from webdriver_manager.firefox import *

except:
    pass

from collections import *
from cryptography.fernet import *
from os import name

import codecs
import base64
import hashlib
import itertools
import numpy as np
import os
import random
import re
import requests
import socket
import struct
import tensorflow as tf
import time
import urllib3

color   = "\033[1;31m"

#create html sessions object
web_session = requests.Session()

#fake user agent
user_agent = {"User-Agent" : "Mozilla/5.0 (X11; Fedora; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36", "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "Accept-Language" : "en-US,en"}

#increased security
requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ":HIGH:!DH:!aNULL"

#increased security
try:
    requests.packages.urllib3.contrib.pyopenssl.util.ssl_.DEFAULT_CIPHERS += ":HIGH:!DH:!aNULL"

except AttributeError:
    pass

#machine learning antivirus detect engine
def av_detect(virus, learn):
    clear()
    ml_virus = av_learn(learn)
    
    list_files = []
    ml_list = []
    possible = []

    progress = 0
    progress_count = 0
    total_progress = 0

    print(color + "preparing")

    for root, dirs, files in os.walk(virus, topdown = True):
        if len(dirs) > 0:
            for directory in dirs:
                for file in files:
                    progress_count += 1
                    list_files.append(root + directory + "/" + file)

        else:
            for file in files:
                progress_count += 1
                list_files.append(root + "/" + file)

    list_files.sort()

    counter = 0

    clear()
    
    print(color + "progress: " + str(total_progress) + "%")

    for file in list_files:
        progress += 1

        if progress == int(progress_count / 100):
            progress = 0
            total_progress += 1
            print(color + "progress: " + str(total_progress) + "%")
        
        try:
            if os.path.isfile(file) and os.path.getsize(file) > 0:
                with open(file, "rb") as f:
                    
                    for chunk in iter(lambda: f.read(128), b""):
                        try:
                            ascii_convert = codecs.decode(chunk, "utf8")
                        
                            clean = str(ascii_convert).replace("b", "")
                            clean = clean.replace("'", "")
                            clean = clean.replace("\x00", "")
                            clean = clean.replace("\x11", "")

                            if clean != "":
                                ml_list.append(clean)
                                
                        except:
                            pass

                ml_list = list(dict.fromkeys(ml_list))

                for string in ml_list:
                    for i in ml_virus:
                        if string == i:
                            counter += 1

                if counter > 0:
                    possible.append(file + ": " + str(counter) + "%")
                    
                counter = 0
                ml_list = []

        except:
            pass

    clear()
    possible.sort()
    
    for i in possible:
        print(i)

#machine learning antivirus learn engine
def av_learn(virus_folder):
    clear()
    list_files = []
    counter_array = np.array([])
    ml_array = np.array([])
    ml_list = []

    print(color + "preparing")

    for root, dirs, files in os.walk(virus_folder, topdown = True):
       for name in files:
          list_files.append(name)

    list_files.sort()

    for file in list_files:
        try:
            if os.path.isfile(virus_folder + "/" + file) and os.path.getsize(virus_folder + "/" + file) > 0:
                with open(virus_folder + "/" + file, "rb") as f:
                    print(color + "learning from: " + file)
                    
                    for chunk in iter(lambda: f.read(128), b""):
                        try:
                            ascii_convert = codecs.decode(chunk, "utf8")
                        
                            clean = str(ascii_convert).replace("b", "")
                            clean = clean.replace("'", "")
                            clean = clean.replace("\x00", "")
                            clean = clean.replace("\x11", "")

                            if clean != "":
                                ml_list.append(clean)
                                
                        except:
                            pass

        except FileNotFoundError:
            pass

    ml_array = np.array(ml_list)
    counter = str(Counter(ml_array).most_common(100))

    super_clean = counter.replace("[", "")
    super_clean = super_clean.replace("]", "")
    super_clean = super_clean.replace("('", "~")
    super_clean = super_clean.replace(")", "")
    super_clean = super_clean.replace("',", "`")
    counter_list = list(super_clean)

    counter_boolean = False
    my_string = ""
    super_counter = []

    for i in counter_list:
        if i == "`":
            my_string = my_string.replace("~", "")
            super_counter.append(my_string)
            my_string = ""
            counter_boolean = False

        if i == "~":
            counter_boolean = True

        if counter_boolean == True:
            my_string += i

    clear()

    return super_counter

#brute force hash
def brute_force_hash(my_hash, minimum = 4, maximum = 36, timer = 60, hash_type = "sha1"):
    dictionary = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if hash_type == "md5":
        crack_boolean = False
        timer *= 60
        hash_count = 0

        clear()

        for i in range (minimum, maximum):
            start = time.time()

            if crack_boolean == True:
                break
            
            print(color + "attempting length: " + str(i))
            
            for ii in itertools.product(dictionary, repeat = i):
                compute = "".join(ii)
                
                result = hashlib.md5(compute.encode("utf8"))

                hash_count += 1

                end = time.time()
                trim = end - start
                
                if trim > timer:
                    print(color + "time out")
                    break
                
                if result.hexdigest() == my_hash:
                    crack_boolean = True
                    print(color + "seconds: " + end - start)
                    print(color + "password: " + compute)
                    break

            print(color + "hashes computed: " + str(hash_count))

    if hash_type == "sha1":
        crack_boolean = False
        timer *= 60
        hash_count = 0

        clear()

        for i in range (minimum, maximum):
            start = time.time()

            if crack_boolean == True:
                break
            
            print(color + "attempting length: " + str(i))
            
            for ii in itertools.product(dictionary, repeat = i):
                compute = "".join(ii)
                
                result = hashlib.sha1(compute.encode("utf8"))

                hash_count += 1

                end = time.time()
                trim = end - start
                
                if trim > timer:
                    print(color + "time out")
                    break
                
                if result.hexdigest() == my_hash:
                    crack_boolean = True
                    print(color + "seconds: " + end - start)
                    print(color + "password: " + compute)
                    break

            print(color + "hashes computed: " + str(hash_count))

#clear console (platform independent)
def clear():
    if name == "nt":
        os.system("cls")

    else:
        os.system("clear")

#brute force hash using dictionary method
def dictionary_hash(my_file, my_hash, hash_type = "sha1"):
    clear()

    if hash_type == "md5":
        print(color + "cracking md5 hash")

        with open(my_file, "r", errors = "ignore") as file:
            for i in file:
                clean = i.replace("\n", "")
                result = hashlib.md5(clean.encode()).hexdigest()

                if result == my_hash:
                    print(color + "password: " + i)
                    break

    if hash_type == "sha1":
        print(color + "cracking sha1 hash")

        with open(my_file, "r", errors = "ignore") as file:
            for i in file:
                clean = i.replace("\n", "")
                result = hashlib.sha1(clean.encode()).hexdigest()

                if result == my_hash:
                    print(color + "password: " + i)
                    break

    print("done")

def email_scanner(url, secure = True, bot = False):
    if secure == True:
        my_secure = "https://"

    if secure == False:
        my_secure = "http://"

    my_url = my_secure + url

    tracker = 0

    email_list = []
    website_list = []
    website_list.append(my_url)

    clear()

    while True:
        website_list = list(dict.fromkeys(website_list))

        if bot == True:
            anti_bot = random.uniform(1, 60)
            
            time.sleep(anti_bot)

        try:
            status = web_session.get(website_list[tracker], verify = False, headers = user_agent, timeout = (5, 30)).status_code

            if status == 200:
                print(color + website_list[tracker])
                my_request = web_session.get(website_list[tracker], verify = False, headers = user_agent, timeout = (5, 30)).text
                tracker += 1

                #urls
                website = re.findall("http://|https://\S+", my_request)
                website = list(dict.fromkeys(website))

                for i in website:
                    try:
                        result = re.split("[\(\)<>\[\],\{\};]", i)
                        result = result[0]
                        result = re.sub("[\"\']", "", result)

                    except:
                        result = i
                        
                    if url in i:
                        website_list.append(re.sub("[\\\"\']", "", result))

                #href
                href = re.sub(" ", "", my_request)
                href = re.findall("href=[\"\']\S+?[\'\"]", href)
                href = list(dict.fromkeys(href))
                for i in href:
                    try:
                        result = re.split("[\(\)<>\[\],\{\};]", i)
                        result = result[0]

                    except:
                        result = i
                    
                    result = re.sub("[\\\"\';]|href=", "", i)

                    if result.startswith("http"):
                        if url in result:
                            website_list.append(result)

                    if result.startswith("http") == False and result[0] != "/":
                        result = re.sub(url, "", result)
                        result = re.sub("www", "", result)
                        website_list.append(my_url + "/" + result)

                    if result.startswith("http") == False and result[0] == "/":
                        result = re.sub(url, "", result)
                        result = re.sub("www", "", result)
                        website_list.append(my_url + result)

                #action
                action = re.sub(" ", "", my_request)
                action = re.findall("action=[\"\']\S+?[\'\"]", action)
                action = list(dict.fromkeys(action))
                
                for i in action:
                    try:
                        result = re.split("[\(\)<>\[\],\{\};]", i)
                        result = result[0]

                    except:
                        result = i
                        
                    result = re.sub("[\\\"\';]|action=", "", i)

                    if result.startswith("http"):
                        if url in result:
                            website_list.append(result)

                    if result.startswith("http") == False and result[0] != "/":
                        result = re.sub(url, "", result)
                        result = re.sub("www", "", result)
                        website_list.append(my_url + "/" + result)

                    if result.startswith("http") == False and result[0] == "/":
                        result = re.sub(url, "", result)
                        result = re.sub("www", "", result)
                        website_list.append(my_url + result)

                #src
                src = re.sub(" ", "", my_request)
                src = re.findall("src=[\"\']\S+?[\'\"]", src)
                src = list(dict.fromkeys(src))

                for i in src:
                    try:
                        result = re.split("[\(\)<>\[\],\{\};]", i)
                        result = result[0]

                    except:
                        result = i
                        
                    result = re.sub("[\\\"\';]|src=", "", i)
                    
                    if result.startswith("http"):
                        if url in result:
                            website_list.append(result)

                    if result.startswith("http") == False and result[0] != "/":
                        result = re.sub(url, "", result)
                        result = re.sub("www", "", result)
                        website_list.append(my_url + "/" + result)

                    if result.startswith("http") == False and result[0] == "/":
                        result = re.sub(url, "", result)
                        result = re.sub("www", "", result)
                        website_list.append(my_url + result)

                #slash
                slash = re.findall("[\'|\"]/\S+[\"|\']", my_request)

                for i in slash:
                    my_search = re.search("\.com|\.edu|\.net|\.org|\.tv|www|http", i)

                    if not my_search:
                        j = re.sub("[\"\']", "", i)
                        j = re.split("[\(\)<>\[\],\{\};�\|]", j)
                        j = j[0]
                        website_list.append(my_url + j)

            else:
                print(color + str(status) + ": " + str(website_list[tracker]))
                website_list.pop(tracker)
                
        except IndexError:
            print(color + "done")
            break

        except:
            print(color + "ERROR: " + str(website_list[tracker]))
            website_list.pop(tracker)

        email = re.findall("[a-z0-9]+@[a-z0-9]+[.][a-z]+", my_request)

        for emails in email:
            email_list.append(emails)

    clear()

    email = list(dict.fromkeys(email))
    email.sort()

    return email_list

#scans for forms
def form_scanner(url, secure = True, parse = "forms"):
    if secure == True:
        my_secure = "https://"

    if secure == False:
        my_secure = "http://"

    url = my_secure + url

    try:
        result = web_session.get(url, verify = False, headers = user_agent, timeout = (5, 30)).text

        try:
            forms = re.findall("<form[\n\w\S\s]+?form>", result)

            for i in forms:
                input_form = re.findall("<input.+?>", i)

            if parse == "forms":
                return forms

            if parse == "input":
                return input_form

        except UnicodeDecodeError:
            return []

    except:
        return []

def gpu_sql_error(url):
    error_message = {"SQL syntax.*?MySQL", "Warning.*?\Wmysqli?_", "MySQLSyntaxErrorException", "valid MySQL result", "check the manual that (corresponds to|fits) your MySQL server version", "check the manual that (corresponds to|fits) your MariaDB server version", "check the manual that (corresponds to|fits) your Drizzle server version", "Unknown column '[^ ]+' in 'field list'", "MySqlClient\.", "com\.mysql\.jdbc", "Zend_Db_(Adapter|Statement)_Mysqli_Exception", "Pdo\[./_\\]Mysql", "MySqlException", "SQLSTATE\[\d+\]: Syntax error or access violation", "MemSQL does not support this type of query", "is not supported by MemSQL", "unsupported nested scalar subselect", "PostgreSQL.*?ERROR", "Warning.*?\Wpg_", "valid PostgreSQL result", "Npgsql\.", "PG::SyntaxError:", "org\.postgresql\.util\.PSQLException", "ERROR:\s\ssyntax error at or near", "ERROR: parser: parse error at or near", "PostgreSQL query failed", "org\.postgresql\.jdbc", "Pdo\[./_\\]Pgsql", "PSQLException", "OLE DB.*? SQL Server", "\bSQL Server[^&lt;&quot;]+Driver", "Warning.*?\W(mssql|sqlsrv)_", "\bSQL Server[^&lt;&quot;]+[0-9a-fA-F]{8}", "System\.Data\.SqlClient\.(SqlException|SqlConnection\.OnError)", "(?s)Exception.*?\bRoadhouse\.Cms\.", "Microsoft SQL Native Client error '[0-9a-fA-F]{8}", "\[SQL Server\]", "ODBC SQL Server Driver", "ODBC Driver \d+ for SQL Server", "SQLServer JDBC Driver", "com\.jnetdirect\.jsql", "macromedia\.jdbc\.sqlserver", "Zend_Db_(Adapter|Statement)_Sqlsrv_Exception", "com\.microsoft\.sqlserver\.jdbc", "Pdo\[./_\\](Mssql|SqlSrv)", "SQL(Srv|Server)Exception", "Unclosed quotation mark after the character string", "Microsoft Access (\d+ )?Driver", "JET Database Engine", "Access Database Engine", "ODBC Microsoft Access", "Syntax error \(missing operator\) in query expression", "\bORA-\d{5}", "Oracle error", "Oracle.*?Driver", "Warning.*?\W(oci|ora)_", "quoted string not properly terminated", "SQL command not properly ended", "macromedia\.jdbc\.oracle", "oracle\.jdbc", "Zend_Db_(Adapter|Statement)_Oracle_Exception", "Pdo\[./_\\](Oracle|OCI)", "OracleException", "CLI Driver.*?DB2", "DB2 SQL error", "\bdb2_\w+\(", "SQLCODE[=:\d, -]+SQLSTATE", "com\.ibm\.db2\.jcc", "Zend_Db_(Adapter|Statement)_Db2_Exception", "Pdo\[./_\\]Ibm", "DB2Exception", "ibm_db_dbi\.ProgrammingError", "Warning.*?\Wifx_", "Exception.*?Informix", "Informix ODBC Driver", "ODBC Informix driver", "com\.informix\.jdbc", "weblogic\.jdbc\.informix", "Pdo\[./_\\]Informix", "IfxException", "Dynamic SQL Error", "Warning.*?\Wibase_", "org\.firebirdsql\.jdbc", "Pdo\[./_\\]Firebird", "SQLite/JDBCDriver", "SQLite\.Exception", "(Microsoft|System)\.Data\.SQLite\.SQLiteException", "Warning.*?\W(sqlite_|SQLite3::)", "\[SQLITE_ERROR\]", "SQLite error \d+:", "sqlite3.OperationalError:", "SQLite3::SQLException", "org\.sqlite\.JDBC", "Pdo\[./_\\]Sqlite", "SQLiteException", "SQL error.*?POS([0-9]+)", "Warning.*?\Wmaxdb_", "DriverSapDB", "-3014.*?Invalid end of SQL statement", "com\.sap\.dbtech\.jdbc", "\[-3008\].*?: Invalid keyword or missing delimiter", "Warning.*?\Wsybase_", "Sybase message", "Sybase.*?Server message", "SybSQLException", "Sybase\.Data\.AseClient", "com\.sybase\.jdbc", "Warning.*?\Wingres_", "Ingres SQLSTATE", "Ingres\W.*?Driver", "com\.ingres\.gcf\.jdbc", "Exception (condition )?\d+\. Transaction rollback", "com\.frontbase\.jdbc", "Syntax error 1. Missing", "(Semantic|Syntax) error [1-4]\d{2}\.", "Unexpected end of command in statement \[", "Unexpected token.*?in statement \[", "org\.hsqldb\.jdbc", "org\.h2\.jdbc", "\[42000-192\]", "![0-9]{5}![^\n]+(failed|unexpected|error|syntax|expected|violation|exception)", "\[MonetDB\]\[ODBC Driver", "nl\.cwi\.monetdb\.jdbc", "Syntax error: Encountered", "org\.apache\.derby", "ERROR 42X01", ", Sqlstate: (3F|42).{3}, (Routine|Hint|Position):", "/vertica/Parser/scan", "com\.vertica\.jdbc", "org\.jkiss\.dbeaver\.ext\.vertica", "com\.vertica\.dsi\.dataengine", "com\.mckoi\.JDBCDriver", "com\.mckoi\.database\.jdbc", "&lt;REGEX_LITERAL&gt;", "com\.facebook\.presto\.jdbc", "io\.prestosql\.jdbc", "com\.simba\.presto\.jdbc", "UNION query has different number of fields: \d+, \d+", "Altibase\.jdbc\.driver", "com\.mimer\.jdbc", "Syntax error,[^\n]+assumed to mean", "io\.crate\.client\.jdbc", "encountered after end of query", "A comparison operator is required here", "-10048: Syntax error", "rdmStmtPrepare\(.+?\) returned", "SQ074: Line \d+:", "SR185: Undefined procedure", "SQ200: No table ", "Virtuoso S0002 Error", "\[(Virtuoso Driver|Virtuoso iODBC Driver)\]\[Virtuoso Server\]"}

    my_url = re.findall("https://|http://\S+", str(url))
    my_url = re.sub(",", "", my_url[0])
    my_url = my_url[:-1]

    my_request = web_session.get(my_url, headers = user_agent).text

    for i in error_message:
        result = re.search(i, my_request)

        if result:
            return "true: " + str(i) + " " + str(result.span()) + " " + str(my_url)

    return "none"

def hex_viewer(file):
    clear()

    count = 0

    my_string = ""
    
    with open(file, "rb") as f:
        for chunk in iter(lambda: f.read(2), b""):
            try:
                hex_code = codecs.decode(chunk, "hex")
                clean = str(hex_code).replace("b", "")
                clean = clean.replace("'", "")
                clean = clean.replace("\\", "")
                clean = clean.replace("x", "")

                my_string += clean

                count += 1

                if count == 64:
                    print(color + my_string)
                    
                    count = 0
                    my_string = ""
                    
            except:
                pass

    print("\ndone")
    
def link_scanner(url, secure = True, bot = False):
    if secure == True:
        my_secure = "https://"

    if secure == False:
        my_secure = "http://"

    my_url = my_secure + url

    tracker = 0

    website_list = []
    website_list.append(my_url)

    clear()

    while True:
        website_list = list(dict.fromkeys(website_list))

        if bot == True:
            anti_bot = random.uniform(1, 60)
            
            time.sleep(anti_bot)

        try:
            status = web_session.get(website_list[tracker], verify = False, headers = user_agent, timeout = (5, 30)).status_code

            if status == 200:
                print(color + website_list[tracker])
                my_request = web_session.get(website_list[tracker], verify = False, headers = user_agent, timeout = (5, 30)).text
                tracker += 1

                #urls
                website = re.findall("http://|https://\S+", my_request)
                website = list(dict.fromkeys(website))

                for i in website:
                    try:
                        result = re.split("[\(\)<>\[\],\{\};]", i)
                        result = result[0]
                        result = re.sub("[\"\']", "", result)

                    except:
                        result = i
                        
                    if url in i:
                        website_list.append(re.sub("[\\\"\']", "", result))

                #href
                href = re.sub(" ", "", my_request)
                href = re.findall("href=[\"\']\S+?[\'\"]", href)
                href = list(dict.fromkeys(href))
                for i in href:
                    try:
                        result = re.split("[\(\)<>\[\],\{\};]", i)
                        result = result[0]

                    except:
                        result = i
                    
                    result = re.sub("[\\\"\';]|href=", "", i)

                    if result.startswith("http"):
                        if url in result:
                            website_list.append(result)

                    if result.startswith("http") == False and result[0] != "/":
                        result = re.sub(url, "", result)
                        result = re.sub("www", "", result)
                        website_list.append(my_url + "/" + result)

                    if result.startswith("http") == False and result[0] == "/":
                        result = re.sub(url, "", result)
                        result = re.sub("www", "", result)
                        website_list.append(my_url + result)

                #action
                action = re.sub(" ", "", my_request)
                action = re.findall("action=[\"\']\S+?[\'\"]", action)
                action = list(dict.fromkeys(action))
                
                for i in action:
                    try:
                        result = re.split("[\(\)<>\[\],\{\};]", i)
                        result = result[0]

                    except:
                        result = i
                        
                    result = re.sub("[\\\"\';]|action=", "", i)

                    if result.startswith("http"):
                        if url in result:
                            website_list.append(result)

                    if result.startswith("http") == False and result[0] != "/":
                        result = re.sub(url, "", result)
                        result = re.sub("www", "", result)
                        website_list.append(my_url + "/" + result)

                    if result.startswith("http") == False and result[0] == "/":
                        result = re.sub(url, "", result)
                        result = re.sub("www", "", result)
                        website_list.append(my_url + result)

                #src
                src = re.sub(" ", "", my_request)
                src = re.findall("src=[\"\']\S+?[\'\"]", src)
                src = list(dict.fromkeys(src))

                for i in src:
                    try:
                        result = re.split("[\(\)<>\[\],\{\};]", i)
                        result = result[0]

                    except:
                        result = i
                        
                    result = re.sub("[\\\"\';]|src=", "", i)
                    
                    if result.startswith("http"):
                        if url in result:
                            website_list.append(result)

                    if result.startswith("http") == False and result[0] != "/":
                        result = re.sub(url, "", result)
                        result = re.sub("www", "", result)
                        website_list.append(my_url + "/" + result)

                    if result.startswith("http") == False and result[0] == "/":
                        result = re.sub(url, "", result)
                        result = re.sub("www", "", result)
                        website_list.append(my_url + result)

                #slash
                slash = re.findall("[\'|\"]/\S+[\"|\']", my_request)

                for i in slash:
                    my_search = re.search("\.com|\.edu|\.net|\.org|\.tv|www|http", i)

                    if not my_search:
                        j = re.sub("[\"\']", "", i)
                        j = re.split("[\(\)<>\[\],\{\};�\|]", j)
                        j = j[0]
                        website_list.append(my_url + j)

            else:
                print(color + str(status) + ": " + str(website_list[tracker]))
                website_list.pop(tracker)

        except IndexError:
            print(color + "done")
            break

        except:
            print(color + "ERROR: " + str(website_list[tracker]))
            website_list.pop(tracker)


    website_list = list(dict.fromkeys(website_list))

    website_list.sort()

    clear()

    return website_list

#scans for hyperlinks using selenium
def link_scanner_selenium(url):
    result = "http://" + url
    
    driver = webdriver.Firefox(service = Service(GeckoDriverManager().install()))

    i = -1
    total_web_list = []
    total_web_list.append(result)
    web_list = []

    while True:
        i = i + 1
        
        try:
            print(color + total_web_list[i])
            driver.get(total_web_list[i])

        except IndexError:
            break

        except:
            continue
        
        try:
            for ii in driver.find_elements(by = By.XPATH, value = ".//a"):
                web_list.append(ii.get_attribute("href"))

        except:
            pass

        web_list = list(dict.fromkeys(web_list))

        for iii in web_list:
            try:
                domain_name = result in iii

                parse = iii.index(result, 0, len(result))
                
                if domain_name == True and parse == 0:
                    total_web_list.append(iii)
                    total_web_list = list(dict.fromkeys(total_web_list))

            except:
                continue

    total_web_list = list(dict.fromkeys(total_web_list))
    total_web_list.sort()

    clear()

    return total_web_list

def nmap(ip = 192, bot = False):
    clear()
    
    progress = 0
    progress_tracker = 0

    result_list = []

    print(color + str(progress_tracker) + "%")

    if ip == 192:
        total_progress = 65536

        for i in range(0, 256):
            for ii in range(0, 256):
                if bot == True:
                    anti_bot = random.uniform(1, 60)
                    
                    time.sleep(anti_bot)

                progress += 1

                if progress % int(total_progress / 100) == 0:
                    clear()
                    progress_tracker += 1
                    print(color + str(progress_tracker) + "%")

                try:
                    result = socket.gethostbyaddr("192.168." + str(i) + "." + str(ii))
                    result_list.append(result)

                except socket.herror:
                    continue

        clear()
        for i in result_list:
            print(color + str(i))

    if ip == 172:
        total_progress = 983040
        
        for pwn in range(16, 32):
            for i in range(0, 256):
                for ii in range(0, 256):
                    if bot == True:
                        anti_bot = random.uniform(1, 60)
                        
                        time.sleep(anti_bot)
                        
                    progress += 1

                    if progress % int(total_progress / 100) == 0:
                        clear()
                        progress_tracker += 1
                        print(color + str(progress_tracker) + "%")

                    try:
                        result = socket.gethostbyaddr("172" + "." + str(pwn) + "." + str(i) + "." + str(ii))
                        result_list.append(result)

                    except socket.herror:
                        continue

        clear()
        for i in result_list:
            print(color + str(i))

    if ip == 10:
        total_progress = 16711680

        for pwn in range(0, 256):
            for i in range(0, 256):
                for ii in range(0, 256):
                    if bot == True:
                        anti_bot = random.uniform(1, 60)
                        
                        time.sleep(anti_bot)
                        
                    progress += 1

                    if progress % int(total_progress / 100) == 0:
                        clear()
                        progress_tracker += 1
                        print(color + str(progress_tracker) + "%")

                    try:
                        result = socket.gethostbyaddr("10" + "." + str(pwn) + "." + str(i) + "." + str(ii))
                        result_list.append(result)

                    except socket.herror:
                        continue

        clear()
        for i in result_list:
            print(color + str(i))

def packet_sniffer(protocol = " ", data = False, parse = " ", hex_dump = False):
    clear()

    cyan = "\033[1;36m"
    green = "\033[0;32m"

    my_socket = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))

    while True:
        try:
            packet = my_socket.recvfrom(65536)

            #data
            data_hex = binascii.hexlify(packet[0])
            data_hex = str(data_hex).replace("b'", "")
            data_hex = data_hex.replace("'", "")

            data_ascii = codecs.decode(packet[0], errors = "replace")
            
            #mac stuff
            mac_destination = struct.unpack("!6s", packet[0][0:6])
            super_mac_destination = binascii.hexlify(mac_destination[0])
            super_mac_destination = str(super_mac_destination).replace("b'", "")
            super_mac_destination = super_mac_destination.replace("'", "")

            mac_source = struct.unpack("!6s", packet[0][6:12])
            super_mac_source = binascii.hexlify(mac_source[0])
            super_mac_source = str(super_mac_source).replace("b'", "")
            super_mac_source = super_mac_source.replace("'", "")

            #protocol
            my_protocol = struct.unpack("!1s", packet[0][23:24])
            super_protocol = binascii.hexlify(my_protocol[0])
            super_protocol = str(super_protocol).replace("b'", "")
            super_protocol = super_protocol.replace("'", "")

            proto = super_protocol

            if super_protocol == "00":
                proto = "HOPOPT"

            if super_protocol == "01":
                proto = "ICMP"

            if super_protocol == "02":
                proto = "IGMP"

            if super_protocol == "03":
                proto = "GGP"

            if super_protocol == "04":
                proto = "IP-in-IP"

            if super_protocol == "05":
                proto = "ST"
            
            if super_protocol == "06":
                proto = "TCP"

            if super_protocol == "07":
                proto = "CBT"

            if super_protocol == "08":
                proto = "EGP"

            if super_protocol == "09":
                proto = "IGP"

            if super_protocol == "0a":
                proto = "BBN-RCC-MON"

            if super_protocol == "0b":
                proto = "NVP-II"

            if super_protocol == "0c":
                proto = "PUP"

            if super_protocol == "0d":
                proto = "ARGUS"

            if super_protocol == "0e":
                proto = "EMCON"

            if super_protocol == "0f":
                proto = "XNET"

            if super_protocol == "10":
                proto = "CHAOS"

            if super_protocol == "11":
                proto = "UDP"

            if super_protocol == "12":
                proto = "MUX"

            if super_protocol == "13":
                proto = "DCN-MEAS"

            if super_protocol == "14":
                proto = "HMP"

            if super_protocol == "15":
                proto = "PRM"

            if super_protocol == "16":
                proto = "XNS-IDP"

            if super_protocol == "17":
                proto = "TRUNK-1"

            if super_protocol == "18":
                proto = "TRUNK-2"

            if super_protocol == "19":
                proto = "LEAF-1"

            if super_protocol == "1a":
                proto = "LEAF-2"

            if super_protocol == "1b":
                proto = "RDP"

            if super_protocol == "1c":
                proto = "IRTP"

            if super_protocol == "1d":
                proto = "ISO-TP4"

            if super_protocol == "1e":
                proto = "NETBLT"

            if super_protocol == "1f":
                proto = "MFE-NSP"

            if super_protocol == "20":
                proto = "MERIT-INP"

            if super_protocol == "21":
                proto = "DCCP"

            if super_protocol == "22":
                proto = "3PC"

            if super_protocol == "23":
                proto = "IDPR"

            if super_protocol == "24":
                proto = "XTP"

            if super_protocol == "25":
                proto = "DDP"

            if super_protocol == "26":
                proto = "IDPR-CMTP"

            if super_protocol == "27":
                proto = "TP++"

            if super_protocol == "28":
                proto = "IL"

            if super_protocol == "29":
                proto = "IPv6"

            if super_protocol == "2a":
                proto = "SDRP"

            if super_protocol == "2b":
                proto = "IPv6-Route"

            if super_protocol == "2c":
                proto = "IPv6-Frag"

            if super_protocol == "2d":
                proto = "IDRP"

            if super_protocol == "2e":
                proto = "RSVP"

            if super_protocol == "2f":
                proto = "GRE"

            if super_protocol == "30":
                proto = "DSR"

            if super_protocol == "31":
                proto = "BNA"

            if super_protocol == "32":
                proto = "ESP"

            if super_protocol == "33":
                proto = "AH"

            if super_protocol == "34":
                proto = "I-NLSP"

            if super_protocol == "35":
                proto = "SwIPe"

            if super_protocol == "36":
                proto = "NARP"

            if super_protocol == "37":
                proto = "MOBILE"

            if super_protocol == "38":
                proto = "TLSP"

            if super_protocol == "39":
                proto = "SKIP"

            if super_protocol == "3a":
                proto = "IPv6-ICMP"

            if super_protocol == "3b":
                proto = "IPv6-NoNxt"

            if super_protocol == "3c":
                proto = "IPv6-Opts"

            if super_protocol == "3d":
                proto = "3d"

            if super_protocol == "3e":
                proto = "CFTP"

            if super_protocol == "3f":
                proto = "3f"

            if super_protocol == "40":
                proto = "SAT-EXPAK"

            if super_protocol == "41":
                proto = "KRYPTOLAN"

            if super_protocol == "42":
                proto = "RVD"

            if super_protocol == "43":
                proto = "IPPC"

            if super_protocol == "44":
                proto = "44"

            if super_protocol == "45":
                proto = "SAT-MON"

            if super_protocol == "46":
                proto = "VISA"

            if super_protocol == "47":
                proto = "IPCU"

            if super_protocol == "48":
                proto = "CPNX"

            if super_protocol == "49":
                proto = "CPHB"

            if super_protocol == "4a":
                proto = "WSN"

            if super_protocol == "4b":
                proto = "PVP"

            if super_protocol == "4c":
                proto = "BR-SAT-MON"

            if super_protocol == "4d":
                proto = "SUN-ND"

            if super_protocol == "4e":
                proto = "WB-MON"

            if super_protocol == "4f":
                proto = "WB-EXPAK"

            if super_protocol == "50":
                proto = "ISO-IP"

            if super_protocol == "51":
                proto = "VMTP"

            if super_protocol == "52":
                proto = "SECURE-VMTP"

            if super_protocol == "53":
                proto = "VINES"

            if super_protocol == "54":
                proto = "TTP"

            if super_protocol == "55":
                proto = "NSFNET-IGP"

            if super_protocol == "56":
                proto = "DGP"

            if super_protocol == "57":
                proto = "TCF"

            if super_protocol == "58":
                proto = "EIGRP"

            if super_protocol == "59":
                proto = "OSPF"

            if super_protocol == "5a":
                proto = "Sprite-RPC"

            if super_protocol == "5b":
                proto = "LARP"

            if super_protocol == "5c":
                proto = "MTP"

            if super_protocol == "5d":
                proto = "AX.25"

            if super_protocol == "5e":
                proto = "OS"

            if super_protocol == "5f":
                proto = "MICP"

            if super_protocol == "61":
                proto = "ETHERIP"

            if super_protocol == "62":
                proto = "ENCAP"

            if super_mac_destination == "ffffffffffff":
                proto = "ARP"

            #ip stuff
            ip_header = packet[0][26:34]
            super_ip_header = struct.unpack("!4s4s", ip_header)

            #formatting
            destination = socket.inet_ntoa(super_ip_header[1])
            source = socket.inet_ntoa(super_ip_header[0])

            #checksum
            checksum = packet[0][24:26]
            checksum = struct.unpack("!2s", checksum)
            checksum = binascii.hexlify(checksum[0])
            checksum = str(checksum).replace("b'", "")
            checksum = checksum.replace("'", "")

            #protocol header
            source_port = packet[0][34:36]
            source_port = struct.unpack("!2s", source_port)
            source_port = binascii.hexlify(source_port[0])
            source_port = int(source_port, 16)

            destination_port = packet[0][36:38]
            destination_port = struct.unpack("!2s", destination_port)
            destination_port = binascii.hexlify(destination_port[0])
            destination_port = int(destination_port, 16)
            
            if proto == "UDP":
                checksum_protocol_udp = packet[0][40:42]
                checksum_protocol_udp = struct.unpack("!2s", checksum_protocol_udp)
                checksum_protocol_udp = binascii.hexlify(checksum_protocol_udp[0])
                checksum_protocol_udp = str(checksum_protocol_udp).replace("b'", "")
                checksum_protocol_udp = checksum_protocol_udp.replace("'", "")

            if proto == "TCP":
                try:
                    checksum_protocol_tcp = packet[0][42:44]
                    checksum_protocol_tcp = struct.unpack("!2s", checksum_protocol_tcp)
                    checksum_protocol_tcp = binascii.hexlify(checksum_protocol_tcp[0])
                    checksum_protocol_tcp = str(checksum_protocol_tcp).replace("b'", "")
                    checksum_protocol_tcp = checksum_protocol_tcp.replace("'", "")

                except:
                    pass
                
            #other protocols
            if destination_port == 22 or source_port == 22:
                proto = "SSH"
                
            if destination_port == 80 or source_port == 80:
                proto = "HTTP"

            if destination_port == 443 or source_port == 443:
                proto = "HTTPS"
            
            #display
            if protocol == " ":
                print(color + "source ip: " + str(source) + " | source mac: " + str(super_mac_source) + " | source port: " + str(source_port))
                print(color + "destination ip: " + str(destination) + " | destination mac: " + str(super_mac_destination) + " | destination port: " + str(destination_port))
                print(color + "protocol: " + proto)

                if proto == "UDP":
                    print(color + "checksum (ip): " + checksum + " | checksum (protocol): " + str(checksum_protocol_udp))

                if proto == "TCP":
                    print(color + "checksum (ip): " + checksum + " | checksum (protocol): " + str(checksum_protocol_tcp))

                if parse == "all":
                    email = re.findall("[a-z0-9]+@[a-z0-9]+[.][a-z]+", data_ascii)
                    email = list(dict.fromkeys(email))
                    website = re.findall("[^\"\'=]https://|http://|www\S+[$;\"\']", str(packet[0]))
                    website = list(dict.fromkeys(website))

                    if len(email) > 0 or len(website) > 0:
                        print(color + "emails: " + str(email))
                        print(color + "websites: " + str(website))

                if parse == "email":
                    email = re.findall("[a-z0-9]+@[a-z0-9]+[.][a-z]+", str(packet[0]))
                    email = list(dict.fromkeys(email))

                    if len(email) > 0:
                        print(color + "emails: " + str(email))

                if parse == "url":
                    website = re.findall("[^\"\'=]https://|http://|www\S+[$;\"\']", str(packet[0]))
                    website = list(dict.fromkeys(website))

                    if len(website) > 0:
                        print(color + "websites: " + str(website))

                
                if data == True:
                    print(cyan + "hex data: " + str(data_hex))
                    print(green + "utf-8 data: " + str(data_ascii))

                if hex_dump == True:
                    with open("hex dump.txt", "a") as file:
                        file.write(data_hex + "\n")

                print("")

            if protocol == proto:
                print(color + "source ip: " + str(source) + " | source mac: " + str(super_mac_source) + " | source port: " + str(source_port))
                print(color + "destination ip: " + str(destination) + " | destination mac: " + str(super_mac_destination) + " | destination port: " + str(destination_port))
                print(color + "protocol: " + proto)

                if proto == "UDP":
                    print(color + "checksum (ip): " + checksum + " | checksum (protocol): " + str(checksum_protocol_udp))

                if proto == "TCP":
                    print(color + "checksum (ip): " + checksum + " | checksum (protocol): " + str(checksum_protocol_tcp))

                if parse == "all":
                    email = re.findall("[a-z0-9]+@[a-z0-9]+[.][a-z]+", packet[0])
                    email = list(dict.fromkeys(email))
                    website = re.findall("[^\"\'=]https://|http://|www\S+[$;\"\']", str(packet[0]))
                    website = list(dict.fromkeys(website))

                    if len(email) > 0 or len(website) > 0:
                        print(color + "emails: " + str(email))
                        print(color + "websites: " + str(website))

                if parse == "email":
                    email = re.findall("[a-z0-9]+@[a-z0-9]+[.][a-z]+", str(packet[0]))
                    email = list(dict.fromkeys(email))

                    if len(email) > 0:
                        print(color + "emails: " + str(email))

                if parse == "url":
                    website = re.findall("[^\"\'=]https://|http://|www\S+[$;\"\']", str(packet[0]))
                    website = list(dict.fromkeys(website))

                    if len(website) > 0:
                        print(color + "websites: " + str(website))
                        
                if data == True:
                    print(cyan + "hex data: " + str(data_hex))
                    print(green + "utf-8 data: " + str(data_ascii))

                if hex_dump == True:
                    with open("hex dump.txt", "a") as file:
                        file.write(data_hex + "\n")
                        
                print("")

        except:
            print(color + "ERROR!")
            continue

def port_scanner(url, bot = False):
    clear()
    my_list = []

    for port in range(1,65535):
        if bot == True:
            anti_bot = random.uniform(1, 60)
            
            time.sleep(anti_bot)
            
        print(color + "checking port: " + str(port))
        sock = socket.socket()
        sock.settimeout(0.5)
        result = sock.connect_ex((url, port))
        sock.close()

        if result == 0:
            print(True)
            my_list.append(port)

        else:
            print(False)

    clear()
    return my_list

def search_engine_string(url, string, secure = True, bot = False):
    if secure == True:
        my_secure = "https://"

    if secure == False:
        my_secure = "http://"

    clear()
    user_input = input("1 = scan all | 2 = scan domain\n")
    clear()

    counter = 0

    string_list = []
    web_list = []

    web_list.append(my_secure + url)

    if user_input == "1":
        while True:
            if bot == True:
                anti_bot = random.uniform(1, 60)
                
                time.sleep(anti_bot)
                
            try:
                done = web_list[counter]

            except IndexError:
                break
            
            try:
                my_request = web_session.get(web_list[counter], headers = user_agent, timeout = (5,30)).text

                if string in my_request:
                    print(color + web_list[counter])
                    string_list.append(web_list[counter])

            except:
                pass

            counter += 1

            if len(my_request) <= 25000000:
                website = re.findall("[^\"\'=]https://|http://|www\S+[$;\"\']", my_request)
                website = list(dict.fromkeys(website))

                for i in website:
                    clean = i.replace('"', " ")
                    clean = clean.replace("'", " ")
                    clean = clean.replace(";", " ")
                    clean = clean.replace("///", " ")
                    clean = clean.replace("\\", "")
                    clean = clean.replace("%", " ")
                    clean = clean.split()

                    
                    try:
                        if "http" not in i:
                            web_list.append(my_secure + clean[0])

                        else:
                            web_list.append(clean[0])

                    except:
                        pass

                web_list = list(dict.fromkeys(web_list))

    if user_input == "2":
        while True:
            if bot == True:
                anti_bot = random.uniform(1, 60)
                
                time.sleep(anti_bot)

            try:
                done = web_list[counter]

            except IndexError:
                break
            
            try:
                my_request = web_session.get(web_list[counter], headers = user_agent, timeout = (5,30)).text

                if string in my_request:
                    print(color + web_list[counter])
                    string_list.append(web_list[counter])

            except:
                pass

            counter += 1

            if len(my_request) <= 25000000:
                website = re.findall("[^\"\'=]https://|http://|www\S+[$;\"\']", my_request)
                website = list(dict.fromkeys(website))

                for i in website:
                    if i in url:
                        clean = i.replace('"', " ")
                        clean = clean.replace("'", " ")
                        clean = clean.replace(";", " ")
                        clean = clean.replace("///", " ")
                        clean = clean.replace("\\", "")
                        clean = clean.replace("%", " ")
                        clean = clean.split()

                        try:
                            if "http" not in i:
                                web_list.append(my_secure + clean[0])

                            else:
                                web_list.append(clean[0])

                        except:
                            pass

                href = re.findall("href=\S+", my_request)
                href = list(dict.fromkeys(href))

            for i in href:
                    clean = i.replace('"', "")
                    clean = clean.replace("'", "")
                    clean = clean.replace(";", " ")
                    clean = clean.replace("///", " ")
                    clean = clean.replace("\\", "")
                    clean = clean.replace(">", " ")
                    clean = clean.replace("href=", "")
                    clean = clean.replace("%", " ")
                    clean = clean.split()

                    try:
                        if "http" not in i:
                            web_list.append(my_secure + url + "/" + clean[0])

                        else:
                            if url in i:
                                web_list.append(clean[0])

                    except:
                        pass

            web_list = list(dict.fromkeys(web_list))

    clear()

    return web_list

def source_code_viewer(file, keyword = ""):
    clear()

    count = 0
    
    with open(file, "rb") as f:
        for i in f:
            hex_code = str(i).replace("b'", "")
            hex_code = str(hex_code).replace("'", "")
            hex_code = str(hex_code).replace("b\"", "")
            hex_code = str(hex_code).replace("\"", "")
            hex_code = str(hex_code).replace("\\x", "")

            result = str(i, "ascii", errors = "replace")

            if keyword in result or keyword in hex_code:
                print(color + result)
                print(color + hex_code)

                count += 1

                if count == 128:
                    count = 0
                    pause = input()

    print(color + "\ndone")
    
def sql_injection_scanner(url, secure = True, bot = False):
    if secure == True:
        my_secure = "https://"

    if secure == False:
        my_secure = "http://"
    
    my_url = my_secure + url

    #sql errors
    error_message = {"SQL syntax.*?MySQL", "Warning.*?\Wmysqli?_", "MySQLSyntaxErrorException", "valid MySQL result", "check the manual that (corresponds to|fits) your MySQL server version", "check the manual that (corresponds to|fits) your MariaDB server version", "check the manual that (corresponds to|fits) your Drizzle server version", "Unknown column '[^ ]+' in 'field list'", "MySqlClient\.", "com\.mysql\.jdbc", "Zend_Db_(Adapter|Statement)_Mysqli_Exception", "Pdo\[./_\\]Mysql", "MySqlException", "SQLSTATE\[\d+\]: Syntax error or access violation", "MemSQL does not support this type of query", "is not supported by MemSQL", "unsupported nested scalar subselect", "PostgreSQL.*?ERROR", "Warning.*?\Wpg_", "valid PostgreSQL result", "Npgsql\.", "PG::SyntaxError:", "org\.postgresql\.util\.PSQLException", "ERROR:\s\ssyntax error at or near", "ERROR: parser: parse error at or near", "PostgreSQL query failed", "org\.postgresql\.jdbc", "Pdo\[./_\\]Pgsql", "PSQLException", "OLE DB.*? SQL Server", "\bSQL Server[^&lt;&quot;]+Driver", "Warning.*?\W(mssql|sqlsrv)_", "\bSQL Server[^&lt;&quot;]+[0-9a-fA-F]{8}", "System\.Data\.SqlClient\.(SqlException|SqlConnection\.OnError)", "(?s)Exception.*?\bRoadhouse\.Cms\.", "Microsoft SQL Native Client error '[0-9a-fA-F]{8}", "\[SQL Server\]", "ODBC SQL Server Driver", "ODBC Driver \d+ for SQL Server", "SQLServer JDBC Driver", "com\.jnetdirect\.jsql", "macromedia\.jdbc\.sqlserver", "Zend_Db_(Adapter|Statement)_Sqlsrv_Exception", "com\.microsoft\.sqlserver\.jdbc", "Pdo\[./_\\](Mssql|SqlSrv)", "SQL(Srv|Server)Exception", "Unclosed quotation mark after the character string", "Microsoft Access (\d+ )?Driver", "JET Database Engine", "Access Database Engine", "ODBC Microsoft Access", "Syntax error \(missing operator\) in query expression", "\bORA-\d{5}", "Oracle error", "Oracle.*?Driver", "Warning.*?\W(oci|ora)_", "quoted string not properly terminated", "SQL command not properly ended", "macromedia\.jdbc\.oracle", "oracle\.jdbc", "Zend_Db_(Adapter|Statement)_Oracle_Exception", "Pdo\[./_\\](Oracle|OCI)", "OracleException", "CLI Driver.*?DB2", "DB2 SQL error", "\bdb2_\w+\(", "SQLCODE[=:\d, -]+SQLSTATE", "com\.ibm\.db2\.jcc", "Zend_Db_(Adapter|Statement)_Db2_Exception", "Pdo\[./_\\]Ibm", "DB2Exception", "ibm_db_dbi\.ProgrammingError", "Warning.*?\Wifx_", "Exception.*?Informix", "Informix ODBC Driver", "ODBC Informix driver", "com\.informix\.jdbc", "weblogic\.jdbc\.informix", "Pdo\[./_\\]Informix", "IfxException", "Dynamic SQL Error", "Warning.*?\Wibase_", "org\.firebirdsql\.jdbc", "Pdo\[./_\\]Firebird", "SQLite/JDBCDriver", "SQLite\.Exception", "(Microsoft|System)\.Data\.SQLite\.SQLiteException", "Warning.*?\W(sqlite_|SQLite3::)", "\[SQLITE_ERROR\]", "SQLite error \d+:", "sqlite3.OperationalError:", "SQLite3::SQLException", "org\.sqlite\.JDBC", "Pdo\[./_\\]Sqlite", "SQLiteException", "SQL error.*?POS([0-9]+)", "Warning.*?\Wmaxdb_", "DriverSapDB", "-3014.*?Invalid end of SQL statement", "com\.sap\.dbtech\.jdbc", "\[-3008\].*?: Invalid keyword or missing delimiter", "Warning.*?\Wsybase_", "Sybase message", "Sybase.*?Server message", "SybSQLException", "Sybase\.Data\.AseClient", "com\.sybase\.jdbc", "Warning.*?\Wingres_", "Ingres SQLSTATE", "Ingres\W.*?Driver", "com\.ingres\.gcf\.jdbc", "Exception (condition )?\d+\. Transaction rollback", "com\.frontbase\.jdbc", "Syntax error 1. Missing", "(Semantic|Syntax) error [1-4]\d{2}\.", "Unexpected end of command in statement \[", "Unexpected token.*?in statement \[", "org\.hsqldb\.jdbc", "org\.h2\.jdbc", "\[42000-192\]", "![0-9]{5}![^\n]+(failed|unexpected|error|syntax|expected|violation|exception)", "\[MonetDB\]\[ODBC Driver", "nl\.cwi\.monetdb\.jdbc", "Syntax error: Encountered", "org\.apache\.derby", "ERROR 42X01", ", Sqlstate: (3F|42).{3}, (Routine|Hint|Position):", "/vertica/Parser/scan", "com\.vertica\.jdbc", "org\.jkiss\.dbeaver\.ext\.vertica", "com\.vertica\.dsi\.dataengine", "com\.mckoi\.JDBCDriver", "com\.mckoi\.database\.jdbc", "&lt;REGEX_LITERAL&gt;", "com\.facebook\.presto\.jdbc", "io\.prestosql\.jdbc", "com\.simba\.presto\.jdbc", "UNION query has different number of fields: \d+, \d+", "Altibase\.jdbc\.driver", "com\.mimer\.jdbc", "Syntax error,[^\n]+assumed to mean", "io\.crate\.client\.jdbc", "encountered after end of query", "A comparison operator is required here", "-10048: Syntax error", "rdmStmtPrepare\(.+?\) returned", "SQ074: Line \d+:", "SR185: Undefined procedure", "SQ200: No table ", "Virtuoso S0002 Error", "\[(Virtuoso Driver|Virtuoso iODBC Driver)\]\[Virtuoso Server\]"}
    
    #malicious sql code
    email_mal = re.sub("www", "", url)
    boolean_sql = ['support" or "1" = "1', "support' or '1' = '1", "support@" + str(email_mal) + '" or "1" = "1', "support@" + str(email_mal) + "' or '1' = '1"]
    mal_sql = ["\"", "\'", ";", "*"]
    mal_password = "Pa$$w0rd"

    my_list = []

    clear()

    user_input = input("1 = scan url | 2 = scan url and hyperlinks (requests) | 3 = scan url and hyperlinks (selenium)\n")

    clear()
    
    if user_input == "1":
        for c in mal_sql:
            new_url = f"{my_url}{c}"
            print(color + "checking: " + new_url)

            if bot == True:
                anti_bot = random.uniform(1, 60)
                
                time.sleep(anti_bot)
            
            try:
                result = web_session.get(new_url, verify = False, headers = user_agent, timeout = (5, 30))
                
                if len(result.text) >= 25000000:
                    gpu = tf.py_function(func = gpu_sql_error, inp = [new_url], Tout = tf.string)

                    gpu = re.findall("b\'.+?\'", str(gpu))
                    gpu = re.sub("b\'", "", gpu[0])
                    gpu = gpu[:-1]

                    if gpu != "none":
                        print(color + gpu)
                        my_list.append(gpu)
                        
    
                if len(result.text) < 25000000:
                    for i in error_message:
                        my_regex = re.search(i, result.text)

                        try:
                            if my_regex:
                                print(color + "true: " + str(i) + " " + str(my_regex.span()) + " " + new_url)
                                my_list.append("true: " + str(i) + " " + str(my_regex.span()) + " " + new_url)
                                break

                        except UnicodeDecodeError:
                            break

            except requests.exceptions.SSLError:
                print(color + "ERROR: invalid certificate!")
                continue

            except urllib3.exceptions.LocationParseError:
                print(color + "ERROR: location parse error!")
                continue

            except requests.exceptions.ConnectionError:
                print(color + "ERROR: connection error!")
                continue

            except requests.exceptions.ConnectTimeout:
                print(color + "ERROR: connect timeout!")
                continue

            except requests.exceptions.InvalidSchema:
                print(color + "ERROR: invalid schema!")
                continue

            except requests.exceptions.InvalidURL:
                print(color + "ERROR: invalid url!")
                continue

            except requests.exceptions.MissingSchema:
                print(color + "ERROR: missing schema!")
                continue

            except requests.exceptions.TooManyRedirects:
                print(color + "ERROR: too many redirects!")
                continue

            except requests.exceptions.ReadTimeout:
                print(color + "ERROR: read timeout!")
                continue

        try:
            print(color + "checking for forms on: " + my_url)

            get_input = form_scanner(url, secure = secure, parse = "input")

            form_list = []
            password_form = ""

            try:
                for i in get_input:
                    if "email" in str(i):
                        name = str(re.findall("name.+\".+\"", i)).split("\"")
                        form_list.append(name[1])

                    if "hidden" in str(i):
                        name = str(re.findall("name.+\".+\"", i)).split("\"")
                        form_list.append(name[1])
                        
                    if "number" in str(i):
                        name = str(re.findall("name.+\".+\"", i)).split("\"")
                        form_list.append(name[1])

                    if "password" in str(i):
                        name = str(re.findall("name.+\".+\"", i)).split("\"")
                        form_list.append(name[1])
                        password_form = name[1]

                    if "query" in str(i):
                        name = str(re.findall("name.+\".+\"", i)).split("\"")
                        form_list.append(name[1])

                    if "search" in str(i):
                        name = str(re.findall("name.+\".+\"", i)).split("\"")
                        form_list.append(name[1])

                    if "tel" in str(i):
                        name = str(re.findall("name.+\".+\"", i)).split("\"")
                        form_list.append(name[1])

                    if "text" in str(i):
                        name = str(re.findall("name.+\".+\"", i)).split("\"")
                        form_list.append(name[1])
                        

                    if "url" in str(i):
                        name = str(re.findall("name.+\".+\"", i)).split("\"")
                        form_list.append(name[1])

            except:
                pass

            form_list = list(dict.fromkeys(form_list))
            form_list.sort()

            my_forms = form_scanner(url, secure = secure)

            for forms in form_list:
                if bot == True:
                    anti_bot = random.uniform(1, 60)
                    
                    time.sleep(anti_bot)

                for i in my_forms:
                    name_regex = re.search(forms, i)
                    get_regex = re.search("get", i)
                    post_regex = re.search("post", i)

                    if name_regex and get_regex:
                        password_search = re.sub(" ", "", i)
                        password_search = re.search("type=\"password\"", password_search)

                        if password_search:
                            for boolean_mal in boolean_sql:
                                try:
                                    mal_dict = {forms: boolean_mal, password_form: mal_password}

                                    print(color + "checking form (" + boolean_mal + "): " + forms)

                                    get = web_session.get(my_url, verify = False, headers = user_agent, timeout = (5, 30))
                                    get_check = web_session.get(my_url, params = mal_dict, verify = False, headers = user_agent, timeout = (5, 30))

                                    if get.text != get_check.text:
                                        print(color + "true: " + boolean_mal + " " + url + " form: " + forms + " (boolean)")
                                        my_list.append("true: " + boolean_mal + " " + url + " form: " + forms + " (boolean)")

                                except:
                                    pass

                    if name_regex and post_regex:
                        password_search = re.sub(" ", "", i)
                        password_search = re.search("type=\"password\"", password_search)

                        if password_search:
                            for boolean_mal in boolean_sql:
                                try:
                                    mal_dict = {forms: boolean_mal, password_form: mal_password}

                                    print(color + "checking form (" + boolean_mal + "): " + forms)

                                    post = web_session.get(my_url, verify = False, headers = user_agent, timeout = (5, 30))
                                    post_check = web_session.post(my_url, data = mal_dict, verify = False, headers = user_agent, timeout = (5, 30))

                                    if post.text != post_check.text:
                                        print(color + "true: " + boolean_mal + " " + url + " form: " + forms + " (boolean)")
                                        my_list.append("true: " + boolean_mal + " " + url + " form: " + forms + " (boolean)")

                                except:
                                    pass

            for forms in form_list:
                for mal in mal_sql:
                    form_dict = {forms: mal}

                    if bot == True:
                        anti_bot = random.uniform(1, 60)
                        
                        time.sleep(anti_bot)

                    for i in my_forms:
                        name_regex = re.search(forms, i)
                        get_regex = re.search("get", i)
                        post_regex = re.search("post", i)
                        
                        if name_regex and get_regex:
                            print(color + "checking form (" + mal + "): " + forms)
                            get_data = web_session.get(my_url, params = form_dict, verify = False, headers = user_agent, timeout = (5, 30)).text

                            for ii in error_message:
                                my_regex = re.search(ii, get_data)
                                my_boolean = False

                                try:
                                    if my_regex:
                                            my_boolean = True
                                            break

                                except UnicodeDecodeError:
                                    continue
                                
                                if my_boolean == True:
                                    print(color + "true: " + url + " form: " + forms + " (error)")
                                    my_list.append(url + " form: " + forms + " (error)")

                        if name_regex and post_regex:
                            print(color + "checking form (" + mal + "): " + forms)
                            send_data = web_session.post(my_url, data = form_dict, verify = False, headers = user_agent, timeout = (5, 30)).text

                            for ii in error_message:
                                my_regex = re.search(ii, send_data)
                                my_boolean = False

                                try:
                                    if my_regex:
                                        my_boolean = True
                                        break

                                except UnicodeDecodeError:
                                    continue

                                if my_boolean == True:
                                    print(color + "true: " + url + " form: " + forms + " (error)")
                                    my_list.append(url + " form: " + forms + " (error)")

        except requests.exceptions.SSLError:
            print(color + "ERROR: invalid certificate!")
            pass

        except urllib3.exceptions.LocationParseError:
            print(color + "ERROR: location parse error!")
            pass

        except requests.exceptions.ConnectionError:
            print(color + "ERROR: connection error!")
            pass

        except requests.exceptions.ConnectTimeout:
            print(color + "ERROR: connect timeout!")
            pass

        except requests.exceptions.InvalidSchema:
            print(color + "ERROR: invalid schema!")
            pass

        except requests.exceptions.InvalidURL:
            print(color + "ERROR: invalid url!")
            pass

        except requests.exceptions.MissingSchema:
            print(color + "ERROR: missing schema!")
            pass

        except requests.exceptions.TooManyRedirects:
            print(color + "ERROR: too many redirects!")
            pass

        except requests.exceptions.ReadTimeout:
            print(color + "ERROR: read timeout!")
            pass

    if user_input == "2":
        my_result = link_scanner(url, secure = secure, bot = bot)

        for j in my_result:
            for c in mal_sql:
                new_url = f"{j}{c}"

                if bot == True:
                    anti_bot = random.uniform(1, 60)
                    
                    time.sleep(anti_bot)

                print(color + "checking: " + new_url)

                try:
                    result = web_session.get(new_url, verify = False, headers = user_agent, timeout = (5, 30))

                    if len(result.text) >= 25000000:
                        gpu = tf.py_function(func = gpu_sql_error, inp = [new_url], Tout = tf.string)

                        gpu = re.findall("b\'.+?\'", str(gpu))
                        gpu = re.sub("b\'", "", gpu[0])
                        gpu = gpu[:-1]

                        if gpu != "none":
                            print(color + gpu)
                            my_list.append(gpu)
                            
        
                    if len(result.text) < 25000000:
                        for i in error_message:
                            my_regex = re.search(i, result.text)

                            try:
                                if my_regex:
                                    print(color + "true: " + str(i) + " " + str(my_regex.span()) + " " + new_url)
                                    my_list.append("true: " + str(i) + " " + str(my_regex.span()) + " " + new_url)
                                    break

                            except UnicodeDecodeError:
                                break

                except requests.exceptions.SSLError:
                    print(color + "ERROR: invalid certificate!")
                    pass

                except urllib3.exceptions.LocationParseError:
                    print(color + "ERROR: location parse error!")
                    pass

                except requests.exceptions.ConnectionError:
                    print(color + "ERROR: connection error!")
                    pass

                except requests.exceptions.ConnectTimeout:
                    print(color + "ERROR: connect timeout!")
                    pass

                except requests.exceptions.InvalidSchema:
                    print(color + "ERROR: invalid schema!")
                    pass

                except requests.exceptions.InvalidURL:
                    print(color + "ERROR: invalid url!")
                    pass

                except requests.exceptions.MissingSchema:
                    print(color + "ERROR: missing schema!")
                    pass

                except requests.exceptions.TooManyRedirects:
                    print(color + "ERROR: too many redirects!")
                    pass

                except requests.exceptions.ReadTimeout:
                    print(color + "ERROR: read timeout!")
                    pass
                
            try:
                print(color + "checking for forms on: " + j)

                if "http://" in j:
                    super_j = re.sub("http://", "", j)

                if "https://" in j:
                    super_j = re.sub("https://", "", j)

                get_input = form_scanner(super_j, secure = secure, parse = "input")

                form_list = []

                try:
                    for i in get_input:
                        if "email" in str(i):
                            name = str(re.findall("name.+\".+\"", i)).split("\"")
                            form_list.append(name[1])

                        if "hidden" in str(i):
                            name = str(re.findall("name.+\".+\"", i)).split("\"")
                            form_list.append(name[1])
                            
                        if "number" in str(i):
                            name = str(re.findall("name.+\".+\"", i)).split("\"")
                            form_list.append(name[1])

                        if "password" in str(i):
                            name = str(re.findall("name.+\".+\"", i)).split("\"")
                            form_list.append(name[1])
                            password_form = name[1]

                        if "query" in str(i):
                            name = str(re.findall("name.+\".+\"", i)).split("\"")
                            form_list.append(name[1])

                        if "search" in str(i):
                            name = str(re.findall("name.+\".+\"", i)).split("\"")
                            form_list.append(name[1])

                        if "tel" in str(i):
                            name = str(re.findall("name.+\".+\"", i)).split("\"")
                            form_list.append(name[1])

                        if "text" in str(i):
                            name = str(re.findall("name.+\".+\"", i)).split("\"")
                            form_list.append(name[1])

                        if "url" in str(i):
                            name = str(re.findall("name.+\".+\"", i)).split("\"")
                            form_list.append(name[1])

                except:
                    pass

                form_list = list(dict.fromkeys(form_list))
                form_list.sort()

                if "http://" in j:
                    super_j = re.sub("http://", "", j)

                if "https://" in j:
                    super_j = re.sub("https://", "", j)

                my_forms = form_scanner(super_j, secure = secure)

                for forms in form_list:
                    if bot == True:
                        anti_bot = random.uniform(1, 60)
                        
                        time.sleep(anti_bot)

                    for i in my_forms:
                        name_regex = re.search(forms, i)
                        get_regex = re.search("get", i)
                        post_regex = re.search("post", i)

                        if name_regex and get_regex:
                            password_search = re.sub(" ", "", i)
                            password_search = re.search("type=\"password\"", password_search)

                            if password_search:
                                for boolean_mal in boolean_sql:
                                    try:
                                        mal_dict = {forms: boolean_mal, password_form: mal_password}

                                        print(color + "checking form (" + boolean_mal + "): " + forms)

                                        get = web_session.get(j, verify = False, headers = user_agent, timeout = (5, 30))
                                        get_check = web_session.get(j, params = mal_dict, verify = False, headers = user_agent, timeout = (5, 30))

                                        if get.text != get_check.text:
                                            print(color + "true: " + boolean_mal + " " + url + " form: " + forms + " (boolean)")
                                            my_list.append("true: " + boolean_mal + " " + url + " form: " + forms + " (boolean)")

                                    except:
                                        pass

                        if name_regex and post_regex:
                            password_search = re.sub(" ", "", i)
                            password_search = re.search("type=\"password\"", password_search)

                            if password_search:
                                for boolean_mal in boolean_sql:
                                    try:
                                        mal_dict = {forms: boolean_mal, password_form: mal_password}

                                        print(color + "checking form (" + boolean_mal + "): " + forms)

                                        post = web_session.get(j, verify = False, headers = user_agent, timeout = (5, 30))
                                        post_check = web_session.post(j, data = mal_dict, verify = False, headers = user_agent, timeout = (5, 30))

                                        if post.text != post_check.text:
                                            print(color + "true: " + boolean_mal + " " + url + " form: " + forms + " (boolean)")
                                            my_list.append("true: " + boolean_mal + " " + url + " form: " + forms + " (boolean)")

                                    except:
                                        pass

                for forms in form_list:
                    for mal in mal_sql:
                        form_dict = {forms: mal}

                        if bot == True:
                            anti_bot = random.uniform(1, 60)
                            
                            time.sleep(anti_bot)

                        for i in my_forms:
                            name_regex = re.search(forms, i)
                            get_regex = re.search("get", i)
                            post_regex = re.search("post", i)
                            
                            if name_regex and get_regex:
                                print(color + "checking form (" + mal + "): " + forms)
                                get_data = web_session.get(j, params = form_dict, verify = False, headers = user_agent, timeout = (5, 30)).text

                                for ii in error_message:
                                    my_regex = re.search(ii, get_data)
                                    my_boolean = False

                                    try:
                                        if my_regex:
                                                my_boolean = True
                                                break

                                    except UnicodeDecodeError:
                                        continue
                                    
                                    if my_boolean == True:
                                        print(color + "true: " + j + " form: " + forms + " (error)")
                                        my_list.append(j + " form: " + forms + " (error)")

                            if name_regex and post_regex:
                                print(color + "checking form (" + mal + "): " + forms)
                                send_data = web_session.post(j, data = form_dict, verify = False, headers = user_agent, timeout = (5, 30)).text

                                for ii in error_message:
                                    my_regex = re.search(ii, send_data)
                                    my_boolean = False

                                    try:
                                        if my_regex:
                                            my_boolean = True
                                            break

                                    except UnicodeDecodeError:
                                        continue

                                    if my_boolean == True:
                                        print(color + "true: " + j + " form: " + forms + " (error)")
                                        my_list.append(j + " form: " + forms + " (error)")

            except requests.exceptions.SSLError:
                print(color + "ERROR: invalid certificate!")
                continue

            except urllib3.exceptions.LocationParseError:
                print(color + "ERROR: location parse error!")
                continue

            except requests.exceptions.ConnectionError:
                print(color + "ERROR: connection error!")
                continue

            except requests.exceptions.ConnectTimeout:
                print(color + "ERROR: connect timeout!")
                continue

            except requests.exceptions.InvalidSchema:
                print(color + "ERROR: invalid schema!")
                continue

            except requests.exceptions.InvalidURL:
                print("ERROR: invalid url!")
                continue

            except requests.exceptions.MissingSchema:
                print(color + "ERROR: missing schema!")
                continue

            except requests.exceptions.TooManyRedirects:
                print(color + "ERROR: too many redirects!")
                continue

            except requests.exceptions.ReadTimeout:
                print(color + "ERROR: read timeout!")
                continue

    if user_input == "3":
        my_result = link_scanner_selenium(url)

        for j in my_result:
            for c in mal_sql:
                new_url = f"{j}{c}"

                if bot == True:
                    anti_bot = random.uniform(1, 60)
                    
                    time.sleep(anti_bot)

                print(color + "checking: " + new_url)

                try:
                    result = web_session.get(j, verify = False, headers = user_agent, timeout = (5, 30))

                    if len(result.text) >= 25000000:
                        gpu = tf.py_function(func = gpu_sql_error, inp = [new_url], Tout = tf.string)

                        gpu = re.findall("b\'.+?\'", str(gpu))
                        gpu = re.sub("b\'", "", gpu[0])
                        gpu = gpu[:-1]

                        if gpu != "none":
                            print(color + gpu)
                            my_list.append(gpu)
                            
        
                    if len(result.text) < 25000000:
                        for i in error_message:
                            my_regex = re.search(i, result.text)

                            try:
                                if my_regex:
                                    print(color + "true: " + str(i) + " " + str(my_regex.span()) + " " + new_url)
                                    my_list.append("true: " + str(i) + " " + str(my_regex.span()) + " " + new_url)
                                    break

                            except UnicodeDecodeError:
                                break

                except requests.exceptions.SSLError:
                    print(color + "ERROR: invalid certificate!")
                    pass

                except urllib3.exceptions.LocationParseError:
                    print(color + "ERROR: location parse error!")
                    pass

                except requests.exceptions.ConnectionError:
                    print(color + "ERROR: connection error!")
                    pass

                except requests.exceptions.ConnectTimeout:
                    print(color + "ERROR: connect timeout!")
                    pass

                except requests.exceptions.InvalidSchema:
                    print(color + "ERROR: invalid schema!")
                    pass

                except requests.exceptions.InvalidURL:
                    print(color + "ERROR: invalid url!")
                    pass

                except requests.exceptions.MissingSchema:
                    print(color + "ERROR: missing schema!")
                    pass

                except requests.exceptions.TooManyRedirects:
                    print(color + "ERROR: too many redirects!")
                    pass

                except requests.exceptions.ReadTimeout:
                    print(color + "ERROR: read timeout!")
                    pass
                
            try:
                print(color + "checking for forms on: " + j)

                get_input = form_scanner(j, secure = secure, parse = "input")

                form_list = []

                try:
                    for i in get_input:
                        if "email" in str(i):
                            name = str(re.findall("name.+\".+\"", i)).split("\"")
                            form_list.append(name[1])

                        if "hidden" in str(i):
                            name = str(re.findall("name.+\".+\"", i)).split("\"")
                            form_list.append(name[1])
                            
                        if "number" in str(i):
                            name = str(re.findall("name.+\".+\"", i)).split("\"")
                            form_list.append(name[1])

                        if "password" in str(i):
                            name = str(re.findall("name.+\".+\"", i)).split("\"")
                            form_list.append(name[1])
                            password_form = name[1]

                        if "query" in str(i):
                            name = str(re.findall("name.+\".+\"", i)).split("\"")
                            form_list.append(name[1])

                        if "search" in str(i):
                            name = str(re.findall("name.+\".+\"", i)).split("\"")
                            form_list.append(name[1])

                        if "tel" in str(i):
                            name = str(re.findall("name.+\".+\"", i)).split("\"")
                            form_list.append(name[1])

                        if "text" in str(i):
                            name = str(re.findall("name.+\".+\"", i)).split("\"")
                            form_list.append(name[1])

                        if "url" in str(i):
                            name = str(re.findall("name.+\".+\"", i)).split("\"")
                            form_list.append(name[1])

                except:
                    pass

                form_list = list(dict.fromkeys(form_list))
                form_list.sort()

                my_forms = form_scanner(url, secure = secure)

                for forms in form_list:
                    if bot == True:
                        anti_bot = random.uniform(1, 60)
                        
                        time.sleep(anti_bot)

                    for i in my_forms:
                        name_regex = re.search(forms, i)
                        get_regex = re.search("get", i)
                        post_regex = re.search("post", i)

                        if name_regex and get_regex:
                            password_search = re.sub(" ", "", i)
                            password_search = re.search("type=\"password\"", password_search)

                            if password_search:
                                for boolean_mal in boolean_sql:
                                    try:
                                        mal_dict = {forms: boolean_mal, password_form: mal_password}

                                        print(color + "checking form (" + boolean_mal + "): " + forms)

                                        get = web_session.get(j, verify = False, headers = user_agent, timeout = (5, 30))
                                        get_check = web_session.get(j, params = mal_dict, verify = False, headers = user_agent, timeout = (5, 30))

                                        if get.text != get_check.text:
                                            print(color + "true: " + boolean_mal + " " + url + " form: " + forms + " (boolean)")
                                            my_list.append("true: " + boolean_mal + " " + url + " form: " + forms + " (boolean)")

                                    except:
                                        pass

                        if name_regex and post_regex:
                            password_search = re.sub(" ", "", i)
                            password_search = re.search("type=\"password\"", password_search)

                            if password_search:
                                for boolean_mal in boolean_sql:
                                    try:
                                        mal_dict = {forms: boolean_mal, password_form: mal_password}

                                        print(color + "checking form (" + boolean_mal + "): " + forms)

                                        post = web_session.get(j, verify = False, headers = user_agent, timeout = (5, 30))
                                        post_check = web_session.post(j, data = mal_dict, verify = False, headers = user_agent, timeout = (5, 30))

                                        if post.text != post_check.text:
                                            print(color + "true: " + boolean_mal + " " + url + " form: " + forms + " (boolean)")
                                            my_list.append("true: " + boolean_mal + " " + url + " form: " + forms + " (boolean)")

                                    except:
                                        pass

                for forms in form_list:
                    for mal in mal_sql:
                        form_dict = {forms: mal}

                        if bot == True:
                            anti_bot = random.uniform(1, 60)
                            
                            time.sleep(anti_bot)

                        for i in my_forms:
                            name_regex = re.search(forms, i)
                            get_regex = re.search("get", i)
                            post_regex = re.search("post", i)
                            
                            if name_regex and get_regex:
                                print(color + "checking form (" + mal + "): " + forms)
                                get_data = web_session.get(j, params = form_dict, verify = False, headers = user_agent, timeout = (5, 30)).text

                                for ii in error_message:
                                    my_regex = re.search(ii, get_data)
                                    my_boolean = False

                                    try:
                                        if my_regex:
                                                my_boolean = True
                                                break

                                    except UnicodeDecodeError:
                                        continue
                                    
                                    if my_boolean == True:
                                        print(color + "true: " + j + " form: " + forms + " (error)")
                                        my_list.append(j + " form: " + forms + " (error)")

                            if name_regex and post_regex:
                                print(color + "checking form (" + mal + "): " + forms)
                                send_data = web_session.post(j, data = form_dict, verify = False, headers = user_agent, timeout = (5, 30)).text

                                for ii in error_message:
                                    my_regex = re.search(ii, send_data)
                                    my_boolean = False

                                    try:
                                        if my_regex:
                                            my_boolean = True
                                            break

                                    except UnicodeDecodeError:
                                        continue

                                    if my_boolean == True:
                                        print(color + "true: " + j + " form: " + forms + " (error)")
                                        my_list.append(j + " form: " + forms + " (error)")

            except requests.exceptions.SSLError:
                print(color + "ERROR: invalid certificate!")
                continue

            except urllib3.exceptions.LocationParseError:
                print(color + "ERROR: location parse error!")
                continue

            except requests.exceptions.ConnectionError:
                print(color + "ERROR: connection error!")
                continue

            except requests.exceptions.ConnectTimeout:
                print(color + "ERROR: connect timeout!")
                continue

            except requests.exceptions.InvalidSchema:
                print(color + "ERROR: invalid schema!")
                continue

            except requests.exceptions.InvalidURL:
                print("ERROR: invalid url!")
                continue

            except requests.exceptions.MissingSchema:
                print(color + "ERROR: missing schema!")
                continue

            except requests.exceptions.TooManyRedirects:
                print(color + "ERROR: too many redirects!")
                continue

            except requests.exceptions.ReadTimeout:
                print(color + "ERROR: read timeout!")
                continue

    clear()
    
    return my_list

def subdomain_scanner(url, secure = True, bot = False):
    domain_list = []

    website = link_scanner(url, secure, bot = bot)

    clear()

    for i in website:
        if bot == True:
            anti_bot = random.uniform(1, 60)
            
            time.sleep(anti_bot)

        domain = re.findall("[^https|http][a-z0-9]+", i.lower())

        try:
            domain = str(domain[0]).replace("/", "")
            domain_list.append(domain)

        except:
            continue
        
    domain_list = list(dict.fromkeys(domain_list))
    domain_list.sort()

    return domain_list

def xss_scanner(url, secure = True, bot = False):
    if secure == True:
        my_secure = "https://"

    if secure == False:
        my_secure = "http://"
        
    my_list = []
    my_url = my_secure + url
    
    #malicious script
    mal_script = "<script>alert('The Silent')</script>"

    clear()

    user_input = input("1 = scan url | 2 = scan url and hyperlinks (requests) | 3 = scan url and hyperlinks (selenium)\n")

    clear()

    if user_input == "1":
        try:
            super_result = my_url.split("=")
            print(color + "checking: " + super_result[0] + "=" + mal_script)
            result = web_session.get(super_result[0] + "=" + mal_script, verify = False, headers = user_agent, timeout = (5, 30))

            if mal_script in result.text:
                print(color + "True: " + super_result[0] + "=" + mal_script + " (script in url)")
                my_list.append(super_result[0] + "=" + mal_script + " (script in url)")

        except requests.exceptions.SSLError:
            print(color + "ERROR: invalid certificate!")
            pass

        except urllib3.exceptions.LocationParseError:
            print(color + "ERROR: location parse error!")
            pass

        except requests.exceptions.ConnectionError:
            print(color + "ERROR: connection error!")
            pass

        except requests.exceptions.ConnectTimeout:
            print(color + "ERROR: connect timeout!")
            pass

        except requests.exceptions.InvalidSchema:
            print(color + "ERROR: invalid schema!")
            pass

        except requests.exceptions.InvalidURL:
            print(color + "ERROR: invalid url!")
            pass

        except requests.exceptions.MissingSchema:
            print(color + "ERROR: missing schema!")
            pass

        except requests.exceptions.TooManyRedirects:
            print(color + "ERROR: too many redirects!")
            pass

        except requests.exceptions.ReadTimeout:
            print(color + "ERROR: read timeout!")
            pass

        except UnicodeError:
            pass
        
        try:
            print(color + "checking: " + my_url + mal_script)
            result = web_session.get(my_url + mal_script, verify = False, headers = user_agent, timeout = (5, 30))

            if mal_script in result.text:
                print(color + "True: " + my_url + mal_script + " (script in url)")
                my_list.append(my_url + mal_script + " (script in url)")

        except requests.exceptions.SSLError:
            print(color + "ERROR: invalid certificate!")
            pass

        except urllib3.exceptions.LocationParseError:
            print(color + "ERROR: location parse error!")
            pass

        except requests.exceptions.ConnectionError:
            print(color + "ERROR: connection error!")
            pass

        except requests.exceptions.ConnectTimeout:
            print(color + "ERROR: connect timeout!")
            pass

        except requests.exceptions.InvalidSchema:
            print(color + "ERROR: invalid schema!")
            pass

        except requests.exceptions.InvalidURL:
            print(color + "ERROR: invalid url!")
            pass

        except requests.exceptions.MissingSchema:
            print(color + "ERROR: missing schema!")
            pass

        except requests.exceptions.TooManyRedirects:
            print(color + "ERROR: too many redirects!")
            pass

        except requests.exceptions.ReadTimeout:
            print(color + "ERROR: read timeout!")
            pass

        except UnicodeError:
            pass

        try:
            print(color + "Checking for forms on: " + my_url)

            get_input = form_scanner(url, secure = secure, parse = "input")

            form_list = []

            try:
                for i in get_input:
                    if "email" in str(i):
                        name = str(re.findall("name.+\".+\"", i)).split("\"")
                        form_list.append(name[1])

                    if "hidden" in str(i):
                        name = str(re.findall("name.+\".+\"", i)).split("\"")
                        form_list.append(name[1])
                        
                    if "number" in str(i):
                        name = str(re.findall("name.+\".+\"", i)).split("\"")
                        form_list.append(name[1])

                    if "password" in str(i):
                        name = str(re.findall("name.+\".+\"", i)).split("\"")
                        form_list.append(name[1])

                    if "query" in str(i):
                        name = str(re.findall("name.+\".+\"", i)).split("\"")
                        form_list.append(name[1])

                    if "search" in str(i):
                        name = str(re.findall("name.+\".+\"", i)).split("\"")
                        form_list.append(name[1])

                    if "tel" in str(i):
                        name = str(re.findall("name.+\".+\"", i)).split("\"")
                        form_list.append(name[1])

                    if "text" in str(i):
                        name = str(re.findall("name.+\".+\"", i)).split("\"")
                        form_list.append(name[1])
                        

                    if "url" in str(i):
                        name = str(re.findall("name.+\".+\"", i)).split("\"")
                        form_list.append(name[1])

            except:
                pass

            form_list = list(dict.fromkeys(form_list))
            form_list.sort()

            my_forms = form_scanner(url, secure = secure)

            for forms in form_list:
                print(color + "checking form: " + forms)
                mal_dict = {forms: mal_script}

                for i in my_forms:
                    if forms in i and "get" in i:
                        get_data = web_session.get(my_url, params = mal_dict, verify = False, headers = user_agent, timeout = (5, 30)).text

                        if mal_script in get_data:
                            print(color + "true: " + url + " form: " + forms)
                            my_list.append(url + " form: " + forms)

                    if forms in i and "post" in i:
                        send_data = web_session.post(my_url, data = mal_dict, verify = False, headers = user_agent, timeout = (5, 30)).text

                        if mal_script in send_data:
                            print(color + "true: " + url + " form: " + forms)
                            my_list.append(url + " form: " + forms)

        except requests.exceptions.SSLError:
            print(color + "ERROR: invalid certificate!")
            pass

        except urllib3.exceptions.LocationParseError:
            print(color + "ERROR: location parse error!")
            pass

        except requests.exceptions.ConnectionError:
            print(color + "ERROR: connection error!")
            pass

        except requests.exceptions.ConnectTimeout:
            print(color + "ERROR: connect timeout!")
            pass

        except requests.exceptions.InvalidSchema:
            print(color + "ERROR: invalid schema!")
            pass

        except requests.exceptions.InvalidURL:
            print(color + "ERROR: invalid url!")
            pass

        except requests.exceptions.MissingSchema:
            print(color + "ERROR: missing schema!")
            pass

        except requests.exceptions.TooManyRedirects:
            print(color + "ERROR: too many redirects!")
            pass

        except requests.exceptions.ReadTimeout:
            print(color + "ERROR: read timeout!")
            pass

        except UnicodeError:
            pass

    if user_input == "2":
        my_result = link_scanner(url, secure = secure, bot = bot) 

        for links in my_result:
            if bot == True:
                anti_bot = random.uniform(1, 60)
                
                time.sleep(anti_bot)

            try:
                super_result = links.split("=")
                print(color + "checking: " + super_result[0] + "=" + mal_script)
                result = web_session.get(super_result[0] + "=" + mal_script, verify = False, headers = user_agent, timeout = (5, 30))

                if mal_script in result.text:
                    print(color + "True: " + super_result[0] + "=" + mal_script + " (script in url)")
                    my_list.append(super_result[0] + "=" + mal_script + " (script in url)")

            except requests.exceptions.SSLError:
                print(color + "ERROR: invalid certificate!")
                pass

            except urllib3.exceptions.LocationParseError:
                print(color + "ERROR: location parse error!")
                pass

            except requests.exceptions.ConnectionError:
                print(color + "ERROR: connection error!")
                pass

            except requests.exceptions.ConnectTimeout:
                print(color + "ERROR: connect timeout!")
                pass

            except requests.exceptions.InvalidSchema:
                print(color + "ERROR: invalid schema!")
                pass

            except requests.exceptions.InvalidURL:
                print(color + "ERROR: invalid url!")
                pass

            except requests.exceptions.MissingSchema:
                print(color + "ERROR: missing schema!")
                pass

            except requests.exceptions.TooManyRedirects:
                print(color + "ERROR: too many redirects!")
                pass

            except requests.exceptions.ReadTimeout:
                print(color + "ERROR: read timeout!")
                pass

            except UnicodeError:
                pass
                
            try:
                print(color + "checking: " + links + mal_script)
                
                result = web_session.get(links + mal_script, verify = False, headers = user_agent, timeout = (5, 30))

                if mal_script in result.text:
                    print(color + "True: " + links  + mal_script + " (script in url)")
                    my_list.append(links  + mal_script + " (script in url)")

            except requests.exceptions.SSLError:
                print(color + "ERROR: invalid certificate!")
                pass

            except urllib3.exceptions.LocationParseError:
                print(color + "ERROR: location parse error!")
                pass

            except requests.exceptions.ConnectionError:
                print(color + "ERROR: connection error!")
                pass

            except requests.exceptions.ConnectTimeout:
                print(color + "ERROR: connect timeout!")
                pass

            except requests.exceptions.InvalidSchema:
                print(color + "ERROR: invalid schema!")
                pass

            except requests.exceptions.InvalidURL:
                print(color + "ERROR: invalid url!")
                pass

            except requests.exceptions.MissingSchema:
                print(color + "ERROR: missing schema!")
                pass

            except requests.exceptions.TooManyRedirects:
                print(color + "ERROR: too many redirects!")
                pass

            except requests.exceptions.ReadTimeout:
                print(color + "ERROR: read timeout!")
                pass

            except UnicodeError:
                pass

            try:
                print(color + "checking for forms on: " + links)

                if "http://" in links:
                    super_links = re.sub("http://", "", links)

                if "https://" in links:
                    super_links = re.sub("https://", "", links)

                get_input = form_scanner(super_links, secure = secure, parse = "input")

                form_list = []

                try:
                    for i in get_input:
                        if "email" in str(i):
                            name = str(re.findall("name.+\".+\"", i)).split("\"")
                            form_list.append(name[1])

                        if "hidden" in str(i):
                            name = str(re.findall("name.+\".+\"", i)).split("\"")
                            form_list.append(name[1])
                            
                        if "number" in str(i):
                            name = str(re.findall("name.+\".+\"", i)).split("\"")
                            form_list.append(name[1])

                        if "password" in str(i):
                            name = str(re.findall("name.+\".+\"", i)).split("\"")
                            form_list.append(name[1])

                        if "query" in str(i):
                            name = str(re.findall("name.+\".+\"", i)).split("\"")
                            form_list.append(name[1])

                        if "search" in str(i):
                            name = str(re.findall("name.+\".+\"", i)).split("\"")
                            form_list.append(name[1])

                        if "tel" in str(i):
                            name = str(re.findall("name.+\".+\"", i)).split("\"")
                            form_list.append(name[1])

                        if "text" in str(i):
                            name = str(re.findall("name.+\".+\"", i)).split("\"")
                            form_list.append(name[1])
                            

                        if "url" in str(i):
                            name = str(re.findall("name.+\".+\"", i)).split("\"")
                            form_list.append(name[1])

                except:
                    pass

                form_list = list(dict.fromkeys(form_list))
                form_list.sort()

                if "http://" in links:
                    super_links = re.sub("http://", "", links)

                if "https://" in links:
                    super_links = re.sub("https://", "", links)

                my_forms = form_scanner(super_links, secure = secure)

                for forms in form_list:
                    print(color + "checking form: " + forms)
                    mal_dict = {forms: mal_script}

                    if bot == True:
                        anti_bot = random.uniform(1, 60)
                        
                        time.sleep(anti_bot)

                    for i in my_forms:
                        if forms in i and "get" in i:
                            get_data = web_session.get(links, params = mal_dict, verify = False, headers = user_agent, timeout = (5, 30)).text

                            if mal_script in get_data:
                                print(color + "true: " + url + " form: " + forms)
                                my_list.append(url + " form: " + forms)

                        if forms in i and "post" in i:
                            send_data = web_session.post(links, data = mal_dict, verify = False, headers = user_agent, timeout = (5, 30)).text

                            if mal_script in send_data:
                                print(color + "true: " + url + " form: " + forms)
                                my_list.append(url + " form: " + forms)

            except requests.exceptions.SSLError:
                print(color + "ERROR: invalid certificate!")
                pass

            except urllib3.exceptions.LocationParseError:
                print(color + "ERROR: location parse error!")
                pass

            except requests.exceptions.ConnectionError:
                print(color + "ERROR: connection error!")
                pass

            except requests.exceptions.ConnectTimeout:
                print(color + "ERROR: connect timeout!")
                pass

            except requests.exceptions.InvalidSchema:
                print(color + "ERROR: invalid schema!")
                pass

            except requests.exceptions.InvalidURL:
                print(color + "ERROR: invalid url!")
                pass

            except requests.exceptions.MissingSchema:
                print(color + "ERROR: missing schema!")
                pass

            except requests.exceptions.TooManyRedirects:
                print(color + "ERROR: too many redirects!")
                pass

            except requests.exceptions.ReadTimeout:
                print(color + "ERROR: read timeout!")
                pass

            except UnicodeError:
                pass

    if user_input == "3":
        my_result = link_scanner_selenium(url) 

        for links in my_result:
            if bot == True:
                anti_bot = random.uniform(1, 60)
                
                time.sleep(anti_bot)

            try:
                super_result = links.split("=")
                print(color + "checking: " + super_result[0] + "=" + mal_script)
                result = web_session.get(super_result[0] + "=" + mal_script, verify = False, headers = user_agent, timeout = (5, 30))

                if mal_script in result.text:
                    print(color + "True: " + super_result[0] + "=" + mal_script + " (script in url)")
                    my_list.append(super_result[0] + "=" + mal_script + " (script in url)")

            except requests.exceptions.SSLError:
                print(color + "ERROR: invalid certificate!")
                pass

            except urllib3.exceptions.LocationParseError:
                print(color + "ERROR: location parse error!")
                pass

            except requests.exceptions.ConnectionError:
                print(color + "ERROR: connection error!")
                pass

            except requests.exceptions.ConnectTimeout:
                print(color + "ERROR: connect timeout!")
                pass

            except requests.exceptions.InvalidSchema:
                print(color + "ERROR: invalid schema!")
                pass

            except requests.exceptions.InvalidURL:
                print(color + "ERROR: invalid url!")
                pass

            except requests.exceptions.MissingSchema:
                print(color + "ERROR: missing schema!")
                pass

            except requests.exceptions.TooManyRedirects:
                print(color + "ERROR: too many redirects!")
                pass

            except requests.exceptions.ReadTimeout:
                print(color + "ERROR: read timeout!")
                pass

            except UnicodeError:
                pass
                
            try:
                print(color + "checking: " + links + mal_script)
                
                result = web_session.get(links + mal_script, verify = False, headers = user_agent, timeout = (5, 30))

                if mal_script in result.text:
                    print(color + "True: " + links  + mal_script + " (script in url)")
                    my_list.append(links  + mal_script + " (script in url)")

            except requests.exceptions.SSLError:
                print(color + "ERROR: invalid certificate!")
                pass

            except urllib3.exceptions.LocationParseError:
                print(color + "ERROR: location parse error!")
                pass

            except requests.exceptions.ConnectionError:
                print(color + "ERROR: connection error!")
                pass

            except requests.exceptions.ConnectTimeout:
                print(color + "ERROR: connect timeout!")
                pass

            except requests.exceptions.InvalidSchema:
                print(color + "ERROR: invalid schema!")
                pass

            except requests.exceptions.InvalidURL:
                print(color + "ERROR: invalid url!")
                pass

            except requests.exceptions.MissingSchema:
                print(color + "ERROR: missing schema!")
                pass

            except requests.exceptions.TooManyRedirects:
                print(color + "ERROR: too many redirects!")
                pass

            except requests.exceptions.ReadTimeout:
                print(color + "ERROR: read timeout!")
                pass

            except UnicodeError:
                pass

            try:
                print(color + "checking for forms on: " + links)

                get_input = form_scanner(links, secure = secure, parse = "input")

                form_list = []

                try:
                    for i in get_input:
                        if "email" in str(i):
                            name = str(re.findall("name.+\".+\"", i)).split("\"")
                            form_list.append(name[1])

                        if "hidden" in str(i):
                            name = str(re.findall("name.+\".+\"", i)).split("\"")
                            form_list.append(name[1])
                            
                        if "number" in str(i):
                            name = str(re.findall("name.+\".+\"", i)).split("\"")
                            form_list.append(name[1])

                        if "password" in str(i):
                            name = str(re.findall("name.+\".+\"", i)).split("\"")
                            form_list.append(name[1])

                        if "query" in str(i):
                            name = str(re.findall("name.+\".+\"", i)).split("\"")
                            form_list.append(name[1])

                        if "search" in str(i):
                            name = str(re.findall("name.+\".+\"", i)).split("\"")
                            form_list.append(name[1])

                        if "tel" in str(i):
                            name = str(re.findall("name.+\".+\"", i)).split("\"")
                            form_list.append(name[1])

                        if "text" in str(i):
                            name = str(re.findall("name.+\".+\"", i)).split("\"")
                            form_list.append(name[1])
                            

                        if "url" in str(i):
                            name = str(re.findall("name.+\".+\"", i)).split("\"")
                            form_list.append(name[1])

                except:
                    pass

                form_list = list(dict.fromkeys(form_list))
                form_list.sort()

                if "http://" in links:
                    super_links = re.sub("http://", "", links)

                if "https://" in links:
                    super_links = re.sub("https://", "", links)

                my_forms = form_scanner(super_links, secure = secure)

                for forms in form_list:
                    print(color + "checking form: " + forms)
                    mal_dict = {forms: mal_script}

                    if bot == True:
                        anti_bot = random.uniform(1, 60)
                        
                        time.sleep(anti_bot)

                    for i in my_forms:
                        if forms in i and "get" in i:
                            get_data = web_session.get(links, params = mal_dict, verify = False, headers = user_agent, timeout = (5, 30)).text

                            if mal_script in get_data:
                                print(color + "true: " + url + " form: " + forms)
                                my_list.append(url + " form: " + forms)

                        if forms in i and "post" in i:
                            send_data = web_session.post(links, data = mal_dict, verify = False, headers = user_agent, timeout = (5, 30)).text

                            if mal_script in send_data:
                                print(color + "true: " + url + " form: " + forms)
                                my_list.append(url + " form: " + forms)

            except requests.exceptions.SSLError:
                print(color + "ERROR: invalid certificate!")
                pass

            except urllib3.exceptions.LocationParseError:
                print(color + "ERROR: location parse error!")
                pass

            except requests.exceptions.ConnectionError:
                print(color + "ERROR: connection error!")
                pass

            except requests.exceptions.ConnectTimeout:
                print(color + "ERROR: connect timeout!")
                pass

            except requests.exceptions.InvalidSchema:
                print(color + "ERROR: invalid schema!")
                pass

            except requests.exceptions.InvalidURL:
                print(color + "ERROR: invalid url!")
                pass

            except requests.exceptions.MissingSchema:
                print(color + "ERROR: missing schema!")
                pass

            except requests.exceptions.TooManyRedirects:
                print(color + "ERROR: too many redirects!")
                pass

            except requests.exceptions.ReadTimeout:
                print(color + "ERROR: read timeout!")
                pass

            except UnicodeError:
                pass

    my_list = list(dict.fromkeys(my_list))
    my_list.sort()

    clear()

    return my_list
