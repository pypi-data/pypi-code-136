from .decoradores import Singleton
from typing import Any

def get_dbutils(spark = None):
    # We import DBUtils version
    try:
        # up to DBR 8.2
        from dbutils import DBUtils  # pylint: disable=import-error,wrong-import-position
        NEW_DBUTILS = False
    except:
        # above DBR 8.3
        from dbruntime.dbutils import DBUtils  # pylint: disable=import-error,wrong-import-position
        NEW_DBUTILS = True
        
    # We try to create dbutils from spark or by using IPython
    try:
        return DBUtils(spark)
    except:
        import IPython
        return IPython.get_ipython().user_ns["dbutils"]

@Singleton
class Observer:
    """
    An observer class. This type of class let's you to add attributes,
    fetch their values and remove them dynamiclly. Quite useful to access
    data inside a defined scope as it behaves as a Singleton.
    """
    def set(self, key: str, val: Any) -> None:
        """
        Let's you add and overwrite atributes given the name and value.
        You could also overwrite it by just accessing the value, but
        that may not be recommended as later version may change attributes
        to be encapsulated.

        Args:
            key (str): Name of the attribute to create/modify.
            val (Any): Value of the attribute to create/modify.
        """
        setattr(self, key, val)
        
    def get(self, key: str) -> Any:
        """
        Let's you fetch data from the object. Current version let's you
        access data directly, but later version may not support this, so
        the use of this method is highly recommended.

        Args:
            key (str): Name of the attribute you want to fetch.

        Returns:
            Any: The value stored in the attribute.
        """
        return getattr(self, key)
      
    def rem(self, key: str) -> None:
        """
        Let's you remove data from the object.

        Args:
            key (str): Name of the attribute to remove.
        """
        delattr(self, key)