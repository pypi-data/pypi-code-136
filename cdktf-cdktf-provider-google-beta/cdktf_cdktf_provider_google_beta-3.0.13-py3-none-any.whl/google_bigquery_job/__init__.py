'''
# `google_bigquery_job`

Refer to the Terraform Registory for docs: [`google_bigquery_job`](https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job).
'''
import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

import cdktf
import constructs


class GoogleBigqueryJob(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryJob.GoogleBigqueryJob",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job google_bigquery_job}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        job_id: builtins.str,
        copy: typing.Optional[typing.Union["GoogleBigqueryJobCopy", typing.Dict[str, typing.Any]]] = None,
        extract: typing.Optional[typing.Union["GoogleBigqueryJobExtract", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        job_timeout_ms: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        load: typing.Optional[typing.Union["GoogleBigqueryJobLoad", typing.Dict[str, typing.Any]]] = None,
        location: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        query: typing.Optional[typing.Union["GoogleBigqueryJobQuery", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["GoogleBigqueryJobTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job google_bigquery_job} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param job_id: The ID of the job. The ID must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). The maximum length is 1,024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#job_id GoogleBigqueryJob#job_id}
        :param copy: copy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#copy GoogleBigqueryJob#copy}
        :param extract: extract block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#extract GoogleBigqueryJob#extract}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#id GoogleBigqueryJob#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param job_timeout_ms: Job timeout in milliseconds. If this time limit is exceeded, BigQuery may attempt to terminate the job. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#job_timeout_ms GoogleBigqueryJob#job_timeout_ms}
        :param labels: The labels associated with this job. You can use these to organize and group your jobs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#labels GoogleBigqueryJob#labels}
        :param load: load block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#load GoogleBigqueryJob#load}
        :param location: The geographic location of the job. The default value is US. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#location GoogleBigqueryJob#location}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#project GoogleBigqueryJob#project}.
        :param query: query block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#query GoogleBigqueryJob#query}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#timeouts GoogleBigqueryJob#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJob.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleBigqueryJobConfig(
            job_id=job_id,
            copy=copy,
            extract=extract,
            id=id,
            job_timeout_ms=job_timeout_ms,
            labels=labels,
            load=load,
            location=location,
            project=project,
            query=query,
            timeouts=timeouts,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putCopy")
    def put_copy(
        self,
        *,
        source_tables: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleBigqueryJobCopySourceTables", typing.Dict[str, typing.Any]]]],
        create_disposition: typing.Optional[builtins.str] = None,
        destination_encryption_configuration: typing.Optional[typing.Union["GoogleBigqueryJobCopyDestinationEncryptionConfiguration", typing.Dict[str, typing.Any]]] = None,
        destination_table: typing.Optional[typing.Union["GoogleBigqueryJobCopyDestinationTable", typing.Dict[str, typing.Any]]] = None,
        write_disposition: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param source_tables: source_tables block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#source_tables GoogleBigqueryJob#source_tables}
        :param create_disposition: Specifies whether the job is allowed to create new tables. The following values are supported: CREATE_IF_NEEDED: If the table does not exist, BigQuery creates the table. CREATE_NEVER: The table must already exist. If it does not, a 'notFound' error is returned in the job result. Creation, truncation and append actions occur as one atomic update upon job completion Default value: "CREATE_IF_NEEDED" Possible values: ["CREATE_IF_NEEDED", "CREATE_NEVER"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#create_disposition GoogleBigqueryJob#create_disposition}
        :param destination_encryption_configuration: destination_encryption_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#destination_encryption_configuration GoogleBigqueryJob#destination_encryption_configuration}
        :param destination_table: destination_table block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#destination_table GoogleBigqueryJob#destination_table}
        :param write_disposition: Specifies the action that occurs if the destination table already exists. The following values are supported: WRITE_TRUNCATE: If the table already exists, BigQuery overwrites the table data and uses the schema from the query result. WRITE_APPEND: If the table already exists, BigQuery appends the data to the table. WRITE_EMPTY: If the table already exists and contains data, a 'duplicate' error is returned in the job result. Each action is atomic and only occurs if BigQuery is able to complete the job successfully. Creation, truncation and append actions occur as one atomic update upon job completion. Default value: "WRITE_EMPTY" Possible values: ["WRITE_TRUNCATE", "WRITE_APPEND", "WRITE_EMPTY"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#write_disposition GoogleBigqueryJob#write_disposition}
        '''
        value = GoogleBigqueryJobCopy(
            source_tables=source_tables,
            create_disposition=create_disposition,
            destination_encryption_configuration=destination_encryption_configuration,
            destination_table=destination_table,
            write_disposition=write_disposition,
        )

        return typing.cast(None, jsii.invoke(self, "putCopy", [value]))

    @jsii.member(jsii_name="putExtract")
    def put_extract(
        self,
        *,
        destination_uris: typing.Sequence[builtins.str],
        compression: typing.Optional[builtins.str] = None,
        destination_format: typing.Optional[builtins.str] = None,
        field_delimiter: typing.Optional[builtins.str] = None,
        print_header: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        source_model: typing.Optional[typing.Union["GoogleBigqueryJobExtractSourceModel", typing.Dict[str, typing.Any]]] = None,
        source_table: typing.Optional[typing.Union["GoogleBigqueryJobExtractSourceTable", typing.Dict[str, typing.Any]]] = None,
        use_avro_logical_types: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param destination_uris: A list of fully-qualified Google Cloud Storage URIs where the extracted table should be written. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#destination_uris GoogleBigqueryJob#destination_uris}
        :param compression: The compression type to use for exported files. Possible values include GZIP, DEFLATE, SNAPPY, and NONE. The default value is NONE. DEFLATE and SNAPPY are only supported for Avro. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#compression GoogleBigqueryJob#compression}
        :param destination_format: The exported file format. Possible values include CSV, NEWLINE_DELIMITED_JSON and AVRO for tables and SAVED_MODEL for models. The default value for tables is CSV. Tables with nested or repeated fields cannot be exported as CSV. The default value for models is SAVED_MODEL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#destination_format GoogleBigqueryJob#destination_format}
        :param field_delimiter: When extracting data in CSV format, this defines the delimiter to use between fields in the exported data. Default is ',' Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#field_delimiter GoogleBigqueryJob#field_delimiter}
        :param print_header: Whether to print out a header row in the results. Default is true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#print_header GoogleBigqueryJob#print_header}
        :param source_model: source_model block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#source_model GoogleBigqueryJob#source_model}
        :param source_table: source_table block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#source_table GoogleBigqueryJob#source_table}
        :param use_avro_logical_types: Whether to use logical types when extracting to AVRO format. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#use_avro_logical_types GoogleBigqueryJob#use_avro_logical_types}
        '''
        value = GoogleBigqueryJobExtract(
            destination_uris=destination_uris,
            compression=compression,
            destination_format=destination_format,
            field_delimiter=field_delimiter,
            print_header=print_header,
            source_model=source_model,
            source_table=source_table,
            use_avro_logical_types=use_avro_logical_types,
        )

        return typing.cast(None, jsii.invoke(self, "putExtract", [value]))

    @jsii.member(jsii_name="putLoad")
    def put_load(
        self,
        *,
        destination_table: typing.Union["GoogleBigqueryJobLoadDestinationTable", typing.Dict[str, typing.Any]],
        source_uris: typing.Sequence[builtins.str],
        allow_jagged_rows: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_quoted_newlines: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        autodetect: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        create_disposition: typing.Optional[builtins.str] = None,
        destination_encryption_configuration: typing.Optional[typing.Union["GoogleBigqueryJobLoadDestinationEncryptionConfiguration", typing.Dict[str, typing.Any]]] = None,
        encoding: typing.Optional[builtins.str] = None,
        field_delimiter: typing.Optional[builtins.str] = None,
        ignore_unknown_values: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        json_extension: typing.Optional[builtins.str] = None,
        max_bad_records: typing.Optional[jsii.Number] = None,
        null_marker: typing.Optional[builtins.str] = None,
        projection_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
        quote: typing.Optional[builtins.str] = None,
        schema_update_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        skip_leading_rows: typing.Optional[jsii.Number] = None,
        source_format: typing.Optional[builtins.str] = None,
        time_partitioning: typing.Optional[typing.Union["GoogleBigqueryJobLoadTimePartitioning", typing.Dict[str, typing.Any]]] = None,
        write_disposition: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param destination_table: destination_table block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#destination_table GoogleBigqueryJob#destination_table}
        :param source_uris: The fully-qualified URIs that point to your data in Google Cloud. For Google Cloud Storage URIs: Each URI can contain one '*' wildcard character and it must come after the 'bucket' name. Size limits related to load jobs apply to external data sources. For Google Cloud Bigtable URIs: Exactly one URI can be specified and it has be a fully specified and valid HTTPS URL for a Google Cloud Bigtable table. For Google Cloud Datastore backups: Exactly one URI can be specified. Also, the '*' wildcard character is not allowed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#source_uris GoogleBigqueryJob#source_uris}
        :param allow_jagged_rows: Accept rows that are missing trailing optional columns. The missing values are treated as nulls. If false, records with missing trailing columns are treated as bad records, and if there are too many bad records, an invalid error is returned in the job result. The default value is false. Only applicable to CSV, ignored for other formats. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#allow_jagged_rows GoogleBigqueryJob#allow_jagged_rows}
        :param allow_quoted_newlines: Indicates if BigQuery should allow quoted data sections that contain newline characters in a CSV file. The default value is false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#allow_quoted_newlines GoogleBigqueryJob#allow_quoted_newlines}
        :param autodetect: Indicates if we should automatically infer the options and schema for CSV and JSON sources. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#autodetect GoogleBigqueryJob#autodetect}
        :param create_disposition: Specifies whether the job is allowed to create new tables. The following values are supported: CREATE_IF_NEEDED: If the table does not exist, BigQuery creates the table. CREATE_NEVER: The table must already exist. If it does not, a 'notFound' error is returned in the job result. Creation, truncation and append actions occur as one atomic update upon job completion Default value: "CREATE_IF_NEEDED" Possible values: ["CREATE_IF_NEEDED", "CREATE_NEVER"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#create_disposition GoogleBigqueryJob#create_disposition}
        :param destination_encryption_configuration: destination_encryption_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#destination_encryption_configuration GoogleBigqueryJob#destination_encryption_configuration}
        :param encoding: The character encoding of the data. The supported values are UTF-8 or ISO-8859-1. The default value is UTF-8. BigQuery decodes the data after the raw, binary data has been split using the values of the quote and fieldDelimiter properties. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#encoding GoogleBigqueryJob#encoding}
        :param field_delimiter: The separator for fields in a CSV file. The separator can be any ISO-8859-1 single-byte character. To use a character in the range 128-255, you must encode the character as UTF8. BigQuery converts the string to ISO-8859-1 encoding, and then uses the first byte of the encoded string to split the data in its raw, binary state. BigQuery also supports the escape sequence "\\t" to specify a tab separator. The default value is a comma (','). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#field_delimiter GoogleBigqueryJob#field_delimiter}
        :param ignore_unknown_values: Indicates if BigQuery should allow extra values that are not represented in the table schema. If true, the extra values are ignored. If false, records with extra columns are treated as bad records, and if there are too many bad records, an invalid error is returned in the job result. The default value is false. The sourceFormat property determines what BigQuery treats as an extra value: CSV: Trailing columns JSON: Named values that don't match any column names Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#ignore_unknown_values GoogleBigqueryJob#ignore_unknown_values}
        :param json_extension: If sourceFormat is set to newline-delimited JSON, indicates whether it should be processed as a JSON variant such as GeoJSON. For a sourceFormat other than JSON, omit this field. If the sourceFormat is newline-delimited JSON: - for newline-delimited GeoJSON: set to GEOJSON. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#json_extension GoogleBigqueryJob#json_extension}
        :param max_bad_records: The maximum number of bad records that BigQuery can ignore when running the job. If the number of bad records exceeds this value, an invalid error is returned in the job result. The default value is 0, which requires that all records are valid. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#max_bad_records GoogleBigqueryJob#max_bad_records}
        :param null_marker: Specifies a string that represents a null value in a CSV file. For example, if you specify "\\N", BigQuery interprets "\\N" as a null value when loading a CSV file. The default value is the empty string. If you set this property to a custom value, BigQuery throws an error if an empty string is present for all data types except for STRING and BYTE. For STRING and BYTE columns, BigQuery interprets the empty string as an empty value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#null_marker GoogleBigqueryJob#null_marker}
        :param projection_fields: If sourceFormat is set to "DATASTORE_BACKUP", indicates which entity properties to load into BigQuery from a Cloud Datastore backup. Property names are case sensitive and must be top-level properties. If no properties are specified, BigQuery loads all properties. If any named property isn't found in the Cloud Datastore backup, an invalid error is returned in the job result. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#projection_fields GoogleBigqueryJob#projection_fields}
        :param quote: The value that is used to quote data sections in a CSV file. BigQuery converts the string to ISO-8859-1 encoding, and then uses the first byte of the encoded string to split the data in its raw, binary state. The default value is a double-quote ('"'). If your data does not contain quoted sections, set the property value to an empty string. If your data contains quoted newline characters, you must also set the allowQuotedNewlines property to true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#quote GoogleBigqueryJob#quote}
        :param schema_update_options: Allows the schema of the destination table to be updated as a side effect of the load job if a schema is autodetected or supplied in the job configuration. Schema update options are supported in two cases: when writeDisposition is WRITE_APPEND; when writeDisposition is WRITE_TRUNCATE and the destination table is a partition of a table, specified by partition decorators. For normal tables, WRITE_TRUNCATE will always overwrite the schema. One or more of the following values are specified: ALLOW_FIELD_ADDITION: allow adding a nullable field to the schema. ALLOW_FIELD_RELAXATION: allow relaxing a required field in the original schema to nullable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#schema_update_options GoogleBigqueryJob#schema_update_options}
        :param skip_leading_rows: The number of rows at the top of a CSV file that BigQuery will skip when loading the data. The default value is 0. This property is useful if you have header rows in the file that should be skipped. When autodetect is on, the behavior is the following: skipLeadingRows unspecified - Autodetect tries to detect headers in the first row. If they are not detected, the row is read as data. Otherwise data is read starting from the second row. skipLeadingRows is 0 - Instructs autodetect that there are no headers and data should be read starting from the first row. skipLeadingRows = N > 0 - Autodetect skips N-1 rows and tries to detect headers in row N. If headers are not detected, row N is just skipped. Otherwise row N is used to extract column names for the detected schema. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#skip_leading_rows GoogleBigqueryJob#skip_leading_rows}
        :param source_format: The format of the data files. For CSV files, specify "CSV". For datastore backups, specify "DATASTORE_BACKUP". For newline-delimited JSON, specify "NEWLINE_DELIMITED_JSON". For Avro, specify "AVRO". For parquet, specify "PARQUET". For orc, specify "ORC". [Beta] For Bigtable, specify "BIGTABLE". The default value is CSV. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#source_format GoogleBigqueryJob#source_format}
        :param time_partitioning: time_partitioning block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#time_partitioning GoogleBigqueryJob#time_partitioning}
        :param write_disposition: Specifies the action that occurs if the destination table already exists. The following values are supported: WRITE_TRUNCATE: If the table already exists, BigQuery overwrites the table data and uses the schema from the query result. WRITE_APPEND: If the table already exists, BigQuery appends the data to the table. WRITE_EMPTY: If the table already exists and contains data, a 'duplicate' error is returned in the job result. Each action is atomic and only occurs if BigQuery is able to complete the job successfully. Creation, truncation and append actions occur as one atomic update upon job completion. Default value: "WRITE_EMPTY" Possible values: ["WRITE_TRUNCATE", "WRITE_APPEND", "WRITE_EMPTY"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#write_disposition GoogleBigqueryJob#write_disposition}
        '''
        value = GoogleBigqueryJobLoad(
            destination_table=destination_table,
            source_uris=source_uris,
            allow_jagged_rows=allow_jagged_rows,
            allow_quoted_newlines=allow_quoted_newlines,
            autodetect=autodetect,
            create_disposition=create_disposition,
            destination_encryption_configuration=destination_encryption_configuration,
            encoding=encoding,
            field_delimiter=field_delimiter,
            ignore_unknown_values=ignore_unknown_values,
            json_extension=json_extension,
            max_bad_records=max_bad_records,
            null_marker=null_marker,
            projection_fields=projection_fields,
            quote=quote,
            schema_update_options=schema_update_options,
            skip_leading_rows=skip_leading_rows,
            source_format=source_format,
            time_partitioning=time_partitioning,
            write_disposition=write_disposition,
        )

        return typing.cast(None, jsii.invoke(self, "putLoad", [value]))

    @jsii.member(jsii_name="putQuery")
    def put_query(
        self,
        *,
        query: builtins.str,
        allow_large_results: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        create_disposition: typing.Optional[builtins.str] = None,
        default_dataset: typing.Optional[typing.Union["GoogleBigqueryJobQueryDefaultDataset", typing.Dict[str, typing.Any]]] = None,
        destination_encryption_configuration: typing.Optional[typing.Union["GoogleBigqueryJobQueryDestinationEncryptionConfiguration", typing.Dict[str, typing.Any]]] = None,
        destination_table: typing.Optional[typing.Union["GoogleBigqueryJobQueryDestinationTable", typing.Dict[str, typing.Any]]] = None,
        flatten_results: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        maximum_billing_tier: typing.Optional[jsii.Number] = None,
        maximum_bytes_billed: typing.Optional[builtins.str] = None,
        parameter_mode: typing.Optional[builtins.str] = None,
        priority: typing.Optional[builtins.str] = None,
        schema_update_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        script_options: typing.Optional[typing.Union["GoogleBigqueryJobQueryScriptOptions", typing.Dict[str, typing.Any]]] = None,
        use_legacy_sql: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        use_query_cache: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        user_defined_function_resources: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleBigqueryJobQueryUserDefinedFunctionResources", typing.Dict[str, typing.Any]]]]] = None,
        write_disposition: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param query: SQL query text to execute. The useLegacySql field can be used to indicate whether the query uses legacy SQL or standard SQL. NOTE*: queries containing `DML language <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-manipulation-language>`_ ('DELETE', 'UPDATE', 'MERGE', 'INSERT') must specify 'create_disposition = ""' and 'write_disposition = ""'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#query GoogleBigqueryJob#query}
        :param allow_large_results: If true and query uses legacy SQL dialect, allows the query to produce arbitrarily large result tables at a slight cost in performance. Requires destinationTable to be set. For standard SQL queries, this flag is ignored and large results are always allowed. However, you must still set destinationTable when result size exceeds the allowed maximum response size. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#allow_large_results GoogleBigqueryJob#allow_large_results}
        :param create_disposition: Specifies whether the job is allowed to create new tables. The following values are supported: CREATE_IF_NEEDED: If the table does not exist, BigQuery creates the table. CREATE_NEVER: The table must already exist. If it does not, a 'notFound' error is returned in the job result. Creation, truncation and append actions occur as one atomic update upon job completion Default value: "CREATE_IF_NEEDED" Possible values: ["CREATE_IF_NEEDED", "CREATE_NEVER"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#create_disposition GoogleBigqueryJob#create_disposition}
        :param default_dataset: default_dataset block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#default_dataset GoogleBigqueryJob#default_dataset}
        :param destination_encryption_configuration: destination_encryption_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#destination_encryption_configuration GoogleBigqueryJob#destination_encryption_configuration}
        :param destination_table: destination_table block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#destination_table GoogleBigqueryJob#destination_table}
        :param flatten_results: If true and query uses legacy SQL dialect, flattens all nested and repeated fields in the query results. allowLargeResults must be true if this is set to false. For standard SQL queries, this flag is ignored and results are never flattened. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#flatten_results GoogleBigqueryJob#flatten_results}
        :param maximum_billing_tier: Limits the billing tier for this job. Queries that have resource usage beyond this tier will fail (without incurring a charge). If unspecified, this will be set to your project default. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#maximum_billing_tier GoogleBigqueryJob#maximum_billing_tier}
        :param maximum_bytes_billed: Limits the bytes billed for this job. Queries that will have bytes billed beyond this limit will fail (without incurring a charge). If unspecified, this will be set to your project default. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#maximum_bytes_billed GoogleBigqueryJob#maximum_bytes_billed}
        :param parameter_mode: Standard SQL only. Set to POSITIONAL to use positional (?) query parameters or to NAMED to use named (@myparam) query parameters in this query. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#parameter_mode GoogleBigqueryJob#parameter_mode}
        :param priority: Specifies a priority for the query. Default value: "INTERACTIVE" Possible values: ["INTERACTIVE", "BATCH"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#priority GoogleBigqueryJob#priority}
        :param schema_update_options: Allows the schema of the destination table to be updated as a side effect of the query job. Schema update options are supported in two cases: when writeDisposition is WRITE_APPEND; when writeDisposition is WRITE_TRUNCATE and the destination table is a partition of a table, specified by partition decorators. For normal tables, WRITE_TRUNCATE will always overwrite the schema. One or more of the following values are specified: ALLOW_FIELD_ADDITION: allow adding a nullable field to the schema. ALLOW_FIELD_RELAXATION: allow relaxing a required field in the original schema to nullable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#schema_update_options GoogleBigqueryJob#schema_update_options}
        :param script_options: script_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#script_options GoogleBigqueryJob#script_options}
        :param use_legacy_sql: Specifies whether to use BigQuery's legacy SQL dialect for this query. The default value is true. If set to false, the query will use BigQuery's standard SQL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#use_legacy_sql GoogleBigqueryJob#use_legacy_sql}
        :param use_query_cache: Whether to look for the result in the query cache. The query cache is a best-effort cache that will be flushed whenever tables in the query are modified. Moreover, the query cache is only available when a query does not have a destination table specified. The default value is true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#use_query_cache GoogleBigqueryJob#use_query_cache}
        :param user_defined_function_resources: user_defined_function_resources block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#user_defined_function_resources GoogleBigqueryJob#user_defined_function_resources}
        :param write_disposition: Specifies the action that occurs if the destination table already exists. The following values are supported: WRITE_TRUNCATE: If the table already exists, BigQuery overwrites the table data and uses the schema from the query result. WRITE_APPEND: If the table already exists, BigQuery appends the data to the table. WRITE_EMPTY: If the table already exists and contains data, a 'duplicate' error is returned in the job result. Each action is atomic and only occurs if BigQuery is able to complete the job successfully. Creation, truncation and append actions occur as one atomic update upon job completion. Default value: "WRITE_EMPTY" Possible values: ["WRITE_TRUNCATE", "WRITE_APPEND", "WRITE_EMPTY"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#write_disposition GoogleBigqueryJob#write_disposition}
        '''
        value = GoogleBigqueryJobQuery(
            query=query,
            allow_large_results=allow_large_results,
            create_disposition=create_disposition,
            default_dataset=default_dataset,
            destination_encryption_configuration=destination_encryption_configuration,
            destination_table=destination_table,
            flatten_results=flatten_results,
            maximum_billing_tier=maximum_billing_tier,
            maximum_bytes_billed=maximum_bytes_billed,
            parameter_mode=parameter_mode,
            priority=priority,
            schema_update_options=schema_update_options,
            script_options=script_options,
            use_legacy_sql=use_legacy_sql,
            use_query_cache=use_query_cache,
            user_defined_function_resources=user_defined_function_resources,
            write_disposition=write_disposition,
        )

        return typing.cast(None, jsii.invoke(self, "putQuery", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#create GoogleBigqueryJob#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#delete GoogleBigqueryJob#delete}.
        '''
        value = GoogleBigqueryJobTimeouts(create=create, delete=delete)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetCopy")
    def reset_copy(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCopy", []))

    @jsii.member(jsii_name="resetExtract")
    def reset_extract(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExtract", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetJobTimeoutMs")
    def reset_job_timeout_ms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJobTimeoutMs", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetLoad")
    def reset_load(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoad", []))

    @jsii.member(jsii_name="resetLocation")
    def reset_location(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLocation", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetQuery")
    def reset_query(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQuery", []))

    @jsii.member(jsii_name="resetTimeouts")
    def reset_timeouts(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimeouts", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="copy")
    def copy(self) -> "GoogleBigqueryJobCopyOutputReference":
        return typing.cast("GoogleBigqueryJobCopyOutputReference", jsii.get(self, "copy"))

    @builtins.property
    @jsii.member(jsii_name="extract")
    def extract(self) -> "GoogleBigqueryJobExtractOutputReference":
        return typing.cast("GoogleBigqueryJobExtractOutputReference", jsii.get(self, "extract"))

    @builtins.property
    @jsii.member(jsii_name="jobType")
    def job_type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jobType"))

    @builtins.property
    @jsii.member(jsii_name="load")
    def load(self) -> "GoogleBigqueryJobLoadOutputReference":
        return typing.cast("GoogleBigqueryJobLoadOutputReference", jsii.get(self, "load"))

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> "GoogleBigqueryJobQueryOutputReference":
        return typing.cast("GoogleBigqueryJobQueryOutputReference", jsii.get(self, "query"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> "GoogleBigqueryJobStatusList":
        return typing.cast("GoogleBigqueryJobStatusList", jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleBigqueryJobTimeoutsOutputReference":
        return typing.cast("GoogleBigqueryJobTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="userEmail")
    def user_email(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "userEmail"))

    @builtins.property
    @jsii.member(jsii_name="copyInput")
    def copy_input(self) -> typing.Optional["GoogleBigqueryJobCopy"]:
        return typing.cast(typing.Optional["GoogleBigqueryJobCopy"], jsii.get(self, "copyInput"))

    @builtins.property
    @jsii.member(jsii_name="extractInput")
    def extract_input(self) -> typing.Optional["GoogleBigqueryJobExtract"]:
        return typing.cast(typing.Optional["GoogleBigqueryJobExtract"], jsii.get(self, "extractInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="jobIdInput")
    def job_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jobIdInput"))

    @builtins.property
    @jsii.member(jsii_name="jobTimeoutMsInput")
    def job_timeout_ms_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jobTimeoutMsInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="loadInput")
    def load_input(self) -> typing.Optional["GoogleBigqueryJobLoad"]:
        return typing.cast(typing.Optional["GoogleBigqueryJobLoad"], jsii.get(self, "loadInput"))

    @builtins.property
    @jsii.member(jsii_name="locationInput")
    def location_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "locationInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="queryInput")
    def query_input(self) -> typing.Optional["GoogleBigqueryJobQuery"]:
        return typing.cast(typing.Optional["GoogleBigqueryJobQuery"], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleBigqueryJobTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleBigqueryJobTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJob, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="jobId")
    def job_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jobId"))

    @job_id.setter
    def job_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJob, "job_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobId", value)

    @builtins.property
    @jsii.member(jsii_name="jobTimeoutMs")
    def job_timeout_ms(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jobTimeoutMs"))

    @job_timeout_ms.setter
    def job_timeout_ms(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJob, "job_timeout_ms").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobTimeoutMs", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJob, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @location.setter
    def location(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJob, "location").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "location", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJob, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryJob.GoogleBigqueryJobConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "job_id": "jobId",
        "copy": "copy",
        "extract": "extract",
        "id": "id",
        "job_timeout_ms": "jobTimeoutMs",
        "labels": "labels",
        "load": "load",
        "location": "location",
        "project": "project",
        "query": "query",
        "timeouts": "timeouts",
    },
)
class GoogleBigqueryJobConfig(cdktf.TerraformMetaArguments):
    def __init__(
        self,
        *,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
        job_id: builtins.str,
        copy: typing.Optional[typing.Union["GoogleBigqueryJobCopy", typing.Dict[str, typing.Any]]] = None,
        extract: typing.Optional[typing.Union["GoogleBigqueryJobExtract", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        job_timeout_ms: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        load: typing.Optional[typing.Union["GoogleBigqueryJobLoad", typing.Dict[str, typing.Any]]] = None,
        location: typing.Optional[builtins.str] = None,
        project: typing.Optional[builtins.str] = None,
        query: typing.Optional[typing.Union["GoogleBigqueryJobQuery", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["GoogleBigqueryJobTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param job_id: The ID of the job. The ID must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). The maximum length is 1,024 characters. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#job_id GoogleBigqueryJob#job_id}
        :param copy: copy block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#copy GoogleBigqueryJob#copy}
        :param extract: extract block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#extract GoogleBigqueryJob#extract}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#id GoogleBigqueryJob#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param job_timeout_ms: Job timeout in milliseconds. If this time limit is exceeded, BigQuery may attempt to terminate the job. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#job_timeout_ms GoogleBigqueryJob#job_timeout_ms}
        :param labels: The labels associated with this job. You can use these to organize and group your jobs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#labels GoogleBigqueryJob#labels}
        :param load: load block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#load GoogleBigqueryJob#load}
        :param location: The geographic location of the job. The default value is US. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#location GoogleBigqueryJob#location}
        :param project: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#project GoogleBigqueryJob#project}.
        :param query: query block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#query GoogleBigqueryJob#query}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#timeouts GoogleBigqueryJob#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(copy, dict):
            copy = GoogleBigqueryJobCopy(**copy)
        if isinstance(extract, dict):
            extract = GoogleBigqueryJobExtract(**extract)
        if isinstance(load, dict):
            load = GoogleBigqueryJobLoad(**load)
        if isinstance(query, dict):
            query = GoogleBigqueryJobQuery(**query)
        if isinstance(timeouts, dict):
            timeouts = GoogleBigqueryJobTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument job_id", value=job_id, expected_type=type_hints["job_id"])
            check_type(argname="argument copy", value=copy, expected_type=type_hints["copy"])
            check_type(argname="argument extract", value=extract, expected_type=type_hints["extract"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument job_timeout_ms", value=job_timeout_ms, expected_type=type_hints["job_timeout_ms"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument load", value=load, expected_type=type_hints["load"])
            check_type(argname="argument location", value=location, expected_type=type_hints["location"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "job_id": job_id,
        }
        if connection is not None:
            self._values["connection"] = connection
        if count is not None:
            self._values["count"] = count
        if depends_on is not None:
            self._values["depends_on"] = depends_on
        if for_each is not None:
            self._values["for_each"] = for_each
        if lifecycle is not None:
            self._values["lifecycle"] = lifecycle
        if provider is not None:
            self._values["provider"] = provider
        if provisioners is not None:
            self._values["provisioners"] = provisioners
        if copy is not None:
            self._values["copy"] = copy
        if extract is not None:
            self._values["extract"] = extract
        if id is not None:
            self._values["id"] = id
        if job_timeout_ms is not None:
            self._values["job_timeout_ms"] = job_timeout_ms
        if labels is not None:
            self._values["labels"] = labels
        if load is not None:
            self._values["load"] = load
        if location is not None:
            self._values["location"] = location
        if project is not None:
            self._values["project"] = project
        if query is not None:
            self._values["query"] = query
        if timeouts is not None:
            self._values["timeouts"] = timeouts

    @builtins.property
    def connection(
        self,
    ) -> typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("connection")
        return typing.cast(typing.Optional[typing.Union[cdktf.SSHProvisionerConnection, cdktf.WinrmProvisionerConnection]], result)

    @builtins.property
    def count(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("count")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def depends_on(self) -> typing.Optional[typing.List[cdktf.ITerraformDependable]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("depends_on")
        return typing.cast(typing.Optional[typing.List[cdktf.ITerraformDependable]], result)

    @builtins.property
    def for_each(self) -> typing.Optional[cdktf.ITerraformIterator]:
        '''
        :stability: experimental
        '''
        result = self._values.get("for_each")
        return typing.cast(typing.Optional[cdktf.ITerraformIterator], result)

    @builtins.property
    def lifecycle(self) -> typing.Optional[cdktf.TerraformResourceLifecycle]:
        '''
        :stability: experimental
        '''
        result = self._values.get("lifecycle")
        return typing.cast(typing.Optional[cdktf.TerraformResourceLifecycle], result)

    @builtins.property
    def provider(self) -> typing.Optional[cdktf.TerraformProvider]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provider")
        return typing.cast(typing.Optional[cdktf.TerraformProvider], result)

    @builtins.property
    def provisioners(
        self,
    ) -> typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("provisioners")
        return typing.cast(typing.Optional[typing.List[typing.Union[cdktf.FileProvisioner, cdktf.LocalExecProvisioner, cdktf.RemoteExecProvisioner]]], result)

    @builtins.property
    def job_id(self) -> builtins.str:
        '''The ID of the job.

        The ID must contain only letters (a-z, A-Z), numbers (0-9), underscores (_), or dashes (-). The maximum length is 1,024 characters.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#job_id GoogleBigqueryJob#job_id}
        '''
        result = self._values.get("job_id")
        assert result is not None, "Required property 'job_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def copy(self) -> typing.Optional["GoogleBigqueryJobCopy"]:
        '''copy block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#copy GoogleBigqueryJob#copy}
        '''
        result = self._values.get("copy")
        return typing.cast(typing.Optional["GoogleBigqueryJobCopy"], result)

    @builtins.property
    def extract(self) -> typing.Optional["GoogleBigqueryJobExtract"]:
        '''extract block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#extract GoogleBigqueryJob#extract}
        '''
        result = self._values.get("extract")
        return typing.cast(typing.Optional["GoogleBigqueryJobExtract"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#id GoogleBigqueryJob#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def job_timeout_ms(self) -> typing.Optional[builtins.str]:
        '''Job timeout in milliseconds. If this time limit is exceeded, BigQuery may attempt to terminate the job.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#job_timeout_ms GoogleBigqueryJob#job_timeout_ms}
        '''
        result = self._values.get("job_timeout_ms")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''The labels associated with this job. You can use these to organize and group your jobs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#labels GoogleBigqueryJob#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def load(self) -> typing.Optional["GoogleBigqueryJobLoad"]:
        '''load block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#load GoogleBigqueryJob#load}
        '''
        result = self._values.get("load")
        return typing.cast(typing.Optional["GoogleBigqueryJobLoad"], result)

    @builtins.property
    def location(self) -> typing.Optional[builtins.str]:
        '''The geographic location of the job. The default value is US.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#location GoogleBigqueryJob#location}
        '''
        result = self._values.get("location")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#project GoogleBigqueryJob#project}.'''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def query(self) -> typing.Optional["GoogleBigqueryJobQuery"]:
        '''query block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#query GoogleBigqueryJob#query}
        '''
        result = self._values.get("query")
        return typing.cast(typing.Optional["GoogleBigqueryJobQuery"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleBigqueryJobTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#timeouts GoogleBigqueryJob#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleBigqueryJobTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryJobConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryJob.GoogleBigqueryJobCopy",
    jsii_struct_bases=[],
    name_mapping={
        "source_tables": "sourceTables",
        "create_disposition": "createDisposition",
        "destination_encryption_configuration": "destinationEncryptionConfiguration",
        "destination_table": "destinationTable",
        "write_disposition": "writeDisposition",
    },
)
class GoogleBigqueryJobCopy:
    def __init__(
        self,
        *,
        source_tables: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleBigqueryJobCopySourceTables", typing.Dict[str, typing.Any]]]],
        create_disposition: typing.Optional[builtins.str] = None,
        destination_encryption_configuration: typing.Optional[typing.Union["GoogleBigqueryJobCopyDestinationEncryptionConfiguration", typing.Dict[str, typing.Any]]] = None,
        destination_table: typing.Optional[typing.Union["GoogleBigqueryJobCopyDestinationTable", typing.Dict[str, typing.Any]]] = None,
        write_disposition: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param source_tables: source_tables block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#source_tables GoogleBigqueryJob#source_tables}
        :param create_disposition: Specifies whether the job is allowed to create new tables. The following values are supported: CREATE_IF_NEEDED: If the table does not exist, BigQuery creates the table. CREATE_NEVER: The table must already exist. If it does not, a 'notFound' error is returned in the job result. Creation, truncation and append actions occur as one atomic update upon job completion Default value: "CREATE_IF_NEEDED" Possible values: ["CREATE_IF_NEEDED", "CREATE_NEVER"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#create_disposition GoogleBigqueryJob#create_disposition}
        :param destination_encryption_configuration: destination_encryption_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#destination_encryption_configuration GoogleBigqueryJob#destination_encryption_configuration}
        :param destination_table: destination_table block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#destination_table GoogleBigqueryJob#destination_table}
        :param write_disposition: Specifies the action that occurs if the destination table already exists. The following values are supported: WRITE_TRUNCATE: If the table already exists, BigQuery overwrites the table data and uses the schema from the query result. WRITE_APPEND: If the table already exists, BigQuery appends the data to the table. WRITE_EMPTY: If the table already exists and contains data, a 'duplicate' error is returned in the job result. Each action is atomic and only occurs if BigQuery is able to complete the job successfully. Creation, truncation and append actions occur as one atomic update upon job completion. Default value: "WRITE_EMPTY" Possible values: ["WRITE_TRUNCATE", "WRITE_APPEND", "WRITE_EMPTY"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#write_disposition GoogleBigqueryJob#write_disposition}
        '''
        if isinstance(destination_encryption_configuration, dict):
            destination_encryption_configuration = GoogleBigqueryJobCopyDestinationEncryptionConfiguration(**destination_encryption_configuration)
        if isinstance(destination_table, dict):
            destination_table = GoogleBigqueryJobCopyDestinationTable(**destination_table)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobCopy.__init__)
            check_type(argname="argument source_tables", value=source_tables, expected_type=type_hints["source_tables"])
            check_type(argname="argument create_disposition", value=create_disposition, expected_type=type_hints["create_disposition"])
            check_type(argname="argument destination_encryption_configuration", value=destination_encryption_configuration, expected_type=type_hints["destination_encryption_configuration"])
            check_type(argname="argument destination_table", value=destination_table, expected_type=type_hints["destination_table"])
            check_type(argname="argument write_disposition", value=write_disposition, expected_type=type_hints["write_disposition"])
        self._values: typing.Dict[str, typing.Any] = {
            "source_tables": source_tables,
        }
        if create_disposition is not None:
            self._values["create_disposition"] = create_disposition
        if destination_encryption_configuration is not None:
            self._values["destination_encryption_configuration"] = destination_encryption_configuration
        if destination_table is not None:
            self._values["destination_table"] = destination_table
        if write_disposition is not None:
            self._values["write_disposition"] = write_disposition

    @builtins.property
    def source_tables(
        self,
    ) -> typing.Union[cdktf.IResolvable, typing.List["GoogleBigqueryJobCopySourceTables"]]:
        '''source_tables block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#source_tables GoogleBigqueryJob#source_tables}
        '''
        result = self._values.get("source_tables")
        assert result is not None, "Required property 'source_tables' is missing"
        return typing.cast(typing.Union[cdktf.IResolvable, typing.List["GoogleBigqueryJobCopySourceTables"]], result)

    @builtins.property
    def create_disposition(self) -> typing.Optional[builtins.str]:
        '''Specifies whether the job is allowed to create new tables.

        The following values are supported:
        CREATE_IF_NEEDED: If the table does not exist, BigQuery creates the table.
        CREATE_NEVER: The table must already exist. If it does not, a 'notFound' error is returned in the job result.
        Creation, truncation and append actions occur as one atomic update upon job completion Default value: "CREATE_IF_NEEDED" Possible values: ["CREATE_IF_NEEDED", "CREATE_NEVER"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#create_disposition GoogleBigqueryJob#create_disposition}
        '''
        result = self._values.get("create_disposition")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def destination_encryption_configuration(
        self,
    ) -> typing.Optional["GoogleBigqueryJobCopyDestinationEncryptionConfiguration"]:
        '''destination_encryption_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#destination_encryption_configuration GoogleBigqueryJob#destination_encryption_configuration}
        '''
        result = self._values.get("destination_encryption_configuration")
        return typing.cast(typing.Optional["GoogleBigqueryJobCopyDestinationEncryptionConfiguration"], result)

    @builtins.property
    def destination_table(
        self,
    ) -> typing.Optional["GoogleBigqueryJobCopyDestinationTable"]:
        '''destination_table block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#destination_table GoogleBigqueryJob#destination_table}
        '''
        result = self._values.get("destination_table")
        return typing.cast(typing.Optional["GoogleBigqueryJobCopyDestinationTable"], result)

    @builtins.property
    def write_disposition(self) -> typing.Optional[builtins.str]:
        '''Specifies the action that occurs if the destination table already exists.

        The following values are supported:
        WRITE_TRUNCATE: If the table already exists, BigQuery overwrites the table data and uses the schema from the query result.
        WRITE_APPEND: If the table already exists, BigQuery appends the data to the table.
        WRITE_EMPTY: If the table already exists and contains data, a 'duplicate' error is returned in the job result.
        Each action is atomic and only occurs if BigQuery is able to complete the job successfully.
        Creation, truncation and append actions occur as one atomic update upon job completion. Default value: "WRITE_EMPTY" Possible values: ["WRITE_TRUNCATE", "WRITE_APPEND", "WRITE_EMPTY"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#write_disposition GoogleBigqueryJob#write_disposition}
        '''
        result = self._values.get("write_disposition")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryJobCopy(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryJob.GoogleBigqueryJobCopyDestinationEncryptionConfiguration",
    jsii_struct_bases=[],
    name_mapping={"kms_key_name": "kmsKeyName"},
)
class GoogleBigqueryJobCopyDestinationEncryptionConfiguration:
    def __init__(self, *, kms_key_name: builtins.str) -> None:
        '''
        :param kms_key_name: Describes the Cloud KMS encryption key that will be used to protect destination BigQuery table. The BigQuery Service Account associated with your project requires access to this encryption key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#kms_key_name GoogleBigqueryJob#kms_key_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobCopyDestinationEncryptionConfiguration.__init__)
            check_type(argname="argument kms_key_name", value=kms_key_name, expected_type=type_hints["kms_key_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "kms_key_name": kms_key_name,
        }

    @builtins.property
    def kms_key_name(self) -> builtins.str:
        '''Describes the Cloud KMS encryption key that will be used to protect destination BigQuery table.

        The BigQuery Service Account associated with your project requires access to this encryption key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#kms_key_name GoogleBigqueryJob#kms_key_name}
        '''
        result = self._values.get("kms_key_name")
        assert result is not None, "Required property 'kms_key_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryJobCopyDestinationEncryptionConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryJobCopyDestinationEncryptionConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryJob.GoogleBigqueryJobCopyDestinationEncryptionConfigurationOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobCopyDestinationEncryptionConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="kmsKeyVersion")
    def kms_key_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyVersion"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyNameInput")
    def kms_key_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyName")
    def kms_key_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyName"))

    @kms_key_name.setter
    def kms_key_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobCopyDestinationEncryptionConfigurationOutputReference, "kms_key_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleBigqueryJobCopyDestinationEncryptionConfiguration]:
        return typing.cast(typing.Optional[GoogleBigqueryJobCopyDestinationEncryptionConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryJobCopyDestinationEncryptionConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobCopyDestinationEncryptionConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryJob.GoogleBigqueryJobCopyDestinationTable",
    jsii_struct_bases=[],
    name_mapping={
        "table_id": "tableId",
        "dataset_id": "datasetId",
        "project_id": "projectId",
    },
)
class GoogleBigqueryJobCopyDestinationTable:
    def __init__(
        self,
        *,
        table_id: builtins.str,
        dataset_id: typing.Optional[builtins.str] = None,
        project_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param table_id: The table. Can be specified '{{table_id}}' if 'project_id' and 'dataset_id' are also set, or of the form 'projects/{{project}}/datasets/{{dataset_id}}/tables/{{table_id}}' if not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#table_id GoogleBigqueryJob#table_id}
        :param dataset_id: The ID of the dataset containing this table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#dataset_id GoogleBigqueryJob#dataset_id}
        :param project_id: The ID of the project containing this table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#project_id GoogleBigqueryJob#project_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobCopyDestinationTable.__init__)
            check_type(argname="argument table_id", value=table_id, expected_type=type_hints["table_id"])
            check_type(argname="argument dataset_id", value=dataset_id, expected_type=type_hints["dataset_id"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "table_id": table_id,
        }
        if dataset_id is not None:
            self._values["dataset_id"] = dataset_id
        if project_id is not None:
            self._values["project_id"] = project_id

    @builtins.property
    def table_id(self) -> builtins.str:
        '''The table. Can be specified '{{table_id}}' if 'project_id' and 'dataset_id' are also set, or of the form 'projects/{{project}}/datasets/{{dataset_id}}/tables/{{table_id}}' if not.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#table_id GoogleBigqueryJob#table_id}
        '''
        result = self._values.get("table_id")
        assert result is not None, "Required property 'table_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dataset_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the dataset containing this table.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#dataset_id GoogleBigqueryJob#dataset_id}
        '''
        result = self._values.get("dataset_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the project containing this table.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#project_id GoogleBigqueryJob#project_id}
        '''
        result = self._values.get("project_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryJobCopyDestinationTable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryJobCopyDestinationTableOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryJob.GoogleBigqueryJobCopyDestinationTableOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobCopyDestinationTableOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDatasetId")
    def reset_dataset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatasetId", []))

    @jsii.member(jsii_name="resetProjectId")
    def reset_project_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProjectId", []))

    @builtins.property
    @jsii.member(jsii_name="datasetIdInput")
    def dataset_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datasetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="projectIdInput")
    def project_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="tableIdInput")
    def table_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableIdInput"))

    @builtins.property
    @jsii.member(jsii_name="datasetId")
    def dataset_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datasetId"))

    @dataset_id.setter
    def dataset_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobCopyDestinationTableOutputReference, "dataset_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetId", value)

    @builtins.property
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectId"))

    @project_id.setter
    def project_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobCopyDestinationTableOutputReference, "project_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectId", value)

    @builtins.property
    @jsii.member(jsii_name="tableId")
    def table_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tableId"))

    @table_id.setter
    def table_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobCopyDestinationTableOutputReference, "table_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleBigqueryJobCopyDestinationTable]:
        return typing.cast(typing.Optional[GoogleBigqueryJobCopyDestinationTable], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryJobCopyDestinationTable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobCopyDestinationTableOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleBigqueryJobCopyOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryJob.GoogleBigqueryJobCopyOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobCopyOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDestinationEncryptionConfiguration")
    def put_destination_encryption_configuration(
        self,
        *,
        kms_key_name: builtins.str,
    ) -> None:
        '''
        :param kms_key_name: Describes the Cloud KMS encryption key that will be used to protect destination BigQuery table. The BigQuery Service Account associated with your project requires access to this encryption key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#kms_key_name GoogleBigqueryJob#kms_key_name}
        '''
        value = GoogleBigqueryJobCopyDestinationEncryptionConfiguration(
            kms_key_name=kms_key_name
        )

        return typing.cast(None, jsii.invoke(self, "putDestinationEncryptionConfiguration", [value]))

    @jsii.member(jsii_name="putDestinationTable")
    def put_destination_table(
        self,
        *,
        table_id: builtins.str,
        dataset_id: typing.Optional[builtins.str] = None,
        project_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param table_id: The table. Can be specified '{{table_id}}' if 'project_id' and 'dataset_id' are also set, or of the form 'projects/{{project}}/datasets/{{dataset_id}}/tables/{{table_id}}' if not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#table_id GoogleBigqueryJob#table_id}
        :param dataset_id: The ID of the dataset containing this table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#dataset_id GoogleBigqueryJob#dataset_id}
        :param project_id: The ID of the project containing this table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#project_id GoogleBigqueryJob#project_id}
        '''
        value = GoogleBigqueryJobCopyDestinationTable(
            table_id=table_id, dataset_id=dataset_id, project_id=project_id
        )

        return typing.cast(None, jsii.invoke(self, "putDestinationTable", [value]))

    @jsii.member(jsii_name="putSourceTables")
    def put_source_tables(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleBigqueryJobCopySourceTables", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobCopyOutputReference.put_source_tables)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putSourceTables", [value]))

    @jsii.member(jsii_name="resetCreateDisposition")
    def reset_create_disposition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreateDisposition", []))

    @jsii.member(jsii_name="resetDestinationEncryptionConfiguration")
    def reset_destination_encryption_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationEncryptionConfiguration", []))

    @jsii.member(jsii_name="resetDestinationTable")
    def reset_destination_table(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationTable", []))

    @jsii.member(jsii_name="resetWriteDisposition")
    def reset_write_disposition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWriteDisposition", []))

    @builtins.property
    @jsii.member(jsii_name="destinationEncryptionConfiguration")
    def destination_encryption_configuration(
        self,
    ) -> GoogleBigqueryJobCopyDestinationEncryptionConfigurationOutputReference:
        return typing.cast(GoogleBigqueryJobCopyDestinationEncryptionConfigurationOutputReference, jsii.get(self, "destinationEncryptionConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="destinationTable")
    def destination_table(self) -> GoogleBigqueryJobCopyDestinationTableOutputReference:
        return typing.cast(GoogleBigqueryJobCopyDestinationTableOutputReference, jsii.get(self, "destinationTable"))

    @builtins.property
    @jsii.member(jsii_name="sourceTables")
    def source_tables(self) -> "GoogleBigqueryJobCopySourceTablesList":
        return typing.cast("GoogleBigqueryJobCopySourceTablesList", jsii.get(self, "sourceTables"))

    @builtins.property
    @jsii.member(jsii_name="createDispositionInput")
    def create_disposition_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createDispositionInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationEncryptionConfigurationInput")
    def destination_encryption_configuration_input(
        self,
    ) -> typing.Optional[GoogleBigqueryJobCopyDestinationEncryptionConfiguration]:
        return typing.cast(typing.Optional[GoogleBigqueryJobCopyDestinationEncryptionConfiguration], jsii.get(self, "destinationEncryptionConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationTableInput")
    def destination_table_input(
        self,
    ) -> typing.Optional[GoogleBigqueryJobCopyDestinationTable]:
        return typing.cast(typing.Optional[GoogleBigqueryJobCopyDestinationTable], jsii.get(self, "destinationTableInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceTablesInput")
    def source_tables_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleBigqueryJobCopySourceTables"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleBigqueryJobCopySourceTables"]]], jsii.get(self, "sourceTablesInput"))

    @builtins.property
    @jsii.member(jsii_name="writeDispositionInput")
    def write_disposition_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "writeDispositionInput"))

    @builtins.property
    @jsii.member(jsii_name="createDisposition")
    def create_disposition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createDisposition"))

    @create_disposition.setter
    def create_disposition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobCopyOutputReference, "create_disposition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createDisposition", value)

    @builtins.property
    @jsii.member(jsii_name="writeDisposition")
    def write_disposition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "writeDisposition"))

    @write_disposition.setter
    def write_disposition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobCopyOutputReference, "write_disposition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "writeDisposition", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleBigqueryJobCopy]:
        return typing.cast(typing.Optional[GoogleBigqueryJobCopy], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[GoogleBigqueryJobCopy]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobCopyOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryJob.GoogleBigqueryJobCopySourceTables",
    jsii_struct_bases=[],
    name_mapping={
        "table_id": "tableId",
        "dataset_id": "datasetId",
        "project_id": "projectId",
    },
)
class GoogleBigqueryJobCopySourceTables:
    def __init__(
        self,
        *,
        table_id: builtins.str,
        dataset_id: typing.Optional[builtins.str] = None,
        project_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param table_id: The table. Can be specified '{{table_id}}' if 'project_id' and 'dataset_id' are also set, or of the form 'projects/{{project}}/datasets/{{dataset_id}}/tables/{{table_id}}' if not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#table_id GoogleBigqueryJob#table_id}
        :param dataset_id: The ID of the dataset containing this table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#dataset_id GoogleBigqueryJob#dataset_id}
        :param project_id: The ID of the project containing this table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#project_id GoogleBigqueryJob#project_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobCopySourceTables.__init__)
            check_type(argname="argument table_id", value=table_id, expected_type=type_hints["table_id"])
            check_type(argname="argument dataset_id", value=dataset_id, expected_type=type_hints["dataset_id"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "table_id": table_id,
        }
        if dataset_id is not None:
            self._values["dataset_id"] = dataset_id
        if project_id is not None:
            self._values["project_id"] = project_id

    @builtins.property
    def table_id(self) -> builtins.str:
        '''The table. Can be specified '{{table_id}}' if 'project_id' and 'dataset_id' are also set, or of the form 'projects/{{project}}/datasets/{{dataset_id}}/tables/{{table_id}}' if not.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#table_id GoogleBigqueryJob#table_id}
        '''
        result = self._values.get("table_id")
        assert result is not None, "Required property 'table_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dataset_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the dataset containing this table.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#dataset_id GoogleBigqueryJob#dataset_id}
        '''
        result = self._values.get("dataset_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the project containing this table.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#project_id GoogleBigqueryJob#project_id}
        '''
        result = self._values.get("project_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryJobCopySourceTables(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryJobCopySourceTablesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryJob.GoogleBigqueryJobCopySourceTablesList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobCopySourceTablesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleBigqueryJobCopySourceTablesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobCopySourceTablesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleBigqueryJobCopySourceTablesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobCopySourceTablesList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobCopySourceTablesList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobCopySourceTablesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleBigqueryJobCopySourceTables]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleBigqueryJobCopySourceTables]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleBigqueryJobCopySourceTables]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobCopySourceTablesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleBigqueryJobCopySourceTablesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryJob.GoogleBigqueryJobCopySourceTablesOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobCopySourceTablesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetDatasetId")
    def reset_dataset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatasetId", []))

    @jsii.member(jsii_name="resetProjectId")
    def reset_project_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProjectId", []))

    @builtins.property
    @jsii.member(jsii_name="datasetIdInput")
    def dataset_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datasetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="projectIdInput")
    def project_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="tableIdInput")
    def table_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableIdInput"))

    @builtins.property
    @jsii.member(jsii_name="datasetId")
    def dataset_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datasetId"))

    @dataset_id.setter
    def dataset_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobCopySourceTablesOutputReference, "dataset_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetId", value)

    @builtins.property
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectId"))

    @project_id.setter
    def project_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobCopySourceTablesOutputReference, "project_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectId", value)

    @builtins.property
    @jsii.member(jsii_name="tableId")
    def table_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tableId"))

    @table_id.setter
    def table_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobCopySourceTablesOutputReference, "table_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleBigqueryJobCopySourceTables, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleBigqueryJobCopySourceTables, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleBigqueryJobCopySourceTables, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobCopySourceTablesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryJob.GoogleBigqueryJobExtract",
    jsii_struct_bases=[],
    name_mapping={
        "destination_uris": "destinationUris",
        "compression": "compression",
        "destination_format": "destinationFormat",
        "field_delimiter": "fieldDelimiter",
        "print_header": "printHeader",
        "source_model": "sourceModel",
        "source_table": "sourceTable",
        "use_avro_logical_types": "useAvroLogicalTypes",
    },
)
class GoogleBigqueryJobExtract:
    def __init__(
        self,
        *,
        destination_uris: typing.Sequence[builtins.str],
        compression: typing.Optional[builtins.str] = None,
        destination_format: typing.Optional[builtins.str] = None,
        field_delimiter: typing.Optional[builtins.str] = None,
        print_header: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        source_model: typing.Optional[typing.Union["GoogleBigqueryJobExtractSourceModel", typing.Dict[str, typing.Any]]] = None,
        source_table: typing.Optional[typing.Union["GoogleBigqueryJobExtractSourceTable", typing.Dict[str, typing.Any]]] = None,
        use_avro_logical_types: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param destination_uris: A list of fully-qualified Google Cloud Storage URIs where the extracted table should be written. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#destination_uris GoogleBigqueryJob#destination_uris}
        :param compression: The compression type to use for exported files. Possible values include GZIP, DEFLATE, SNAPPY, and NONE. The default value is NONE. DEFLATE and SNAPPY are only supported for Avro. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#compression GoogleBigqueryJob#compression}
        :param destination_format: The exported file format. Possible values include CSV, NEWLINE_DELIMITED_JSON and AVRO for tables and SAVED_MODEL for models. The default value for tables is CSV. Tables with nested or repeated fields cannot be exported as CSV. The default value for models is SAVED_MODEL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#destination_format GoogleBigqueryJob#destination_format}
        :param field_delimiter: When extracting data in CSV format, this defines the delimiter to use between fields in the exported data. Default is ',' Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#field_delimiter GoogleBigqueryJob#field_delimiter}
        :param print_header: Whether to print out a header row in the results. Default is true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#print_header GoogleBigqueryJob#print_header}
        :param source_model: source_model block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#source_model GoogleBigqueryJob#source_model}
        :param source_table: source_table block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#source_table GoogleBigqueryJob#source_table}
        :param use_avro_logical_types: Whether to use logical types when extracting to AVRO format. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#use_avro_logical_types GoogleBigqueryJob#use_avro_logical_types}
        '''
        if isinstance(source_model, dict):
            source_model = GoogleBigqueryJobExtractSourceModel(**source_model)
        if isinstance(source_table, dict):
            source_table = GoogleBigqueryJobExtractSourceTable(**source_table)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobExtract.__init__)
            check_type(argname="argument destination_uris", value=destination_uris, expected_type=type_hints["destination_uris"])
            check_type(argname="argument compression", value=compression, expected_type=type_hints["compression"])
            check_type(argname="argument destination_format", value=destination_format, expected_type=type_hints["destination_format"])
            check_type(argname="argument field_delimiter", value=field_delimiter, expected_type=type_hints["field_delimiter"])
            check_type(argname="argument print_header", value=print_header, expected_type=type_hints["print_header"])
            check_type(argname="argument source_model", value=source_model, expected_type=type_hints["source_model"])
            check_type(argname="argument source_table", value=source_table, expected_type=type_hints["source_table"])
            check_type(argname="argument use_avro_logical_types", value=use_avro_logical_types, expected_type=type_hints["use_avro_logical_types"])
        self._values: typing.Dict[str, typing.Any] = {
            "destination_uris": destination_uris,
        }
        if compression is not None:
            self._values["compression"] = compression
        if destination_format is not None:
            self._values["destination_format"] = destination_format
        if field_delimiter is not None:
            self._values["field_delimiter"] = field_delimiter
        if print_header is not None:
            self._values["print_header"] = print_header
        if source_model is not None:
            self._values["source_model"] = source_model
        if source_table is not None:
            self._values["source_table"] = source_table
        if use_avro_logical_types is not None:
            self._values["use_avro_logical_types"] = use_avro_logical_types

    @builtins.property
    def destination_uris(self) -> typing.List[builtins.str]:
        '''A list of fully-qualified Google Cloud Storage URIs where the extracted table should be written.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#destination_uris GoogleBigqueryJob#destination_uris}
        '''
        result = self._values.get("destination_uris")
        assert result is not None, "Required property 'destination_uris' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def compression(self) -> typing.Optional[builtins.str]:
        '''The compression type to use for exported files.

        Possible values include GZIP, DEFLATE, SNAPPY, and NONE.
        The default value is NONE. DEFLATE and SNAPPY are only supported for Avro.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#compression GoogleBigqueryJob#compression}
        '''
        result = self._values.get("compression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def destination_format(self) -> typing.Optional[builtins.str]:
        '''The exported file format.

        Possible values include CSV, NEWLINE_DELIMITED_JSON and AVRO for tables and SAVED_MODEL for models.
        The default value for tables is CSV. Tables with nested or repeated fields cannot be exported as CSV.
        The default value for models is SAVED_MODEL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#destination_format GoogleBigqueryJob#destination_format}
        '''
        result = self._values.get("destination_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def field_delimiter(self) -> typing.Optional[builtins.str]:
        '''When extracting data in CSV format, this defines the delimiter to use between fields in the exported data.

        Default is ','

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#field_delimiter GoogleBigqueryJob#field_delimiter}
        '''
        result = self._values.get("field_delimiter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def print_header(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to print out a header row in the results. Default is true.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#print_header GoogleBigqueryJob#print_header}
        '''
        result = self._values.get("print_header")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def source_model(self) -> typing.Optional["GoogleBigqueryJobExtractSourceModel"]:
        '''source_model block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#source_model GoogleBigqueryJob#source_model}
        '''
        result = self._values.get("source_model")
        return typing.cast(typing.Optional["GoogleBigqueryJobExtractSourceModel"], result)

    @builtins.property
    def source_table(self) -> typing.Optional["GoogleBigqueryJobExtractSourceTable"]:
        '''source_table block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#source_table GoogleBigqueryJob#source_table}
        '''
        result = self._values.get("source_table")
        return typing.cast(typing.Optional["GoogleBigqueryJobExtractSourceTable"], result)

    @builtins.property
    def use_avro_logical_types(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to use logical types when extracting to AVRO format.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#use_avro_logical_types GoogleBigqueryJob#use_avro_logical_types}
        '''
        result = self._values.get("use_avro_logical_types")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryJobExtract(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryJobExtractOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryJob.GoogleBigqueryJobExtractOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobExtractOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putSourceModel")
    def put_source_model(
        self,
        *,
        dataset_id: builtins.str,
        model_id: builtins.str,
        project_id: builtins.str,
    ) -> None:
        '''
        :param dataset_id: The ID of the dataset containing this model. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#dataset_id GoogleBigqueryJob#dataset_id}
        :param model_id: The ID of the model. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#model_id GoogleBigqueryJob#model_id}
        :param project_id: The ID of the project containing this model. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#project_id GoogleBigqueryJob#project_id}
        '''
        value = GoogleBigqueryJobExtractSourceModel(
            dataset_id=dataset_id, model_id=model_id, project_id=project_id
        )

        return typing.cast(None, jsii.invoke(self, "putSourceModel", [value]))

    @jsii.member(jsii_name="putSourceTable")
    def put_source_table(
        self,
        *,
        table_id: builtins.str,
        dataset_id: typing.Optional[builtins.str] = None,
        project_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param table_id: The table. Can be specified '{{table_id}}' if 'project_id' and 'dataset_id' are also set, or of the form 'projects/{{project}}/datasets/{{dataset_id}}/tables/{{table_id}}' if not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#table_id GoogleBigqueryJob#table_id}
        :param dataset_id: The ID of the dataset containing this table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#dataset_id GoogleBigqueryJob#dataset_id}
        :param project_id: The ID of the project containing this table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#project_id GoogleBigqueryJob#project_id}
        '''
        value = GoogleBigqueryJobExtractSourceTable(
            table_id=table_id, dataset_id=dataset_id, project_id=project_id
        )

        return typing.cast(None, jsii.invoke(self, "putSourceTable", [value]))

    @jsii.member(jsii_name="resetCompression")
    def reset_compression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCompression", []))

    @jsii.member(jsii_name="resetDestinationFormat")
    def reset_destination_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationFormat", []))

    @jsii.member(jsii_name="resetFieldDelimiter")
    def reset_field_delimiter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFieldDelimiter", []))

    @jsii.member(jsii_name="resetPrintHeader")
    def reset_print_header(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrintHeader", []))

    @jsii.member(jsii_name="resetSourceModel")
    def reset_source_model(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceModel", []))

    @jsii.member(jsii_name="resetSourceTable")
    def reset_source_table(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceTable", []))

    @jsii.member(jsii_name="resetUseAvroLogicalTypes")
    def reset_use_avro_logical_types(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseAvroLogicalTypes", []))

    @builtins.property
    @jsii.member(jsii_name="sourceModel")
    def source_model(self) -> "GoogleBigqueryJobExtractSourceModelOutputReference":
        return typing.cast("GoogleBigqueryJobExtractSourceModelOutputReference", jsii.get(self, "sourceModel"))

    @builtins.property
    @jsii.member(jsii_name="sourceTable")
    def source_table(self) -> "GoogleBigqueryJobExtractSourceTableOutputReference":
        return typing.cast("GoogleBigqueryJobExtractSourceTableOutputReference", jsii.get(self, "sourceTable"))

    @builtins.property
    @jsii.member(jsii_name="compressionInput")
    def compression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "compressionInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationFormatInput")
    def destination_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "destinationFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationUrisInput")
    def destination_uris_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "destinationUrisInput"))

    @builtins.property
    @jsii.member(jsii_name="fieldDelimiterInput")
    def field_delimiter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fieldDelimiterInput"))

    @builtins.property
    @jsii.member(jsii_name="printHeaderInput")
    def print_header_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "printHeaderInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceModelInput")
    def source_model_input(
        self,
    ) -> typing.Optional["GoogleBigqueryJobExtractSourceModel"]:
        return typing.cast(typing.Optional["GoogleBigqueryJobExtractSourceModel"], jsii.get(self, "sourceModelInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceTableInput")
    def source_table_input(
        self,
    ) -> typing.Optional["GoogleBigqueryJobExtractSourceTable"]:
        return typing.cast(typing.Optional["GoogleBigqueryJobExtractSourceTable"], jsii.get(self, "sourceTableInput"))

    @builtins.property
    @jsii.member(jsii_name="useAvroLogicalTypesInput")
    def use_avro_logical_types_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "useAvroLogicalTypesInput"))

    @builtins.property
    @jsii.member(jsii_name="compression")
    def compression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "compression"))

    @compression.setter
    def compression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobExtractOutputReference, "compression").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "compression", value)

    @builtins.property
    @jsii.member(jsii_name="destinationFormat")
    def destination_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "destinationFormat"))

    @destination_format.setter
    def destination_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobExtractOutputReference, "destination_format").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationFormat", value)

    @builtins.property
    @jsii.member(jsii_name="destinationUris")
    def destination_uris(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "destinationUris"))

    @destination_uris.setter
    def destination_uris(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobExtractOutputReference, "destination_uris").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "destinationUris", value)

    @builtins.property
    @jsii.member(jsii_name="fieldDelimiter")
    def field_delimiter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fieldDelimiter"))

    @field_delimiter.setter
    def field_delimiter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobExtractOutputReference, "field_delimiter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fieldDelimiter", value)

    @builtins.property
    @jsii.member(jsii_name="printHeader")
    def print_header(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "printHeader"))

    @print_header.setter
    def print_header(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobExtractOutputReference, "print_header").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "printHeader", value)

    @builtins.property
    @jsii.member(jsii_name="useAvroLogicalTypes")
    def use_avro_logical_types(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "useAvroLogicalTypes"))

    @use_avro_logical_types.setter
    def use_avro_logical_types(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobExtractOutputReference, "use_avro_logical_types").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useAvroLogicalTypes", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleBigqueryJobExtract]:
        return typing.cast(typing.Optional[GoogleBigqueryJobExtract], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[GoogleBigqueryJobExtract]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobExtractOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryJob.GoogleBigqueryJobExtractSourceModel",
    jsii_struct_bases=[],
    name_mapping={
        "dataset_id": "datasetId",
        "model_id": "modelId",
        "project_id": "projectId",
    },
)
class GoogleBigqueryJobExtractSourceModel:
    def __init__(
        self,
        *,
        dataset_id: builtins.str,
        model_id: builtins.str,
        project_id: builtins.str,
    ) -> None:
        '''
        :param dataset_id: The ID of the dataset containing this model. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#dataset_id GoogleBigqueryJob#dataset_id}
        :param model_id: The ID of the model. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#model_id GoogleBigqueryJob#model_id}
        :param project_id: The ID of the project containing this model. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#project_id GoogleBigqueryJob#project_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobExtractSourceModel.__init__)
            check_type(argname="argument dataset_id", value=dataset_id, expected_type=type_hints["dataset_id"])
            check_type(argname="argument model_id", value=model_id, expected_type=type_hints["model_id"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "dataset_id": dataset_id,
            "model_id": model_id,
            "project_id": project_id,
        }

    @builtins.property
    def dataset_id(self) -> builtins.str:
        '''The ID of the dataset containing this model.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#dataset_id GoogleBigqueryJob#dataset_id}
        '''
        result = self._values.get("dataset_id")
        assert result is not None, "Required property 'dataset_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def model_id(self) -> builtins.str:
        '''The ID of the model.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#model_id GoogleBigqueryJob#model_id}
        '''
        result = self._values.get("model_id")
        assert result is not None, "Required property 'model_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_id(self) -> builtins.str:
        '''The ID of the project containing this model.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#project_id GoogleBigqueryJob#project_id}
        '''
        result = self._values.get("project_id")
        assert result is not None, "Required property 'project_id' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryJobExtractSourceModel(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryJobExtractSourceModelOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryJob.GoogleBigqueryJobExtractSourceModelOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobExtractSourceModelOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="datasetIdInput")
    def dataset_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datasetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="modelIdInput")
    def model_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modelIdInput"))

    @builtins.property
    @jsii.member(jsii_name="projectIdInput")
    def project_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="datasetId")
    def dataset_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datasetId"))

    @dataset_id.setter
    def dataset_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobExtractSourceModelOutputReference, "dataset_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetId", value)

    @builtins.property
    @jsii.member(jsii_name="modelId")
    def model_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "modelId"))

    @model_id.setter
    def model_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobExtractSourceModelOutputReference, "model_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "modelId", value)

    @builtins.property
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectId"))

    @project_id.setter
    def project_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobExtractSourceModelOutputReference, "project_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleBigqueryJobExtractSourceModel]:
        return typing.cast(typing.Optional[GoogleBigqueryJobExtractSourceModel], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryJobExtractSourceModel],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobExtractSourceModelOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryJob.GoogleBigqueryJobExtractSourceTable",
    jsii_struct_bases=[],
    name_mapping={
        "table_id": "tableId",
        "dataset_id": "datasetId",
        "project_id": "projectId",
    },
)
class GoogleBigqueryJobExtractSourceTable:
    def __init__(
        self,
        *,
        table_id: builtins.str,
        dataset_id: typing.Optional[builtins.str] = None,
        project_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param table_id: The table. Can be specified '{{table_id}}' if 'project_id' and 'dataset_id' are also set, or of the form 'projects/{{project}}/datasets/{{dataset_id}}/tables/{{table_id}}' if not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#table_id GoogleBigqueryJob#table_id}
        :param dataset_id: The ID of the dataset containing this table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#dataset_id GoogleBigqueryJob#dataset_id}
        :param project_id: The ID of the project containing this table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#project_id GoogleBigqueryJob#project_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobExtractSourceTable.__init__)
            check_type(argname="argument table_id", value=table_id, expected_type=type_hints["table_id"])
            check_type(argname="argument dataset_id", value=dataset_id, expected_type=type_hints["dataset_id"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "table_id": table_id,
        }
        if dataset_id is not None:
            self._values["dataset_id"] = dataset_id
        if project_id is not None:
            self._values["project_id"] = project_id

    @builtins.property
    def table_id(self) -> builtins.str:
        '''The table. Can be specified '{{table_id}}' if 'project_id' and 'dataset_id' are also set, or of the form 'projects/{{project}}/datasets/{{dataset_id}}/tables/{{table_id}}' if not.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#table_id GoogleBigqueryJob#table_id}
        '''
        result = self._values.get("table_id")
        assert result is not None, "Required property 'table_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dataset_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the dataset containing this table.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#dataset_id GoogleBigqueryJob#dataset_id}
        '''
        result = self._values.get("dataset_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the project containing this table.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#project_id GoogleBigqueryJob#project_id}
        '''
        result = self._values.get("project_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryJobExtractSourceTable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryJobExtractSourceTableOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryJob.GoogleBigqueryJobExtractSourceTableOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobExtractSourceTableOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDatasetId")
    def reset_dataset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatasetId", []))

    @jsii.member(jsii_name="resetProjectId")
    def reset_project_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProjectId", []))

    @builtins.property
    @jsii.member(jsii_name="datasetIdInput")
    def dataset_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datasetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="projectIdInput")
    def project_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="tableIdInput")
    def table_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableIdInput"))

    @builtins.property
    @jsii.member(jsii_name="datasetId")
    def dataset_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datasetId"))

    @dataset_id.setter
    def dataset_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobExtractSourceTableOutputReference, "dataset_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetId", value)

    @builtins.property
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectId"))

    @project_id.setter
    def project_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobExtractSourceTableOutputReference, "project_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectId", value)

    @builtins.property
    @jsii.member(jsii_name="tableId")
    def table_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tableId"))

    @table_id.setter
    def table_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobExtractSourceTableOutputReference, "table_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleBigqueryJobExtractSourceTable]:
        return typing.cast(typing.Optional[GoogleBigqueryJobExtractSourceTable], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryJobExtractSourceTable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobExtractSourceTableOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryJob.GoogleBigqueryJobLoad",
    jsii_struct_bases=[],
    name_mapping={
        "destination_table": "destinationTable",
        "source_uris": "sourceUris",
        "allow_jagged_rows": "allowJaggedRows",
        "allow_quoted_newlines": "allowQuotedNewlines",
        "autodetect": "autodetect",
        "create_disposition": "createDisposition",
        "destination_encryption_configuration": "destinationEncryptionConfiguration",
        "encoding": "encoding",
        "field_delimiter": "fieldDelimiter",
        "ignore_unknown_values": "ignoreUnknownValues",
        "json_extension": "jsonExtension",
        "max_bad_records": "maxBadRecords",
        "null_marker": "nullMarker",
        "projection_fields": "projectionFields",
        "quote": "quote",
        "schema_update_options": "schemaUpdateOptions",
        "skip_leading_rows": "skipLeadingRows",
        "source_format": "sourceFormat",
        "time_partitioning": "timePartitioning",
        "write_disposition": "writeDisposition",
    },
)
class GoogleBigqueryJobLoad:
    def __init__(
        self,
        *,
        destination_table: typing.Union["GoogleBigqueryJobLoadDestinationTable", typing.Dict[str, typing.Any]],
        source_uris: typing.Sequence[builtins.str],
        allow_jagged_rows: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_quoted_newlines: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        autodetect: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        create_disposition: typing.Optional[builtins.str] = None,
        destination_encryption_configuration: typing.Optional[typing.Union["GoogleBigqueryJobLoadDestinationEncryptionConfiguration", typing.Dict[str, typing.Any]]] = None,
        encoding: typing.Optional[builtins.str] = None,
        field_delimiter: typing.Optional[builtins.str] = None,
        ignore_unknown_values: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        json_extension: typing.Optional[builtins.str] = None,
        max_bad_records: typing.Optional[jsii.Number] = None,
        null_marker: typing.Optional[builtins.str] = None,
        projection_fields: typing.Optional[typing.Sequence[builtins.str]] = None,
        quote: typing.Optional[builtins.str] = None,
        schema_update_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        skip_leading_rows: typing.Optional[jsii.Number] = None,
        source_format: typing.Optional[builtins.str] = None,
        time_partitioning: typing.Optional[typing.Union["GoogleBigqueryJobLoadTimePartitioning", typing.Dict[str, typing.Any]]] = None,
        write_disposition: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param destination_table: destination_table block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#destination_table GoogleBigqueryJob#destination_table}
        :param source_uris: The fully-qualified URIs that point to your data in Google Cloud. For Google Cloud Storage URIs: Each URI can contain one '*' wildcard character and it must come after the 'bucket' name. Size limits related to load jobs apply to external data sources. For Google Cloud Bigtable URIs: Exactly one URI can be specified and it has be a fully specified and valid HTTPS URL for a Google Cloud Bigtable table. For Google Cloud Datastore backups: Exactly one URI can be specified. Also, the '*' wildcard character is not allowed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#source_uris GoogleBigqueryJob#source_uris}
        :param allow_jagged_rows: Accept rows that are missing trailing optional columns. The missing values are treated as nulls. If false, records with missing trailing columns are treated as bad records, and if there are too many bad records, an invalid error is returned in the job result. The default value is false. Only applicable to CSV, ignored for other formats. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#allow_jagged_rows GoogleBigqueryJob#allow_jagged_rows}
        :param allow_quoted_newlines: Indicates if BigQuery should allow quoted data sections that contain newline characters in a CSV file. The default value is false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#allow_quoted_newlines GoogleBigqueryJob#allow_quoted_newlines}
        :param autodetect: Indicates if we should automatically infer the options and schema for CSV and JSON sources. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#autodetect GoogleBigqueryJob#autodetect}
        :param create_disposition: Specifies whether the job is allowed to create new tables. The following values are supported: CREATE_IF_NEEDED: If the table does not exist, BigQuery creates the table. CREATE_NEVER: The table must already exist. If it does not, a 'notFound' error is returned in the job result. Creation, truncation and append actions occur as one atomic update upon job completion Default value: "CREATE_IF_NEEDED" Possible values: ["CREATE_IF_NEEDED", "CREATE_NEVER"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#create_disposition GoogleBigqueryJob#create_disposition}
        :param destination_encryption_configuration: destination_encryption_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#destination_encryption_configuration GoogleBigqueryJob#destination_encryption_configuration}
        :param encoding: The character encoding of the data. The supported values are UTF-8 or ISO-8859-1. The default value is UTF-8. BigQuery decodes the data after the raw, binary data has been split using the values of the quote and fieldDelimiter properties. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#encoding GoogleBigqueryJob#encoding}
        :param field_delimiter: The separator for fields in a CSV file. The separator can be any ISO-8859-1 single-byte character. To use a character in the range 128-255, you must encode the character as UTF8. BigQuery converts the string to ISO-8859-1 encoding, and then uses the first byte of the encoded string to split the data in its raw, binary state. BigQuery also supports the escape sequence "\\t" to specify a tab separator. The default value is a comma (','). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#field_delimiter GoogleBigqueryJob#field_delimiter}
        :param ignore_unknown_values: Indicates if BigQuery should allow extra values that are not represented in the table schema. If true, the extra values are ignored. If false, records with extra columns are treated as bad records, and if there are too many bad records, an invalid error is returned in the job result. The default value is false. The sourceFormat property determines what BigQuery treats as an extra value: CSV: Trailing columns JSON: Named values that don't match any column names Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#ignore_unknown_values GoogleBigqueryJob#ignore_unknown_values}
        :param json_extension: If sourceFormat is set to newline-delimited JSON, indicates whether it should be processed as a JSON variant such as GeoJSON. For a sourceFormat other than JSON, omit this field. If the sourceFormat is newline-delimited JSON: - for newline-delimited GeoJSON: set to GEOJSON. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#json_extension GoogleBigqueryJob#json_extension}
        :param max_bad_records: The maximum number of bad records that BigQuery can ignore when running the job. If the number of bad records exceeds this value, an invalid error is returned in the job result. The default value is 0, which requires that all records are valid. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#max_bad_records GoogleBigqueryJob#max_bad_records}
        :param null_marker: Specifies a string that represents a null value in a CSV file. For example, if you specify "\\N", BigQuery interprets "\\N" as a null value when loading a CSV file. The default value is the empty string. If you set this property to a custom value, BigQuery throws an error if an empty string is present for all data types except for STRING and BYTE. For STRING and BYTE columns, BigQuery interprets the empty string as an empty value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#null_marker GoogleBigqueryJob#null_marker}
        :param projection_fields: If sourceFormat is set to "DATASTORE_BACKUP", indicates which entity properties to load into BigQuery from a Cloud Datastore backup. Property names are case sensitive and must be top-level properties. If no properties are specified, BigQuery loads all properties. If any named property isn't found in the Cloud Datastore backup, an invalid error is returned in the job result. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#projection_fields GoogleBigqueryJob#projection_fields}
        :param quote: The value that is used to quote data sections in a CSV file. BigQuery converts the string to ISO-8859-1 encoding, and then uses the first byte of the encoded string to split the data in its raw, binary state. The default value is a double-quote ('"'). If your data does not contain quoted sections, set the property value to an empty string. If your data contains quoted newline characters, you must also set the allowQuotedNewlines property to true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#quote GoogleBigqueryJob#quote}
        :param schema_update_options: Allows the schema of the destination table to be updated as a side effect of the load job if a schema is autodetected or supplied in the job configuration. Schema update options are supported in two cases: when writeDisposition is WRITE_APPEND; when writeDisposition is WRITE_TRUNCATE and the destination table is a partition of a table, specified by partition decorators. For normal tables, WRITE_TRUNCATE will always overwrite the schema. One or more of the following values are specified: ALLOW_FIELD_ADDITION: allow adding a nullable field to the schema. ALLOW_FIELD_RELAXATION: allow relaxing a required field in the original schema to nullable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#schema_update_options GoogleBigqueryJob#schema_update_options}
        :param skip_leading_rows: The number of rows at the top of a CSV file that BigQuery will skip when loading the data. The default value is 0. This property is useful if you have header rows in the file that should be skipped. When autodetect is on, the behavior is the following: skipLeadingRows unspecified - Autodetect tries to detect headers in the first row. If they are not detected, the row is read as data. Otherwise data is read starting from the second row. skipLeadingRows is 0 - Instructs autodetect that there are no headers and data should be read starting from the first row. skipLeadingRows = N > 0 - Autodetect skips N-1 rows and tries to detect headers in row N. If headers are not detected, row N is just skipped. Otherwise row N is used to extract column names for the detected schema. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#skip_leading_rows GoogleBigqueryJob#skip_leading_rows}
        :param source_format: The format of the data files. For CSV files, specify "CSV". For datastore backups, specify "DATASTORE_BACKUP". For newline-delimited JSON, specify "NEWLINE_DELIMITED_JSON". For Avro, specify "AVRO". For parquet, specify "PARQUET". For orc, specify "ORC". [Beta] For Bigtable, specify "BIGTABLE". The default value is CSV. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#source_format GoogleBigqueryJob#source_format}
        :param time_partitioning: time_partitioning block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#time_partitioning GoogleBigqueryJob#time_partitioning}
        :param write_disposition: Specifies the action that occurs if the destination table already exists. The following values are supported: WRITE_TRUNCATE: If the table already exists, BigQuery overwrites the table data and uses the schema from the query result. WRITE_APPEND: If the table already exists, BigQuery appends the data to the table. WRITE_EMPTY: If the table already exists and contains data, a 'duplicate' error is returned in the job result. Each action is atomic and only occurs if BigQuery is able to complete the job successfully. Creation, truncation and append actions occur as one atomic update upon job completion. Default value: "WRITE_EMPTY" Possible values: ["WRITE_TRUNCATE", "WRITE_APPEND", "WRITE_EMPTY"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#write_disposition GoogleBigqueryJob#write_disposition}
        '''
        if isinstance(destination_table, dict):
            destination_table = GoogleBigqueryJobLoadDestinationTable(**destination_table)
        if isinstance(destination_encryption_configuration, dict):
            destination_encryption_configuration = GoogleBigqueryJobLoadDestinationEncryptionConfiguration(**destination_encryption_configuration)
        if isinstance(time_partitioning, dict):
            time_partitioning = GoogleBigqueryJobLoadTimePartitioning(**time_partitioning)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobLoad.__init__)
            check_type(argname="argument destination_table", value=destination_table, expected_type=type_hints["destination_table"])
            check_type(argname="argument source_uris", value=source_uris, expected_type=type_hints["source_uris"])
            check_type(argname="argument allow_jagged_rows", value=allow_jagged_rows, expected_type=type_hints["allow_jagged_rows"])
            check_type(argname="argument allow_quoted_newlines", value=allow_quoted_newlines, expected_type=type_hints["allow_quoted_newlines"])
            check_type(argname="argument autodetect", value=autodetect, expected_type=type_hints["autodetect"])
            check_type(argname="argument create_disposition", value=create_disposition, expected_type=type_hints["create_disposition"])
            check_type(argname="argument destination_encryption_configuration", value=destination_encryption_configuration, expected_type=type_hints["destination_encryption_configuration"])
            check_type(argname="argument encoding", value=encoding, expected_type=type_hints["encoding"])
            check_type(argname="argument field_delimiter", value=field_delimiter, expected_type=type_hints["field_delimiter"])
            check_type(argname="argument ignore_unknown_values", value=ignore_unknown_values, expected_type=type_hints["ignore_unknown_values"])
            check_type(argname="argument json_extension", value=json_extension, expected_type=type_hints["json_extension"])
            check_type(argname="argument max_bad_records", value=max_bad_records, expected_type=type_hints["max_bad_records"])
            check_type(argname="argument null_marker", value=null_marker, expected_type=type_hints["null_marker"])
            check_type(argname="argument projection_fields", value=projection_fields, expected_type=type_hints["projection_fields"])
            check_type(argname="argument quote", value=quote, expected_type=type_hints["quote"])
            check_type(argname="argument schema_update_options", value=schema_update_options, expected_type=type_hints["schema_update_options"])
            check_type(argname="argument skip_leading_rows", value=skip_leading_rows, expected_type=type_hints["skip_leading_rows"])
            check_type(argname="argument source_format", value=source_format, expected_type=type_hints["source_format"])
            check_type(argname="argument time_partitioning", value=time_partitioning, expected_type=type_hints["time_partitioning"])
            check_type(argname="argument write_disposition", value=write_disposition, expected_type=type_hints["write_disposition"])
        self._values: typing.Dict[str, typing.Any] = {
            "destination_table": destination_table,
            "source_uris": source_uris,
        }
        if allow_jagged_rows is not None:
            self._values["allow_jagged_rows"] = allow_jagged_rows
        if allow_quoted_newlines is not None:
            self._values["allow_quoted_newlines"] = allow_quoted_newlines
        if autodetect is not None:
            self._values["autodetect"] = autodetect
        if create_disposition is not None:
            self._values["create_disposition"] = create_disposition
        if destination_encryption_configuration is not None:
            self._values["destination_encryption_configuration"] = destination_encryption_configuration
        if encoding is not None:
            self._values["encoding"] = encoding
        if field_delimiter is not None:
            self._values["field_delimiter"] = field_delimiter
        if ignore_unknown_values is not None:
            self._values["ignore_unknown_values"] = ignore_unknown_values
        if json_extension is not None:
            self._values["json_extension"] = json_extension
        if max_bad_records is not None:
            self._values["max_bad_records"] = max_bad_records
        if null_marker is not None:
            self._values["null_marker"] = null_marker
        if projection_fields is not None:
            self._values["projection_fields"] = projection_fields
        if quote is not None:
            self._values["quote"] = quote
        if schema_update_options is not None:
            self._values["schema_update_options"] = schema_update_options
        if skip_leading_rows is not None:
            self._values["skip_leading_rows"] = skip_leading_rows
        if source_format is not None:
            self._values["source_format"] = source_format
        if time_partitioning is not None:
            self._values["time_partitioning"] = time_partitioning
        if write_disposition is not None:
            self._values["write_disposition"] = write_disposition

    @builtins.property
    def destination_table(self) -> "GoogleBigqueryJobLoadDestinationTable":
        '''destination_table block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#destination_table GoogleBigqueryJob#destination_table}
        '''
        result = self._values.get("destination_table")
        assert result is not None, "Required property 'destination_table' is missing"
        return typing.cast("GoogleBigqueryJobLoadDestinationTable", result)

    @builtins.property
    def source_uris(self) -> typing.List[builtins.str]:
        '''The fully-qualified URIs that point to your data in Google Cloud.

        For Google Cloud Storage URIs: Each URI can contain one '*' wildcard character
        and it must come after the 'bucket' name. Size limits related to load jobs apply
        to external data sources. For Google Cloud Bigtable URIs: Exactly one URI can be
        specified and it has be a fully specified and valid HTTPS URL for a Google Cloud Bigtable table.
        For Google Cloud Datastore backups: Exactly one URI can be specified. Also, the '*' wildcard character is not allowed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#source_uris GoogleBigqueryJob#source_uris}
        '''
        result = self._values.get("source_uris")
        assert result is not None, "Required property 'source_uris' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def allow_jagged_rows(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Accept rows that are missing trailing optional columns.

        The missing values are treated as nulls.
        If false, records with missing trailing columns are treated as bad records, and if there are too many bad records,
        an invalid error is returned in the job result. The default value is false. Only applicable to CSV, ignored for other formats.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#allow_jagged_rows GoogleBigqueryJob#allow_jagged_rows}
        '''
        result = self._values.get("allow_jagged_rows")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def allow_quoted_newlines(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Indicates if BigQuery should allow quoted data sections that contain newline characters in a CSV file.

        The default value is false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#allow_quoted_newlines GoogleBigqueryJob#allow_quoted_newlines}
        '''
        result = self._values.get("allow_quoted_newlines")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def autodetect(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Indicates if we should automatically infer the options and schema for CSV and JSON sources.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#autodetect GoogleBigqueryJob#autodetect}
        '''
        result = self._values.get("autodetect")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def create_disposition(self) -> typing.Optional[builtins.str]:
        '''Specifies whether the job is allowed to create new tables.

        The following values are supported:
        CREATE_IF_NEEDED: If the table does not exist, BigQuery creates the table.
        CREATE_NEVER: The table must already exist. If it does not, a 'notFound' error is returned in the job result.
        Creation, truncation and append actions occur as one atomic update upon job completion Default value: "CREATE_IF_NEEDED" Possible values: ["CREATE_IF_NEEDED", "CREATE_NEVER"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#create_disposition GoogleBigqueryJob#create_disposition}
        '''
        result = self._values.get("create_disposition")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def destination_encryption_configuration(
        self,
    ) -> typing.Optional["GoogleBigqueryJobLoadDestinationEncryptionConfiguration"]:
        '''destination_encryption_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#destination_encryption_configuration GoogleBigqueryJob#destination_encryption_configuration}
        '''
        result = self._values.get("destination_encryption_configuration")
        return typing.cast(typing.Optional["GoogleBigqueryJobLoadDestinationEncryptionConfiguration"], result)

    @builtins.property
    def encoding(self) -> typing.Optional[builtins.str]:
        '''The character encoding of the data.

        The supported values are UTF-8 or ISO-8859-1.
        The default value is UTF-8. BigQuery decodes the data after the raw, binary data
        has been split using the values of the quote and fieldDelimiter properties.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#encoding GoogleBigqueryJob#encoding}
        '''
        result = self._values.get("encoding")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def field_delimiter(self) -> typing.Optional[builtins.str]:
        '''The separator for fields in a CSV file.

        The separator can be any ISO-8859-1 single-byte character.
        To use a character in the range 128-255, you must encode the character as UTF8. BigQuery converts
        the string to ISO-8859-1 encoding, and then uses the first byte of the encoded string to split the
        data in its raw, binary state. BigQuery also supports the escape sequence "\\t" to specify a tab separator.
        The default value is a comma (',').

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#field_delimiter GoogleBigqueryJob#field_delimiter}
        '''
        result = self._values.get("field_delimiter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def ignore_unknown_values(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Indicates if BigQuery should allow extra values that are not represented in the table schema.

        If true, the extra values are ignored. If false, records with extra columns are treated as bad records,
        and if there are too many bad records, an invalid error is returned in the job result.
        The default value is false. The sourceFormat property determines what BigQuery treats as an extra value:
        CSV: Trailing columns
        JSON: Named values that don't match any column names

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#ignore_unknown_values GoogleBigqueryJob#ignore_unknown_values}
        '''
        result = self._values.get("ignore_unknown_values")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def json_extension(self) -> typing.Optional[builtins.str]:
        '''If sourceFormat is set to newline-delimited JSON, indicates whether it should be processed as a JSON variant such as GeoJSON.

        For a sourceFormat other than JSON, omit this field. If the sourceFormat is newline-delimited JSON: - for newline-delimited
        GeoJSON: set to GEOJSON.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#json_extension GoogleBigqueryJob#json_extension}
        '''
        result = self._values.get("json_extension")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def max_bad_records(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of bad records that BigQuery can ignore when running the job.

        If the number of bad records exceeds this value,
        an invalid error is returned in the job result. The default value is 0, which requires that all records are valid.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#max_bad_records GoogleBigqueryJob#max_bad_records}
        '''
        result = self._values.get("max_bad_records")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def null_marker(self) -> typing.Optional[builtins.str]:
        '''Specifies a string that represents a null value in a CSV file.

        For example, if you specify "\\N", BigQuery interprets "\\N" as a null value
        when loading a CSV file. The default value is the empty string. If you set this property to a custom value, BigQuery throws an error if an
        empty string is present for all data types except for STRING and BYTE. For STRING and BYTE columns, BigQuery interprets the empty string as
        an empty value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#null_marker GoogleBigqueryJob#null_marker}
        '''
        result = self._values.get("null_marker")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def projection_fields(self) -> typing.Optional[typing.List[builtins.str]]:
        '''If sourceFormat is set to "DATASTORE_BACKUP", indicates which entity properties to load into BigQuery from a Cloud Datastore backup.

        Property names are case sensitive and must be top-level properties. If no properties are specified, BigQuery loads all properties.
        If any named property isn't found in the Cloud Datastore backup, an invalid error is returned in the job result.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#projection_fields GoogleBigqueryJob#projection_fields}
        '''
        result = self._values.get("projection_fields")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def quote(self) -> typing.Optional[builtins.str]:
        '''The value that is used to quote data sections in a CSV file.

        BigQuery converts the string to ISO-8859-1 encoding,
        and then uses the first byte of the encoded string to split the data in its raw, binary state.
        The default value is a double-quote ('"'). If your data does not contain quoted sections, set the property value to an empty string.
        If your data contains quoted newline characters, you must also set the allowQuotedNewlines property to true.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#quote GoogleBigqueryJob#quote}
        '''
        result = self._values.get("quote")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schema_update_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Allows the schema of the destination table to be updated as a side effect of the load job if a schema is autodetected or supplied in the job configuration.

        Schema update options are supported in two cases: when writeDisposition is WRITE_APPEND;
        when writeDisposition is WRITE_TRUNCATE and the destination table is a partition of a table, specified by partition decorators.
        For normal tables, WRITE_TRUNCATE will always overwrite the schema. One or more of the following values are specified:
        ALLOW_FIELD_ADDITION: allow adding a nullable field to the schema.
        ALLOW_FIELD_RELAXATION: allow relaxing a required field in the original schema to nullable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#schema_update_options GoogleBigqueryJob#schema_update_options}
        '''
        result = self._values.get("schema_update_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def skip_leading_rows(self) -> typing.Optional[jsii.Number]:
        '''The number of rows at the top of a CSV file that BigQuery will skip when loading the data.

        The default value is 0. This property is useful if you have header rows in the file that should be skipped.
        When autodetect is on, the behavior is the following:
        skipLeadingRows unspecified - Autodetect tries to detect headers in the first row. If they are not detected,
        the row is read as data. Otherwise data is read starting from the second row.
        skipLeadingRows is 0 - Instructs autodetect that there are no headers and data should be read starting from the first row.
        skipLeadingRows = N > 0 - Autodetect skips N-1 rows and tries to detect headers in row N. If headers are not detected,
        row N is just skipped. Otherwise row N is used to extract column names for the detected schema.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#skip_leading_rows GoogleBigqueryJob#skip_leading_rows}
        '''
        result = self._values.get("skip_leading_rows")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def source_format(self) -> typing.Optional[builtins.str]:
        '''The format of the data files.

        For CSV files, specify "CSV". For datastore backups, specify "DATASTORE_BACKUP".
        For newline-delimited JSON, specify "NEWLINE_DELIMITED_JSON". For Avro, specify "AVRO". For parquet, specify "PARQUET".
        For orc, specify "ORC". [Beta] For Bigtable, specify "BIGTABLE".
        The default value is CSV.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#source_format GoogleBigqueryJob#source_format}
        '''
        result = self._values.get("source_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def time_partitioning(
        self,
    ) -> typing.Optional["GoogleBigqueryJobLoadTimePartitioning"]:
        '''time_partitioning block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#time_partitioning GoogleBigqueryJob#time_partitioning}
        '''
        result = self._values.get("time_partitioning")
        return typing.cast(typing.Optional["GoogleBigqueryJobLoadTimePartitioning"], result)

    @builtins.property
    def write_disposition(self) -> typing.Optional[builtins.str]:
        '''Specifies the action that occurs if the destination table already exists.

        The following values are supported:
        WRITE_TRUNCATE: If the table already exists, BigQuery overwrites the table data and uses the schema from the query result.
        WRITE_APPEND: If the table already exists, BigQuery appends the data to the table.
        WRITE_EMPTY: If the table already exists and contains data, a 'duplicate' error is returned in the job result.
        Each action is atomic and only occurs if BigQuery is able to complete the job successfully.
        Creation, truncation and append actions occur as one atomic update upon job completion. Default value: "WRITE_EMPTY" Possible values: ["WRITE_TRUNCATE", "WRITE_APPEND", "WRITE_EMPTY"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#write_disposition GoogleBigqueryJob#write_disposition}
        '''
        result = self._values.get("write_disposition")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryJobLoad(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryJob.GoogleBigqueryJobLoadDestinationEncryptionConfiguration",
    jsii_struct_bases=[],
    name_mapping={"kms_key_name": "kmsKeyName"},
)
class GoogleBigqueryJobLoadDestinationEncryptionConfiguration:
    def __init__(self, *, kms_key_name: builtins.str) -> None:
        '''
        :param kms_key_name: Describes the Cloud KMS encryption key that will be used to protect destination BigQuery table. The BigQuery Service Account associated with your project requires access to this encryption key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#kms_key_name GoogleBigqueryJob#kms_key_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobLoadDestinationEncryptionConfiguration.__init__)
            check_type(argname="argument kms_key_name", value=kms_key_name, expected_type=type_hints["kms_key_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "kms_key_name": kms_key_name,
        }

    @builtins.property
    def kms_key_name(self) -> builtins.str:
        '''Describes the Cloud KMS encryption key that will be used to protect destination BigQuery table.

        The BigQuery Service Account associated with your project requires access to this encryption key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#kms_key_name GoogleBigqueryJob#kms_key_name}
        '''
        result = self._values.get("kms_key_name")
        assert result is not None, "Required property 'kms_key_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryJobLoadDestinationEncryptionConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryJobLoadDestinationEncryptionConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryJob.GoogleBigqueryJobLoadDestinationEncryptionConfigurationOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobLoadDestinationEncryptionConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="kmsKeyVersion")
    def kms_key_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyVersion"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyNameInput")
    def kms_key_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyName")
    def kms_key_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyName"))

    @kms_key_name.setter
    def kms_key_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobLoadDestinationEncryptionConfigurationOutputReference, "kms_key_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleBigqueryJobLoadDestinationEncryptionConfiguration]:
        return typing.cast(typing.Optional[GoogleBigqueryJobLoadDestinationEncryptionConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryJobLoadDestinationEncryptionConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobLoadDestinationEncryptionConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryJob.GoogleBigqueryJobLoadDestinationTable",
    jsii_struct_bases=[],
    name_mapping={
        "table_id": "tableId",
        "dataset_id": "datasetId",
        "project_id": "projectId",
    },
)
class GoogleBigqueryJobLoadDestinationTable:
    def __init__(
        self,
        *,
        table_id: builtins.str,
        dataset_id: typing.Optional[builtins.str] = None,
        project_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param table_id: The table. Can be specified '{{table_id}}' if 'project_id' and 'dataset_id' are also set, or of the form 'projects/{{project}}/datasets/{{dataset_id}}/tables/{{table_id}}' if not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#table_id GoogleBigqueryJob#table_id}
        :param dataset_id: The ID of the dataset containing this table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#dataset_id GoogleBigqueryJob#dataset_id}
        :param project_id: The ID of the project containing this table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#project_id GoogleBigqueryJob#project_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobLoadDestinationTable.__init__)
            check_type(argname="argument table_id", value=table_id, expected_type=type_hints["table_id"])
            check_type(argname="argument dataset_id", value=dataset_id, expected_type=type_hints["dataset_id"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "table_id": table_id,
        }
        if dataset_id is not None:
            self._values["dataset_id"] = dataset_id
        if project_id is not None:
            self._values["project_id"] = project_id

    @builtins.property
    def table_id(self) -> builtins.str:
        '''The table. Can be specified '{{table_id}}' if 'project_id' and 'dataset_id' are also set, or of the form 'projects/{{project}}/datasets/{{dataset_id}}/tables/{{table_id}}' if not.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#table_id GoogleBigqueryJob#table_id}
        '''
        result = self._values.get("table_id")
        assert result is not None, "Required property 'table_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dataset_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the dataset containing this table.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#dataset_id GoogleBigqueryJob#dataset_id}
        '''
        result = self._values.get("dataset_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the project containing this table.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#project_id GoogleBigqueryJob#project_id}
        '''
        result = self._values.get("project_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryJobLoadDestinationTable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryJobLoadDestinationTableOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryJob.GoogleBigqueryJobLoadDestinationTableOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobLoadDestinationTableOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDatasetId")
    def reset_dataset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatasetId", []))

    @jsii.member(jsii_name="resetProjectId")
    def reset_project_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProjectId", []))

    @builtins.property
    @jsii.member(jsii_name="datasetIdInput")
    def dataset_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datasetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="projectIdInput")
    def project_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="tableIdInput")
    def table_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableIdInput"))

    @builtins.property
    @jsii.member(jsii_name="datasetId")
    def dataset_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datasetId"))

    @dataset_id.setter
    def dataset_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobLoadDestinationTableOutputReference, "dataset_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetId", value)

    @builtins.property
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectId"))

    @project_id.setter
    def project_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobLoadDestinationTableOutputReference, "project_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectId", value)

    @builtins.property
    @jsii.member(jsii_name="tableId")
    def table_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tableId"))

    @table_id.setter
    def table_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobLoadDestinationTableOutputReference, "table_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleBigqueryJobLoadDestinationTable]:
        return typing.cast(typing.Optional[GoogleBigqueryJobLoadDestinationTable], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryJobLoadDestinationTable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobLoadDestinationTableOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleBigqueryJobLoadOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryJob.GoogleBigqueryJobLoadOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobLoadOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDestinationEncryptionConfiguration")
    def put_destination_encryption_configuration(
        self,
        *,
        kms_key_name: builtins.str,
    ) -> None:
        '''
        :param kms_key_name: Describes the Cloud KMS encryption key that will be used to protect destination BigQuery table. The BigQuery Service Account associated with your project requires access to this encryption key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#kms_key_name GoogleBigqueryJob#kms_key_name}
        '''
        value = GoogleBigqueryJobLoadDestinationEncryptionConfiguration(
            kms_key_name=kms_key_name
        )

        return typing.cast(None, jsii.invoke(self, "putDestinationEncryptionConfiguration", [value]))

    @jsii.member(jsii_name="putDestinationTable")
    def put_destination_table(
        self,
        *,
        table_id: builtins.str,
        dataset_id: typing.Optional[builtins.str] = None,
        project_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param table_id: The table. Can be specified '{{table_id}}' if 'project_id' and 'dataset_id' are also set, or of the form 'projects/{{project}}/datasets/{{dataset_id}}/tables/{{table_id}}' if not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#table_id GoogleBigqueryJob#table_id}
        :param dataset_id: The ID of the dataset containing this table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#dataset_id GoogleBigqueryJob#dataset_id}
        :param project_id: The ID of the project containing this table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#project_id GoogleBigqueryJob#project_id}
        '''
        value = GoogleBigqueryJobLoadDestinationTable(
            table_id=table_id, dataset_id=dataset_id, project_id=project_id
        )

        return typing.cast(None, jsii.invoke(self, "putDestinationTable", [value]))

    @jsii.member(jsii_name="putTimePartitioning")
    def put_time_partitioning(
        self,
        *,
        type: builtins.str,
        expiration_ms: typing.Optional[builtins.str] = None,
        field: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: The only type supported is DAY, which will generate one partition per day. Providing an empty string used to cause an error, but in OnePlatform the field will be treated as unset. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#type GoogleBigqueryJob#type}
        :param expiration_ms: Number of milliseconds for which to keep the storage for a partition. A wrapper is used here because 0 is an invalid value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#expiration_ms GoogleBigqueryJob#expiration_ms}
        :param field: If not set, the table is partitioned by pseudo column '_PARTITIONTIME'; if set, the table is partitioned by this field. The field must be a top-level TIMESTAMP or DATE field. Its mode must be NULLABLE or REQUIRED. A wrapper is used here because an empty string is an invalid value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#field GoogleBigqueryJob#field}
        '''
        value = GoogleBigqueryJobLoadTimePartitioning(
            type=type, expiration_ms=expiration_ms, field=field
        )

        return typing.cast(None, jsii.invoke(self, "putTimePartitioning", [value]))

    @jsii.member(jsii_name="resetAllowJaggedRows")
    def reset_allow_jagged_rows(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowJaggedRows", []))

    @jsii.member(jsii_name="resetAllowQuotedNewlines")
    def reset_allow_quoted_newlines(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowQuotedNewlines", []))

    @jsii.member(jsii_name="resetAutodetect")
    def reset_autodetect(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAutodetect", []))

    @jsii.member(jsii_name="resetCreateDisposition")
    def reset_create_disposition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreateDisposition", []))

    @jsii.member(jsii_name="resetDestinationEncryptionConfiguration")
    def reset_destination_encryption_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationEncryptionConfiguration", []))

    @jsii.member(jsii_name="resetEncoding")
    def reset_encoding(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncoding", []))

    @jsii.member(jsii_name="resetFieldDelimiter")
    def reset_field_delimiter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFieldDelimiter", []))

    @jsii.member(jsii_name="resetIgnoreUnknownValues")
    def reset_ignore_unknown_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreUnknownValues", []))

    @jsii.member(jsii_name="resetJsonExtension")
    def reset_json_extension(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJsonExtension", []))

    @jsii.member(jsii_name="resetMaxBadRecords")
    def reset_max_bad_records(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxBadRecords", []))

    @jsii.member(jsii_name="resetNullMarker")
    def reset_null_marker(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetNullMarker", []))

    @jsii.member(jsii_name="resetProjectionFields")
    def reset_projection_fields(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProjectionFields", []))

    @jsii.member(jsii_name="resetQuote")
    def reset_quote(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQuote", []))

    @jsii.member(jsii_name="resetSchemaUpdateOptions")
    def reset_schema_update_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchemaUpdateOptions", []))

    @jsii.member(jsii_name="resetSkipLeadingRows")
    def reset_skip_leading_rows(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSkipLeadingRows", []))

    @jsii.member(jsii_name="resetSourceFormat")
    def reset_source_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceFormat", []))

    @jsii.member(jsii_name="resetTimePartitioning")
    def reset_time_partitioning(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimePartitioning", []))

    @jsii.member(jsii_name="resetWriteDisposition")
    def reset_write_disposition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWriteDisposition", []))

    @builtins.property
    @jsii.member(jsii_name="destinationEncryptionConfiguration")
    def destination_encryption_configuration(
        self,
    ) -> GoogleBigqueryJobLoadDestinationEncryptionConfigurationOutputReference:
        return typing.cast(GoogleBigqueryJobLoadDestinationEncryptionConfigurationOutputReference, jsii.get(self, "destinationEncryptionConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="destinationTable")
    def destination_table(self) -> GoogleBigqueryJobLoadDestinationTableOutputReference:
        return typing.cast(GoogleBigqueryJobLoadDestinationTableOutputReference, jsii.get(self, "destinationTable"))

    @builtins.property
    @jsii.member(jsii_name="timePartitioning")
    def time_partitioning(
        self,
    ) -> "GoogleBigqueryJobLoadTimePartitioningOutputReference":
        return typing.cast("GoogleBigqueryJobLoadTimePartitioningOutputReference", jsii.get(self, "timePartitioning"))

    @builtins.property
    @jsii.member(jsii_name="allowJaggedRowsInput")
    def allow_jagged_rows_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowJaggedRowsInput"))

    @builtins.property
    @jsii.member(jsii_name="allowQuotedNewlinesInput")
    def allow_quoted_newlines_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowQuotedNewlinesInput"))

    @builtins.property
    @jsii.member(jsii_name="autodetectInput")
    def autodetect_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "autodetectInput"))

    @builtins.property
    @jsii.member(jsii_name="createDispositionInput")
    def create_disposition_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createDispositionInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationEncryptionConfigurationInput")
    def destination_encryption_configuration_input(
        self,
    ) -> typing.Optional[GoogleBigqueryJobLoadDestinationEncryptionConfiguration]:
        return typing.cast(typing.Optional[GoogleBigqueryJobLoadDestinationEncryptionConfiguration], jsii.get(self, "destinationEncryptionConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationTableInput")
    def destination_table_input(
        self,
    ) -> typing.Optional[GoogleBigqueryJobLoadDestinationTable]:
        return typing.cast(typing.Optional[GoogleBigqueryJobLoadDestinationTable], jsii.get(self, "destinationTableInput"))

    @builtins.property
    @jsii.member(jsii_name="encodingInput")
    def encoding_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encodingInput"))

    @builtins.property
    @jsii.member(jsii_name="fieldDelimiterInput")
    def field_delimiter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fieldDelimiterInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreUnknownValuesInput")
    def ignore_unknown_values_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ignoreUnknownValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="jsonExtensionInput")
    def json_extension_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jsonExtensionInput"))

    @builtins.property
    @jsii.member(jsii_name="maxBadRecordsInput")
    def max_bad_records_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxBadRecordsInput"))

    @builtins.property
    @jsii.member(jsii_name="nullMarkerInput")
    def null_marker_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "nullMarkerInput"))

    @builtins.property
    @jsii.member(jsii_name="projectionFieldsInput")
    def projection_fields_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "projectionFieldsInput"))

    @builtins.property
    @jsii.member(jsii_name="quoteInput")
    def quote_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "quoteInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaUpdateOptionsInput")
    def schema_update_options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "schemaUpdateOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="skipLeadingRowsInput")
    def skip_leading_rows_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "skipLeadingRowsInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceFormatInput")
    def source_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceUrisInput")
    def source_uris_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourceUrisInput"))

    @builtins.property
    @jsii.member(jsii_name="timePartitioningInput")
    def time_partitioning_input(
        self,
    ) -> typing.Optional["GoogleBigqueryJobLoadTimePartitioning"]:
        return typing.cast(typing.Optional["GoogleBigqueryJobLoadTimePartitioning"], jsii.get(self, "timePartitioningInput"))

    @builtins.property
    @jsii.member(jsii_name="writeDispositionInput")
    def write_disposition_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "writeDispositionInput"))

    @builtins.property
    @jsii.member(jsii_name="allowJaggedRows")
    def allow_jagged_rows(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowJaggedRows"))

    @allow_jagged_rows.setter
    def allow_jagged_rows(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobLoadOutputReference, "allow_jagged_rows").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowJaggedRows", value)

    @builtins.property
    @jsii.member(jsii_name="allowQuotedNewlines")
    def allow_quoted_newlines(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowQuotedNewlines"))

    @allow_quoted_newlines.setter
    def allow_quoted_newlines(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobLoadOutputReference, "allow_quoted_newlines").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowQuotedNewlines", value)

    @builtins.property
    @jsii.member(jsii_name="autodetect")
    def autodetect(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "autodetect"))

    @autodetect.setter
    def autodetect(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobLoadOutputReference, "autodetect").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autodetect", value)

    @builtins.property
    @jsii.member(jsii_name="createDisposition")
    def create_disposition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createDisposition"))

    @create_disposition.setter
    def create_disposition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobLoadOutputReference, "create_disposition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createDisposition", value)

    @builtins.property
    @jsii.member(jsii_name="encoding")
    def encoding(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encoding"))

    @encoding.setter
    def encoding(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobLoadOutputReference, "encoding").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encoding", value)

    @builtins.property
    @jsii.member(jsii_name="fieldDelimiter")
    def field_delimiter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fieldDelimiter"))

    @field_delimiter.setter
    def field_delimiter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobLoadOutputReference, "field_delimiter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fieldDelimiter", value)

    @builtins.property
    @jsii.member(jsii_name="ignoreUnknownValues")
    def ignore_unknown_values(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "ignoreUnknownValues"))

    @ignore_unknown_values.setter
    def ignore_unknown_values(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobLoadOutputReference, "ignore_unknown_values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreUnknownValues", value)

    @builtins.property
    @jsii.member(jsii_name="jsonExtension")
    def json_extension(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jsonExtension"))

    @json_extension.setter
    def json_extension(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobLoadOutputReference, "json_extension").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jsonExtension", value)

    @builtins.property
    @jsii.member(jsii_name="maxBadRecords")
    def max_bad_records(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxBadRecords"))

    @max_bad_records.setter
    def max_bad_records(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobLoadOutputReference, "max_bad_records").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxBadRecords", value)

    @builtins.property
    @jsii.member(jsii_name="nullMarker")
    def null_marker(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "nullMarker"))

    @null_marker.setter
    def null_marker(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobLoadOutputReference, "null_marker").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "nullMarker", value)

    @builtins.property
    @jsii.member(jsii_name="projectionFields")
    def projection_fields(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "projectionFields"))

    @projection_fields.setter
    def projection_fields(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobLoadOutputReference, "projection_fields").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectionFields", value)

    @builtins.property
    @jsii.member(jsii_name="quote")
    def quote(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "quote"))

    @quote.setter
    def quote(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobLoadOutputReference, "quote").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "quote", value)

    @builtins.property
    @jsii.member(jsii_name="schemaUpdateOptions")
    def schema_update_options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "schemaUpdateOptions"))

    @schema_update_options.setter
    def schema_update_options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobLoadOutputReference, "schema_update_options").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schemaUpdateOptions", value)

    @builtins.property
    @jsii.member(jsii_name="skipLeadingRows")
    def skip_leading_rows(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "skipLeadingRows"))

    @skip_leading_rows.setter
    def skip_leading_rows(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobLoadOutputReference, "skip_leading_rows").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skipLeadingRows", value)

    @builtins.property
    @jsii.member(jsii_name="sourceFormat")
    def source_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceFormat"))

    @source_format.setter
    def source_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobLoadOutputReference, "source_format").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceFormat", value)

    @builtins.property
    @jsii.member(jsii_name="sourceUris")
    def source_uris(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sourceUris"))

    @source_uris.setter
    def source_uris(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobLoadOutputReference, "source_uris").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceUris", value)

    @builtins.property
    @jsii.member(jsii_name="writeDisposition")
    def write_disposition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "writeDisposition"))

    @write_disposition.setter
    def write_disposition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobLoadOutputReference, "write_disposition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "writeDisposition", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleBigqueryJobLoad]:
        return typing.cast(typing.Optional[GoogleBigqueryJobLoad], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[GoogleBigqueryJobLoad]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobLoadOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryJob.GoogleBigqueryJobLoadTimePartitioning",
    jsii_struct_bases=[],
    name_mapping={"type": "type", "expiration_ms": "expirationMs", "field": "field"},
)
class GoogleBigqueryJobLoadTimePartitioning:
    def __init__(
        self,
        *,
        type: builtins.str,
        expiration_ms: typing.Optional[builtins.str] = None,
        field: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param type: The only type supported is DAY, which will generate one partition per day. Providing an empty string used to cause an error, but in OnePlatform the field will be treated as unset. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#type GoogleBigqueryJob#type}
        :param expiration_ms: Number of milliseconds for which to keep the storage for a partition. A wrapper is used here because 0 is an invalid value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#expiration_ms GoogleBigqueryJob#expiration_ms}
        :param field: If not set, the table is partitioned by pseudo column '_PARTITIONTIME'; if set, the table is partitioned by this field. The field must be a top-level TIMESTAMP or DATE field. Its mode must be NULLABLE or REQUIRED. A wrapper is used here because an empty string is an invalid value. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#field GoogleBigqueryJob#field}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobLoadTimePartitioning.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument expiration_ms", value=expiration_ms, expected_type=type_hints["expiration_ms"])
            check_type(argname="argument field", value=field, expected_type=type_hints["field"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if expiration_ms is not None:
            self._values["expiration_ms"] = expiration_ms
        if field is not None:
            self._values["field"] = field

    @builtins.property
    def type(self) -> builtins.str:
        '''The only type supported is DAY, which will generate one partition per day.

        Providing an empty string used to cause an error,
        but in OnePlatform the field will be treated as unset.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#type GoogleBigqueryJob#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def expiration_ms(self) -> typing.Optional[builtins.str]:
        '''Number of milliseconds for which to keep the storage for a partition.

        A wrapper is used here because 0 is an invalid value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#expiration_ms GoogleBigqueryJob#expiration_ms}
        '''
        result = self._values.get("expiration_ms")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def field(self) -> typing.Optional[builtins.str]:
        '''If not set, the table is partitioned by pseudo column '_PARTITIONTIME';

        if set, the table is partitioned by this field.
        The field must be a top-level TIMESTAMP or DATE field. Its mode must be NULLABLE or REQUIRED.
        A wrapper is used here because an empty string is an invalid value.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#field GoogleBigqueryJob#field}
        '''
        result = self._values.get("field")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryJobLoadTimePartitioning(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryJobLoadTimePartitioningOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryJob.GoogleBigqueryJobLoadTimePartitioningOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobLoadTimePartitioningOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetExpirationMs")
    def reset_expiration_ms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpirationMs", []))

    @jsii.member(jsii_name="resetField")
    def reset_field(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetField", []))

    @builtins.property
    @jsii.member(jsii_name="expirationMsInput")
    def expiration_ms_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "expirationMsInput"))

    @builtins.property
    @jsii.member(jsii_name="fieldInput")
    def field_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fieldInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="expirationMs")
    def expiration_ms(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "expirationMs"))

    @expiration_ms.setter
    def expiration_ms(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobLoadTimePartitioningOutputReference, "expiration_ms").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expirationMs", value)

    @builtins.property
    @jsii.member(jsii_name="field")
    def field(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "field"))

    @field.setter
    def field(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobLoadTimePartitioningOutputReference, "field").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "field", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobLoadTimePartitioningOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleBigqueryJobLoadTimePartitioning]:
        return typing.cast(typing.Optional[GoogleBigqueryJobLoadTimePartitioning], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryJobLoadTimePartitioning],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobLoadTimePartitioningOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryJob.GoogleBigqueryJobQuery",
    jsii_struct_bases=[],
    name_mapping={
        "query": "query",
        "allow_large_results": "allowLargeResults",
        "create_disposition": "createDisposition",
        "default_dataset": "defaultDataset",
        "destination_encryption_configuration": "destinationEncryptionConfiguration",
        "destination_table": "destinationTable",
        "flatten_results": "flattenResults",
        "maximum_billing_tier": "maximumBillingTier",
        "maximum_bytes_billed": "maximumBytesBilled",
        "parameter_mode": "parameterMode",
        "priority": "priority",
        "schema_update_options": "schemaUpdateOptions",
        "script_options": "scriptOptions",
        "use_legacy_sql": "useLegacySql",
        "use_query_cache": "useQueryCache",
        "user_defined_function_resources": "userDefinedFunctionResources",
        "write_disposition": "writeDisposition",
    },
)
class GoogleBigqueryJobQuery:
    def __init__(
        self,
        *,
        query: builtins.str,
        allow_large_results: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        create_disposition: typing.Optional[builtins.str] = None,
        default_dataset: typing.Optional[typing.Union["GoogleBigqueryJobQueryDefaultDataset", typing.Dict[str, typing.Any]]] = None,
        destination_encryption_configuration: typing.Optional[typing.Union["GoogleBigqueryJobQueryDestinationEncryptionConfiguration", typing.Dict[str, typing.Any]]] = None,
        destination_table: typing.Optional[typing.Union["GoogleBigqueryJobQueryDestinationTable", typing.Dict[str, typing.Any]]] = None,
        flatten_results: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        maximum_billing_tier: typing.Optional[jsii.Number] = None,
        maximum_bytes_billed: typing.Optional[builtins.str] = None,
        parameter_mode: typing.Optional[builtins.str] = None,
        priority: typing.Optional[builtins.str] = None,
        schema_update_options: typing.Optional[typing.Sequence[builtins.str]] = None,
        script_options: typing.Optional[typing.Union["GoogleBigqueryJobQueryScriptOptions", typing.Dict[str, typing.Any]]] = None,
        use_legacy_sql: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        use_query_cache: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        user_defined_function_resources: typing.Optional[typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleBigqueryJobQueryUserDefinedFunctionResources", typing.Dict[str, typing.Any]]]]] = None,
        write_disposition: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param query: SQL query text to execute. The useLegacySql field can be used to indicate whether the query uses legacy SQL or standard SQL. NOTE*: queries containing `DML language <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-manipulation-language>`_ ('DELETE', 'UPDATE', 'MERGE', 'INSERT') must specify 'create_disposition = ""' and 'write_disposition = ""'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#query GoogleBigqueryJob#query}
        :param allow_large_results: If true and query uses legacy SQL dialect, allows the query to produce arbitrarily large result tables at a slight cost in performance. Requires destinationTable to be set. For standard SQL queries, this flag is ignored and large results are always allowed. However, you must still set destinationTable when result size exceeds the allowed maximum response size. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#allow_large_results GoogleBigqueryJob#allow_large_results}
        :param create_disposition: Specifies whether the job is allowed to create new tables. The following values are supported: CREATE_IF_NEEDED: If the table does not exist, BigQuery creates the table. CREATE_NEVER: The table must already exist. If it does not, a 'notFound' error is returned in the job result. Creation, truncation and append actions occur as one atomic update upon job completion Default value: "CREATE_IF_NEEDED" Possible values: ["CREATE_IF_NEEDED", "CREATE_NEVER"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#create_disposition GoogleBigqueryJob#create_disposition}
        :param default_dataset: default_dataset block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#default_dataset GoogleBigqueryJob#default_dataset}
        :param destination_encryption_configuration: destination_encryption_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#destination_encryption_configuration GoogleBigqueryJob#destination_encryption_configuration}
        :param destination_table: destination_table block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#destination_table GoogleBigqueryJob#destination_table}
        :param flatten_results: If true and query uses legacy SQL dialect, flattens all nested and repeated fields in the query results. allowLargeResults must be true if this is set to false. For standard SQL queries, this flag is ignored and results are never flattened. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#flatten_results GoogleBigqueryJob#flatten_results}
        :param maximum_billing_tier: Limits the billing tier for this job. Queries that have resource usage beyond this tier will fail (without incurring a charge). If unspecified, this will be set to your project default. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#maximum_billing_tier GoogleBigqueryJob#maximum_billing_tier}
        :param maximum_bytes_billed: Limits the bytes billed for this job. Queries that will have bytes billed beyond this limit will fail (without incurring a charge). If unspecified, this will be set to your project default. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#maximum_bytes_billed GoogleBigqueryJob#maximum_bytes_billed}
        :param parameter_mode: Standard SQL only. Set to POSITIONAL to use positional (?) query parameters or to NAMED to use named (@myparam) query parameters in this query. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#parameter_mode GoogleBigqueryJob#parameter_mode}
        :param priority: Specifies a priority for the query. Default value: "INTERACTIVE" Possible values: ["INTERACTIVE", "BATCH"]. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#priority GoogleBigqueryJob#priority}
        :param schema_update_options: Allows the schema of the destination table to be updated as a side effect of the query job. Schema update options are supported in two cases: when writeDisposition is WRITE_APPEND; when writeDisposition is WRITE_TRUNCATE and the destination table is a partition of a table, specified by partition decorators. For normal tables, WRITE_TRUNCATE will always overwrite the schema. One or more of the following values are specified: ALLOW_FIELD_ADDITION: allow adding a nullable field to the schema. ALLOW_FIELD_RELAXATION: allow relaxing a required field in the original schema to nullable. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#schema_update_options GoogleBigqueryJob#schema_update_options}
        :param script_options: script_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#script_options GoogleBigqueryJob#script_options}
        :param use_legacy_sql: Specifies whether to use BigQuery's legacy SQL dialect for this query. The default value is true. If set to false, the query will use BigQuery's standard SQL. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#use_legacy_sql GoogleBigqueryJob#use_legacy_sql}
        :param use_query_cache: Whether to look for the result in the query cache. The query cache is a best-effort cache that will be flushed whenever tables in the query are modified. Moreover, the query cache is only available when a query does not have a destination table specified. The default value is true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#use_query_cache GoogleBigqueryJob#use_query_cache}
        :param user_defined_function_resources: user_defined_function_resources block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#user_defined_function_resources GoogleBigqueryJob#user_defined_function_resources}
        :param write_disposition: Specifies the action that occurs if the destination table already exists. The following values are supported: WRITE_TRUNCATE: If the table already exists, BigQuery overwrites the table data and uses the schema from the query result. WRITE_APPEND: If the table already exists, BigQuery appends the data to the table. WRITE_EMPTY: If the table already exists and contains data, a 'duplicate' error is returned in the job result. Each action is atomic and only occurs if BigQuery is able to complete the job successfully. Creation, truncation and append actions occur as one atomic update upon job completion. Default value: "WRITE_EMPTY" Possible values: ["WRITE_TRUNCATE", "WRITE_APPEND", "WRITE_EMPTY"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#write_disposition GoogleBigqueryJob#write_disposition}
        '''
        if isinstance(default_dataset, dict):
            default_dataset = GoogleBigqueryJobQueryDefaultDataset(**default_dataset)
        if isinstance(destination_encryption_configuration, dict):
            destination_encryption_configuration = GoogleBigqueryJobQueryDestinationEncryptionConfiguration(**destination_encryption_configuration)
        if isinstance(destination_table, dict):
            destination_table = GoogleBigqueryJobQueryDestinationTable(**destination_table)
        if isinstance(script_options, dict):
            script_options = GoogleBigqueryJobQueryScriptOptions(**script_options)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobQuery.__init__)
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
            check_type(argname="argument allow_large_results", value=allow_large_results, expected_type=type_hints["allow_large_results"])
            check_type(argname="argument create_disposition", value=create_disposition, expected_type=type_hints["create_disposition"])
            check_type(argname="argument default_dataset", value=default_dataset, expected_type=type_hints["default_dataset"])
            check_type(argname="argument destination_encryption_configuration", value=destination_encryption_configuration, expected_type=type_hints["destination_encryption_configuration"])
            check_type(argname="argument destination_table", value=destination_table, expected_type=type_hints["destination_table"])
            check_type(argname="argument flatten_results", value=flatten_results, expected_type=type_hints["flatten_results"])
            check_type(argname="argument maximum_billing_tier", value=maximum_billing_tier, expected_type=type_hints["maximum_billing_tier"])
            check_type(argname="argument maximum_bytes_billed", value=maximum_bytes_billed, expected_type=type_hints["maximum_bytes_billed"])
            check_type(argname="argument parameter_mode", value=parameter_mode, expected_type=type_hints["parameter_mode"])
            check_type(argname="argument priority", value=priority, expected_type=type_hints["priority"])
            check_type(argname="argument schema_update_options", value=schema_update_options, expected_type=type_hints["schema_update_options"])
            check_type(argname="argument script_options", value=script_options, expected_type=type_hints["script_options"])
            check_type(argname="argument use_legacy_sql", value=use_legacy_sql, expected_type=type_hints["use_legacy_sql"])
            check_type(argname="argument use_query_cache", value=use_query_cache, expected_type=type_hints["use_query_cache"])
            check_type(argname="argument user_defined_function_resources", value=user_defined_function_resources, expected_type=type_hints["user_defined_function_resources"])
            check_type(argname="argument write_disposition", value=write_disposition, expected_type=type_hints["write_disposition"])
        self._values: typing.Dict[str, typing.Any] = {
            "query": query,
        }
        if allow_large_results is not None:
            self._values["allow_large_results"] = allow_large_results
        if create_disposition is not None:
            self._values["create_disposition"] = create_disposition
        if default_dataset is not None:
            self._values["default_dataset"] = default_dataset
        if destination_encryption_configuration is not None:
            self._values["destination_encryption_configuration"] = destination_encryption_configuration
        if destination_table is not None:
            self._values["destination_table"] = destination_table
        if flatten_results is not None:
            self._values["flatten_results"] = flatten_results
        if maximum_billing_tier is not None:
            self._values["maximum_billing_tier"] = maximum_billing_tier
        if maximum_bytes_billed is not None:
            self._values["maximum_bytes_billed"] = maximum_bytes_billed
        if parameter_mode is not None:
            self._values["parameter_mode"] = parameter_mode
        if priority is not None:
            self._values["priority"] = priority
        if schema_update_options is not None:
            self._values["schema_update_options"] = schema_update_options
        if script_options is not None:
            self._values["script_options"] = script_options
        if use_legacy_sql is not None:
            self._values["use_legacy_sql"] = use_legacy_sql
        if use_query_cache is not None:
            self._values["use_query_cache"] = use_query_cache
        if user_defined_function_resources is not None:
            self._values["user_defined_function_resources"] = user_defined_function_resources
        if write_disposition is not None:
            self._values["write_disposition"] = write_disposition

    @builtins.property
    def query(self) -> builtins.str:
        '''SQL query text to execute.

        The useLegacySql field can be used to indicate whether the query uses legacy SQL or standard SQL.
        NOTE*: queries containing `DML language <https://cloud.google.com/bigquery/docs/reference/standard-sql/data-manipulation-language>`_
        ('DELETE', 'UPDATE', 'MERGE', 'INSERT') must specify 'create_disposition = ""' and 'write_disposition = ""'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#query GoogleBigqueryJob#query}
        '''
        result = self._values.get("query")
        assert result is not None, "Required property 'query' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allow_large_results(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true and query uses legacy SQL dialect, allows the query to produce arbitrarily large result tables at a slight cost in performance.

        Requires destinationTable to be set. For standard SQL queries, this flag is ignored and large results are always allowed.
        However, you must still set destinationTable when result size exceeds the allowed maximum response size.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#allow_large_results GoogleBigqueryJob#allow_large_results}
        '''
        result = self._values.get("allow_large_results")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def create_disposition(self) -> typing.Optional[builtins.str]:
        '''Specifies whether the job is allowed to create new tables.

        The following values are supported:
        CREATE_IF_NEEDED: If the table does not exist, BigQuery creates the table.
        CREATE_NEVER: The table must already exist. If it does not, a 'notFound' error is returned in the job result.
        Creation, truncation and append actions occur as one atomic update upon job completion Default value: "CREATE_IF_NEEDED" Possible values: ["CREATE_IF_NEEDED", "CREATE_NEVER"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#create_disposition GoogleBigqueryJob#create_disposition}
        '''
        result = self._values.get("create_disposition")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def default_dataset(
        self,
    ) -> typing.Optional["GoogleBigqueryJobQueryDefaultDataset"]:
        '''default_dataset block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#default_dataset GoogleBigqueryJob#default_dataset}
        '''
        result = self._values.get("default_dataset")
        return typing.cast(typing.Optional["GoogleBigqueryJobQueryDefaultDataset"], result)

    @builtins.property
    def destination_encryption_configuration(
        self,
    ) -> typing.Optional["GoogleBigqueryJobQueryDestinationEncryptionConfiguration"]:
        '''destination_encryption_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#destination_encryption_configuration GoogleBigqueryJob#destination_encryption_configuration}
        '''
        result = self._values.get("destination_encryption_configuration")
        return typing.cast(typing.Optional["GoogleBigqueryJobQueryDestinationEncryptionConfiguration"], result)

    @builtins.property
    def destination_table(
        self,
    ) -> typing.Optional["GoogleBigqueryJobQueryDestinationTable"]:
        '''destination_table block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#destination_table GoogleBigqueryJob#destination_table}
        '''
        result = self._values.get("destination_table")
        return typing.cast(typing.Optional["GoogleBigqueryJobQueryDestinationTable"], result)

    @builtins.property
    def flatten_results(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If true and query uses legacy SQL dialect, flattens all nested and repeated fields in the query results.

        allowLargeResults must be true if this is set to false. For standard SQL queries, this flag is ignored and results are never flattened.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#flatten_results GoogleBigqueryJob#flatten_results}
        '''
        result = self._values.get("flatten_results")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def maximum_billing_tier(self) -> typing.Optional[jsii.Number]:
        '''Limits the billing tier for this job.

        Queries that have resource usage beyond this tier will fail (without incurring a charge).
        If unspecified, this will be set to your project default.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#maximum_billing_tier GoogleBigqueryJob#maximum_billing_tier}
        '''
        result = self._values.get("maximum_billing_tier")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def maximum_bytes_billed(self) -> typing.Optional[builtins.str]:
        '''Limits the bytes billed for this job.

        Queries that will have bytes billed beyond this limit will fail (without incurring a charge).
        If unspecified, this will be set to your project default.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#maximum_bytes_billed GoogleBigqueryJob#maximum_bytes_billed}
        '''
        result = self._values.get("maximum_bytes_billed")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def parameter_mode(self) -> typing.Optional[builtins.str]:
        '''Standard SQL only.

        Set to POSITIONAL to use positional (?) query parameters or to NAMED to use named (@myparam) query parameters in this query.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#parameter_mode GoogleBigqueryJob#parameter_mode}
        '''
        result = self._values.get("parameter_mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def priority(self) -> typing.Optional[builtins.str]:
        '''Specifies a priority for the query. Default value: "INTERACTIVE" Possible values: ["INTERACTIVE", "BATCH"].

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#priority GoogleBigqueryJob#priority}
        '''
        result = self._values.get("priority")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def schema_update_options(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Allows the schema of the destination table to be updated as a side effect of the query job.

        Schema update options are supported in two cases: when writeDisposition is WRITE_APPEND;
        when writeDisposition is WRITE_TRUNCATE and the destination table is a partition of a table,
        specified by partition decorators. For normal tables, WRITE_TRUNCATE will always overwrite the schema.
        One or more of the following values are specified:
        ALLOW_FIELD_ADDITION: allow adding a nullable field to the schema.
        ALLOW_FIELD_RELAXATION: allow relaxing a required field in the original schema to nullable.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#schema_update_options GoogleBigqueryJob#schema_update_options}
        '''
        result = self._values.get("schema_update_options")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def script_options(self) -> typing.Optional["GoogleBigqueryJobQueryScriptOptions"]:
        '''script_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#script_options GoogleBigqueryJob#script_options}
        '''
        result = self._values.get("script_options")
        return typing.cast(typing.Optional["GoogleBigqueryJobQueryScriptOptions"], result)

    @builtins.property
    def use_legacy_sql(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specifies whether to use BigQuery's legacy SQL dialect for this query.

        The default value is true.
        If set to false, the query will use BigQuery's standard SQL.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#use_legacy_sql GoogleBigqueryJob#use_legacy_sql}
        '''
        result = self._values.get("use_legacy_sql")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def use_query_cache(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to look for the result in the query cache.

        The query cache is a best-effort cache that will be flushed whenever
        tables in the query are modified. Moreover, the query cache is only available when a query does not have a destination table specified.
        The default value is true.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#use_query_cache GoogleBigqueryJob#use_query_cache}
        '''
        result = self._values.get("use_query_cache")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def user_defined_function_resources(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleBigqueryJobQueryUserDefinedFunctionResources"]]]:
        '''user_defined_function_resources block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#user_defined_function_resources GoogleBigqueryJob#user_defined_function_resources}
        '''
        result = self._values.get("user_defined_function_resources")
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleBigqueryJobQueryUserDefinedFunctionResources"]]], result)

    @builtins.property
    def write_disposition(self) -> typing.Optional[builtins.str]:
        '''Specifies the action that occurs if the destination table already exists.

        The following values are supported:
        WRITE_TRUNCATE: If the table already exists, BigQuery overwrites the table data and uses the schema from the query result.
        WRITE_APPEND: If the table already exists, BigQuery appends the data to the table.
        WRITE_EMPTY: If the table already exists and contains data, a 'duplicate' error is returned in the job result.
        Each action is atomic and only occurs if BigQuery is able to complete the job successfully.
        Creation, truncation and append actions occur as one atomic update upon job completion. Default value: "WRITE_EMPTY" Possible values: ["WRITE_TRUNCATE", "WRITE_APPEND", "WRITE_EMPTY"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#write_disposition GoogleBigqueryJob#write_disposition}
        '''
        result = self._values.get("write_disposition")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryJobQuery(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryJob.GoogleBigqueryJobQueryDefaultDataset",
    jsii_struct_bases=[],
    name_mapping={"dataset_id": "datasetId", "project_id": "projectId"},
)
class GoogleBigqueryJobQueryDefaultDataset:
    def __init__(
        self,
        *,
        dataset_id: builtins.str,
        project_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param dataset_id: The dataset. Can be specified '{{dataset_id}}' if 'project_id' is also set, or of the form 'projects/{{project}}/datasets/{{dataset_id}}' if not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#dataset_id GoogleBigqueryJob#dataset_id}
        :param project_id: The ID of the project containing this table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#project_id GoogleBigqueryJob#project_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobQueryDefaultDataset.__init__)
            check_type(argname="argument dataset_id", value=dataset_id, expected_type=type_hints["dataset_id"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "dataset_id": dataset_id,
        }
        if project_id is not None:
            self._values["project_id"] = project_id

    @builtins.property
    def dataset_id(self) -> builtins.str:
        '''The dataset. Can be specified '{{dataset_id}}' if 'project_id' is also set, or of the form 'projects/{{project}}/datasets/{{dataset_id}}' if not.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#dataset_id GoogleBigqueryJob#dataset_id}
        '''
        result = self._values.get("dataset_id")
        assert result is not None, "Required property 'dataset_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def project_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the project containing this table.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#project_id GoogleBigqueryJob#project_id}
        '''
        result = self._values.get("project_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryJobQueryDefaultDataset(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryJobQueryDefaultDatasetOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryJob.GoogleBigqueryJobQueryDefaultDatasetOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobQueryDefaultDatasetOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetProjectId")
    def reset_project_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProjectId", []))

    @builtins.property
    @jsii.member(jsii_name="datasetIdInput")
    def dataset_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datasetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="projectIdInput")
    def project_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="datasetId")
    def dataset_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datasetId"))

    @dataset_id.setter
    def dataset_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobQueryDefaultDatasetOutputReference, "dataset_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetId", value)

    @builtins.property
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectId"))

    @project_id.setter
    def project_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobQueryDefaultDatasetOutputReference, "project_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleBigqueryJobQueryDefaultDataset]:
        return typing.cast(typing.Optional[GoogleBigqueryJobQueryDefaultDataset], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryJobQueryDefaultDataset],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobQueryDefaultDatasetOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryJob.GoogleBigqueryJobQueryDestinationEncryptionConfiguration",
    jsii_struct_bases=[],
    name_mapping={"kms_key_name": "kmsKeyName"},
)
class GoogleBigqueryJobQueryDestinationEncryptionConfiguration:
    def __init__(self, *, kms_key_name: builtins.str) -> None:
        '''
        :param kms_key_name: Describes the Cloud KMS encryption key that will be used to protect destination BigQuery table. The BigQuery Service Account associated with your project requires access to this encryption key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#kms_key_name GoogleBigqueryJob#kms_key_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobQueryDestinationEncryptionConfiguration.__init__)
            check_type(argname="argument kms_key_name", value=kms_key_name, expected_type=type_hints["kms_key_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "kms_key_name": kms_key_name,
        }

    @builtins.property
    def kms_key_name(self) -> builtins.str:
        '''Describes the Cloud KMS encryption key that will be used to protect destination BigQuery table.

        The BigQuery Service Account associated with your project requires access to this encryption key.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#kms_key_name GoogleBigqueryJob#kms_key_name}
        '''
        result = self._values.get("kms_key_name")
        assert result is not None, "Required property 'kms_key_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryJobQueryDestinationEncryptionConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryJobQueryDestinationEncryptionConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryJob.GoogleBigqueryJobQueryDestinationEncryptionConfigurationOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobQueryDestinationEncryptionConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="kmsKeyVersion")
    def kms_key_version(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyVersion"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyNameInput")
    def kms_key_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "kmsKeyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="kmsKeyName")
    def kms_key_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "kmsKeyName"))

    @kms_key_name.setter
    def kms_key_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobQueryDestinationEncryptionConfigurationOutputReference, "kms_key_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleBigqueryJobQueryDestinationEncryptionConfiguration]:
        return typing.cast(typing.Optional[GoogleBigqueryJobQueryDestinationEncryptionConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryJobQueryDestinationEncryptionConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobQueryDestinationEncryptionConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryJob.GoogleBigqueryJobQueryDestinationTable",
    jsii_struct_bases=[],
    name_mapping={
        "table_id": "tableId",
        "dataset_id": "datasetId",
        "project_id": "projectId",
    },
)
class GoogleBigqueryJobQueryDestinationTable:
    def __init__(
        self,
        *,
        table_id: builtins.str,
        dataset_id: typing.Optional[builtins.str] = None,
        project_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param table_id: The table. Can be specified '{{table_id}}' if 'project_id' and 'dataset_id' are also set, or of the form 'projects/{{project}}/datasets/{{dataset_id}}/tables/{{table_id}}' if not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#table_id GoogleBigqueryJob#table_id}
        :param dataset_id: The ID of the dataset containing this table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#dataset_id GoogleBigqueryJob#dataset_id}
        :param project_id: The ID of the project containing this table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#project_id GoogleBigqueryJob#project_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobQueryDestinationTable.__init__)
            check_type(argname="argument table_id", value=table_id, expected_type=type_hints["table_id"])
            check_type(argname="argument dataset_id", value=dataset_id, expected_type=type_hints["dataset_id"])
            check_type(argname="argument project_id", value=project_id, expected_type=type_hints["project_id"])
        self._values: typing.Dict[str, typing.Any] = {
            "table_id": table_id,
        }
        if dataset_id is not None:
            self._values["dataset_id"] = dataset_id
        if project_id is not None:
            self._values["project_id"] = project_id

    @builtins.property
    def table_id(self) -> builtins.str:
        '''The table. Can be specified '{{table_id}}' if 'project_id' and 'dataset_id' are also set, or of the form 'projects/{{project}}/datasets/{{dataset_id}}/tables/{{table_id}}' if not.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#table_id GoogleBigqueryJob#table_id}
        '''
        result = self._values.get("table_id")
        assert result is not None, "Required property 'table_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def dataset_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the dataset containing this table.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#dataset_id GoogleBigqueryJob#dataset_id}
        '''
        result = self._values.get("dataset_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def project_id(self) -> typing.Optional[builtins.str]:
        '''The ID of the project containing this table.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#project_id GoogleBigqueryJob#project_id}
        '''
        result = self._values.get("project_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryJobQueryDestinationTable(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryJobQueryDestinationTableOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryJob.GoogleBigqueryJobQueryDestinationTableOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobQueryDestinationTableOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetDatasetId")
    def reset_dataset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDatasetId", []))

    @jsii.member(jsii_name="resetProjectId")
    def reset_project_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProjectId", []))

    @builtins.property
    @jsii.member(jsii_name="datasetIdInput")
    def dataset_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datasetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="projectIdInput")
    def project_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectIdInput"))

    @builtins.property
    @jsii.member(jsii_name="tableIdInput")
    def table_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableIdInput"))

    @builtins.property
    @jsii.member(jsii_name="datasetId")
    def dataset_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datasetId"))

    @dataset_id.setter
    def dataset_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobQueryDestinationTableOutputReference, "dataset_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetId", value)

    @builtins.property
    @jsii.member(jsii_name="projectId")
    def project_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "projectId"))

    @project_id.setter
    def project_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobQueryDestinationTableOutputReference, "project_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "projectId", value)

    @builtins.property
    @jsii.member(jsii_name="tableId")
    def table_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tableId"))

    @table_id.setter
    def table_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobQueryDestinationTableOutputReference, "table_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleBigqueryJobQueryDestinationTable]:
        return typing.cast(typing.Optional[GoogleBigqueryJobQueryDestinationTable], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryJobQueryDestinationTable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobQueryDestinationTableOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleBigqueryJobQueryOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryJob.GoogleBigqueryJobQueryOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobQueryOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putDefaultDataset")
    def put_default_dataset(
        self,
        *,
        dataset_id: builtins.str,
        project_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param dataset_id: The dataset. Can be specified '{{dataset_id}}' if 'project_id' is also set, or of the form 'projects/{{project}}/datasets/{{dataset_id}}' if not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#dataset_id GoogleBigqueryJob#dataset_id}
        :param project_id: The ID of the project containing this table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#project_id GoogleBigqueryJob#project_id}
        '''
        value = GoogleBigqueryJobQueryDefaultDataset(
            dataset_id=dataset_id, project_id=project_id
        )

        return typing.cast(None, jsii.invoke(self, "putDefaultDataset", [value]))

    @jsii.member(jsii_name="putDestinationEncryptionConfiguration")
    def put_destination_encryption_configuration(
        self,
        *,
        kms_key_name: builtins.str,
    ) -> None:
        '''
        :param kms_key_name: Describes the Cloud KMS encryption key that will be used to protect destination BigQuery table. The BigQuery Service Account associated with your project requires access to this encryption key. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#kms_key_name GoogleBigqueryJob#kms_key_name}
        '''
        value = GoogleBigqueryJobQueryDestinationEncryptionConfiguration(
            kms_key_name=kms_key_name
        )

        return typing.cast(None, jsii.invoke(self, "putDestinationEncryptionConfiguration", [value]))

    @jsii.member(jsii_name="putDestinationTable")
    def put_destination_table(
        self,
        *,
        table_id: builtins.str,
        dataset_id: typing.Optional[builtins.str] = None,
        project_id: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param table_id: The table. Can be specified '{{table_id}}' if 'project_id' and 'dataset_id' are also set, or of the form 'projects/{{project}}/datasets/{{dataset_id}}/tables/{{table_id}}' if not. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#table_id GoogleBigqueryJob#table_id}
        :param dataset_id: The ID of the dataset containing this table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#dataset_id GoogleBigqueryJob#dataset_id}
        :param project_id: The ID of the project containing this table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#project_id GoogleBigqueryJob#project_id}
        '''
        value = GoogleBigqueryJobQueryDestinationTable(
            table_id=table_id, dataset_id=dataset_id, project_id=project_id
        )

        return typing.cast(None, jsii.invoke(self, "putDestinationTable", [value]))

    @jsii.member(jsii_name="putScriptOptions")
    def put_script_options(
        self,
        *,
        key_result_statement: typing.Optional[builtins.str] = None,
        statement_byte_budget: typing.Optional[builtins.str] = None,
        statement_timeout_ms: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key_result_statement: Determines which statement in the script represents the "key result", used to populate the schema and query results of the script job. Possible values: ["LAST", "FIRST_SELECT"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#key_result_statement GoogleBigqueryJob#key_result_statement}
        :param statement_byte_budget: Limit on the number of bytes billed per statement. Exceeding this budget results in an error. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#statement_byte_budget GoogleBigqueryJob#statement_byte_budget}
        :param statement_timeout_ms: Timeout period for each statement in a script. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#statement_timeout_ms GoogleBigqueryJob#statement_timeout_ms}
        '''
        value = GoogleBigqueryJobQueryScriptOptions(
            key_result_statement=key_result_statement,
            statement_byte_budget=statement_byte_budget,
            statement_timeout_ms=statement_timeout_ms,
        )

        return typing.cast(None, jsii.invoke(self, "putScriptOptions", [value]))

    @jsii.member(jsii_name="putUserDefinedFunctionResources")
    def put_user_defined_function_resources(
        self,
        value: typing.Union[cdktf.IResolvable, typing.Sequence[typing.Union["GoogleBigqueryJobQueryUserDefinedFunctionResources", typing.Dict[str, typing.Any]]]],
    ) -> None:
        '''
        :param value: -
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobQueryOutputReference.put_user_defined_function_resources)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        return typing.cast(None, jsii.invoke(self, "putUserDefinedFunctionResources", [value]))

    @jsii.member(jsii_name="resetAllowLargeResults")
    def reset_allow_large_results(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowLargeResults", []))

    @jsii.member(jsii_name="resetCreateDisposition")
    def reset_create_disposition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreateDisposition", []))

    @jsii.member(jsii_name="resetDefaultDataset")
    def reset_default_dataset(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDefaultDataset", []))

    @jsii.member(jsii_name="resetDestinationEncryptionConfiguration")
    def reset_destination_encryption_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationEncryptionConfiguration", []))

    @jsii.member(jsii_name="resetDestinationTable")
    def reset_destination_table(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDestinationTable", []))

    @jsii.member(jsii_name="resetFlattenResults")
    def reset_flatten_results(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFlattenResults", []))

    @jsii.member(jsii_name="resetMaximumBillingTier")
    def reset_maximum_billing_tier(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaximumBillingTier", []))

    @jsii.member(jsii_name="resetMaximumBytesBilled")
    def reset_maximum_bytes_billed(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaximumBytesBilled", []))

    @jsii.member(jsii_name="resetParameterMode")
    def reset_parameter_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetParameterMode", []))

    @jsii.member(jsii_name="resetPriority")
    def reset_priority(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPriority", []))

    @jsii.member(jsii_name="resetSchemaUpdateOptions")
    def reset_schema_update_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchemaUpdateOptions", []))

    @jsii.member(jsii_name="resetScriptOptions")
    def reset_script_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScriptOptions", []))

    @jsii.member(jsii_name="resetUseLegacySql")
    def reset_use_legacy_sql(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseLegacySql", []))

    @jsii.member(jsii_name="resetUseQueryCache")
    def reset_use_query_cache(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseQueryCache", []))

    @jsii.member(jsii_name="resetUserDefinedFunctionResources")
    def reset_user_defined_function_resources(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUserDefinedFunctionResources", []))

    @jsii.member(jsii_name="resetWriteDisposition")
    def reset_write_disposition(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetWriteDisposition", []))

    @builtins.property
    @jsii.member(jsii_name="defaultDataset")
    def default_dataset(self) -> GoogleBigqueryJobQueryDefaultDatasetOutputReference:
        return typing.cast(GoogleBigqueryJobQueryDefaultDatasetOutputReference, jsii.get(self, "defaultDataset"))

    @builtins.property
    @jsii.member(jsii_name="destinationEncryptionConfiguration")
    def destination_encryption_configuration(
        self,
    ) -> GoogleBigqueryJobQueryDestinationEncryptionConfigurationOutputReference:
        return typing.cast(GoogleBigqueryJobQueryDestinationEncryptionConfigurationOutputReference, jsii.get(self, "destinationEncryptionConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="destinationTable")
    def destination_table(
        self,
    ) -> GoogleBigqueryJobQueryDestinationTableOutputReference:
        return typing.cast(GoogleBigqueryJobQueryDestinationTableOutputReference, jsii.get(self, "destinationTable"))

    @builtins.property
    @jsii.member(jsii_name="scriptOptions")
    def script_options(self) -> "GoogleBigqueryJobQueryScriptOptionsOutputReference":
        return typing.cast("GoogleBigqueryJobQueryScriptOptionsOutputReference", jsii.get(self, "scriptOptions"))

    @builtins.property
    @jsii.member(jsii_name="userDefinedFunctionResources")
    def user_defined_function_resources(
        self,
    ) -> "GoogleBigqueryJobQueryUserDefinedFunctionResourcesList":
        return typing.cast("GoogleBigqueryJobQueryUserDefinedFunctionResourcesList", jsii.get(self, "userDefinedFunctionResources"))

    @builtins.property
    @jsii.member(jsii_name="allowLargeResultsInput")
    def allow_large_results_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "allowLargeResultsInput"))

    @builtins.property
    @jsii.member(jsii_name="createDispositionInput")
    def create_disposition_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createDispositionInput"))

    @builtins.property
    @jsii.member(jsii_name="defaultDatasetInput")
    def default_dataset_input(
        self,
    ) -> typing.Optional[GoogleBigqueryJobQueryDefaultDataset]:
        return typing.cast(typing.Optional[GoogleBigqueryJobQueryDefaultDataset], jsii.get(self, "defaultDatasetInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationEncryptionConfigurationInput")
    def destination_encryption_configuration_input(
        self,
    ) -> typing.Optional[GoogleBigqueryJobQueryDestinationEncryptionConfiguration]:
        return typing.cast(typing.Optional[GoogleBigqueryJobQueryDestinationEncryptionConfiguration], jsii.get(self, "destinationEncryptionConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="destinationTableInput")
    def destination_table_input(
        self,
    ) -> typing.Optional[GoogleBigqueryJobQueryDestinationTable]:
        return typing.cast(typing.Optional[GoogleBigqueryJobQueryDestinationTable], jsii.get(self, "destinationTableInput"))

    @builtins.property
    @jsii.member(jsii_name="flattenResultsInput")
    def flatten_results_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "flattenResultsInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumBillingTierInput")
    def maximum_billing_tier_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maximumBillingTierInput"))

    @builtins.property
    @jsii.member(jsii_name="maximumBytesBilledInput")
    def maximum_bytes_billed_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "maximumBytesBilledInput"))

    @builtins.property
    @jsii.member(jsii_name="parameterModeInput")
    def parameter_mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "parameterModeInput"))

    @builtins.property
    @jsii.member(jsii_name="priorityInput")
    def priority_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "priorityInput"))

    @builtins.property
    @jsii.member(jsii_name="queryInput")
    def query_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaUpdateOptionsInput")
    def schema_update_options_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "schemaUpdateOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="scriptOptionsInput")
    def script_options_input(
        self,
    ) -> typing.Optional["GoogleBigqueryJobQueryScriptOptions"]:
        return typing.cast(typing.Optional["GoogleBigqueryJobQueryScriptOptions"], jsii.get(self, "scriptOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="useLegacySqlInput")
    def use_legacy_sql_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "useLegacySqlInput"))

    @builtins.property
    @jsii.member(jsii_name="useQueryCacheInput")
    def use_query_cache_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "useQueryCacheInput"))

    @builtins.property
    @jsii.member(jsii_name="userDefinedFunctionResourcesInput")
    def user_defined_function_resources_input(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleBigqueryJobQueryUserDefinedFunctionResources"]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List["GoogleBigqueryJobQueryUserDefinedFunctionResources"]]], jsii.get(self, "userDefinedFunctionResourcesInput"))

    @builtins.property
    @jsii.member(jsii_name="writeDispositionInput")
    def write_disposition_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "writeDispositionInput"))

    @builtins.property
    @jsii.member(jsii_name="allowLargeResults")
    def allow_large_results(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "allowLargeResults"))

    @allow_large_results.setter
    def allow_large_results(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobQueryOutputReference, "allow_large_results").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowLargeResults", value)

    @builtins.property
    @jsii.member(jsii_name="createDisposition")
    def create_disposition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "createDisposition"))

    @create_disposition.setter
    def create_disposition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobQueryOutputReference, "create_disposition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "createDisposition", value)

    @builtins.property
    @jsii.member(jsii_name="flattenResults")
    def flatten_results(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "flattenResults"))

    @flatten_results.setter
    def flatten_results(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobQueryOutputReference, "flatten_results").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "flattenResults", value)

    @builtins.property
    @jsii.member(jsii_name="maximumBillingTier")
    def maximum_billing_tier(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maximumBillingTier"))

    @maximum_billing_tier.setter
    def maximum_billing_tier(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobQueryOutputReference, "maximum_billing_tier").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumBillingTier", value)

    @builtins.property
    @jsii.member(jsii_name="maximumBytesBilled")
    def maximum_bytes_billed(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "maximumBytesBilled"))

    @maximum_bytes_billed.setter
    def maximum_bytes_billed(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobQueryOutputReference, "maximum_bytes_billed").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maximumBytesBilled", value)

    @builtins.property
    @jsii.member(jsii_name="parameterMode")
    def parameter_mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "parameterMode"))

    @parameter_mode.setter
    def parameter_mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobQueryOutputReference, "parameter_mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "parameterMode", value)

    @builtins.property
    @jsii.member(jsii_name="priority")
    def priority(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "priority"))

    @priority.setter
    def priority(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobQueryOutputReference, "priority").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "priority", value)

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "query"))

    @query.setter
    def query(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobQueryOutputReference, "query").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "query", value)

    @builtins.property
    @jsii.member(jsii_name="schemaUpdateOptions")
    def schema_update_options(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "schemaUpdateOptions"))

    @schema_update_options.setter
    def schema_update_options(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobQueryOutputReference, "schema_update_options").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schemaUpdateOptions", value)

    @builtins.property
    @jsii.member(jsii_name="useLegacySql")
    def use_legacy_sql(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "useLegacySql"))

    @use_legacy_sql.setter
    def use_legacy_sql(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobQueryOutputReference, "use_legacy_sql").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useLegacySql", value)

    @builtins.property
    @jsii.member(jsii_name="useQueryCache")
    def use_query_cache(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "useQueryCache"))

    @use_query_cache.setter
    def use_query_cache(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobQueryOutputReference, "use_query_cache").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useQueryCache", value)

    @builtins.property
    @jsii.member(jsii_name="writeDisposition")
    def write_disposition(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "writeDisposition"))

    @write_disposition.setter
    def write_disposition(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobQueryOutputReference, "write_disposition").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "writeDisposition", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleBigqueryJobQuery]:
        return typing.cast(typing.Optional[GoogleBigqueryJobQuery], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[GoogleBigqueryJobQuery]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobQueryOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryJob.GoogleBigqueryJobQueryScriptOptions",
    jsii_struct_bases=[],
    name_mapping={
        "key_result_statement": "keyResultStatement",
        "statement_byte_budget": "statementByteBudget",
        "statement_timeout_ms": "statementTimeoutMs",
    },
)
class GoogleBigqueryJobQueryScriptOptions:
    def __init__(
        self,
        *,
        key_result_statement: typing.Optional[builtins.str] = None,
        statement_byte_budget: typing.Optional[builtins.str] = None,
        statement_timeout_ms: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param key_result_statement: Determines which statement in the script represents the "key result", used to populate the schema and query results of the script job. Possible values: ["LAST", "FIRST_SELECT"] Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#key_result_statement GoogleBigqueryJob#key_result_statement}
        :param statement_byte_budget: Limit on the number of bytes billed per statement. Exceeding this budget results in an error. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#statement_byte_budget GoogleBigqueryJob#statement_byte_budget}
        :param statement_timeout_ms: Timeout period for each statement in a script. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#statement_timeout_ms GoogleBigqueryJob#statement_timeout_ms}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobQueryScriptOptions.__init__)
            check_type(argname="argument key_result_statement", value=key_result_statement, expected_type=type_hints["key_result_statement"])
            check_type(argname="argument statement_byte_budget", value=statement_byte_budget, expected_type=type_hints["statement_byte_budget"])
            check_type(argname="argument statement_timeout_ms", value=statement_timeout_ms, expected_type=type_hints["statement_timeout_ms"])
        self._values: typing.Dict[str, typing.Any] = {}
        if key_result_statement is not None:
            self._values["key_result_statement"] = key_result_statement
        if statement_byte_budget is not None:
            self._values["statement_byte_budget"] = statement_byte_budget
        if statement_timeout_ms is not None:
            self._values["statement_timeout_ms"] = statement_timeout_ms

    @builtins.property
    def key_result_statement(self) -> typing.Optional[builtins.str]:
        '''Determines which statement in the script represents the "key result", used to populate the schema and query results of the script job.

        Possible values: ["LAST", "FIRST_SELECT"]

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#key_result_statement GoogleBigqueryJob#key_result_statement}
        '''
        result = self._values.get("key_result_statement")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def statement_byte_budget(self) -> typing.Optional[builtins.str]:
        '''Limit on the number of bytes billed per statement. Exceeding this budget results in an error.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#statement_byte_budget GoogleBigqueryJob#statement_byte_budget}
        '''
        result = self._values.get("statement_byte_budget")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def statement_timeout_ms(self) -> typing.Optional[builtins.str]:
        '''Timeout period for each statement in a script.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#statement_timeout_ms GoogleBigqueryJob#statement_timeout_ms}
        '''
        result = self._values.get("statement_timeout_ms")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryJobQueryScriptOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryJobQueryScriptOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryJob.GoogleBigqueryJobQueryScriptOptionsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobQueryScriptOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetKeyResultStatement")
    def reset_key_result_statement(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetKeyResultStatement", []))

    @jsii.member(jsii_name="resetStatementByteBudget")
    def reset_statement_byte_budget(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatementByteBudget", []))

    @jsii.member(jsii_name="resetStatementTimeoutMs")
    def reset_statement_timeout_ms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetStatementTimeoutMs", []))

    @builtins.property
    @jsii.member(jsii_name="keyResultStatementInput")
    def key_result_statement_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "keyResultStatementInput"))

    @builtins.property
    @jsii.member(jsii_name="statementByteBudgetInput")
    def statement_byte_budget_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statementByteBudgetInput"))

    @builtins.property
    @jsii.member(jsii_name="statementTimeoutMsInput")
    def statement_timeout_ms_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "statementTimeoutMsInput"))

    @builtins.property
    @jsii.member(jsii_name="keyResultStatement")
    def key_result_statement(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "keyResultStatement"))

    @key_result_statement.setter
    def key_result_statement(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobQueryScriptOptionsOutputReference, "key_result_statement").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "keyResultStatement", value)

    @builtins.property
    @jsii.member(jsii_name="statementByteBudget")
    def statement_byte_budget(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "statementByteBudget"))

    @statement_byte_budget.setter
    def statement_byte_budget(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobQueryScriptOptionsOutputReference, "statement_byte_budget").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statementByteBudget", value)

    @builtins.property
    @jsii.member(jsii_name="statementTimeoutMs")
    def statement_timeout_ms(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "statementTimeoutMs"))

    @statement_timeout_ms.setter
    def statement_timeout_ms(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobQueryScriptOptionsOutputReference, "statement_timeout_ms").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "statementTimeoutMs", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleBigqueryJobQueryScriptOptions]:
        return typing.cast(typing.Optional[GoogleBigqueryJobQueryScriptOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryJobQueryScriptOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobQueryScriptOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryJob.GoogleBigqueryJobQueryUserDefinedFunctionResources",
    jsii_struct_bases=[],
    name_mapping={"inline_code": "inlineCode", "resource_uri": "resourceUri"},
)
class GoogleBigqueryJobQueryUserDefinedFunctionResources:
    def __init__(
        self,
        *,
        inline_code: typing.Optional[builtins.str] = None,
        resource_uri: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param inline_code: An inline resource that contains code for a user-defined function (UDF). Providing a inline code resource is equivalent to providing a URI for a file containing the same code. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#inline_code GoogleBigqueryJob#inline_code}
        :param resource_uri: A code resource to load from a Google Cloud Storage URI (gs://bucket/path). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#resource_uri GoogleBigqueryJob#resource_uri}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobQueryUserDefinedFunctionResources.__init__)
            check_type(argname="argument inline_code", value=inline_code, expected_type=type_hints["inline_code"])
            check_type(argname="argument resource_uri", value=resource_uri, expected_type=type_hints["resource_uri"])
        self._values: typing.Dict[str, typing.Any] = {}
        if inline_code is not None:
            self._values["inline_code"] = inline_code
        if resource_uri is not None:
            self._values["resource_uri"] = resource_uri

    @builtins.property
    def inline_code(self) -> typing.Optional[builtins.str]:
        '''An inline resource that contains code for a user-defined function (UDF).

        Providing a inline code resource is equivalent to providing a URI for a file containing the same code.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#inline_code GoogleBigqueryJob#inline_code}
        '''
        result = self._values.get("inline_code")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def resource_uri(self) -> typing.Optional[builtins.str]:
        '''A code resource to load from a Google Cloud Storage URI (gs://bucket/path).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#resource_uri GoogleBigqueryJob#resource_uri}
        '''
        result = self._values.get("resource_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryJobQueryUserDefinedFunctionResources(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryJobQueryUserDefinedFunctionResourcesList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryJob.GoogleBigqueryJobQueryUserDefinedFunctionResourcesList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobQueryUserDefinedFunctionResourcesList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleBigqueryJobQueryUserDefinedFunctionResourcesOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobQueryUserDefinedFunctionResourcesList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleBigqueryJobQueryUserDefinedFunctionResourcesOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobQueryUserDefinedFunctionResourcesList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobQueryUserDefinedFunctionResourcesList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobQueryUserDefinedFunctionResourcesList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleBigqueryJobQueryUserDefinedFunctionResources]]]:
        return typing.cast(typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleBigqueryJobQueryUserDefinedFunctionResources]]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[cdktf.IResolvable, typing.List[GoogleBigqueryJobQueryUserDefinedFunctionResources]]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobQueryUserDefinedFunctionResourcesList, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleBigqueryJobQueryUserDefinedFunctionResourcesOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryJob.GoogleBigqueryJobQueryUserDefinedFunctionResourcesOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobQueryUserDefinedFunctionResourcesOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @jsii.member(jsii_name="resetInlineCode")
    def reset_inline_code(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetInlineCode", []))

    @jsii.member(jsii_name="resetResourceUri")
    def reset_resource_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetResourceUri", []))

    @builtins.property
    @jsii.member(jsii_name="inlineCodeInput")
    def inline_code_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "inlineCodeInput"))

    @builtins.property
    @jsii.member(jsii_name="resourceUriInput")
    def resource_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "resourceUriInput"))

    @builtins.property
    @jsii.member(jsii_name="inlineCode")
    def inline_code(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "inlineCode"))

    @inline_code.setter
    def inline_code(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobQueryUserDefinedFunctionResourcesOutputReference, "inline_code").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "inlineCode", value)

    @builtins.property
    @jsii.member(jsii_name="resourceUri")
    def resource_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "resourceUri"))

    @resource_uri.setter
    def resource_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobQueryUserDefinedFunctionResourcesOutputReference, "resource_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "resourceUri", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleBigqueryJobQueryUserDefinedFunctionResources, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleBigqueryJobQueryUserDefinedFunctionResources, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleBigqueryJobQueryUserDefinedFunctionResources, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobQueryUserDefinedFunctionResourcesOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryJob.GoogleBigqueryJobStatus",
    jsii_struct_bases=[],
    name_mapping={},
)
class GoogleBigqueryJobStatus:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryJobStatus(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryJob.GoogleBigqueryJobStatusErrorResult",
    jsii_struct_bases=[],
    name_mapping={},
)
class GoogleBigqueryJobStatusErrorResult:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryJobStatusErrorResult(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryJobStatusErrorResultList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryJob.GoogleBigqueryJobStatusErrorResultList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobStatusErrorResultList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(
        self,
        index: jsii.Number,
    ) -> "GoogleBigqueryJobStatusErrorResultOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobStatusErrorResultList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleBigqueryJobStatusErrorResultOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobStatusErrorResultList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobStatusErrorResultList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobStatusErrorResultList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class GoogleBigqueryJobStatusErrorResultOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryJob.GoogleBigqueryJobStatusErrorResultOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobStatusErrorResultOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "message"))

    @builtins.property
    @jsii.member(jsii_name="reason")
    def reason(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "reason"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleBigqueryJobStatusErrorResult]:
        return typing.cast(typing.Optional[GoogleBigqueryJobStatusErrorResult], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryJobStatusErrorResult],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobStatusErrorResultOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryJob.GoogleBigqueryJobStatusErrors",
    jsii_struct_bases=[],
    name_mapping={},
)
class GoogleBigqueryJobStatusErrors:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryJobStatusErrors(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryJobStatusErrorsList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryJob.GoogleBigqueryJobStatusErrorsList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobStatusErrorsList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "GoogleBigqueryJobStatusErrorsOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobStatusErrorsList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleBigqueryJobStatusErrorsOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobStatusErrorsList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobStatusErrorsList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobStatusErrorsList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class GoogleBigqueryJobStatusErrorsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryJob.GoogleBigqueryJobStatusErrorsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobStatusErrorsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @builtins.property
    @jsii.member(jsii_name="message")
    def message(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "message"))

    @builtins.property
    @jsii.member(jsii_name="reason")
    def reason(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "reason"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleBigqueryJobStatusErrors]:
        return typing.cast(typing.Optional[GoogleBigqueryJobStatusErrors], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryJobStatusErrors],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobStatusErrorsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleBigqueryJobStatusList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryJob.GoogleBigqueryJobStatusList",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        wraps_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param wraps_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobStatusList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "GoogleBigqueryJobStatusOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobStatusList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleBigqueryJobStatusOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobStatusList, "_terraform_attribute").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformAttribute", value)

    @builtins.property
    @jsii.member(jsii_name="terraformResource")
    def _terraform_resource(self) -> cdktf.IInterpolatingParent:
        '''The parent resource.'''
        return typing.cast(cdktf.IInterpolatingParent, jsii.get(self, "terraformResource"))

    @_terraform_resource.setter
    def _terraform_resource(self, value: cdktf.IInterpolatingParent) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobStatusList, "_terraform_resource").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "terraformResource", value)

    @builtins.property
    @jsii.member(jsii_name="wrapsSet")
    def _wraps_set(self) -> builtins.bool:
        '''whether the list is wrapping a set (will add tolist() to be able to access an item via an index).'''
        return typing.cast(builtins.bool, jsii.get(self, "wrapsSet"))

    @_wraps_set.setter
    def _wraps_set(self, value: builtins.bool) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobStatusList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class GoogleBigqueryJobStatusOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryJob.GoogleBigqueryJobStatusOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
        complex_object_index: jsii.Number,
        complex_object_is_from_set: builtins.bool,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        :param complex_object_index: the index of this item in the list.
        :param complex_object_is_from_set: whether the list is wrapping a set (will add tolist() to be able to access an item via an index).
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobStatusOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="errorResult")
    def error_result(self) -> GoogleBigqueryJobStatusErrorResultList:
        return typing.cast(GoogleBigqueryJobStatusErrorResultList, jsii.get(self, "errorResult"))

    @builtins.property
    @jsii.member(jsii_name="errors")
    def errors(self) -> GoogleBigqueryJobStatusErrorsList:
        return typing.cast(GoogleBigqueryJobStatusErrorsList, jsii.get(self, "errors"))

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleBigqueryJobStatus]:
        return typing.cast(typing.Optional[GoogleBigqueryJobStatus], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[GoogleBigqueryJobStatus]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobStatusOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryJob.GoogleBigqueryJobTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete"},
)
class GoogleBigqueryJobTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#create GoogleBigqueryJob#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#delete GoogleBigqueryJob#delete}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#create GoogleBigqueryJob#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_job#delete GoogleBigqueryJob#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryJobTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryJobTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryJob.GoogleBigqueryJobTimeoutsOutputReference",
):
    def __init__(
        self,
        terraform_resource: cdktf.IInterpolatingParent,
        terraform_attribute: builtins.str,
    ) -> None:
        '''
        :param terraform_resource: The parent resource.
        :param terraform_attribute: The attribute on the parent resource this class is referencing.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryJobTimeoutsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetCreate")
    def reset_create(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCreate", []))

    @jsii.member(jsii_name="resetDelete")
    def reset_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDelete", []))

    @builtins.property
    @jsii.member(jsii_name="createInput")
    def create_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "createInput"))

    @builtins.property
    @jsii.member(jsii_name="deleteInput")
    def delete_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "deleteInput"))

    @builtins.property
    @jsii.member(jsii_name="create")
    def create(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "create"))

    @create.setter
    def create(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleBigqueryJobTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleBigqueryJobTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleBigqueryJobTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryJobTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleBigqueryJob",
    "GoogleBigqueryJobConfig",
    "GoogleBigqueryJobCopy",
    "GoogleBigqueryJobCopyDestinationEncryptionConfiguration",
    "GoogleBigqueryJobCopyDestinationEncryptionConfigurationOutputReference",
    "GoogleBigqueryJobCopyDestinationTable",
    "GoogleBigqueryJobCopyDestinationTableOutputReference",
    "GoogleBigqueryJobCopyOutputReference",
    "GoogleBigqueryJobCopySourceTables",
    "GoogleBigqueryJobCopySourceTablesList",
    "GoogleBigqueryJobCopySourceTablesOutputReference",
    "GoogleBigqueryJobExtract",
    "GoogleBigqueryJobExtractOutputReference",
    "GoogleBigqueryJobExtractSourceModel",
    "GoogleBigqueryJobExtractSourceModelOutputReference",
    "GoogleBigqueryJobExtractSourceTable",
    "GoogleBigqueryJobExtractSourceTableOutputReference",
    "GoogleBigqueryJobLoad",
    "GoogleBigqueryJobLoadDestinationEncryptionConfiguration",
    "GoogleBigqueryJobLoadDestinationEncryptionConfigurationOutputReference",
    "GoogleBigqueryJobLoadDestinationTable",
    "GoogleBigqueryJobLoadDestinationTableOutputReference",
    "GoogleBigqueryJobLoadOutputReference",
    "GoogleBigqueryJobLoadTimePartitioning",
    "GoogleBigqueryJobLoadTimePartitioningOutputReference",
    "GoogleBigqueryJobQuery",
    "GoogleBigqueryJobQueryDefaultDataset",
    "GoogleBigqueryJobQueryDefaultDatasetOutputReference",
    "GoogleBigqueryJobQueryDestinationEncryptionConfiguration",
    "GoogleBigqueryJobQueryDestinationEncryptionConfigurationOutputReference",
    "GoogleBigqueryJobQueryDestinationTable",
    "GoogleBigqueryJobQueryDestinationTableOutputReference",
    "GoogleBigqueryJobQueryOutputReference",
    "GoogleBigqueryJobQueryScriptOptions",
    "GoogleBigqueryJobQueryScriptOptionsOutputReference",
    "GoogleBigqueryJobQueryUserDefinedFunctionResources",
    "GoogleBigqueryJobQueryUserDefinedFunctionResourcesList",
    "GoogleBigqueryJobQueryUserDefinedFunctionResourcesOutputReference",
    "GoogleBigqueryJobStatus",
    "GoogleBigqueryJobStatusErrorResult",
    "GoogleBigqueryJobStatusErrorResultList",
    "GoogleBigqueryJobStatusErrorResultOutputReference",
    "GoogleBigqueryJobStatusErrors",
    "GoogleBigqueryJobStatusErrorsList",
    "GoogleBigqueryJobStatusErrorsOutputReference",
    "GoogleBigqueryJobStatusList",
    "GoogleBigqueryJobStatusOutputReference",
    "GoogleBigqueryJobTimeouts",
    "GoogleBigqueryJobTimeoutsOutputReference",
]

publication.publish()
