from pandas import DataFrame, concat
from typing import List, Callable
from tqdm import tqdm
from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
from .exceptions import ParameterTypingException
from .tools import get_dbutils

sc = SparkContext.getOrCreate()
spark = SparkSession(sc)
dbutils = get_dbutils()

from .exceptions import EmptyDataFrameException
from .decoradores import Singleton

@Singleton
class DeltaManager:
    def __init__(self):
        # We get all the table names
        table_names = list(map(lambda table: table.name, spark.catalog.listTables()))
        
        self.tables_info = DataFrame(columns = ['name', 'database', 'path', 'type', 'is_temporary', 'description'])
        self.tables_hist = DataFrame(columns=["name", "version", "operation", "readVersion", "isBlindAppend", "date", "time"])
        
        for table_name in table_names:
            # tables_info
            try:
                table = Table(table_name.lower())
                self.tables_info = concat([self.tables_info, table.table_info])
                setattr(self, table_name.lower(), table)
                
                # tables_hist
                temp_hist = table.table_history.copy()
                temp_hist["name"] = table_name
                temp_hist = temp_hist[["name", "version", "operation", "readVersion", "isBlindAppend", "date", "time"]]
                self.tables_hist = concat([self.tables_hist, temp_hist])
            except:
                pass
                # We add this while we find out how to solve the abfss:// situation.

    def mount(self, 
              storage:     str,
              key:         str,
              mount_point: str       = '/mnt/',
              mounts:      List[str] = ["raw", "silver", "gold"], 
              postfix:     str       = '-zone',
              include_tqdm:        bool      = False
              ):
        """
            Mounts a set of zones into the system.
            Args:
                storage (str): The name of the storage to mount. This can be found at keys access in your storage account.
                key (str): The key of the storage to mount. This can be found at keys access in your storage account.
                mount_point (str, optional): The mount point to use. 
                    Defaults to '/mnt/'.
                mounts (List[str], optional): A list of all the mounts you want. This doesn't include the prefix. Check example. 
                    Defaults to ["raw", "silver", "gold"].
                postfix (str, optional): The postfix is the ending you want to put to your mount zones. Set it to an empty 
                string if you don't want to apply it. 
                    Defaults to '-zone'.
                include_tqdm (bool, optional): A flag to include tqdm bars for mounts. 
                    Defaults to False.
        """
        def __mount(mount_name: str):
            """
                Mounts a single zone to the system.
                Args:
                    mount_name (str): The name of the zone to mount.
            """
            if not f"{mount_point}{mount_name}{postfix}" in list(map(lambda mount: mount.mountPoint, dbutils.fs.mounts())):
                dbutils.fs.mount(
                    source = f"wasbs://{mount_name}{postfix}@{storage}.blob.core.windows.net/",
                    mount_point = f"{mount_point}{mount_name}{postfix}",
                    extra_configs = { 
                        f"fs.azure.account.key.{storage}.blob.core.windows.net": key
                    }
                )

        if include_tqdm:
            list(map(lambda mount_name: __mount(mount_name), tqdm(mounts, desc="Mounts", position=0, leave=True)))
        else:
            list(map(lambda mount_name: __mount(mount_name), mounts))

    def create_table(self, table_name: str):
        Table(table_name)

class Table:
    def __init__(self, table_name: str):
        # We reload the table information
        self.table_name = table_name
        
        # We reload the table information
        self._reload_stats()
        
    def insert(self, 
               df: DataFrame,
               destination_path: str = None,
               mode = "overwrite"
            ):
        """
        
        """
        # 
        if str(type(df)) == "<class 'pandas.core.frame.DataFrame'>":
            try:
                df = spark.createDataFrame(df) 
            except:
                raise
                
        # We try to write the DataFrame
        try:
            df.write.mode(mode).saveAsTable(self.table_name)
        except:
            raise
        
        # We reload the table information
        self._reload_stats()
            
        
    
    def load(self,
             raw_path:     str,
             destionation_path: str,
             write_mode:   str  = 'overwrite',
             query:        str  = None,
             transformer        = None,
             file_name:    str  = None,
             nested:       bool = False
            ):
        """
        Creates a new table given a name, a path where the parquet is located and a destination path.

        Args:
            table_name (str): The name of the table.
            
            raw_path (str): The path to the file you want to ingest.
            
            destionation_path (str): The path to the location you want to create the parquet at. 
            
            write_mode (str, optional): Behaviour if the table already exists. Options are 'overwrite' and 'append'. 
                Defaults to 'overwrite'.
            
            query (str, optional): A SQL query to transform the original table. This is applied before the transormer.
            
            transformer (Callable[DataFrame], optional): A function, that takes a Spark DataFrame as a parameter. 
            Return should be a Spark DataFrame. This is executed after the query, so any transformation done by the
            query will affect the input parameter of the transformer.

            file_name (str, optional): The name of the file to inglest. If not specified or None, it will be set
            to the table name as default. 
                Defaults to None.

            nested (bool, optional): A flag that let's the function know if the input is a folder with partitioned data
            or a raw file. True for nested folder, false for raw file. 
                Defaults to False.

        Raises:
            Exception: General Exception to return.
            EmptyDataFrameException: An exception that is thrown when the data to ingest is empty.
        """
        table_name = self.table_name
        
        if not file_name:
            file_name = table_name

        # We read the data from the parquet into a dataframe. 
        if nested:
            _df = DataFrame(list(map(lambda file: (file.name, file.path, file.size) , dbutils.fs.ls(raw_path))), columns = ["name", "path", "size"])
            path = _df[_df.name.str.lower().str.startswith(self.table_name)].path.to_list()[0]
            _df = DataFrame(list(map(lambda file: (file.name, file.path, file.size) , dbutils.fs.ls(path))), columns = ["name", "path", "size"])
            filename = _df[_df.name.str.lower().str.startswith(self.table_name)].path.to_list()[0].split("/")[-1]
            del _df
            df = spark.read.parquet(f"{path}/{filename}")
        else:
            df = spark.read.parquet(f"dbfs:{raw_path}{file_name}.parquet")

        # Filters the data using a SQL query if apply.
        if query:
            df.createOrReplaceTempView(table_name.lower())
            df = spark.sql(query)
            spark.catalog.dropTempView(table_name.lower())

        # The transform function would apply here.
        if transformer:
            if callable(transformer):
                df = transformer(df)
            else:
                pass
#                 ParameterTypingException()

        # We check if there is data in the dataframe.
        if df.count() > 0:
            # Check if the table already exist, then we overwrite it.
            if table_name.lower() in [table.name for table in spark.catalog.listTables()]:
                df.write.mode(write_mode).format("delta").option("mergeSchema", "true").saveAsTable(table_name.lower())
            else:
                # In case the table doesn't exist, we create it.
                try:
                    # We write the df in the destionation_path
                    df.write.format('delta').save(destionation_path+file_name.lower())
                except Exception as error:
                    EOL = '\n'
                    raise Exception(f'Tried to {write_mode} the table and failed with the following message:{EOL}{error}')
                # Create the table.
                spark.sql("CREATE TABLE " + table_name.lower() + " USING DELTA LOCATION " + f"'{destionation_path}{table_name.lower()}'")
        else:
            raise EmptyDataFrameException()
            
        # We reload the table information
        self._reload_stats()
    
    def delete(self):
        dbutils.fs.rm(self.location, True)
        spark.sql(f"DROP TABLE IF EXISTS {self.table_name}")
    
    def rollback(self,
                 no_of_versions: int = 1,
                 aim_version: int = None,
                 date: str = None, 
                 timestamp: str = '00:00:00') -> None:
        """
        Rolls back the table. It can take a date or a version as a parameter.

        Args:
            table_name (str): The table to rollback.
            no_of_versions (int, optional): The number of versions to go back in time. Defaults to 1.
            aim_version (int, optional): The version you want to select. Defaults to None.
            date (str, optional): The date you want to rollback to. Defaults to None.
                Format: YYYY-MM-DD
            timestamp (_type_, optional): The time you want to rollback to. Defaults to '00:00:00'.
                Format: HH:MM:SS
        """
        if date:
            spark.sql(f"RESTORE TABLE {self.table_name} TO TIMESTAMP AS OF '{date} {timestamp}'")
        else:
            if not aim_version:
                current_version = spark.sql(f"DESCRIBE HISTORY {self.table_name}").toPandas()["version"].max()
                aim_version = current_version - no_of_versions
            
            if aim_version > 0 and aim_version < current_version:
                spark.sql(f"RESTORE TABLE {self.table_name} TO VERSION AS OF {str(aim_version)}")
    
    def rename(self, table_name):
        spark.sql(f"ALTER TABLE {self.table_name} RENAME TO {table_name}")
        dbutils.fs.mv(self.location, "/".join("dbfs:/mnt/silver-zone/dnewcont/cnvpuc/CNDENTIDAD".split("/")[:-1]) + "/" + table_name, True)
        self.table_info['name'] = table_name
        self.table_name = table_name
    
    def rename_column(self, column_name: str):
        spark.sql(f"ALTER TABLE {self.table_name} RENAME COLUMN {column_name}")
    
    def drop_column(self, column_name: str):
        spark.sql(f"ALTER TABLE {self.table_name} DROP COLUMN {column_name}")
        
    def _reload_stats(self):
        # We find the data from this table.
        _nombre_tablas = list(map(lambda table: (table.name, table.database, table.description, table.tableType, table.isTemporary), spark.catalog.listTables()))
        _df = DataFrame(_nombre_tablas, columns = ["name", "database", "description", "type", "is_temporary"])
        _df["description"] = _df["description"].fillna("")
        self.table_info = _df[_df.name == self.table_name]
        del _df
        
        if not self.table_info.is_temporary.all():
            self.location = spark.sql(f"desc formatted {self.table_name}").toPandas().set_index("col_name").drop("comment", axis = 1)["data_type"]["Location"]
            self.table_info['location'] = self.location
        try:
            self.table_history = spark.sql(f"DESC HISTORY {self.table_name}").drop("userId", "userName", "operationParameters", "job", "notebook", "clusterId", "operationMetrics", "userMetadata", "engineInfo", "isolationLevel").toPandas()
            self.table_history["date"] = self.table_history.apply(lambda row: str(row["timestamp"]).split(" ")[0], axis = 1)
            self.table_history["time"] = self.table_history.apply(lambda row: str(row["timestamp"]).split(" ")[1], axis = 1)
            self.table_history.drop(columns = ["timestamp"], inplace = True)
        except:
            self.table_history = None