import pandas as pd
import traceback
from typing import List, Optional, Any, Iterator, Type, Union
from wepipe.source.base_source import BaseSource, BaseSourceConfig
from wepipe.core.payload import RecordPayload


class PandasSourceConfig(BaseSourceConfig):
    TYPE: str = "Pandas"

    dataframe: pd.DataFrame = None
    file_url: Optional[str] = None
    file_upload: Optional[Any] = None
    datetime_columns: Optional[List[str]] = None
    numeric_columns: Optional[List[str]] = None
    category_columns: Optional[List[str]] = None
    text_columns: Optional[List[str]] = None
    text_separator: Optional[str] = " "
    include_columns: Optional[List[str]] = None # if set to None, all columns will be imported

    def __init__(self, **data: Any):
        super().__init__(**data)
        # read dataframe
        if self.dataframe is None:
            if self.file_upload is not None:
                self.dataframe = self._read_file(self.file_upload)
            elif self.file_url is not None:
                self.dataframe = self._read_file(self.file_url)
            else:
                raise ValueError("No readable dataframe, `file_url` or `file_upload` must be provided. ")      
        # datetime columns
        if self.datetime_columns:
            if self.datetime_columns == ['']:
                self.datetime_columns = None
            else:
                self._check_columns("datetime_columns", "datetime")
        # text columns
        if self.text_columns:
            if self.text_columns == ['']:
                self.text_columns = None
            else:
                self._check_columns("text_columns", "string")
        # numerical columns
        if self.numeric_columns:
            if self.numeric_columns == ['']:
                self.numeric_columns = None
            else:
                self._check_columns("numeric_columns", "numeric")
        # categorical columns
        if self.category_columns:
            if self.category_columns == ['']:
                self.category_columns = None
            else:
                self._check_columns("category_columns", "category")       
            
    def _read_file(self, file_address):
        df = pd.read_csv(file_address)
        return df

    def _check_columns(self, columns_attr, dtype):
        """
        columns_attr:
            "text_columns", "datetime_columns", "numeric_columns", "category_columns"
        dtype:
            "string", "datetime", "numeric", "category"
        """
        columns = getattr(self, columns_attr)
        if not all(
            [column in self.dataframe.columns for column in columns]
        ):
            raise ValueError("Every `{}` should be present in `dataframe`".format(columns_attr))
        try:
            if columns_attr == "datetime_columns":
                self.dataframe[columns] = self.dataframe[
                    columns
                ].apply(pd.to_datetime)   
            elif columns_attr == "numeric_columns":
                self.dataframe[columns] = self.dataframe[
                    columns
                ].apply(pd.to_numeric)   
            else:
                self.dataframe[columns] = self.dataframe[
                    columns
                ].astype(dtype)                
        except TypeError as e:
            raise ValueError("Unable to convert `{}` to dtype `{}`".format(columns_attr, dtype))
        return True


class PandasSource(BaseSource):
    NAME: Optional[str] = "Pandas"

    def read(self, config: PandasSourceConfig, **kwargs) -> Iterator[RecordPayload]:  # type: ignore[override]
        df_to_records = config.dataframe.to_dict("records")
        # iterate
        try:
            for record in df_to_records:
                yield RecordPayload(
                    source_name=self.NAME,
                    raw={key: record[key] for key in config.include_columns} 
                    if config.include_columns is not None
                    else record,
                    processed_text=config.text_separator.join(
                        [record.get(text_column) for text_column in config.text_columns]
                    )
                    if config.text_columns is not None
                    else None,
                )
        except Exception as err:
            reason = f"Failed to read data of {config.TYPE, self.Name} at {record}: {repr(err)}\n{traceback.format_exc()}"
            # logger.error(reason)
            print(reason)
            raise err


    def load(self, config: PandasSourceConfig, **kwargs) -> List[RecordPayload]:  # type: ignore[override]
        df_to_records = config.dataframe.to_dict("records")
        source_responses: List[RecordPayload] = [
            RecordPayload(
                source_name=self.NAME,     
                raw={key: record[key] for key in config.include_columns}
                if config.include_columns is not None
                else record,                           
                processed_text=config.text_separator.join(
                    [record.get(text_column) for text_column in config.text_columns]
                )
                if config.text_columns is not None
                else None,                
            )
            for record in df_to_records
        ]
        return source_responses