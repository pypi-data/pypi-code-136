# Copyright 2022 by Kyvos Insights
# Created By: Eugene Asahara
# Created Date: 
# version ='1.0'
# 
"""
Main module of the Kyvos Python Library.

Because pyodbc isn't the most robust way to deal with data sources, try to restrict calls to
pyodbc to just the execute and connect methods - as a DAL (data access layer). This way,
when I can change to a better access method, the code is restricted to just a few methods.

Warnings:

The only reference to a sub-library is to the Metadata.
"""
from datetime import datetime
import pathlib
from numpy import insert, isin

# from tkinter.messagebox import NO
from pandas.core.frame import DataFrame

import pyodbc   # Try to restrict actually calling pyodbc to just execute_kyvos_sqland openConnection.
import pandas as pd
import os

from abc import ABC, abstractproperty
from abc import abstractmethod
from enum import Enum
from enum import IntEnum

import concurrent.futures

from multiprocessing import Lock
from collections import namedtuple
from functools import reduce
import json
from json import JSONEncoder
from typing import Union
import hashlib
import time

CompOpTuple = namedtuple("CompOpTuple", ["value", "symbol"])

class CompOp(CompOpTuple):
    GT = CompOpTuple(0, ">")
    LT = CompOpTuple(1, "<")
    EQ = CompOpTuple(2, "==")
    LE = CompOpTuple(3, "<=")
    GE = CompOpTuple(4, ">=")
    NE = CompOpTuple(5, "<>")


class SQLFunc(Enum):
    SUM = 0
    MAX = 1
    MIN = 2

def sql_func_symbol(sym:SQLFunc):
    return SQLFunc.name

QLang = namedtuple("QLang",["name", "enclose", "close", "is_sql", "kyvos_lang", "db_type", "case_eq"])
"""
case_eq - the equal sign within a CASE. Kyvos is ==
db_type - used so we know the database platform. ex: SQL Server, Snowflake, Databricks.
"""

class QueryLanguage(QLang):  # This is to help with serializing.
    KyvosSQL = QLang("KyvosSQL", "`", "`", True, True, "Kyvos", "==")
    SparkSQL = QLang("SparkSQL","","",True,False, "Spark", "=")
    MDX = QLang("MDX","","",False,True, "Kyvos", "==")
    DAX = QLang("DAX","","",False,True, "Azure Analysis Services", "==")
    AnsiSQL = QLang("AnsiSQL","","",True,False, "Generic SQL DB", "=")
    TSQL = QLang("TSQL","[","]",True,True, "SQL Server", "=")
    PLSQL = QLang("PLSQL", "", "", True, True, "Oracle", "=")
    SFSQL = QLang("SFSQL", "", "", True, True, "Snowflake", "=")

def unpack_ql(lang:QueryLanguage):
    return lang.enclose, lang.close, lang.case_eq



DEFAULT_QUERY_LANGUAGE = QueryLanguage.KyvosSQL

class QueryOutputFormat(IntEnum):
    PandasDataframe = 0,
    PyOdbc = 1,  # This is how data is natively received from PyOdbc.
    SparkDataframe = 2,
    SparkDataset = 3,
    Json = 4,
    CSV = 5,
    XML = 6

DEFAULT_OUTPUT_FORMAT = QueryOutputFormat.PandasDataframe

DEFAULT_PARAMETER_PREFIX:str = "@"

TIMING_FORMAT:str = "%Y-%m-%d %H:%M:%S:%f"


def hash_string(string_to_hash:str)->str:
    """md5 has of fully-qualified attribute"""
    return hashlib.md5(string_to_hash.encode()).hexdigest()

def display_now()->str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# def kyvosEnvVar()->dict:
#     """Retrive dictionary of kyvos environment variables"""
#     """Display like this:
#     for k,v in ky.kyvosEnvVar().items():
#         print(k,v)
#     """
#     return {v:os.environ[v] for v in ["KYVOS_INPUT_DATA_DIR","KYVOS_OUTPUT_DATA_DIR","KYVOS_METADATA","KYVOS_UID"]}
  
class EnvVar:

    CONFIG_FILENAME = "kypyconfig.json"

    eVars = {
        "KYVOS_INPUT_DATA_DIR":{"Description":"General data input drop for KyPy."},
        "KYVOS_OUTPUT_DATA_DIR":{"Description":"General data output drop for KyPy."},
        "KYVOS_METADATA":{"Description":"Cube metadata export from Kyvos"},
        "KYVOS_UID":{"Description":"Default UID."},  
        "KYVOS_MASTER_DATA_MANAGEMENT":{"Description":"Mapping files."},
        "KYVOS_STAR_SCHEMA":{"Description":"Data Mesh star schema files."},
        "KYVOS_CUBE_XMLA":{"Description":"Output XMLA transformed from star schema files."},
        "KYVOS_OLAP_QUERIES":{"Description":"OlapQueryDefqueries saved for re-use."},
        "KYVOS_MARKOV_DIR":{"Description":"Markov models."},
        "KYVOS_ENTERPRISE_GRAPH":{"Description":"Folder for landing data for import into the Enterprise Graph."}
    }

    # I'm choosing to let error out if there is no configuration file.
    if os.path.isfile(f"./{CONFIG_FILENAME}"):
        configdata = json.load(open(file=f"./{CONFIG_FILENAME}"))
    else:
        raise Exception(f"Missing config file: {os.getcwd()}/{CONFIG_FILENAME}")
    
    for key,val in eVars.items():
        if key in configdata.keys():
            val.update({"Value": configdata[key]["Value"]})
        else:
            print(f'Must add environmental variable: {key} - {val["Description"]}')

    @staticmethod
    def config_exists()->bool:
        if os.path.isfile(f"./{EnvVar.CONFIG_FILENAME}"):
            return True
        else:
            print(f"Missing config file: {os.getcwd()}/{EnvVar.CONFIG_FILENAME}")
            return False

    @staticmethod
    def get_var(varName:str)->str:
        if varName in EnvVar.eVars:
            return EnvVar.eVars[varName].get("Value")
        return None

    @staticmethod
    def formatted_eVars():
        """ Nicely formatted json of the environment variables.

        This is good for setting up the KyPy environment.
        """
        return json.dumps(EnvVar.eVars, indent=2)

    @staticmethod
    def get_vars()->dict:
        return {k:v for k,v in EnvVar.eVars.items()}

    @staticmethod
    def append_filename_path(file_name:str, env_var_key:str, suffix:str=None)->str:
        suffix = suffix if suffix else ""
        if suffix and not suffix.startswith("."):
            suffix = f".{suffix}"
        return f"{EnvVar.get_var(env_var_key)}{file_name}{suffix}"

    @staticmethod
    def prepend_filename_path(file_name:str, env_var_key:str, suffix:str=None)->str:
        """Prepend a directory name to a file name.
        
        Returns:
        ----
            str

        Usage:
        ----
            >>> test_full_file_path = ky.EnvVar.prepend_filename_path("test.csv","KYVOS_INPUT_DATA_DIR")

        """
        suffix = '' if not suffix else suffix
        # If suffix is specified and it doesn't have a period, prepend the period.
        if suffix and not suffix.startswith("."):
            suffix = f".{suffix}"
        return f"{EnvVar.get_var(env_var_key)}{file_name}{suffix}"

    def __str__():
        return json.dumps(EnvVar.eVars, indent=2)
    
class MDXPartBase(ABC):
    def __init__(self, mdx_expression:str=""):
        self.mdx_expression = mdx_expression

    def __str__(self):
        return str(self.mdx_expression)

class MDXPartSet(MDXPartBase):
    """Class defining an MDX expression as a set object"""
    def __init__(self, mdx_expression:str):
        super().__init__(mdx_expression)

class MDXPartMember(MDXPartBase):
    """Class defining an MDX expression as a member object"""
    def __init__(self, mdx_expression:str):
        super().__init__(mdx_expression)

class MDXPartValue(MDXPartBase):
    """Class defining an MDX expression as a value object"""
    def __init__(self, mdx_expression:str):
        super().__init__(mdx_expression)

class MDXStatement(MDXPartBase):
    """Class defining an MDX expression as an MDX statement object"""
    def __init__(self, mdx_expression:str):
        super().__init__(mdx_expression)

"""
The following definitions are used in other modules of KyPy, particularly KyvosStatsLib and GraphDatabaseLib.
"""
graph_edge_elements = ["NodeA", "NodeB", "observed_count","node_color","probability"]
GraphEdge = namedtuple('GraphEdge',graph_edge_elements) 
graph_node_elements = ["Node","Color","cube","attribute"]
GraphNode = namedtuple("GraphNode",graph_node_elements)


class CubeDef:
    """Metadata of a Kyvos Cube.

        This object is passed to ky.execute_sql_query.

        Usage:
        ----
            >>> cubedef = ky.CubeDef(cubeSchema=cube_schema, cubeName=cube_name, dsn=dsn)
    """
    def __init__ (self,cubeSchema:str, cubeName:str, dsn:str=None, load_cube_metadata:bool=False, lang:QueryLanguage=DEFAULT_QUERY_LANGUAGE):
        self.cubeSchema = cubeSchema 
        self.cubeName = cubeName 
        self.dsn = dsn
        self.cube_metadata = self._load_metadata() if load_cube_metadata else None  # The cube metadata isn't always needed. It requires reading a file, so don't do it if not needed.
        self.lang = lang
    def __eq__(self, other):
        return self.cubeSchema == other.cubeSchema and self.cubeName == other.cubeName and self.dsn == other.dsn

    @property
    def cube_name_sql(self):
        """Returns a string to just show that the connection object is set up.
        Should deprecate in favor of cube_name.
        """
        e, c,_ = unpack_ql(self.lang)
        return f"{e}{self.cubeSchema}{c}.{e}{self.cubeName}{c} {e}s{c}"

    def query_expression(self, lang:QueryLanguage=None):
        e, c, _ = unpack_ql(lang if lang else self.lang)
        return f"{e}{self.cubeSchema}{c}.{e}{self.cubeName}{c} {e}s{c}"

    def __str__(self):
        return self.query_expression()

    def __repr__(self):
        return f"{self.__class__.__name__}(cubeSchema={self.cubeSchema},cubeName={self.cubeName},dsn={self.dsn})"

    def __save__(self)->dict:
        return {"Cube":{"dsn":self.dsn, "cubeSchema":self.cubeSchema, "cubeName":self.cubeName}}

    def _load_metadata(self):
        from . Metadata import MetadataLib as kym  # import here to avoid circular reference. Not good practice, but ...
        cube_metadata = kym.CubeMetadata(self.cubeName)
        if not cube_metadata.metadata_success:
            cube_metadata = None
        return cube_metadata

    def attribute_hash(self,attribute:str)->str:
        """hash of fully-qualified attribute"""
        return hash_string(f"{self.dsn}{self.cubeSchema}{self.cubeName}{attribute}")

    @property
    def cube_hash(self)->str:
        return hash_string(f"{self.dsn}{self.cubeSchema}{self.cubeName}")

    @staticmethod
    def __loadQueryJSON__(jsonStr):
        ojson = json.loads(jsonStr)
        jcube = ojson["cube"]
        return CubeDef(
            cubeSchema=jcube["cubeSchema"], 
            cubeName=jcube["cubeName"], 
            dsn=jcube["dsn"]
        )


"""
Note that this states https://documentation.kyvosinsights.com/display/KD20211/Spark+SQL what is allowed in Kyvos SQL.

Open connection to Kyvos Cube, execute a SQL, and fetch all rows.
"""
def open_kyvos_connection(
        dsn:str,
        cubeSchema:str=None,
        cubeName:str=None,
        lang:QueryLanguage=DEFAULT_QUERY_LANGUAGE,
        load_cube_metadata:bool=False
    ):
    """Open a connection to a Kyvos cube.
    Returns:
    ----
        tuple

    Usage:
    ----
        >>> results=ky.openKyvosConnection(dsn="KyvosNew",cubeSchema="Eugene Training",cubeName="iowa_liquor_sales")
    """
    cube_info = CubeDef(cubeSchema=cubeSchema, cubeName=cubeName, dsn=dsn, load_cube_metadata=load_cube_metadata)
    cursor,cnxn = _get_kyvos_connection(dsn,lang)
    return cursor, cnxn, cube_info

pyodbc_column_index:int = 0  # Index of the pyodbc index of the description tuples.

def _get_kyvos_connection(dsn:str, lang:QueryLanguage=DEFAULT_QUERY_LANGUAGE)->pyodbc.Connection:
    cnxn = pyodbc.connect(conn_string(dsn,lang=lang), autocommit=True)
    cursor = cnxn.cursor()
    return cursor, cnxn

conn_stuff = namedtuple('conn_stuff', ['cursor', 'cnxn', 'cube_info'])

class KyvosConnection():
    """Connection Manager-enabled"""
    def __init__(
        self,
        dsn:str=None,
        cube_schema:str=None,
        cube_name:str=None,
        lang:QueryLanguage=DEFAULT_QUERY_LANGUAGE,
        load_cube_metadata:bool=False,
        cube_info:CubeDef=None  # Alternatively submit cube_info instead of dsn, cube_schema, cube_name
    ):
        self.cube_info = CubeDef(cubeSchema=cube_schema, cubeName=cube_name, dsn=dsn, load_cube_metadata=load_cube_metadata) if cube_info is None else cube_info
        self.cursor,self.cnxn = _get_kyvos_connection(self.cube_info.dsn)

    def __enter__(self):
        return conn_stuff(self.cursor, self.cnxn, self.cube_info)

    def __exit__(self, type, value, traceback):
        self.cursor.close()
        self.cnxn.close()

def _format_sql_query(query_source, show_sql:bool, parameters:dict=None, parameter_prepend_char:str=None)->str:
    """ Takes an OlapQueryDef and generates a sql.

    If query_source is a str, it takes that str, but applies parameters. 
    """
    sql_query = str(query_source) if isinstance(query_source, OlapQueryDef) else query_source 
    if show_sql:
        print(sql_query)
    if parameters:
        for k, v in parameters.items():
            sql_query = sql_query.replace(f"{parameter_prepend_char}{k}", v)
    return sql_query

def _output_exec(cursor, pyodbc_resultset, query_source)->Union[DataFrame, list, None]:  # Could return several kinds of variables, so don't specify.
    """ Branch to the requested output format.
    """
    # Note that is query_source is a str (ex. called from execute_kyvos_sql as a str), we don't
    # know outputformat, so it defaults to DataFrame.
    output_format = query_source.outputformat if isinstance(query_source, OlapQueryDef) else QueryOutputFormat.PandasDataframe
    if output_format == QueryOutputFormat.PandasDataframe:
        result = pd.DataFrame.from_records(pyodbc_resultset, columns=[col[0] for col in cursor.description])

        #result = pd.DataFrame([tuple(t) for t in pyodbc_resultset]) 
        #result.columns = [column[pyodbc_column_index] for column in cursor.description]  # Set column name otherwise will be 0,1,2...                                                                 #
    elif output_format == QueryOutputFormat.PyOdbc:
        result = pyodbc_resultset  # automatically comes back as tuples, so nothing to do.
    elif output_format == QueryOutputFormat.SparkDataframe:
        result = None
    elif output_format == QueryOutputFormat.Json:
        result = json.dumps([tuple(t) for t in pyodbc_resultset], indent=2)
    elif output_format == QueryOutputFormat.SparkDataset:
        result = None
    else:
        result = pd.DataFrame()  # Default to empty pandas dataframe.
    return result


def execute_kyvos_sql(
    cursor,
    query_source,
    empty_dataframe_onerror:bool=False,
    show_sql:bool=False,
    parameters:dict=None,  # dict of parameters that will just do a replace 
    parameter_prepend_char:str = DEFAULT_PARAMETER_PREFIX,  # Charater that prepends a parameter to tag it as a parameter.
    show_perf:bool = False
    )->DataFrame:
    """Execute a query

    Returns:
    ----
        pd.DataFrame

    Usage:
    ----
        >>> df = ky.execute_kyvos_sql(cursor=cnxn, query_source=qdef, show_sql=True, show_perf=True) 
    """
    # query_source could be a str or a OlapQueryDef
    try:
        # Could pass an OlapQueryDefor a SQL string
        # Advantage of OlapQueryDefis that it should have the query language and return format.
        _sql_query = _format_sql_query(query_source, show_sql, parameters, parameter_prepend_char)

        # print(f"call to kyvos {display_now()}")

        _start_time = time.perf_counter()
        _output_format = query_source.outputformat if isinstance(query_source, OlapQueryDef) else QueryOutputFormat.PandasDataframe
        if isinstance(cursor, pyodbc.Cursor):
            _cursor = cursor
        elif isinstance(cursor, conn_stuff):
            _cursor = cursor.cursor
        else:
            raise Exception(f"Cursor must be of type KyPy.KyvosLib.conn_stuff or pyodbc.Cursor")

        if _output_format == QueryOutputFormat.PandasDataframe and isinstance(cursor, conn_stuff):
            # This is a special case where we can load directly using pandas.read_sql.
            _df = pd.read_sql(_sql_query, cursor.cnxn)
        else:
            cursor.execute(_sql_query)
            result_set = cursor.fetchall() #todo: fetch in chunks using cursor as a generator.
            _df = _output_exec(_cursor, result_set, query_source)

        
        if show_perf:
            _end_time = time.perf_counter()
            _perf = displayBasicDataframeInfo(_df, _start_time, _end_time)
            # This is really bad practice. I should have returned an object with these items, but didn't have time to retrofit.
            # The Olap_QueryDef object should not be modified in this function. It's not too bad since we're adding
            # a fairly benign property, but yet, shouldn't do this.
            if isinstance(query_source, OlapQueryDef):
                query_source.rows = _perf[1]
                query_source.query_time = _perf[0]
        return _df

    except pyodbc.Error as perr:
        print(f"pyodbc error: {perr.args[1]}")
        return pd.DataFrame() if empty_dataframe_onerror else e

    except Exception as e:
        print(str(e))
        # print(f"Error execute_kyvos_sql: {e}") #See what sort of errors are returned
        # Can return an empty dataframe (cursor.fetchall will error out if the result is empty.
        # Sometimes, an error is better.
        return pd.DataFrame() if empty_dataframe_onerror else e

def _current_time(caption:str)->str:
    _now = datetime.now()
    print(f'{caption}: {datetime.now()}')

def execute_kyvos_sql_generator(
    cursor,
    query_source,  # Union[OlapQueryDef,str]
    empty_dataframe_onerror:bool=False,  # Return an empty dataframe is there is an error.
    show_sql:bool=False,
    parameters:dict=None,  # dict of parameters that will just do a replace 
    parameter_prepend_char:str=DEFAULT_PARAMETER_PREFIX,  # Charater that prepends a parameter to tag it as a parameter.
    max_rows:int=100,  # If a value is specified, this becomes a generator.
    show_perf:bool=False
    )->DataFrame:
    """Execute a query as a generator.

    Primarily so we don't blow memory and can process massive results in chunks. However, we should try to push-down
    logic as much as we can with filters and having down to the Kyvos engine.

    This is useful if we usually may want to see just the first few rows without waiting for all rows to be read in.
    """
    # query_source could be a str or a OlapQueryDef
    try:
        # Could pass an OlapQueryDefor a SQL string
        # Advantage of OlapQueryDefis that it should have the query language and return format.
        sql_query = _format_sql_query(query_source, show_sql, parameters, parameter_prepend_char)

        if isinstance(cursor, pyodbc.Cursor):
            _cursor = cursor
        elif isinstance(cursor, conn_stuff):
            _cursor = cursor.cursor
        else:
            raise Exception(f"Cursor must be of type KyPy.KyvosLib.conn_stuff or pyodbc.Cursor")
        if show_perf:
            _current_time("Call to Kyvos")

        _cursor.execute(sql_query)
        if show_perf:
            _current_time("Response from Kyvos") # Kyvos will return almost immediately. The processing starts after first fetchmany call.

        result_set = _cursor.fetchmany(max_rows)
        if show_perf:
            _current_time("After first fetchmany") # This is where the upfront is long. Kyvos has processed the whole query.

        while result_set:
            yield _output_exec(_cursor, result_set, query_source)
            result_set = _cursor.fetchmany(max_rows)
            if show_perf:
                _current_time(f"After fetchmany")


    except Exception as e:
        print(str(e))
        # print(f"Error execute_kyvos_sql: {e}") #See what sort of errors are returned
        # Can return an empty dataframe (cursor.fetchall will error out if the result is empty.
        # Sometimes, an error is better.
        return None

# This named tuple is used to return a collection of SQLPart metadata. This is originally to use for building
# a graph database of metadata.
att = namedtuple('att', ["QueryPart", "Attribute", "Member","Measure","Set"])  

class OlapQueryDef:
    """Metadata of a cube query.

    CubeDefs could be by metadata or by query_string.

    By metadata: Use cubedef,group_by_array, measure_array,where_array, having_array, OrderByArray
    By query: Use cubedef and query_string
    """
    def __init__ (self,
        cube:CubeDef,
        group_by_array:list=None,  # None = "All aggregation" The list of columns for the SELECT and GROUP BY list.
        measure_array:list=None,
        where_array:list=None,
        having_array:list=None,
        ord_array:list=None,
        lang:QueryLanguage=None, # Should default to cube.lang.
        outputformat:QueryOutputFormat=DEFAULT_OUTPUT_FORMAT,
        query_string:str=None
    ):

        if not group_by_array and not measure_array:
            raise Exception(f"Select List and/or measure list must be specified.")
        
        self.cube = cube
        if query_string:
            self.__query_string = query_string
        else:
            self.group_by_array = group_by_array
            self.measure_array = measure_array  # measure_array could be None if we just want members.
            self.where_array = where_array
            self.having_array = having_array
            self.ord_array = ord_array

        self.lang = lang if lang else cube.lang
        self.outputformat = outputformat
        self.rows:int=0 # # of rows returned when queried.
        self.query_time:float=0 # Time it takes to run in seconds when queried.


    
    def __eq__(self,other):
        return self.cube == other.cube and \
            self.group_by_array==other.group_by_array and \
            self.measure_array==other.measure_array and \
            self.where_array == other.where_array and \
            self.ord_array == other.ord_array and \
            self.having_array == other.having_array


    def __repr__(self):
        measure_str = [{','.join([str(v) for v in self.measure_array])}] if isinstance(self.measure_array,list) else "" 
        return f"{self.__class__.__name__}(group_by_array=[{','.join([v for v in self.group_by_array])}],measure_array={measure_str},where_array={where_string(self.where_array)})"

    def __str__(self) -> str:
        """ Returns the query (SQL) this object represents.
        """
        # groupByString = ','.join([v if v != v else f"`s`.`{v}`" for v in self.group_by_array])
        #if self.measure_array:
        #    measure_sum = [str(v) for v in self.measure_array]
        #else: 
        #    measure_sum = ""
        return self.query(self.lang)

    @property
    def where_array(self):
        return self._where_array

    @where_array.setter
    def where_array(self, val):
        """Sets where_array.

        Most measures are simple sums. So the user is allowed to just specify the measure name.
        """
        if val is None:
            self._where_array = None
        else:
            self._where_array = val

    @property
    def where_partition(self):
        return WherePartition.get_WherePartition(self)


    @property
    def measure_array(self):
        return self._measure_array

    @measure_array.setter
    def measure_array(self, val):
        """Sets measure_array.

        Most measures are simple sums. So the user is allowed to just specify the measure name.
        """
        if val is None:
            self._measure_array = None
        else:
            self._measure_array = [Agg(v) if isinstance(v,str) else v for v in val] # Converts str into an agg object.

    @property
    def query_string(self):
        return self.__query_string

    @query_string.setter
    def query_string(self, val):
        self.__query_string = val

    @property
    def cube_hash(self):
        if self.cube:
            return self.cube.cube_hash
        return None

    @property
    def hash(self):
        return hash_string(str(self)) # This should be a hash of the query, which will be different if anything changes.

 
    def query(self, lang:QueryLanguage=DEFAULT_QUERY_LANGUAGE)->str:
        """Let's query strings be formulated without setting the query_string.

        This way, a user can see what a query will look like without setting the query string.
        
        """
        if lang.is_sql:
            query = self._formatSQL(lang)
        elif lang == QueryLanguage.MDX:
            query = str(self._formatMDX())
        else:
            query = None
        return query

    def _formatSQL(self, lang:QueryLanguage=DEFAULT_QUERY_LANGUAGE)->str:
        """
        enc - A string enclosing elements of the SQL. It defaults to ` which is used by Kyvos SQL.
        """
        if not lang.is_sql:
            raise Exception(f"Specified language must be a SQL dialect")

        e,c, _ = unpack_ql(lang)

        select_list = ','.join([v if v != v else f"{e}s{c}.{e}{v}{c}" for v in self.group_by_array]) if self.group_by_array else ""
        group_by_string = f" GROUP BY {select_list}" if select_list!="" else ""
        #if self.group_by_array:
        #    select_list=','.join([v if v != v else f"`s`.`{v}`" for v in self.group_by_array])
        #    group_by_string=f" GROUP BY {select_list}"

        if self.measure_array:
            measure_sum = (','.join([v.query_expression(lang) for v in self.measure_array]))
        else:
            measure_sum = "" # Cannot use None because that will literally be printed.
        sel_measure_delimiter = "," if select_list != "" and measure_sum != ""  else ""

        return f'SELECT {select_list}{sel_measure_delimiter}{measure_sum} FROM {self.cube.query_expression(lang)} {where_string(self.where_array, lang=lang)}{group_by_string} {having_string(self.having_array,lang=lang)} {order_string(self.ord_array, lang=lang)}'
    

    def _formatMDX(self)->MDXStatement:
        axes = ','.join([f"{self._add_hierarchy_name(v)}.MEMBERS ON {idx}" for idx,v in enumerate(self.group_by_array)])

        agg_items = []
        with_items = []
        measureDim = None
        for i in self.measure_array:
            if issubclass(type(i), AggBase):
                if i.is_MDX_calculated_measure:
                    with_items.append(i.query(QueryLanguage.MDX))
                else:
                    agg_items.append(i.query(QueryLanguage.MDX))

        where_items = []
        if self.where_array:
            for i in self.where_array:
                if ("_formatMDX" in type(i).__dict__) or (type(i) is WhereTermEquality and i.equality==CompOp.EQ.symbol):
                    where_items.append(i.query(QueryLanguage.MDX))

        if len(agg_items) == 1:
            # If there is only 1 non-calc agg, use it as the measure to appear in cells.
            where_items.append(agg_items[0])
        elif len(agg_items) > 1:
            axes = axes + ',{' + ','.join(agg_items)+f"}} ON {str(len(self.group_by_array))}"

        where_string = "WHERE (" + (','.join([v for v in where_items])) + ")" if len(where_items) > 0 else ""
        with_string = "WITH " + ' '.join([v for v in with_items]) + " " if len(with_items) > 0 else ""

        return MDXStatement(f"{with_string}SELECT {axes} FROM [{self.cube.cubeName}] {where_string}")

    # to-do: needs more work.
    def _add_hierarchy_name(self,attribute_name:str)->str:
        """Meant for MDX"""
        if self.cube.cube_metadata:
            for k,v in self.cube.cube_metadata.drill_paths.items():
                if attribute_name in v:
                    return f"[{k}].[{attribute_name}]" # The attribute is it's own "hierarchy".
        return f"[{attribute_name}]"

    def __encodeQueryJSON__(self):
        """Returns the __dict__ of this cubedef object"""
        return json.dumps(self, indent=2, cls=OlapQueryDefEncoder)

    def JSON_full_filename(self,filename):
            return EnvVar.prepend_filename_path(filename, 'KYVOS_OLAP_QUERIES', ".json")

    def save_as_JSON(self,filename:str=None)->str:
        if not filename:
            filename = self.hash
        _full_filename = self.JSON_full_filename(filename)
        with open(_full_filename, 'w') as json_file:
            json_file.write(encodeQueryJSON(self))
        return _full_filename


    @staticmethod
    def load_from_JSON(filename:str):
        full_filename = EnvVar.prepend_filename_path(filename, 'KYVOS_OLAP_QUERIES', ".json")
        with open(full_filename, 'r') as json_file:
            jstr = json.dumps(json.load(json_file), indent=2)
        obj = OlapQueryDef.__loadQueryJSON__(jstr)
        return obj

    @staticmethod
    def __loadQueryJSON__(jsonStr):

        def _get_value(key:str):
            return objJSON[key] if key in objJSON else None

        def _key_exists(key:str)->bool:
            return key in objJSON

        objJSON = json.loads(jsonStr)

        _class_array = [AggBase, WhereBase, HavingBase, ord]
        _class_name_array = ["_measure_array", "_where_array", "_having_array", "_ord_array"]  # _measure_array is the underlying variable for the @property named measure_array.
        par = []
        for cls,nm in zip(_class_array, _class_name_array):
            par_array = []
            if _key_exists(nm) and objJSON[nm] is not None:
                for v in objJSON[nm]:
                    a = cls.factory(v)
                    if a:
                        par_array.append(a)
            par.append(par_array)


        return OlapQueryDef(
            cube=CubeDef(cubeSchema=objJSON["cube"]["cubeSchema"], cubeName=objJSON["cube"]["cubeName"], dsn=objJSON["cube"]["dsn"]),
            group_by_array=objJSON["group_by_array"],
            measure_array=par[0],
            where_array=par[1],
            having_array=par[2],
            ord_array=par[3],
            lang=getattr(QueryLanguage,objJSON["lang"][0]), # 0 is the name attribute of the tuple.
            outputformat=objJSON["outputformat"],
            query_string=_get_value("_OlapQueryDef__query_string")
        )

    def get_attributes(self)->pd.DataFrame:
        """Parses out attributes and members used in an OLAPQueryDef instance.

        This is utilized in the Insight Space Graph.
        """
        df = pd.DataFrame(columns = ["cube", "schema", "QueryPart", "Attribute", "Member","Measure","hash","Set","Class","repr"])
        _cube_name = self.cube.cubeName
        _cube_schema = self.cube.cubeSchema

        for idx, sqlpart_array in enumerate([self.group_by_array, self.measure_array, self.where_array]):
            if not sqlpart_array:
                continue
            for spart in sqlpart_array:
                if isinstance(spart,SQLPartBase):
                    attributes = spart.get_attributes()
                else:
                    part = "SLICE" if idx == 0 else "METRIC"
                    attributes = [att(part,spart,None,None,None)]

                if attributes:
                    for attr in attributes:
                        df.loc[df.shape[0]] = [
                            _cube_name, 
                            _cube_schema, 
                            attr.QueryPart, 
                            attr.Attribute, 
                            attr.Member, 
                            attr.Measure, 
                            self.hash,
                            attr.Set, 
                            str(type(spart)),repr(spart)
                            ]

        return df

class OlapQueryDefEncoder(JSONEncoder):
    """JSON encoder for OlapQueryDef"""
    def default(self, obj):
        # todo: I think the xmldocument in CubeMetadata doesn't have a __dict__.
        try:
            return obj.__dict__
        except:
            return None


def encodeQueryJSON(obj:OlapQueryDef):
    """execute the __queryJSON__ method if there is one"""
    if (hasattr(obj, "__encodeQueryJSON__")):
        return obj.__encodeQueryJSON__()
    return None

def decodeQueryJSON(objClass,jsonStr):
    """execute the __queryJSON__ method if there is one"""
    if "__loadQueryJSON__" in objClass.__dict__:
        return objClass.__loadQueryJSON__(jsonStr)
    return None

def save_as_JSON(obj,full_filename)->pathlib.Path:
    with open(full_filename, "w") as json_file:
        json_file.write(encodeQueryJSON(obj))
    return full_filename

class DataSourcePlatforms(IntEnum):
    Hadoop = 0
    Snowflake = 1
    SQLServer = 2
    AWS_S1 = 3
    Azure = 4
    Databricks = 5
    Redshift = 6



class SQLPartBase:
    """
    Base class for query expression parts used to construct a full query (SQL or MDX).

    For most classes deriving from SQLPartBase, the __str__ function will return a SQL expression, which
    could be used to construct a full SQL statement.

    For any language that's not Kyvos SQL, there will be another method. For example _format_MDX.
    """
    def __init__(self):
        self.class_name = self.__class__.__name__

    @staticmethod
    def encloseValue(value)->str: #Value should be of undefined type.
        """Returns a value enclosed in single quotes if it's a string """
        return f"'{value}'" if isinstance(value,str) else value

    @abstractmethod
    def get_attributes(self)->list:
        """ Abstract method definition for method to return attribute names of any SQLPartBase.
        """
        return None

    @abstractmethod
    def query_expression(self, lang:QueryLanguage=DEFAULT_QUERY_LANGUAGE)->str:
        return "" # Return a blank string because this will be used in a string concat.


# Note: Remember that classes are recognized by the interpretter if they are defined prior!!!!
class WhereBase(SQLPartBase):
    """Superclass for base"""
    def __init__(self, attribute:str):
        self.attribute = attribute
        super().__init__()
 
    def query(self, lang:QueryLanguage=DEFAULT_QUERY_LANGUAGE)->str:
        """Let's query strings be called independetly"""
        if lang == QueryLanguage.KyvosSQL:
             return str(self)
        elif lang == QueryLanguage.MDX:
            return str(self._formatMDX())
        elif lang == QueryLanguage.SparkSQL:
            return None
        return None

    @abstractmethod
    def _formatMDX(self)->MDXPartBase:
        return MDXPartBase("")

    @staticmethod
    def factory(where_dict:dict):
        if where_dict["class_name"] == "WhereTermIN":
            return WhereTermIN(attribute=where_dict["attribute"], valueArray=where_dict["valueArray"])
        elif where_dict["class_name"] == "WhereTermEquality":
            return WhereTermEquality(attribute=where_dict["attribute"], value=where_dict["value"], equality=where_dict["equality"])
        return None


def order_string(ord_array:list, lang:QueryLanguage=DEFAULT_QUERY_LANGUAGE)->str:
    # Constructs the ORDER sql statement.
#    return " ORDER BY " + ",".join([f"{str(v)}" for v in ord_array]) if ord_array else ""
    e,c, _ = unpack_ql(lang)
    return " ORDER BY " + ",".join([v.query_expression(lang) if isinstance(v,ord) else f"{e}{v}{c}" for v in ord_array]) if ord_array else ""


# Function to Execute a simple GROUP BY SQL from a Kyvos cube. Good example of function in the Kyvos Python package
# cubeSchema - For Kyvos, this is the name of the cube folder.
# cubeName - Name of the Cube.
# group_by_array - array of attribute names. ex. ['store_number','store_name']
# measure_array - array of measure names and alias that will be summed. ex. [['sales','Sales'],['profit','Profit']]

# def dfGetKyvosGroupBySimple1(cursor,setDef):
#    return dfGetKyvosGroupBySimple(cursor,setDef.cube,setDef.group_by_array,setDef.measure_array,setDef.where_array,setDef.having_array)

def where_string(whereClauseArray:list, prefix:str="WHERE", lang:QueryLanguage=DEFAULT_QUERY_LANGUAGE)->str:
    if not whereClauseArray:
        return ""
    #for w in whereClauseArray:
    _where_string = " AND ".join([v if v!=v else v.query_expression(lang) for v in whereClauseArray])
            
    return f" {prefix} {_where_string}"


class WhereTermIN(WhereBase):
    def __init__ (self, attribute:str, valueArray:list=None):
        self.valueArray = valueArray # Array of values: ['Eugene','Ajay']
        super().__init__(attribute)
        
    def __str__(self):
        return self.query_expression()

    def query_expression(self, lang:QueryLanguage=DEFAULT_QUERY_LANGUAGE)->str:
        if lang == QueryLanguage.MDX:
            return self._formatMDX()
        e,c, _ = unpack_ql(lang)

        if isinstance(self.valueArray, str):
            _where_string = f"'{self.valueArray}'"
        else:
            _where_string = ','.join([v if v!=v else f"'{v}'"  for v in self.valueArray])
        return f"({e}s{c}.{e}{self.attribute}{c} IN ({_where_string}))"

    def __repr__(self):
        return f"{self.class_name}(attribute={self.attribute},valuearray=[{','.join([str(v) for v in self.valueArray])}])"

    def _formatMDX(self)->MDXPartBase:
        return MDXPartBase('{' + (','.join([f"[{self.attribute}].[{v}]" for v in self.valueArray])) + "}")

    def get_attributes(self)->list:
        """ Abstract method definition for method to return attribute names of any SQLPartBase.
        """
        _set = sorted_set_name(self.valueArray)
        return [att("FILTER", self.attribute, v, None,_set) for v in self.valueArray]

class WhereTermEquality(WhereBase):
    """
    
    get_attributes inherited from WhereBase
    """
    # Let value be of an open type. However, it should be str, int, float, date.
    def __init__ (self, attribute:str, equality:str, value:Union[str,int,float,None]):
        self.equality = equality if equality else "=" # >, >, =, <=, etc. This will be placed literally because attribute and value.
        self.value = value
        super().__init__(attribute)
        
    def __str__(self):
        return self.query_expression()

    def query_expression(self, lang:QueryLanguage=DEFAULT_QUERY_LANGUAGE)->str:
        if lang == QueryLanguage.MDX:
            return self._formatMDX()
        e,c, _ = unpack_ql(lang)
        return f"({e}s{c}.{e}{self.attribute}{c} {self.equality} {super().encloseValue(self.value)})"

    def __repr__(self):
        return f"{self.class_name}(attribute={self.attribute},value=[{self.value},eqaulity={self.equality})"

    def _formatMDX(self)->MDXPartBase:
        return MDXPartBase(f"[{self.attribute}].[{self.value}]")

    def get_attributes(self)->list:
        """ Default for WhereBase method definition for method to return attribute names of any SQLPartBase.
        """
        return [att("FILTER", self.attribute, self.value,None,None)]



class WhereLikeOptions(IntEnum):
    Contains = 0,
    StartsWith = 1,   
    EndsWith = 2

LIKE_FORMATS = {
    WhereLikeOptions.Contains: lambda val: f'%{val}%',
    WhereLikeOptions.StartsWith: lambda val: f'{val}%',
    WhereLikeOptions.EndsWith: lambda val: f'%{val}',
}

class WhereLike(WhereBase):
    """ Where LIKE clause.
    Let value be of an open type. However, it should be str, int, float, date.
    """
    def __init__ (self, attribute:str, value:Union[str, list], like_option:WhereLikeOptions=WhereLikeOptions.Contains, negate:bool=False):
        self.value = value # If value is a list, this means this is OR. Ex: ['Harry','Mike'] would be: col LIKE 'Harry%' OR col LIKE 'Mike%'
        self.like_option = like_option
        self.negate = negate
        super().__init__(attribute)
        
    def __str__(self):
        return self.query_expression()

    def query_expression(self, lang:QueryLanguage=DEFAULT_QUERY_LANGUAGE)->str:
        if lang == QueryLanguage.MDX:
            return self._formatMDX()
        e,c,_ = unpack_ql(lang)

        def _fmt(val:str):
            _val = LIKE_FORMATS[self.like_option](val)
            return f"({e}s{c}.{e}{self.attribute}{c} {'NOT ' if self.negate else ''} LIKE '{_val}')"

        if isinstance(self.value, list):
            result = " OR ".join([_fmt(val) for val in self.value])
        else:
            result = _fmt(self.value)
        return f"({result})"

    def __repr__(self):
        return f"{self.class_name}(attribute={self.attribute},value=[{self.value})"

    def _formatMDX(self)->MDXPartBase:
        return MDXPartBase(f"[{self.attribute}].[{self.value}]")  # TODO: This isn't good MDX for "contains"

    def get_attributes(self)->list:
        """ Default for WhereBase method definition for method to return attribute names of any SQLPartBase.
        """
        return [att("FILTER", self.attribute, self.value,None,None)]


class WhereConstant(WhereBase):
    """ Where clause to add any string.
    """
    def __init__ (self, value:str):
        self.value = value
        super().__init__(attribute=None)
        
    def __str__(self)->str:
        return self.query_expression()

    def query_expression(self, lang:QueryLanguage=DEFAULT_QUERY_LANGUAGE)->str:
        if lang == QueryLanguage.MDX:
            return self._formatMDX()
        return f"{self.value})"

    def __repr__(self):
        return f"{self.class_name}(value=[{self.value})"

    def _formatMDX(self)->MDXPartBase:
        return MDXPartBase(f"[{self.value}].[{self.value}]") # TODO: This this isn't right because no attribute.

class WherePartition(WhereBase):
    """Special where clause that will iterate through a generator.

        Returns:
        ----
            list:dict

        Usage:
        ----
            >>> results = WherePartition(attribute=<cubeattribute>, members=[<int>,<float>,<str>,<tuple>])
    """
    # WherePartition seems like a subclass of WhereTermEquality, but not really.
    ###
    # members can be a list of str/int/float or it can be a tuple of ranges (start, end). 
    # attribute can be a single attribute or a tuple of attributes.
    # if attribute is a tuple of attributes, members should be a list of tuples.
    def __init__ (self, attribute:Union[tuple,str], members:list, auto_increment_idx:bool=True):
        self.members = members
        self.reset_index()
        self.auto_increment_idx = auto_increment_idx
        super().__init__(attribute)

    def __str__(self)->str:
        return self.query_expression()

    def query_expression(self, lang:QueryLanguage=DEFAULT_QUERY_LANGUAGE)->str:
        """ When __str__ is called, the index increments. This is the iteration mechanism.

        A lock is place on the OlapQueryDef containing this WherePartition. That happens in _exec_by_part_async

        """

        e,c, _ = unpack_ql(lang) # Retrieves starting/ending characters used to encase keywords. For Kyvos SQL, it's ~

        def _text(attribute:str, member, oper:str="=")->str:
            """If the "member is a range, the text will be part of an AND."""
            if isinstance(member,str):
                member = f"'{member}'"
            return f"({e}s{c}.{e}{attribute}{c} {oper} {member})"

        if self.auto_increment_idx:
            self.index = self.index + 1
        if self.index >= 0 and self.index < len(self.members):
            if isinstance(self.members[self.index],tuple):
                _mbrs = [_text(self.attribute[idx], mbr) for idx, mbr in enumerate(self.members[self.index])]
                return " AND ".join(_mbrs)
            else:
                return _text(self.attribute, self.members[self.index])
        return None

    def reset_index(self):
        self.index =- 1 # We're going to iterate from the start of len(members).

    @property
    def member_caption(self):
        """Used to identify the current partition."""
        if self.index >= 0 and self.index < len(self.members) and isinstance(self.attribute,tuple):
            if isinstance(self.members[self.index],tuple):
                return "__".join([f"{str(self.attribute[i])}_{str(m)}" for i, m in enumerate(self.members[self.index])])
            else:
                return str(self.members[self.index])
        return None


    @staticmethod
    def get_WherePartition(query_source:OlapQueryDef):
        """ Look for the WherePartition within the OlapQueryDef's where_array"""
        for val in query_source.where_array:
            if isinstance(val, WherePartition):
                return val
        return None

class WhereTermBetween(WhereBase):
    def __init__ (self, attribute, startValue, endValue):
        self.startValue = startValue  # >, >, =, <=, etc. This will be placed literally because attribute and value.
        self.endValue = endValue
        super().__init__(attribute)
        
    def __str__(self):
        return self.query_expression()

    def query_expression(self, lang:QueryLanguage=DEFAULT_QUERY_LANGUAGE)->str:
        if lang == QueryLanguage.MDX:
            return self._formatMDX()
        e,c,_ = unpack_ql(lang)
        return f"({e}s{c}.{e}{self.attribute}{c} >= {super().encloseValue(self.startValue)} AND {e}s{c}.{e}{self.attribute}{c} <= {super().encloseValue(self.endValue)})"

    def __repr__(self):
        return f'{self.class_name}(attribute="{self.attribute}",startValue=[{super().encloseValue(self.startValue)},endValue=[{super().encloseValue(self.endValue)})'

    def _formatMDX(self)->MDXPartBase:
        return MDXPartBase(f"[{self.attribute}].[{self.startValue}] : [{self.attribute}].[{self.endValue}]")

    def get_attributes(self)->list:
        """ Default for WhereBase method definition for method to return attribute names of any SQLPartBase.
        """
        _member_array = [self.startValue, self.endValue]
        _set = sorted_set_name(_member_array)
        return [att("FILTER", self.attribute, v, None,_set) for v in _member_array]

class HavingBase(SQLPartBase):
    """Superclass for having """
    def __init__(self):
         super().__init__()

    @staticmethod
    def factory(having_dict:dict):
        if having_dict["class_name"] == "HavingTermEquality":
            return HavingTermEquality(attribute=having_dict["attribute"], value=having_dict["value"], equality=having_dict["equality"])
        return None

def having_string(havingClauseArray:list, lang:QueryLanguage=DEFAULT_QUERY_LANGUAGE)->str:
    if not havingClauseArray:
        return ''
    #for w in havingClauseArray:
    _having_string = " AND ".join([v if v!=v else v.query_expression(lang) for v in havingClauseArray])    
    return f'HAVING {_having_string}'
        
class HavingTermEquality(HavingBase):
    def __init__ (self, attribute:str, equality:str, value:Union[str, int, float]):
        self.attribute = attribute  # This is the attribute we're checking for values: [Sales]<60
        self.equality = equality  # >, >, =, <=, etc. This will be placed literally because attribute and value.
        self.value = value
        super().__init__()   
        
    def __str__(self):
        return self.query_expression()

    def query_expression(self, lang:QueryLanguage=DEFAULT_QUERY_LANGUAGE)->str:
        e,c,_ = unpack_ql(lang)
        return f"({e}{self.attribute}{c} {self.equality}{super().encloseValue(self.value)})"

    def __repr__(self):
        return f"{self.class_name}(attribute='{self.attribute}',value='{self.value}',equality='{self.equality}')"

    def get_attributes(self)->list:
        """ Default for WhereBase method definition for method to return attribute names of any SQLPartBase.
        """
        return [att("FILTER", self.attribute, self.value,None,None)]

def displayBasicDataframeInfo(df, startTime:int, endTime:int, countColName:str="count", display_results:bool=True):
    """ Display the r4sponsiveness of a query: Latency + Processing time.

    TODO: I actually don't know how to get the amount of compute time from Kyvos. So what shows here is the "door to door" (compute + transport) time.
    
    startTime and endTime are ints from code: startTime=time.perf_counter()
    countColName is the name of a measure that holds how many facts made up the aggregation. This is to show how many rows would have needed to be read.
    """

    _rows = len(df)
    _underlying_row_count = df[countColName].sum() if countColName in df.columns else None
    _query_time = endTime - startTime
    if display_results:
        print(df.head(10))
        print(f"Rows returned from Kyvos: {str(_rows)}")
        print(f"Total query time: {_query_time:0.4f} seconds")
        if countColName in df.columns:
            print(f"Underlying fact rows: {_underlying_row_count:0.0f}")
    return (round(_query_time,5), _rows)

class AggBase(SQLPartBase):
    """Superclass for agg"""

    def __init__(self,mdx_calc_measure_only:bool=False):
        self.mdx_calc_measure_only = mdx_calc_measure_only    # Will this aggregation appear in a MEASURES axis?
                                                                    # This is as opposed to being a calculated measure used by
                                                                    # Another calculated measure.
        super().__init__()

    def query(self, lang:QueryLanguage=DEFAULT_QUERY_LANGUAGE)->str:
        """Will return query segment for this agg. Let's query strings be called independetly"""
        if lang == QueryLanguage.KyvosSQL:
             return str(self) # Be sure to implement __str__ in each subclass as a KyvosSQL string.
        elif lang == QueryLanguage.MDX:
            return str(self._formatMDX())
        elif lang == QueryLanguage.SparkSQL:
            return self.formatSparkSQL()
        return None

    @abstractproperty
    def is_MDX_calculated_measure(self)->bool:
        return False

    def _formatSQL(self):
        return self.__str__()

    def _formatMDX(self)->MDXPartValue:
        return MDXPartValue()

    def _formatSparkSQL(self):
        #Default to __str__ for now since it's SQL.
        return self.__str__()

    @staticmethod
    def mdx_only_classes():
        """List all agg subclasses that are only MDX"""
        #Code sample: print(ky.AggBase.mdx_only_classes())
        return [c for c in AggBase.__subclasses__() if "_formatMDX" in c.__dict__ and "_formatSQL" not in c.__dict__]

    @staticmethod
    def mdx_option_classes():
        """List all agg subclasses that can format MDX"""
        return [c for c in AggBase.__subclasses__() if "_formatMDX" in c.__dict__]

    @staticmethod
    def factory(agg_dict:dict):
        # TODO: Need to deserialize other types of AggBase objects.
        obj = None
        if agg_dict["class_name"] == "Agg":
            obj = Agg(metric=agg_dict["metric"], alias=agg_dict["alias"], aggFunc=agg_dict["aggFunc"], includeAlias=agg_dict["includeAlias"])
        elif agg_dict["class_name"] == "AggCase":
            obj = AggCase(
                metric=agg_dict["metric"], 
                alias=agg_dict["alias"], 
                aggFunc=agg_dict["aggFunc"], 
                whenAttribute=agg_dict["whenAttribute"],
                whenValue=agg_dict["whenValue"]
            )
            obj.equality = agg_dict["equality"]
        return obj


class AggCase(AggBase):
    def __init__(self, whenAttribute:str, whenValue:str, metric:str, alias:str=None, aggFunc="SUM", equality:CompOp=CompOp.EQ):
        self.whenAttribute = whenAttribute
        self.whenValue = whenValue
        self.metric = metric  # Metric in the cube.
        self.alias = whenValue if not alias else alias
        self.aggFunc = aggFunc
        self.equality = " IN " if isinstance(whenValue,list) else equality.symbol  # Convert to string because CompOp doesn't have a __dict__. json will screw up.
        super().__init__()

    def __str__(self):
        return self.query_expression()

    def query_expression(self, lang:QueryLanguage=DEFAULT_QUERY_LANGUAGE)->str:
        if lang == QueryLanguage.MDX:
            return self._formatMDX()

        def _enclose(v:str)->str: # TODO having problem using super().encloseValue.
            return f"'{v}'"

        _alias_str = self.whenValue if self.alias is None else self.alias
        _when_value = f"({','.join([_enclose(v) for v in self.whenValue])})" if isinstance(self.whenValue,list) else super().encloseValue(self.whenValue)
        e,c, case_eq = unpack_ql(lang)
        eq = self.equality if self.equality=="IN" else case_eq
        return f"{self.aggFunc}(CASE WHEN ({e}s{c}.{e}{self.whenAttribute}{c}{eq}{_when_value}) THEN {e}s{c}.{e}{self.metric}{c} ELSE NULL END) AS {_alias_str}"

    def __repr__(self):
        return f"{self.class_name}(whenAttribute='{self.whenAttribute}',whenValue='{self.whenValue}',metric='{self.metric}',alias='{self.alias}')"

    def _formatMDX(self)->MDXPartValue:
        return MDXPartValue(f"MEMBER [MEASURES].[{self.alias}] AS IIF([{self.whenAttribute}].CURRENTMEMBER.MEMBER_NAME={super().encloseValue(self.whenValue)} THEN [MEASURES].[{self.metric}] ELSE NULL ")

    @property
    def is_MDX_calculated_measure(self)->bool:
        return True

    def get_attributes(self)->list:
        """ Abstract method definition for method to return attribute names of any SQLPartBase.
        """
        _set = ",".join([str(self.metric),str(self.whenValue)] )
 
        return [att("METRIC", self.whenAttribute, self.whenValue,self.metric,_set)]

    @staticmethod
    def agg_case_list(when_attribute:str,metric:str, case_list:list,append_to:list=None) -> list:
        """ Generate a list of AggCase objects based off a list of values.
        """
        _new_aggcase = [
            AggCase(whenAttribute=when_attribute, whenValue=c, metric=metric, alias=c) 
            for c in case_list
            ]
        return append_to.extend(_new_aggcase) if append_to else _new_aggcase


class Agg(AggBase):
    def __init__(self, metric:str, alias:str=None, aggFunc="SUM", includeAlias:bool=True, mdx_calc_measure_only:bool=False):
        self.metric = metric
        self.alias = metric if alias == None else alias
        self.aggFunc = aggFunc
        self.includeAlias = includeAlias
        super().__init__(mdx_calc_measure_only)

    def __str__(self):
        return self.query_expression()

    def query_expression(self, lang:QueryLanguage=DEFAULT_QUERY_LANGUAGE)->str:
        if lang == QueryLanguage.MDX:
            return self._formatMDX()

        e,c,_ = unpack_ql(lang)
        alias_str = f" AS {e}{self.alias}{c}" if self.includeAlias else ""
        return f"{self.aggFunc}({e}s{c}.{e}{self.metric}{c}){alias_str}"

    def __repr__(self):
        return f"{self.class_name}(metric='{self.metric}',alias='{self.alias}',aggFunc='{self.aggFunc}')"

    def _formatMDX(self)->MDXPartValue:
        return f"[MEASURES].[{self.metric}]"

    def get_attributes(self)->list:
        """ Abstract method definition for method to return attribute names of any SQLPartBase.
        """
        return [att("METRIC", self.metric, None, self.metric,None)]

    @property
    def is_MDX_calculated_measure(self)->bool:
        # todo: It should really be that aggFunc is not the function in the cube measure.
        # Need metadata to know that.
        return False if self.aggFunc in ["SUM"] else True


class AggFormula(AggBase):
    """Agg class that allows for a simple formula,"""

    # In formula, create a tag for each item in aggs as %0, %1, etc.
    def __init__(self, aggs:list, formula:str, alias:str):
        self.aggs = aggs # Collection of AggBase objects that plug into the sprint-style formula variable.
        self.alias = alias
        self.formula = formula # sprint-style formula for the aggregation.
        super().__init__()

    def __str__(self):
        return self.query_expression()

    def query_expression(self, lang:QueryLanguage=DEFAULT_QUERY_LANGUAGE)->str:
        if lang == QueryLanguage.MDX:
            return self._formatMDX()
        e , c, _ = unpack_ql(lang)

        processedFormula = f"{self.formula}  AS {e}{self.alias}{c}"
        for idx,agg in enumerate(self.aggs):
            agg.includeAlias = False
            # Note that % is used to denote a formula replace.
            processedFormula = processedFormula.replace(f"%{idx}",agg.query_expression(lang))
        return processedFormula
    
    def __repr__(self):
        _agg_repr = ",".join([repr(agg) for agg in self.aggs])
        return f"{self.class_name}(aggs=[{_agg_repr}],alias='{self.alias}',formula='{self.formula}')"

    @property
    def aggs(self):
        return self._aggs

    @aggs.setter
    def aggs(self,val):
        """Sets measure_array.

        Most measures are simple sums. So the user is allowed to just specify the measure name.
        """
        self._aggs = [Agg(v) if isinstance(v,str) else v for v in val]

    def _formatMDX(self)->MDXPartValue:
        formula = self.formula
        for idx,agg in enumerate(self.aggs):
            agg.includeAlias = False
            formula = formula.replace(f"%{idx}",str(agg.query(QueryLanguage.MDX)))
        return MDXPartValue(f"[MEASURES].[{self.alias}] AS {formula} ")

    @property
    def is_MDX_calculated_measure(self)->bool:
        # todo: It should really be that aggFunc is not the function in the cube measure.
        # Need metadata to know that.
        return True

    def get_attributes(self)->list:
        """ Abstract method definition for method to return attribute names of any SQLPartBase.
        """
        _set = ",".join([agg.metric for agg in self.aggs] )
 
        return [att("METRIC", agg.metric, agg.metric, agg.metric, _set) for agg in self.aggs]

    

class ord(SQLPartBase):
    """For the ORDER BY of the SQL"""
    def __init__(self, column_name:str, descending:bool=False):
        self.column_name = column_name
        self.descending = descending
        super().__init__()

    def __eq__(self, other):
        return self.column_name == other.column_name and self.descending == other.descending 


    def __str__(self):
        return self.query_expression()

    def query_expression(self, lang:QueryLanguage=DEFAULT_QUERY_LANGUAGE)->str:

        # Note: Don't wrap self.column name with `s`.`` because the column name is a post-process column.
        e, c ,_ = unpack_ql(lang)
        return f"{e}{self.column_name}{c} {'DESC' if self.descending else 'ASC'}"

    def __repr__(self):
        return f"{self.class_name}(column_Name=[{self.column_name}],descending={str(self.descending)})"


    @staticmethod
    def factory(ord_dict:dict):
        print(ord_dict)
        if ord_dict["class_name"] == "ord":
            return ord(column_name=ord_dict["column_name"], descending=ord_dict["descending"])

        return None

def date_str_to_order(dateLevel:str,dateStr:str)->datetime:
    """Changes a date level value to a sortable version."""
    # For example, quarters in Kyvos are Q1-2005. It will be changed to 2005-01-01.
    if dateLevel == "Year":
        return datetime.strptime(dateStr, '%Y')
    elif dateLevel == "Quarter":
        return datetime.strptime(dateStr, '%b-%Y')
    return None


def format_output_file(file_name:str)->str:
    """Prepends path to a fileName"""
    return f"{EnvVar.get_var('KYVOS_OUTPUT_DATA_DIR')}{file_name}"

def format_input_file(file_name:str)->str:
    return f"{EnvVar.get_var('KYVOS_OUTPUT_DATA_DIR')}{file_name}"

def execute_by_partition(cursor, query_source:OlapQueryDef, empty_dataframe_onerror:bool=False, show_sql:bool=False)->DataFrame:
    """Serialize execute calls to Kyvos through the generator functionality."""
    # The serialization of the query by some partition eases the burden on limited resources - just like "flattening the curve"
    # of the early Covid-19 days. The idea was we'll all get it, but let's spread it out over a longer time so as to not overburden the healthcare system.
    _where_part = _get_execute_where_part(query_source)
 
    for _ in _where_part.members:
        # The WherePartition object controls the specified partition.
        yield (execute_kyvos_sql(cursor, query_source, empty_dataframe_onerror=empty_dataframe_onerror, show_sql=show_sql))

 

exec_async = namedtuple('exec_async', ['dsn', 'query_source', 'lock', 'empty_dataframe_onerror','post_func',"index_col"])  

# Tuple of performance metrics from asynchronous query.
exec_async_perf = namedtuple('exec_async_perf', ['query_time', 'rows', 'sql', 'caption', 'start_date', 'end_date'])  

exec_async_postfunc_packet = namedtuple('exec_async_postfunc_packet', ['Data','Caption'])  


def execute_by_partition_async(dsn:str, query_source:OlapQueryDef, empty_dataframe_onerror:bool=False, post_func=None, index_col:str=None):
    """Same as execute_by_partition, but asynchronous

    post_func is a function that can be run on each ds. It should not be intense. f will take a df as an argument.
    
    """
    # cnxn is the obdb connection
    # The advantage of running serially (execute_by_partition) is that we reduce the risk of running out of resources.
    _where_part = _get_execute_where_part(query_source)

    lock = Lock() # This is intended to lock the creation of the sql in _exec_by_part_async.
    num_threads = len(_where_part.members)
    df_results = []
    f_results = []
    perf_results = []

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = [executor.submit(_exec_by_part_async, exec_async(dsn, query_source, lock, empty_dataframe_onerror,post_func, index_col)) for idx in range(0,num_threads)]
        for f in concurrent.futures.as_completed(results):
            result = f.result() # Returns a list of two values - data results and the optional post_func results.
            df_results.append(result[0])
            f_results.append(result[1])
            perf_results.append(result[2])

    return df_results, f_results, perf_results # REturn types: list[pd.DataFrame],[],list[exec_async_perf]

def _get_execute_where_part(query_source:OlapQueryDef)->WherePartition:
    """ creates a list of where_part objects based on the presence of a WherePartition object in the query_source where_array. 
    """
    if not query_source.where_partition:
        raise Exception(f"Must include a WherePartition in where_array to run execute_by_partition")
    query_source.where_partition.reset_index()
    return query_source.where_partition

def conn_string(dsn:str, uid:str=None, pwd:str=None, lang:QueryLanguage=DEFAULT_QUERY_LANGUAGE)->str:
    uid = uid if uid else EnvVar.get_var("KYVOS_UID")
#    pwd = pwd if pwd else os.getenv('KYVOS_PWD') # KYVOS_PWD is not in the collection.
#    return f"DSN={dsn};UID={uid};PWD={pwd}"
    if lang.db_type == "SQL Server":
        return f"DSN={dsn}"     
    return f"DSN={dsn};UID={uid}"  # The password is in the Kyvos dsn (ODBC) that is set up.

def _exec_by_part_async(ea:exec_async)->pd.DataFrame:

    with ea.lock:
        _sql = str(ea.query_source)  # The parition is determined in the call to the __str__ function.
                                    # The str on query_source will invoke the str on the WhereParition object, which increments the index.
        # The following lines for are debug purposes.
        # _wp = WherePartition.get_WherePartition(ea.query_source)
        _caption = ea.query_source.where_partition.member_caption


    with pyodbc.connect(conn_string(ea.dsn), autocommit=True) as cnxn:
        try:

            _start_time = time.perf_counter()
            _start_date = datetime.now()
            _result = pd.read_sql_query(sql=_sql, con=cnxn, index_col=ea.index_col)
            _end_date = datetime.now()
            _end_time = time.perf_counter()

            # If there is no result, the return value is of TypeError.
            # It seems like the error, "'NoneType' object is not iterable" comes from the pyodbc driver, when there is no query result.
            if isinstance(_result, pd.DataFrame):
                f_result = ea.post_func(exec_async_postfunc_packet(_result, _caption)) if ea.post_func else None
                _perf = displayBasicDataframeInfo(_result, _start_time, _end_time, countColName=None, display_results=False)
                _perf_tuple = exec_async_perf(_perf[0], _perf[1],_sql, _caption, _start_date.strftime(TIMING_FORMAT), _end_date.strftime(TIMING_FORMAT))
                return [_result, f_result, _perf_tuple]
            return [None, None, None]
        except Exception as e: # Error could be no DF was returned. I think that's something with read_sql.
            print(f"Error in async read: {_caption} {e}")
            return [None, None, None]



"""
dsn=the dsn of the query.
index=the order the query_sources where sent.
query_source =the query souce.
"""
exec_async1 = namedtuple('exec_async1', ['dsn', 'index', 'query_source', 'lock', 'empty_dataframe_onerror'])  

def execute_async(dsn:str, query_sources:list, merge_on:str=None)->Union[list,pd.DataFrame]: # list of CubeDef - todo: when moving to python 3.10, can say query_sources:[CubeDef]
    """Executes a list of CubeDef queries in parallel.

    Optionally merge into a single dataframe.
    
    Returns:
    ----
        list:dict

    Usage:
    ----
        >>> results=ky.execute_async(dsn="KyvosNew",query_sources=[stores,adw,ssb],merge_on="Year")

    """
    df_results = []
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = [executor.submit(_exec_async, exec_async1(dsn, index, query_source, None, False)) for index,query_source in enumerate(query_sources)]
        for f in concurrent.futures.as_completed(results):
            df_results.append(f.result())
    df_results = sorted(df_results, key=lambda x: x[0]) # sort the list of results by index.
    df_results = [df for (index, df) in df_results] # Strip out the index since we've sorted it.
    if merge_on:
        df_results = reduce(lambda lf, rt: pd.merge(lf, rt, on=[merge_on], how='outer'), df_results) # Results in a single dataframe
    return df_results # this is either a list[DataFrame] or a DataFrame.

def _exec_async(ea:exec_async):
    """Thread execution for the execute_async function."""
    with pyodbc.connect(conn_string(ea.dsn), autocommit=True) as cnxn:
        with cnxn.cursor() as thread_cursor:
            thread_cursor.execute(ea.query_source if isinstance(ea.query_source, str) else str(ea.query_source))
            result_set = thread_cursor.fetchall() # todo: fetch in chunks using cursor as a generator.
            result = pd.DataFrame.from_records(result_set, columns=[col[0] for col in thread_cursor.description])

            #result = pd.DataFrame([tuple(t) for t in result_set]) 
            #result.columns = [column[pyodbc_column_index] for column in thread_cursor.description]  # Set column name otherwise will be 0,1,2...                                                                 #
    return (ea.index, result)

def sorted_set_name(lst:list)->str:
    """Return a str representation of a list for the purpose of naming a set or a tuple.
    """
    lst = [str(item) for item in lst]  # Note that the members should be strings. We'll convert to strings just in case.
    lst.sort() # Sort, so we have an easier time re-using the same set.
    return ",".join(lst)
