'''
# `google_bigquery_table`

Refer to the Terraform Registory for docs: [`google_bigquery_table`](https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table).
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


class GoogleBigqueryTable(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTable",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table google_bigquery_table}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        dataset_id: builtins.str,
        table_id: builtins.str,
        clustering: typing.Optional[typing.Sequence[builtins.str]] = None,
        deletion_protection: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        encryption_configuration: typing.Optional[typing.Union["GoogleBigqueryTableEncryptionConfiguration", typing.Dict[str, typing.Any]]] = None,
        expiration_time: typing.Optional[jsii.Number] = None,
        external_data_configuration: typing.Optional[typing.Union["GoogleBigqueryTableExternalDataConfiguration", typing.Dict[str, typing.Any]]] = None,
        friendly_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        materialized_view: typing.Optional[typing.Union["GoogleBigqueryTableMaterializedView", typing.Dict[str, typing.Any]]] = None,
        project: typing.Optional[builtins.str] = None,
        range_partitioning: typing.Optional[typing.Union["GoogleBigqueryTableRangePartitioning", typing.Dict[str, typing.Any]]] = None,
        schema: typing.Optional[builtins.str] = None,
        time_partitioning: typing.Optional[typing.Union["GoogleBigqueryTableTimePartitioning", typing.Dict[str, typing.Any]]] = None,
        view: typing.Optional[typing.Union["GoogleBigqueryTableView", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table google_bigquery_table} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param dataset_id: The dataset ID to create the table in. Changing this forces a new resource to be created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#dataset_id GoogleBigqueryTable#dataset_id}
        :param table_id: A unique ID for the resource. Changing this forces a new resource to be created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#table_id GoogleBigqueryTable#table_id}
        :param clustering: Specifies column names to use for data clustering. Up to four top-level columns are allowed, and should be specified in descending priority order. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#clustering GoogleBigqueryTable#clustering}
        :param deletion_protection: Whether or not to allow Terraform to destroy the instance. Unless this field is set to false in Terraform state, a terraform destroy or terraform apply that would delete the instance will fail. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#deletion_protection GoogleBigqueryTable#deletion_protection}
        :param description: The field description. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#description GoogleBigqueryTable#description}
        :param encryption_configuration: encryption_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#encryption_configuration GoogleBigqueryTable#encryption_configuration}
        :param expiration_time: The time when this table expires, in milliseconds since the epoch. If not present, the table will persist indefinitely. Expired tables will be deleted and their storage reclaimed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#expiration_time GoogleBigqueryTable#expiration_time}
        :param external_data_configuration: external_data_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#external_data_configuration GoogleBigqueryTable#external_data_configuration}
        :param friendly_name: A descriptive name for the table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#friendly_name GoogleBigqueryTable#friendly_name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#id GoogleBigqueryTable#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: A mapping of labels to assign to the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#labels GoogleBigqueryTable#labels}
        :param materialized_view: materialized_view block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#materialized_view GoogleBigqueryTable#materialized_view}
        :param project: The ID of the project in which the resource belongs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#project GoogleBigqueryTable#project}
        :param range_partitioning: range_partitioning block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#range_partitioning GoogleBigqueryTable#range_partitioning}
        :param schema: A JSON schema for the table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#schema GoogleBigqueryTable#schema}
        :param time_partitioning: time_partitioning block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#time_partitioning GoogleBigqueryTable#time_partitioning}
        :param view: view block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#view GoogleBigqueryTable#view}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryTable.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleBigqueryTableConfig(
            dataset_id=dataset_id,
            table_id=table_id,
            clustering=clustering,
            deletion_protection=deletion_protection,
            description=description,
            encryption_configuration=encryption_configuration,
            expiration_time=expiration_time,
            external_data_configuration=external_data_configuration,
            friendly_name=friendly_name,
            id=id,
            labels=labels,
            materialized_view=materialized_view,
            project=project,
            range_partitioning=range_partitioning,
            schema=schema,
            time_partitioning=time_partitioning,
            view=view,
            connection=connection,
            count=count,
            depends_on=depends_on,
            for_each=for_each,
            lifecycle=lifecycle,
            provider=provider,
            provisioners=provisioners,
        )

        jsii.create(self.__class__, self, [scope, id_, config])

    @jsii.member(jsii_name="putEncryptionConfiguration")
    def put_encryption_configuration(self, *, kms_key_name: builtins.str) -> None:
        '''
        :param kms_key_name: The self link or full name of a key which should be used to encrypt this table. Note that the default bigquery service account will need to have encrypt/decrypt permissions on this key - you may want to see the google_bigquery_default_service_account datasource and the google_kms_crypto_key_iam_binding resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#kms_key_name GoogleBigqueryTable#kms_key_name}
        '''
        value = GoogleBigqueryTableEncryptionConfiguration(kms_key_name=kms_key_name)

        return typing.cast(None, jsii.invoke(self, "putEncryptionConfiguration", [value]))

    @jsii.member(jsii_name="putExternalDataConfiguration")
    def put_external_data_configuration(
        self,
        *,
        autodetect: typing.Union[builtins.bool, cdktf.IResolvable],
        source_format: builtins.str,
        source_uris: typing.Sequence[builtins.str],
        compression: typing.Optional[builtins.str] = None,
        connection_id: typing.Optional[builtins.str] = None,
        csv_options: typing.Optional[typing.Union["GoogleBigqueryTableExternalDataConfigurationCsvOptions", typing.Dict[str, typing.Any]]] = None,
        google_sheets_options: typing.Optional[typing.Union["GoogleBigqueryTableExternalDataConfigurationGoogleSheetsOptions", typing.Dict[str, typing.Any]]] = None,
        hive_partitioning_options: typing.Optional[typing.Union["GoogleBigqueryTableExternalDataConfigurationHivePartitioningOptions", typing.Dict[str, typing.Any]]] = None,
        ignore_unknown_values: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        max_bad_records: typing.Optional[jsii.Number] = None,
        schema: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param autodetect: Let BigQuery try to autodetect the schema and format of the table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#autodetect GoogleBigqueryTable#autodetect}
        :param source_format: The data format. Supported values are: "CSV", "GOOGLE_SHEETS", "NEWLINE_DELIMITED_JSON", "AVRO", "PARQUET", "ORC" and "DATASTORE_BACKUP". To use "GOOGLE_SHEETS" the scopes must include "googleapis.com/auth/drive.readonly". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#source_format GoogleBigqueryTable#source_format}
        :param source_uris: A list of the fully-qualified URIs that point to your data in Google Cloud. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#source_uris GoogleBigqueryTable#source_uris}
        :param compression: The compression type of the data source. Valid values are "NONE" or "GZIP". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#compression GoogleBigqueryTable#compression}
        :param connection_id: The connection specifying the credentials to be used to read external storage, such as Azure Blob, Cloud Storage, or S3. The connectionId can have the form "{{project}}.{{location}}.{{connection_id}}" or "projects/{{project}}/locations/{{location}}/connections/{{connection_id}}". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#connection_id GoogleBigqueryTable#connection_id}
        :param csv_options: csv_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#csv_options GoogleBigqueryTable#csv_options}
        :param google_sheets_options: google_sheets_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#google_sheets_options GoogleBigqueryTable#google_sheets_options}
        :param hive_partitioning_options: hive_partitioning_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#hive_partitioning_options GoogleBigqueryTable#hive_partitioning_options}
        :param ignore_unknown_values: Indicates if BigQuery should allow extra values that are not represented in the table schema. If true, the extra values are ignored. If false, records with extra columns are treated as bad records, and if there are too many bad records, an invalid error is returned in the job result. The default value is false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#ignore_unknown_values GoogleBigqueryTable#ignore_unknown_values}
        :param max_bad_records: The maximum number of bad records that BigQuery can ignore when reading data. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#max_bad_records GoogleBigqueryTable#max_bad_records}
        :param schema: A JSON schema for the external table. Schema is required for CSV and JSON formats and is disallowed for Google Cloud Bigtable, Cloud Datastore backups, and Avro formats when using external tables. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#schema GoogleBigqueryTable#schema}
        '''
        value = GoogleBigqueryTableExternalDataConfiguration(
            autodetect=autodetect,
            source_format=source_format,
            source_uris=source_uris,
            compression=compression,
            connection_id=connection_id,
            csv_options=csv_options,
            google_sheets_options=google_sheets_options,
            hive_partitioning_options=hive_partitioning_options,
            ignore_unknown_values=ignore_unknown_values,
            max_bad_records=max_bad_records,
            schema=schema,
        )

        return typing.cast(None, jsii.invoke(self, "putExternalDataConfiguration", [value]))

    @jsii.member(jsii_name="putMaterializedView")
    def put_materialized_view(
        self,
        *,
        query: builtins.str,
        enable_refresh: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        refresh_interval_ms: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param query: A query whose result is persisted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#query GoogleBigqueryTable#query}
        :param enable_refresh: Specifies if BigQuery should automatically refresh materialized view when the base table is updated. The default is true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#enable_refresh GoogleBigqueryTable#enable_refresh}
        :param refresh_interval_ms: Specifies maximum frequency at which this materialized view will be refreshed. The default is 1800000. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#refresh_interval_ms GoogleBigqueryTable#refresh_interval_ms}
        '''
        value = GoogleBigqueryTableMaterializedView(
            query=query,
            enable_refresh=enable_refresh,
            refresh_interval_ms=refresh_interval_ms,
        )

        return typing.cast(None, jsii.invoke(self, "putMaterializedView", [value]))

    @jsii.member(jsii_name="putRangePartitioning")
    def put_range_partitioning(
        self,
        *,
        field: builtins.str,
        range: typing.Union["GoogleBigqueryTableRangePartitioningRange", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param field: The field used to determine how to create a range-based partition. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#field GoogleBigqueryTable#field}
        :param range: range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#range GoogleBigqueryTable#range}
        '''
        value = GoogleBigqueryTableRangePartitioning(field=field, range=range)

        return typing.cast(None, jsii.invoke(self, "putRangePartitioning", [value]))

    @jsii.member(jsii_name="putTimePartitioning")
    def put_time_partitioning(
        self,
        *,
        type: builtins.str,
        expiration_ms: typing.Optional[jsii.Number] = None,
        field: typing.Optional[builtins.str] = None,
        require_partition_filter: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param type: The supported types are DAY, HOUR, MONTH, and YEAR, which will generate one partition per day, hour, month, and year, respectively. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#type GoogleBigqueryTable#type}
        :param expiration_ms: Number of milliseconds for which to keep the storage for a partition. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#expiration_ms GoogleBigqueryTable#expiration_ms}
        :param field: The field used to determine how to create a time-based partition. If time-based partitioning is enabled without this value, the table is partitioned based on the load time. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#field GoogleBigqueryTable#field}
        :param require_partition_filter: If set to true, queries over this table require a partition filter that can be used for partition elimination to be specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#require_partition_filter GoogleBigqueryTable#require_partition_filter}
        '''
        value = GoogleBigqueryTableTimePartitioning(
            type=type,
            expiration_ms=expiration_ms,
            field=field,
            require_partition_filter=require_partition_filter,
        )

        return typing.cast(None, jsii.invoke(self, "putTimePartitioning", [value]))

    @jsii.member(jsii_name="putView")
    def put_view(
        self,
        *,
        query: builtins.str,
        use_legacy_sql: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param query: A query that BigQuery executes when the view is referenced. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#query GoogleBigqueryTable#query}
        :param use_legacy_sql: Specifies whether to use BigQuery's legacy SQL for this view. The default value is true. If set to false, the view will use BigQuery's standard SQL Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#use_legacy_sql GoogleBigqueryTable#use_legacy_sql}
        '''
        value = GoogleBigqueryTableView(query=query, use_legacy_sql=use_legacy_sql)

        return typing.cast(None, jsii.invoke(self, "putView", [value]))

    @jsii.member(jsii_name="resetClustering")
    def reset_clustering(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClustering", []))

    @jsii.member(jsii_name="resetDeletionProtection")
    def reset_deletion_protection(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDeletionProtection", []))

    @jsii.member(jsii_name="resetDescription")
    def reset_description(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetDescription", []))

    @jsii.member(jsii_name="resetEncryptionConfiguration")
    def reset_encryption_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncryptionConfiguration", []))

    @jsii.member(jsii_name="resetExpirationTime")
    def reset_expiration_time(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpirationTime", []))

    @jsii.member(jsii_name="resetExternalDataConfiguration")
    def reset_external_data_configuration(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExternalDataConfiguration", []))

    @jsii.member(jsii_name="resetFriendlyName")
    def reset_friendly_name(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFriendlyName", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetMaterializedView")
    def reset_materialized_view(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaterializedView", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetRangePartitioning")
    def reset_range_partitioning(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRangePartitioning", []))

    @jsii.member(jsii_name="resetSchema")
    def reset_schema(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchema", []))

    @jsii.member(jsii_name="resetTimePartitioning")
    def reset_time_partitioning(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetTimePartitioning", []))

    @jsii.member(jsii_name="resetView")
    def reset_view(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetView", []))

    @jsii.member(jsii_name="synthesizeAttributes")
    def _synthesize_attributes(self) -> typing.Mapping[builtins.str, typing.Any]:
        return typing.cast(typing.Mapping[builtins.str, typing.Any], jsii.invoke(self, "synthesizeAttributes", []))

    @jsii.python.classproperty
    @jsii.member(jsii_name="tfResourceType")
    def TF_RESOURCE_TYPE(cls) -> builtins.str:
        return typing.cast(builtins.str, jsii.sget(cls, "tfResourceType"))

    @builtins.property
    @jsii.member(jsii_name="creationTime")
    def creation_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "creationTime"))

    @builtins.property
    @jsii.member(jsii_name="encryptionConfiguration")
    def encryption_configuration(
        self,
    ) -> "GoogleBigqueryTableEncryptionConfigurationOutputReference":
        return typing.cast("GoogleBigqueryTableEncryptionConfigurationOutputReference", jsii.get(self, "encryptionConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="etag")
    def etag(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "etag"))

    @builtins.property
    @jsii.member(jsii_name="externalDataConfiguration")
    def external_data_configuration(
        self,
    ) -> "GoogleBigqueryTableExternalDataConfigurationOutputReference":
        return typing.cast("GoogleBigqueryTableExternalDataConfigurationOutputReference", jsii.get(self, "externalDataConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="lastModifiedTime")
    def last_modified_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "lastModifiedTime"))

    @builtins.property
    @jsii.member(jsii_name="location")
    def location(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "location"))

    @builtins.property
    @jsii.member(jsii_name="materializedView")
    def materialized_view(self) -> "GoogleBigqueryTableMaterializedViewOutputReference":
        return typing.cast("GoogleBigqueryTableMaterializedViewOutputReference", jsii.get(self, "materializedView"))

    @builtins.property
    @jsii.member(jsii_name="numBytes")
    def num_bytes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numBytes"))

    @builtins.property
    @jsii.member(jsii_name="numLongTermBytes")
    def num_long_term_bytes(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numLongTermBytes"))

    @builtins.property
    @jsii.member(jsii_name="numRows")
    def num_rows(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "numRows"))

    @builtins.property
    @jsii.member(jsii_name="rangePartitioning")
    def range_partitioning(
        self,
    ) -> "GoogleBigqueryTableRangePartitioningOutputReference":
        return typing.cast("GoogleBigqueryTableRangePartitioningOutputReference", jsii.get(self, "rangePartitioning"))

    @builtins.property
    @jsii.member(jsii_name="selfLink")
    def self_link(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "selfLink"))

    @builtins.property
    @jsii.member(jsii_name="timePartitioning")
    def time_partitioning(self) -> "GoogleBigqueryTableTimePartitioningOutputReference":
        return typing.cast("GoogleBigqueryTableTimePartitioningOutputReference", jsii.get(self, "timePartitioning"))

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @builtins.property
    @jsii.member(jsii_name="view")
    def view(self) -> "GoogleBigqueryTableViewOutputReference":
        return typing.cast("GoogleBigqueryTableViewOutputReference", jsii.get(self, "view"))

    @builtins.property
    @jsii.member(jsii_name="clusteringInput")
    def clustering_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "clusteringInput"))

    @builtins.property
    @jsii.member(jsii_name="datasetIdInput")
    def dataset_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "datasetIdInput"))

    @builtins.property
    @jsii.member(jsii_name="deletionProtectionInput")
    def deletion_protection_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "deletionProtectionInput"))

    @builtins.property
    @jsii.member(jsii_name="descriptionInput")
    def description_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "descriptionInput"))

    @builtins.property
    @jsii.member(jsii_name="encryptionConfigurationInput")
    def encryption_configuration_input(
        self,
    ) -> typing.Optional["GoogleBigqueryTableEncryptionConfiguration"]:
        return typing.cast(typing.Optional["GoogleBigqueryTableEncryptionConfiguration"], jsii.get(self, "encryptionConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="expirationTimeInput")
    def expiration_time_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "expirationTimeInput"))

    @builtins.property
    @jsii.member(jsii_name="externalDataConfigurationInput")
    def external_data_configuration_input(
        self,
    ) -> typing.Optional["GoogleBigqueryTableExternalDataConfiguration"]:
        return typing.cast(typing.Optional["GoogleBigqueryTableExternalDataConfiguration"], jsii.get(self, "externalDataConfigurationInput"))

    @builtins.property
    @jsii.member(jsii_name="friendlyNameInput")
    def friendly_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "friendlyNameInput"))

    @builtins.property
    @jsii.member(jsii_name="idInput")
    def id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "idInput"))

    @builtins.property
    @jsii.member(jsii_name="labelsInput")
    def labels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "labelsInput"))

    @builtins.property
    @jsii.member(jsii_name="materializedViewInput")
    def materialized_view_input(
        self,
    ) -> typing.Optional["GoogleBigqueryTableMaterializedView"]:
        return typing.cast(typing.Optional["GoogleBigqueryTableMaterializedView"], jsii.get(self, "materializedViewInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="rangePartitioningInput")
    def range_partitioning_input(
        self,
    ) -> typing.Optional["GoogleBigqueryTableRangePartitioning"]:
        return typing.cast(typing.Optional["GoogleBigqueryTableRangePartitioning"], jsii.get(self, "rangePartitioningInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaInput")
    def schema_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemaInput"))

    @builtins.property
    @jsii.member(jsii_name="tableIdInput")
    def table_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "tableIdInput"))

    @builtins.property
    @jsii.member(jsii_name="timePartitioningInput")
    def time_partitioning_input(
        self,
    ) -> typing.Optional["GoogleBigqueryTableTimePartitioning"]:
        return typing.cast(typing.Optional["GoogleBigqueryTableTimePartitioning"], jsii.get(self, "timePartitioningInput"))

    @builtins.property
    @jsii.member(jsii_name="viewInput")
    def view_input(self) -> typing.Optional["GoogleBigqueryTableView"]:
        return typing.cast(typing.Optional["GoogleBigqueryTableView"], jsii.get(self, "viewInput"))

    @builtins.property
    @jsii.member(jsii_name="clustering")
    def clustering(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "clustering"))

    @clustering.setter
    def clustering(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTable, "clustering").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clustering", value)

    @builtins.property
    @jsii.member(jsii_name="datasetId")
    def dataset_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "datasetId"))

    @dataset_id.setter
    def dataset_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTable, "dataset_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "datasetId", value)

    @builtins.property
    @jsii.member(jsii_name="deletionProtection")
    def deletion_protection(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "deletionProtection"))

    @deletion_protection.setter
    def deletion_protection(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTable, "deletion_protection").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "deletionProtection", value)

    @builtins.property
    @jsii.member(jsii_name="description")
    def description(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "description"))

    @description.setter
    def description(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTable, "description").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "description", value)

    @builtins.property
    @jsii.member(jsii_name="expirationTime")
    def expiration_time(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "expirationTime"))

    @expiration_time.setter
    def expiration_time(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTable, "expiration_time").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expirationTime", value)

    @builtins.property
    @jsii.member(jsii_name="friendlyName")
    def friendly_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "friendlyName"))

    @friendly_name.setter
    def friendly_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTable, "friendly_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "friendlyName", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTable, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTable, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTable, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="schema")
    def schema(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schema"))

    @schema.setter
    def schema(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTable, "schema").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schema", value)

    @builtins.property
    @jsii.member(jsii_name="tableId")
    def table_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "tableId"))

    @table_id.setter
    def table_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTable, "table_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "tableId", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "dataset_id": "datasetId",
        "table_id": "tableId",
        "clustering": "clustering",
        "deletion_protection": "deletionProtection",
        "description": "description",
        "encryption_configuration": "encryptionConfiguration",
        "expiration_time": "expirationTime",
        "external_data_configuration": "externalDataConfiguration",
        "friendly_name": "friendlyName",
        "id": "id",
        "labels": "labels",
        "materialized_view": "materializedView",
        "project": "project",
        "range_partitioning": "rangePartitioning",
        "schema": "schema",
        "time_partitioning": "timePartitioning",
        "view": "view",
    },
)
class GoogleBigqueryTableConfig(cdktf.TerraformMetaArguments):
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
        dataset_id: builtins.str,
        table_id: builtins.str,
        clustering: typing.Optional[typing.Sequence[builtins.str]] = None,
        deletion_protection: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        description: typing.Optional[builtins.str] = None,
        encryption_configuration: typing.Optional[typing.Union["GoogleBigqueryTableEncryptionConfiguration", typing.Dict[str, typing.Any]]] = None,
        expiration_time: typing.Optional[jsii.Number] = None,
        external_data_configuration: typing.Optional[typing.Union["GoogleBigqueryTableExternalDataConfiguration", typing.Dict[str, typing.Any]]] = None,
        friendly_name: typing.Optional[builtins.str] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        materialized_view: typing.Optional[typing.Union["GoogleBigqueryTableMaterializedView", typing.Dict[str, typing.Any]]] = None,
        project: typing.Optional[builtins.str] = None,
        range_partitioning: typing.Optional[typing.Union["GoogleBigqueryTableRangePartitioning", typing.Dict[str, typing.Any]]] = None,
        schema: typing.Optional[builtins.str] = None,
        time_partitioning: typing.Optional[typing.Union["GoogleBigqueryTableTimePartitioning", typing.Dict[str, typing.Any]]] = None,
        view: typing.Optional[typing.Union["GoogleBigqueryTableView", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param dataset_id: The dataset ID to create the table in. Changing this forces a new resource to be created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#dataset_id GoogleBigqueryTable#dataset_id}
        :param table_id: A unique ID for the resource. Changing this forces a new resource to be created. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#table_id GoogleBigqueryTable#table_id}
        :param clustering: Specifies column names to use for data clustering. Up to four top-level columns are allowed, and should be specified in descending priority order. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#clustering GoogleBigqueryTable#clustering}
        :param deletion_protection: Whether or not to allow Terraform to destroy the instance. Unless this field is set to false in Terraform state, a terraform destroy or terraform apply that would delete the instance will fail. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#deletion_protection GoogleBigqueryTable#deletion_protection}
        :param description: The field description. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#description GoogleBigqueryTable#description}
        :param encryption_configuration: encryption_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#encryption_configuration GoogleBigqueryTable#encryption_configuration}
        :param expiration_time: The time when this table expires, in milliseconds since the epoch. If not present, the table will persist indefinitely. Expired tables will be deleted and their storage reclaimed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#expiration_time GoogleBigqueryTable#expiration_time}
        :param external_data_configuration: external_data_configuration block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#external_data_configuration GoogleBigqueryTable#external_data_configuration}
        :param friendly_name: A descriptive name for the table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#friendly_name GoogleBigqueryTable#friendly_name}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#id GoogleBigqueryTable#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: A mapping of labels to assign to the resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#labels GoogleBigqueryTable#labels}
        :param materialized_view: materialized_view block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#materialized_view GoogleBigqueryTable#materialized_view}
        :param project: The ID of the project in which the resource belongs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#project GoogleBigqueryTable#project}
        :param range_partitioning: range_partitioning block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#range_partitioning GoogleBigqueryTable#range_partitioning}
        :param schema: A JSON schema for the table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#schema GoogleBigqueryTable#schema}
        :param time_partitioning: time_partitioning block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#time_partitioning GoogleBigqueryTable#time_partitioning}
        :param view: view block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#view GoogleBigqueryTable#view}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(encryption_configuration, dict):
            encryption_configuration = GoogleBigqueryTableEncryptionConfiguration(**encryption_configuration)
        if isinstance(external_data_configuration, dict):
            external_data_configuration = GoogleBigqueryTableExternalDataConfiguration(**external_data_configuration)
        if isinstance(materialized_view, dict):
            materialized_view = GoogleBigqueryTableMaterializedView(**materialized_view)
        if isinstance(range_partitioning, dict):
            range_partitioning = GoogleBigqueryTableRangePartitioning(**range_partitioning)
        if isinstance(time_partitioning, dict):
            time_partitioning = GoogleBigqueryTableTimePartitioning(**time_partitioning)
        if isinstance(view, dict):
            view = GoogleBigqueryTableView(**view)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryTableConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument dataset_id", value=dataset_id, expected_type=type_hints["dataset_id"])
            check_type(argname="argument table_id", value=table_id, expected_type=type_hints["table_id"])
            check_type(argname="argument clustering", value=clustering, expected_type=type_hints["clustering"])
            check_type(argname="argument deletion_protection", value=deletion_protection, expected_type=type_hints["deletion_protection"])
            check_type(argname="argument description", value=description, expected_type=type_hints["description"])
            check_type(argname="argument encryption_configuration", value=encryption_configuration, expected_type=type_hints["encryption_configuration"])
            check_type(argname="argument expiration_time", value=expiration_time, expected_type=type_hints["expiration_time"])
            check_type(argname="argument external_data_configuration", value=external_data_configuration, expected_type=type_hints["external_data_configuration"])
            check_type(argname="argument friendly_name", value=friendly_name, expected_type=type_hints["friendly_name"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument materialized_view", value=materialized_view, expected_type=type_hints["materialized_view"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument range_partitioning", value=range_partitioning, expected_type=type_hints["range_partitioning"])
            check_type(argname="argument schema", value=schema, expected_type=type_hints["schema"])
            check_type(argname="argument time_partitioning", value=time_partitioning, expected_type=type_hints["time_partitioning"])
            check_type(argname="argument view", value=view, expected_type=type_hints["view"])
        self._values: typing.Dict[str, typing.Any] = {
            "dataset_id": dataset_id,
            "table_id": table_id,
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
        if clustering is not None:
            self._values["clustering"] = clustering
        if deletion_protection is not None:
            self._values["deletion_protection"] = deletion_protection
        if description is not None:
            self._values["description"] = description
        if encryption_configuration is not None:
            self._values["encryption_configuration"] = encryption_configuration
        if expiration_time is not None:
            self._values["expiration_time"] = expiration_time
        if external_data_configuration is not None:
            self._values["external_data_configuration"] = external_data_configuration
        if friendly_name is not None:
            self._values["friendly_name"] = friendly_name
        if id is not None:
            self._values["id"] = id
        if labels is not None:
            self._values["labels"] = labels
        if materialized_view is not None:
            self._values["materialized_view"] = materialized_view
        if project is not None:
            self._values["project"] = project
        if range_partitioning is not None:
            self._values["range_partitioning"] = range_partitioning
        if schema is not None:
            self._values["schema"] = schema
        if time_partitioning is not None:
            self._values["time_partitioning"] = time_partitioning
        if view is not None:
            self._values["view"] = view

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
    def dataset_id(self) -> builtins.str:
        '''The dataset ID to create the table in. Changing this forces a new resource to be created.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#dataset_id GoogleBigqueryTable#dataset_id}
        '''
        result = self._values.get("dataset_id")
        assert result is not None, "Required property 'dataset_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def table_id(self) -> builtins.str:
        '''A unique ID for the resource. Changing this forces a new resource to be created.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#table_id GoogleBigqueryTable#table_id}
        '''
        result = self._values.get("table_id")
        assert result is not None, "Required property 'table_id' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def clustering(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Specifies column names to use for data clustering.

        Up to four top-level columns are allowed, and should be specified in descending priority order.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#clustering GoogleBigqueryTable#clustering}
        '''
        result = self._values.get("clustering")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def deletion_protection(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether or not to allow Terraform to destroy the instance.

        Unless this field is set to false in Terraform state, a terraform destroy or terraform apply that would delete the instance will fail.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#deletion_protection GoogleBigqueryTable#deletion_protection}
        '''
        result = self._values.get("deletion_protection")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def description(self) -> typing.Optional[builtins.str]:
        '''The field description.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#description GoogleBigqueryTable#description}
        '''
        result = self._values.get("description")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def encryption_configuration(
        self,
    ) -> typing.Optional["GoogleBigqueryTableEncryptionConfiguration"]:
        '''encryption_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#encryption_configuration GoogleBigqueryTable#encryption_configuration}
        '''
        result = self._values.get("encryption_configuration")
        return typing.cast(typing.Optional["GoogleBigqueryTableEncryptionConfiguration"], result)

    @builtins.property
    def expiration_time(self) -> typing.Optional[jsii.Number]:
        '''The time when this table expires, in milliseconds since the epoch.

        If not present, the table will persist indefinitely. Expired tables will be deleted and their storage reclaimed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#expiration_time GoogleBigqueryTable#expiration_time}
        '''
        result = self._values.get("expiration_time")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def external_data_configuration(
        self,
    ) -> typing.Optional["GoogleBigqueryTableExternalDataConfiguration"]:
        '''external_data_configuration block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#external_data_configuration GoogleBigqueryTable#external_data_configuration}
        '''
        result = self._values.get("external_data_configuration")
        return typing.cast(typing.Optional["GoogleBigqueryTableExternalDataConfiguration"], result)

    @builtins.property
    def friendly_name(self) -> typing.Optional[builtins.str]:
        '''A descriptive name for the table.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#friendly_name GoogleBigqueryTable#friendly_name}
        '''
        result = self._values.get("friendly_name")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#id GoogleBigqueryTable#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A mapping of labels to assign to the resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#labels GoogleBigqueryTable#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def materialized_view(
        self,
    ) -> typing.Optional["GoogleBigqueryTableMaterializedView"]:
        '''materialized_view block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#materialized_view GoogleBigqueryTable#materialized_view}
        '''
        result = self._values.get("materialized_view")
        return typing.cast(typing.Optional["GoogleBigqueryTableMaterializedView"], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''The ID of the project in which the resource belongs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#project GoogleBigqueryTable#project}
        '''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def range_partitioning(
        self,
    ) -> typing.Optional["GoogleBigqueryTableRangePartitioning"]:
        '''range_partitioning block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#range_partitioning GoogleBigqueryTable#range_partitioning}
        '''
        result = self._values.get("range_partitioning")
        return typing.cast(typing.Optional["GoogleBigqueryTableRangePartitioning"], result)

    @builtins.property
    def schema(self) -> typing.Optional[builtins.str]:
        '''A JSON schema for the table.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#schema GoogleBigqueryTable#schema}
        '''
        result = self._values.get("schema")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def time_partitioning(
        self,
    ) -> typing.Optional["GoogleBigqueryTableTimePartitioning"]:
        '''time_partitioning block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#time_partitioning GoogleBigqueryTable#time_partitioning}
        '''
        result = self._values.get("time_partitioning")
        return typing.cast(typing.Optional["GoogleBigqueryTableTimePartitioning"], result)

    @builtins.property
    def view(self) -> typing.Optional["GoogleBigqueryTableView"]:
        '''view block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#view GoogleBigqueryTable#view}
        '''
        result = self._values.get("view")
        return typing.cast(typing.Optional["GoogleBigqueryTableView"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryTableConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableEncryptionConfiguration",
    jsii_struct_bases=[],
    name_mapping={"kms_key_name": "kmsKeyName"},
)
class GoogleBigqueryTableEncryptionConfiguration:
    def __init__(self, *, kms_key_name: builtins.str) -> None:
        '''
        :param kms_key_name: The self link or full name of a key which should be used to encrypt this table. Note that the default bigquery service account will need to have encrypt/decrypt permissions on this key - you may want to see the google_bigquery_default_service_account datasource and the google_kms_crypto_key_iam_binding resource. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#kms_key_name GoogleBigqueryTable#kms_key_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryTableEncryptionConfiguration.__init__)
            check_type(argname="argument kms_key_name", value=kms_key_name, expected_type=type_hints["kms_key_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "kms_key_name": kms_key_name,
        }

    @builtins.property
    def kms_key_name(self) -> builtins.str:
        '''The self link or full name of a key which should be used to encrypt this table.

        Note that the default bigquery service account will need to have encrypt/decrypt permissions on this key - you may want to see the google_bigquery_default_service_account datasource and the google_kms_crypto_key_iam_binding resource.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#kms_key_name GoogleBigqueryTable#kms_key_name}
        '''
        result = self._values.get("kms_key_name")
        assert result is not None, "Required property 'kms_key_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryTableEncryptionConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryTableEncryptionConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableEncryptionConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(GoogleBigqueryTableEncryptionConfigurationOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTableEncryptionConfigurationOutputReference, "kms_key_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "kmsKeyName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleBigqueryTableEncryptionConfiguration]:
        return typing.cast(typing.Optional[GoogleBigqueryTableEncryptionConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryTableEncryptionConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTableEncryptionConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableExternalDataConfiguration",
    jsii_struct_bases=[],
    name_mapping={
        "autodetect": "autodetect",
        "source_format": "sourceFormat",
        "source_uris": "sourceUris",
        "compression": "compression",
        "connection_id": "connectionId",
        "csv_options": "csvOptions",
        "google_sheets_options": "googleSheetsOptions",
        "hive_partitioning_options": "hivePartitioningOptions",
        "ignore_unknown_values": "ignoreUnknownValues",
        "max_bad_records": "maxBadRecords",
        "schema": "schema",
    },
)
class GoogleBigqueryTableExternalDataConfiguration:
    def __init__(
        self,
        *,
        autodetect: typing.Union[builtins.bool, cdktf.IResolvable],
        source_format: builtins.str,
        source_uris: typing.Sequence[builtins.str],
        compression: typing.Optional[builtins.str] = None,
        connection_id: typing.Optional[builtins.str] = None,
        csv_options: typing.Optional[typing.Union["GoogleBigqueryTableExternalDataConfigurationCsvOptions", typing.Dict[str, typing.Any]]] = None,
        google_sheets_options: typing.Optional[typing.Union["GoogleBigqueryTableExternalDataConfigurationGoogleSheetsOptions", typing.Dict[str, typing.Any]]] = None,
        hive_partitioning_options: typing.Optional[typing.Union["GoogleBigqueryTableExternalDataConfigurationHivePartitioningOptions", typing.Dict[str, typing.Any]]] = None,
        ignore_unknown_values: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        max_bad_records: typing.Optional[jsii.Number] = None,
        schema: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param autodetect: Let BigQuery try to autodetect the schema and format of the table. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#autodetect GoogleBigqueryTable#autodetect}
        :param source_format: The data format. Supported values are: "CSV", "GOOGLE_SHEETS", "NEWLINE_DELIMITED_JSON", "AVRO", "PARQUET", "ORC" and "DATASTORE_BACKUP". To use "GOOGLE_SHEETS" the scopes must include "googleapis.com/auth/drive.readonly". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#source_format GoogleBigqueryTable#source_format}
        :param source_uris: A list of the fully-qualified URIs that point to your data in Google Cloud. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#source_uris GoogleBigqueryTable#source_uris}
        :param compression: The compression type of the data source. Valid values are "NONE" or "GZIP". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#compression GoogleBigqueryTable#compression}
        :param connection_id: The connection specifying the credentials to be used to read external storage, such as Azure Blob, Cloud Storage, or S3. The connectionId can have the form "{{project}}.{{location}}.{{connection_id}}" or "projects/{{project}}/locations/{{location}}/connections/{{connection_id}}". Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#connection_id GoogleBigqueryTable#connection_id}
        :param csv_options: csv_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#csv_options GoogleBigqueryTable#csv_options}
        :param google_sheets_options: google_sheets_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#google_sheets_options GoogleBigqueryTable#google_sheets_options}
        :param hive_partitioning_options: hive_partitioning_options block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#hive_partitioning_options GoogleBigqueryTable#hive_partitioning_options}
        :param ignore_unknown_values: Indicates if BigQuery should allow extra values that are not represented in the table schema. If true, the extra values are ignored. If false, records with extra columns are treated as bad records, and if there are too many bad records, an invalid error is returned in the job result. The default value is false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#ignore_unknown_values GoogleBigqueryTable#ignore_unknown_values}
        :param max_bad_records: The maximum number of bad records that BigQuery can ignore when reading data. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#max_bad_records GoogleBigqueryTable#max_bad_records}
        :param schema: A JSON schema for the external table. Schema is required for CSV and JSON formats and is disallowed for Google Cloud Bigtable, Cloud Datastore backups, and Avro formats when using external tables. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#schema GoogleBigqueryTable#schema}
        '''
        if isinstance(csv_options, dict):
            csv_options = GoogleBigqueryTableExternalDataConfigurationCsvOptions(**csv_options)
        if isinstance(google_sheets_options, dict):
            google_sheets_options = GoogleBigqueryTableExternalDataConfigurationGoogleSheetsOptions(**google_sheets_options)
        if isinstance(hive_partitioning_options, dict):
            hive_partitioning_options = GoogleBigqueryTableExternalDataConfigurationHivePartitioningOptions(**hive_partitioning_options)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryTableExternalDataConfiguration.__init__)
            check_type(argname="argument autodetect", value=autodetect, expected_type=type_hints["autodetect"])
            check_type(argname="argument source_format", value=source_format, expected_type=type_hints["source_format"])
            check_type(argname="argument source_uris", value=source_uris, expected_type=type_hints["source_uris"])
            check_type(argname="argument compression", value=compression, expected_type=type_hints["compression"])
            check_type(argname="argument connection_id", value=connection_id, expected_type=type_hints["connection_id"])
            check_type(argname="argument csv_options", value=csv_options, expected_type=type_hints["csv_options"])
            check_type(argname="argument google_sheets_options", value=google_sheets_options, expected_type=type_hints["google_sheets_options"])
            check_type(argname="argument hive_partitioning_options", value=hive_partitioning_options, expected_type=type_hints["hive_partitioning_options"])
            check_type(argname="argument ignore_unknown_values", value=ignore_unknown_values, expected_type=type_hints["ignore_unknown_values"])
            check_type(argname="argument max_bad_records", value=max_bad_records, expected_type=type_hints["max_bad_records"])
            check_type(argname="argument schema", value=schema, expected_type=type_hints["schema"])
        self._values: typing.Dict[str, typing.Any] = {
            "autodetect": autodetect,
            "source_format": source_format,
            "source_uris": source_uris,
        }
        if compression is not None:
            self._values["compression"] = compression
        if connection_id is not None:
            self._values["connection_id"] = connection_id
        if csv_options is not None:
            self._values["csv_options"] = csv_options
        if google_sheets_options is not None:
            self._values["google_sheets_options"] = google_sheets_options
        if hive_partitioning_options is not None:
            self._values["hive_partitioning_options"] = hive_partitioning_options
        if ignore_unknown_values is not None:
            self._values["ignore_unknown_values"] = ignore_unknown_values
        if max_bad_records is not None:
            self._values["max_bad_records"] = max_bad_records
        if schema is not None:
            self._values["schema"] = schema

    @builtins.property
    def autodetect(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        '''Let BigQuery try to autodetect the schema and format of the table.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#autodetect GoogleBigqueryTable#autodetect}
        '''
        result = self._values.get("autodetect")
        assert result is not None, "Required property 'autodetect' is missing"
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], result)

    @builtins.property
    def source_format(self) -> builtins.str:
        '''The data format.

        Supported values are: "CSV", "GOOGLE_SHEETS", "NEWLINE_DELIMITED_JSON", "AVRO", "PARQUET", "ORC" and "DATASTORE_BACKUP". To use "GOOGLE_SHEETS" the scopes must include "googleapis.com/auth/drive.readonly".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#source_format GoogleBigqueryTable#source_format}
        '''
        result = self._values.get("source_format")
        assert result is not None, "Required property 'source_format' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def source_uris(self) -> typing.List[builtins.str]:
        '''A list of the fully-qualified URIs that point to your data in Google Cloud.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#source_uris GoogleBigqueryTable#source_uris}
        '''
        result = self._values.get("source_uris")
        assert result is not None, "Required property 'source_uris' is missing"
        return typing.cast(typing.List[builtins.str], result)

    @builtins.property
    def compression(self) -> typing.Optional[builtins.str]:
        '''The compression type of the data source. Valid values are "NONE" or "GZIP".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#compression GoogleBigqueryTable#compression}
        '''
        result = self._values.get("compression")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def connection_id(self) -> typing.Optional[builtins.str]:
        '''The connection specifying the credentials to be used to read external storage, such as Azure Blob, Cloud Storage, or S3.

        The connectionId can have the form "{{project}}.{{location}}.{{connection_id}}" or "projects/{{project}}/locations/{{location}}/connections/{{connection_id}}".

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#connection_id GoogleBigqueryTable#connection_id}
        '''
        result = self._values.get("connection_id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def csv_options(
        self,
    ) -> typing.Optional["GoogleBigqueryTableExternalDataConfigurationCsvOptions"]:
        '''csv_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#csv_options GoogleBigqueryTable#csv_options}
        '''
        result = self._values.get("csv_options")
        return typing.cast(typing.Optional["GoogleBigqueryTableExternalDataConfigurationCsvOptions"], result)

    @builtins.property
    def google_sheets_options(
        self,
    ) -> typing.Optional["GoogleBigqueryTableExternalDataConfigurationGoogleSheetsOptions"]:
        '''google_sheets_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#google_sheets_options GoogleBigqueryTable#google_sheets_options}
        '''
        result = self._values.get("google_sheets_options")
        return typing.cast(typing.Optional["GoogleBigqueryTableExternalDataConfigurationGoogleSheetsOptions"], result)

    @builtins.property
    def hive_partitioning_options(
        self,
    ) -> typing.Optional["GoogleBigqueryTableExternalDataConfigurationHivePartitioningOptions"]:
        '''hive_partitioning_options block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#hive_partitioning_options GoogleBigqueryTable#hive_partitioning_options}
        '''
        result = self._values.get("hive_partitioning_options")
        return typing.cast(typing.Optional["GoogleBigqueryTableExternalDataConfigurationHivePartitioningOptions"], result)

    @builtins.property
    def ignore_unknown_values(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Indicates if BigQuery should allow extra values that are not represented in the table schema.

        If true, the extra values are ignored. If false, records with extra columns are treated as bad records, and if there are too many bad records, an invalid error is returned in the job result. The default value is false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#ignore_unknown_values GoogleBigqueryTable#ignore_unknown_values}
        '''
        result = self._values.get("ignore_unknown_values")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def max_bad_records(self) -> typing.Optional[jsii.Number]:
        '''The maximum number of bad records that BigQuery can ignore when reading data.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#max_bad_records GoogleBigqueryTable#max_bad_records}
        '''
        result = self._values.get("max_bad_records")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def schema(self) -> typing.Optional[builtins.str]:
        '''A JSON schema for the external table.

        Schema is required for CSV and JSON formats and is disallowed for Google Cloud Bigtable, Cloud Datastore backups, and Avro formats when using external tables.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#schema GoogleBigqueryTable#schema}
        '''
        result = self._values.get("schema")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryTableExternalDataConfiguration(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableExternalDataConfigurationCsvOptions",
    jsii_struct_bases=[],
    name_mapping={
        "quote": "quote",
        "allow_jagged_rows": "allowJaggedRows",
        "allow_quoted_newlines": "allowQuotedNewlines",
        "encoding": "encoding",
        "field_delimiter": "fieldDelimiter",
        "skip_leading_rows": "skipLeadingRows",
    },
)
class GoogleBigqueryTableExternalDataConfigurationCsvOptions:
    def __init__(
        self,
        *,
        quote: builtins.str,
        allow_jagged_rows: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_quoted_newlines: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        encoding: typing.Optional[builtins.str] = None,
        field_delimiter: typing.Optional[builtins.str] = None,
        skip_leading_rows: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param quote: The value that is used to quote data sections in a CSV file. If your data does not contain quoted sections, set the property value to an empty string. If your data contains quoted newline characters, you must also set the allow_quoted_newlines property to true. The API-side default is ", specified in Terraform escaped as ". Due to limitations with Terraform default values, this value is required to be explicitly set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#quote GoogleBigqueryTable#quote}
        :param allow_jagged_rows: Indicates if BigQuery should accept rows that are missing trailing optional columns. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#allow_jagged_rows GoogleBigqueryTable#allow_jagged_rows}
        :param allow_quoted_newlines: Indicates if BigQuery should allow quoted data sections that contain newline characters in a CSV file. The default value is false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#allow_quoted_newlines GoogleBigqueryTable#allow_quoted_newlines}
        :param encoding: The character encoding of the data. The supported values are UTF-8 or ISO-8859-1. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#encoding GoogleBigqueryTable#encoding}
        :param field_delimiter: The separator for fields in a CSV file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#field_delimiter GoogleBigqueryTable#field_delimiter}
        :param skip_leading_rows: The number of rows at the top of a CSV file that BigQuery will skip when reading the data. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#skip_leading_rows GoogleBigqueryTable#skip_leading_rows}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryTableExternalDataConfigurationCsvOptions.__init__)
            check_type(argname="argument quote", value=quote, expected_type=type_hints["quote"])
            check_type(argname="argument allow_jagged_rows", value=allow_jagged_rows, expected_type=type_hints["allow_jagged_rows"])
            check_type(argname="argument allow_quoted_newlines", value=allow_quoted_newlines, expected_type=type_hints["allow_quoted_newlines"])
            check_type(argname="argument encoding", value=encoding, expected_type=type_hints["encoding"])
            check_type(argname="argument field_delimiter", value=field_delimiter, expected_type=type_hints["field_delimiter"])
            check_type(argname="argument skip_leading_rows", value=skip_leading_rows, expected_type=type_hints["skip_leading_rows"])
        self._values: typing.Dict[str, typing.Any] = {
            "quote": quote,
        }
        if allow_jagged_rows is not None:
            self._values["allow_jagged_rows"] = allow_jagged_rows
        if allow_quoted_newlines is not None:
            self._values["allow_quoted_newlines"] = allow_quoted_newlines
        if encoding is not None:
            self._values["encoding"] = encoding
        if field_delimiter is not None:
            self._values["field_delimiter"] = field_delimiter
        if skip_leading_rows is not None:
            self._values["skip_leading_rows"] = skip_leading_rows

    @builtins.property
    def quote(self) -> builtins.str:
        '''The value that is used to quote data sections in a CSV file.

        If your data does not contain quoted sections, set the property value to an empty string. If your data contains quoted newline characters, you must also set the allow_quoted_newlines property to true. The API-side default is ", specified in Terraform escaped as ". Due to limitations with Terraform default values, this value is required to be explicitly set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#quote GoogleBigqueryTable#quote}
        '''
        result = self._values.get("quote")
        assert result is not None, "Required property 'quote' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def allow_jagged_rows(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Indicates if BigQuery should accept rows that are missing trailing optional columns.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#allow_jagged_rows GoogleBigqueryTable#allow_jagged_rows}
        '''
        result = self._values.get("allow_jagged_rows")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def allow_quoted_newlines(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Indicates if BigQuery should allow quoted data sections that contain newline characters in a CSV file.

        The default value is false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#allow_quoted_newlines GoogleBigqueryTable#allow_quoted_newlines}
        '''
        result = self._values.get("allow_quoted_newlines")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def encoding(self) -> typing.Optional[builtins.str]:
        '''The character encoding of the data. The supported values are UTF-8 or ISO-8859-1.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#encoding GoogleBigqueryTable#encoding}
        '''
        result = self._values.get("encoding")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def field_delimiter(self) -> typing.Optional[builtins.str]:
        '''The separator for fields in a CSV file.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#field_delimiter GoogleBigqueryTable#field_delimiter}
        '''
        result = self._values.get("field_delimiter")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def skip_leading_rows(self) -> typing.Optional[jsii.Number]:
        '''The number of rows at the top of a CSV file that BigQuery will skip when reading the data.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#skip_leading_rows GoogleBigqueryTable#skip_leading_rows}
        '''
        result = self._values.get("skip_leading_rows")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryTableExternalDataConfigurationCsvOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryTableExternalDataConfigurationCsvOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableExternalDataConfigurationCsvOptionsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleBigqueryTableExternalDataConfigurationCsvOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetAllowJaggedRows")
    def reset_allow_jagged_rows(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowJaggedRows", []))

    @jsii.member(jsii_name="resetAllowQuotedNewlines")
    def reset_allow_quoted_newlines(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetAllowQuotedNewlines", []))

    @jsii.member(jsii_name="resetEncoding")
    def reset_encoding(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEncoding", []))

    @jsii.member(jsii_name="resetFieldDelimiter")
    def reset_field_delimiter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFieldDelimiter", []))

    @jsii.member(jsii_name="resetSkipLeadingRows")
    def reset_skip_leading_rows(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSkipLeadingRows", []))

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
    @jsii.member(jsii_name="encodingInput")
    def encoding_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "encodingInput"))

    @builtins.property
    @jsii.member(jsii_name="fieldDelimiterInput")
    def field_delimiter_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fieldDelimiterInput"))

    @builtins.property
    @jsii.member(jsii_name="quoteInput")
    def quote_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "quoteInput"))

    @builtins.property
    @jsii.member(jsii_name="skipLeadingRowsInput")
    def skip_leading_rows_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "skipLeadingRowsInput"))

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
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTableExternalDataConfigurationCsvOptionsOutputReference, "allow_jagged_rows").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTableExternalDataConfigurationCsvOptionsOutputReference, "allow_quoted_newlines").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "allowQuotedNewlines", value)

    @builtins.property
    @jsii.member(jsii_name="encoding")
    def encoding(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "encoding"))

    @encoding.setter
    def encoding(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTableExternalDataConfigurationCsvOptionsOutputReference, "encoding").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "encoding", value)

    @builtins.property
    @jsii.member(jsii_name="fieldDelimiter")
    def field_delimiter(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "fieldDelimiter"))

    @field_delimiter.setter
    def field_delimiter(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTableExternalDataConfigurationCsvOptionsOutputReference, "field_delimiter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fieldDelimiter", value)

    @builtins.property
    @jsii.member(jsii_name="quote")
    def quote(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "quote"))

    @quote.setter
    def quote(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTableExternalDataConfigurationCsvOptionsOutputReference, "quote").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "quote", value)

    @builtins.property
    @jsii.member(jsii_name="skipLeadingRows")
    def skip_leading_rows(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "skipLeadingRows"))

    @skip_leading_rows.setter
    def skip_leading_rows(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTableExternalDataConfigurationCsvOptionsOutputReference, "skip_leading_rows").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skipLeadingRows", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleBigqueryTableExternalDataConfigurationCsvOptions]:
        return typing.cast(typing.Optional[GoogleBigqueryTableExternalDataConfigurationCsvOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryTableExternalDataConfigurationCsvOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTableExternalDataConfigurationCsvOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableExternalDataConfigurationGoogleSheetsOptions",
    jsii_struct_bases=[],
    name_mapping={"range": "range", "skip_leading_rows": "skipLeadingRows"},
)
class GoogleBigqueryTableExternalDataConfigurationGoogleSheetsOptions:
    def __init__(
        self,
        *,
        range: typing.Optional[builtins.str] = None,
        skip_leading_rows: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param range: Range of a sheet to query from. Only used when non-empty. At least one of range or skip_leading_rows must be set. Typical format: "sheet_name!top_left_cell_id:bottom_right_cell_id" For example: "sheet1!A1:B20" Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#range GoogleBigqueryTable#range}
        :param skip_leading_rows: The number of rows at the top of the sheet that BigQuery will skip when reading the data. At least one of range or skip_leading_rows must be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#skip_leading_rows GoogleBigqueryTable#skip_leading_rows}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryTableExternalDataConfigurationGoogleSheetsOptions.__init__)
            check_type(argname="argument range", value=range, expected_type=type_hints["range"])
            check_type(argname="argument skip_leading_rows", value=skip_leading_rows, expected_type=type_hints["skip_leading_rows"])
        self._values: typing.Dict[str, typing.Any] = {}
        if range is not None:
            self._values["range"] = range
        if skip_leading_rows is not None:
            self._values["skip_leading_rows"] = skip_leading_rows

    @builtins.property
    def range(self) -> typing.Optional[builtins.str]:
        '''Range of a sheet to query from.

        Only used when non-empty. At least one of range or skip_leading_rows must be set. Typical format: "sheet_name!top_left_cell_id:bottom_right_cell_id" For example: "sheet1!A1:B20"

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#range GoogleBigqueryTable#range}
        '''
        result = self._values.get("range")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def skip_leading_rows(self) -> typing.Optional[jsii.Number]:
        '''The number of rows at the top of the sheet that BigQuery will skip when reading the data.

        At least one of range or skip_leading_rows must be set.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#skip_leading_rows GoogleBigqueryTable#skip_leading_rows}
        '''
        result = self._values.get("skip_leading_rows")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryTableExternalDataConfigurationGoogleSheetsOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryTableExternalDataConfigurationGoogleSheetsOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableExternalDataConfigurationGoogleSheetsOptionsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleBigqueryTableExternalDataConfigurationGoogleSheetsOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetRange")
    def reset_range(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRange", []))

    @jsii.member(jsii_name="resetSkipLeadingRows")
    def reset_skip_leading_rows(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSkipLeadingRows", []))

    @builtins.property
    @jsii.member(jsii_name="rangeInput")
    def range_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "rangeInput"))

    @builtins.property
    @jsii.member(jsii_name="skipLeadingRowsInput")
    def skip_leading_rows_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "skipLeadingRowsInput"))

    @builtins.property
    @jsii.member(jsii_name="range")
    def range(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "range"))

    @range.setter
    def range(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTableExternalDataConfigurationGoogleSheetsOptionsOutputReference, "range").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "range", value)

    @builtins.property
    @jsii.member(jsii_name="skipLeadingRows")
    def skip_leading_rows(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "skipLeadingRows"))

    @skip_leading_rows.setter
    def skip_leading_rows(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTableExternalDataConfigurationGoogleSheetsOptionsOutputReference, "skip_leading_rows").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "skipLeadingRows", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleBigqueryTableExternalDataConfigurationGoogleSheetsOptions]:
        return typing.cast(typing.Optional[GoogleBigqueryTableExternalDataConfigurationGoogleSheetsOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryTableExternalDataConfigurationGoogleSheetsOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTableExternalDataConfigurationGoogleSheetsOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableExternalDataConfigurationHivePartitioningOptions",
    jsii_struct_bases=[],
    name_mapping={
        "mode": "mode",
        "require_partition_filter": "requirePartitionFilter",
        "source_uri_prefix": "sourceUriPrefix",
    },
)
class GoogleBigqueryTableExternalDataConfigurationHivePartitioningOptions:
    def __init__(
        self,
        *,
        mode: typing.Optional[builtins.str] = None,
        require_partition_filter: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        source_uri_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param mode: When set, what mode of hive partitioning to use when reading data. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#mode GoogleBigqueryTable#mode}
        :param require_partition_filter: If set to true, queries over this table require a partition filter that can be used for partition elimination to be specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#require_partition_filter GoogleBigqueryTable#require_partition_filter}
        :param source_uri_prefix: When hive partition detection is requested, a common for all source uris must be required. The prefix must end immediately before the partition key encoding begins. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#source_uri_prefix GoogleBigqueryTable#source_uri_prefix}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryTableExternalDataConfigurationHivePartitioningOptions.__init__)
            check_type(argname="argument mode", value=mode, expected_type=type_hints["mode"])
            check_type(argname="argument require_partition_filter", value=require_partition_filter, expected_type=type_hints["require_partition_filter"])
            check_type(argname="argument source_uri_prefix", value=source_uri_prefix, expected_type=type_hints["source_uri_prefix"])
        self._values: typing.Dict[str, typing.Any] = {}
        if mode is not None:
            self._values["mode"] = mode
        if require_partition_filter is not None:
            self._values["require_partition_filter"] = require_partition_filter
        if source_uri_prefix is not None:
            self._values["source_uri_prefix"] = source_uri_prefix

    @builtins.property
    def mode(self) -> typing.Optional[builtins.str]:
        '''When set, what mode of hive partitioning to use when reading data.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#mode GoogleBigqueryTable#mode}
        '''
        result = self._values.get("mode")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def require_partition_filter(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If set to true, queries over this table require a partition filter that can be used for partition elimination to be specified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#require_partition_filter GoogleBigqueryTable#require_partition_filter}
        '''
        result = self._values.get("require_partition_filter")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def source_uri_prefix(self) -> typing.Optional[builtins.str]:
        '''When hive partition detection is requested, a common for all source uris must be required.

        The prefix must end immediately before the partition key encoding begins.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#source_uri_prefix GoogleBigqueryTable#source_uri_prefix}
        '''
        result = self._values.get("source_uri_prefix")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryTableExternalDataConfigurationHivePartitioningOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryTableExternalDataConfigurationHivePartitioningOptionsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableExternalDataConfigurationHivePartitioningOptionsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleBigqueryTableExternalDataConfigurationHivePartitioningOptionsOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetMode")
    def reset_mode(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMode", []))

    @jsii.member(jsii_name="resetRequirePartitionFilter")
    def reset_require_partition_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequirePartitionFilter", []))

    @jsii.member(jsii_name="resetSourceUriPrefix")
    def reset_source_uri_prefix(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSourceUriPrefix", []))

    @builtins.property
    @jsii.member(jsii_name="modeInput")
    def mode_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "modeInput"))

    @builtins.property
    @jsii.member(jsii_name="requirePartitionFilterInput")
    def require_partition_filter_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "requirePartitionFilterInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceUriPrefixInput")
    def source_uri_prefix_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceUriPrefixInput"))

    @builtins.property
    @jsii.member(jsii_name="mode")
    def mode(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mode"))

    @mode.setter
    def mode(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTableExternalDataConfigurationHivePartitioningOptionsOutputReference, "mode").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mode", value)

    @builtins.property
    @jsii.member(jsii_name="requirePartitionFilter")
    def require_partition_filter(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "requirePartitionFilter"))

    @require_partition_filter.setter
    def require_partition_filter(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTableExternalDataConfigurationHivePartitioningOptionsOutputReference, "require_partition_filter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requirePartitionFilter", value)

    @builtins.property
    @jsii.member(jsii_name="sourceUriPrefix")
    def source_uri_prefix(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceUriPrefix"))

    @source_uri_prefix.setter
    def source_uri_prefix(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTableExternalDataConfigurationHivePartitioningOptionsOutputReference, "source_uri_prefix").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceUriPrefix", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleBigqueryTableExternalDataConfigurationHivePartitioningOptions]:
        return typing.cast(typing.Optional[GoogleBigqueryTableExternalDataConfigurationHivePartitioningOptions], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryTableExternalDataConfigurationHivePartitioningOptions],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTableExternalDataConfigurationHivePartitioningOptionsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleBigqueryTableExternalDataConfigurationOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableExternalDataConfigurationOutputReference",
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
            type_hints = typing.get_type_hints(GoogleBigqueryTableExternalDataConfigurationOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putCsvOptions")
    def put_csv_options(
        self,
        *,
        quote: builtins.str,
        allow_jagged_rows: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        allow_quoted_newlines: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        encoding: typing.Optional[builtins.str] = None,
        field_delimiter: typing.Optional[builtins.str] = None,
        skip_leading_rows: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param quote: The value that is used to quote data sections in a CSV file. If your data does not contain quoted sections, set the property value to an empty string. If your data contains quoted newline characters, you must also set the allow_quoted_newlines property to true. The API-side default is ", specified in Terraform escaped as ". Due to limitations with Terraform default values, this value is required to be explicitly set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#quote GoogleBigqueryTable#quote}
        :param allow_jagged_rows: Indicates if BigQuery should accept rows that are missing trailing optional columns. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#allow_jagged_rows GoogleBigqueryTable#allow_jagged_rows}
        :param allow_quoted_newlines: Indicates if BigQuery should allow quoted data sections that contain newline characters in a CSV file. The default value is false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#allow_quoted_newlines GoogleBigqueryTable#allow_quoted_newlines}
        :param encoding: The character encoding of the data. The supported values are UTF-8 or ISO-8859-1. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#encoding GoogleBigqueryTable#encoding}
        :param field_delimiter: The separator for fields in a CSV file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#field_delimiter GoogleBigqueryTable#field_delimiter}
        :param skip_leading_rows: The number of rows at the top of a CSV file that BigQuery will skip when reading the data. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#skip_leading_rows GoogleBigqueryTable#skip_leading_rows}
        '''
        value = GoogleBigqueryTableExternalDataConfigurationCsvOptions(
            quote=quote,
            allow_jagged_rows=allow_jagged_rows,
            allow_quoted_newlines=allow_quoted_newlines,
            encoding=encoding,
            field_delimiter=field_delimiter,
            skip_leading_rows=skip_leading_rows,
        )

        return typing.cast(None, jsii.invoke(self, "putCsvOptions", [value]))

    @jsii.member(jsii_name="putGoogleSheetsOptions")
    def put_google_sheets_options(
        self,
        *,
        range: typing.Optional[builtins.str] = None,
        skip_leading_rows: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param range: Range of a sheet to query from. Only used when non-empty. At least one of range or skip_leading_rows must be set. Typical format: "sheet_name!top_left_cell_id:bottom_right_cell_id" For example: "sheet1!A1:B20" Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#range GoogleBigqueryTable#range}
        :param skip_leading_rows: The number of rows at the top of the sheet that BigQuery will skip when reading the data. At least one of range or skip_leading_rows must be set. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#skip_leading_rows GoogleBigqueryTable#skip_leading_rows}
        '''
        value = GoogleBigqueryTableExternalDataConfigurationGoogleSheetsOptions(
            range=range, skip_leading_rows=skip_leading_rows
        )

        return typing.cast(None, jsii.invoke(self, "putGoogleSheetsOptions", [value]))

    @jsii.member(jsii_name="putHivePartitioningOptions")
    def put_hive_partitioning_options(
        self,
        *,
        mode: typing.Optional[builtins.str] = None,
        require_partition_filter: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        source_uri_prefix: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param mode: When set, what mode of hive partitioning to use when reading data. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#mode GoogleBigqueryTable#mode}
        :param require_partition_filter: If set to true, queries over this table require a partition filter that can be used for partition elimination to be specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#require_partition_filter GoogleBigqueryTable#require_partition_filter}
        :param source_uri_prefix: When hive partition detection is requested, a common for all source uris must be required. The prefix must end immediately before the partition key encoding begins. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#source_uri_prefix GoogleBigqueryTable#source_uri_prefix}
        '''
        value = GoogleBigqueryTableExternalDataConfigurationHivePartitioningOptions(
            mode=mode,
            require_partition_filter=require_partition_filter,
            source_uri_prefix=source_uri_prefix,
        )

        return typing.cast(None, jsii.invoke(self, "putHivePartitioningOptions", [value]))

    @jsii.member(jsii_name="resetCompression")
    def reset_compression(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCompression", []))

    @jsii.member(jsii_name="resetConnectionId")
    def reset_connection_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetConnectionId", []))

    @jsii.member(jsii_name="resetCsvOptions")
    def reset_csv_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetCsvOptions", []))

    @jsii.member(jsii_name="resetGoogleSheetsOptions")
    def reset_google_sheets_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetGoogleSheetsOptions", []))

    @jsii.member(jsii_name="resetHivePartitioningOptions")
    def reset_hive_partitioning_options(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHivePartitioningOptions", []))

    @jsii.member(jsii_name="resetIgnoreUnknownValues")
    def reset_ignore_unknown_values(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetIgnoreUnknownValues", []))

    @jsii.member(jsii_name="resetMaxBadRecords")
    def reset_max_bad_records(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMaxBadRecords", []))

    @jsii.member(jsii_name="resetSchema")
    def reset_schema(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSchema", []))

    @builtins.property
    @jsii.member(jsii_name="csvOptions")
    def csv_options(
        self,
    ) -> GoogleBigqueryTableExternalDataConfigurationCsvOptionsOutputReference:
        return typing.cast(GoogleBigqueryTableExternalDataConfigurationCsvOptionsOutputReference, jsii.get(self, "csvOptions"))

    @builtins.property
    @jsii.member(jsii_name="googleSheetsOptions")
    def google_sheets_options(
        self,
    ) -> GoogleBigqueryTableExternalDataConfigurationGoogleSheetsOptionsOutputReference:
        return typing.cast(GoogleBigqueryTableExternalDataConfigurationGoogleSheetsOptionsOutputReference, jsii.get(self, "googleSheetsOptions"))

    @builtins.property
    @jsii.member(jsii_name="hivePartitioningOptions")
    def hive_partitioning_options(
        self,
    ) -> GoogleBigqueryTableExternalDataConfigurationHivePartitioningOptionsOutputReference:
        return typing.cast(GoogleBigqueryTableExternalDataConfigurationHivePartitioningOptionsOutputReference, jsii.get(self, "hivePartitioningOptions"))

    @builtins.property
    @jsii.member(jsii_name="autodetectInput")
    def autodetect_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "autodetectInput"))

    @builtins.property
    @jsii.member(jsii_name="compressionInput")
    def compression_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "compressionInput"))

    @builtins.property
    @jsii.member(jsii_name="connectionIdInput")
    def connection_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "connectionIdInput"))

    @builtins.property
    @jsii.member(jsii_name="csvOptionsInput")
    def csv_options_input(
        self,
    ) -> typing.Optional[GoogleBigqueryTableExternalDataConfigurationCsvOptions]:
        return typing.cast(typing.Optional[GoogleBigqueryTableExternalDataConfigurationCsvOptions], jsii.get(self, "csvOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="googleSheetsOptionsInput")
    def google_sheets_options_input(
        self,
    ) -> typing.Optional[GoogleBigqueryTableExternalDataConfigurationGoogleSheetsOptions]:
        return typing.cast(typing.Optional[GoogleBigqueryTableExternalDataConfigurationGoogleSheetsOptions], jsii.get(self, "googleSheetsOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="hivePartitioningOptionsInput")
    def hive_partitioning_options_input(
        self,
    ) -> typing.Optional[GoogleBigqueryTableExternalDataConfigurationHivePartitioningOptions]:
        return typing.cast(typing.Optional[GoogleBigqueryTableExternalDataConfigurationHivePartitioningOptions], jsii.get(self, "hivePartitioningOptionsInput"))

    @builtins.property
    @jsii.member(jsii_name="ignoreUnknownValuesInput")
    def ignore_unknown_values_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "ignoreUnknownValuesInput"))

    @builtins.property
    @jsii.member(jsii_name="maxBadRecordsInput")
    def max_bad_records_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxBadRecordsInput"))

    @builtins.property
    @jsii.member(jsii_name="schemaInput")
    def schema_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "schemaInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceFormatInput")
    def source_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "sourceFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="sourceUrisInput")
    def source_uris_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "sourceUrisInput"))

    @builtins.property
    @jsii.member(jsii_name="autodetect")
    def autodetect(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "autodetect"))

    @autodetect.setter
    def autodetect(self, value: typing.Union[builtins.bool, cdktf.IResolvable]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTableExternalDataConfigurationOutputReference, "autodetect").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "autodetect", value)

    @builtins.property
    @jsii.member(jsii_name="compression")
    def compression(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "compression"))

    @compression.setter
    def compression(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTableExternalDataConfigurationOutputReference, "compression").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "compression", value)

    @builtins.property
    @jsii.member(jsii_name="connectionId")
    def connection_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "connectionId"))

    @connection_id.setter
    def connection_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTableExternalDataConfigurationOutputReference, "connection_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "connectionId", value)

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
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTableExternalDataConfigurationOutputReference, "ignore_unknown_values").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "ignoreUnknownValues", value)

    @builtins.property
    @jsii.member(jsii_name="maxBadRecords")
    def max_bad_records(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxBadRecords"))

    @max_bad_records.setter
    def max_bad_records(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTableExternalDataConfigurationOutputReference, "max_bad_records").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxBadRecords", value)

    @builtins.property
    @jsii.member(jsii_name="schema")
    def schema(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "schema"))

    @schema.setter
    def schema(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTableExternalDataConfigurationOutputReference, "schema").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "schema", value)

    @builtins.property
    @jsii.member(jsii_name="sourceFormat")
    def source_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "sourceFormat"))

    @source_format.setter
    def source_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTableExternalDataConfigurationOutputReference, "source_format").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceFormat", value)

    @builtins.property
    @jsii.member(jsii_name="sourceUris")
    def source_uris(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "sourceUris"))

    @source_uris.setter
    def source_uris(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTableExternalDataConfigurationOutputReference, "source_uris").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "sourceUris", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleBigqueryTableExternalDataConfiguration]:
        return typing.cast(typing.Optional[GoogleBigqueryTableExternalDataConfiguration], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryTableExternalDataConfiguration],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTableExternalDataConfigurationOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableMaterializedView",
    jsii_struct_bases=[],
    name_mapping={
        "query": "query",
        "enable_refresh": "enableRefresh",
        "refresh_interval_ms": "refreshIntervalMs",
    },
)
class GoogleBigqueryTableMaterializedView:
    def __init__(
        self,
        *,
        query: builtins.str,
        enable_refresh: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        refresh_interval_ms: typing.Optional[jsii.Number] = None,
    ) -> None:
        '''
        :param query: A query whose result is persisted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#query GoogleBigqueryTable#query}
        :param enable_refresh: Specifies if BigQuery should automatically refresh materialized view when the base table is updated. The default is true. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#enable_refresh GoogleBigqueryTable#enable_refresh}
        :param refresh_interval_ms: Specifies maximum frequency at which this materialized view will be refreshed. The default is 1800000. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#refresh_interval_ms GoogleBigqueryTable#refresh_interval_ms}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryTableMaterializedView.__init__)
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
            check_type(argname="argument enable_refresh", value=enable_refresh, expected_type=type_hints["enable_refresh"])
            check_type(argname="argument refresh_interval_ms", value=refresh_interval_ms, expected_type=type_hints["refresh_interval_ms"])
        self._values: typing.Dict[str, typing.Any] = {
            "query": query,
        }
        if enable_refresh is not None:
            self._values["enable_refresh"] = enable_refresh
        if refresh_interval_ms is not None:
            self._values["refresh_interval_ms"] = refresh_interval_ms

    @builtins.property
    def query(self) -> builtins.str:
        '''A query whose result is persisted.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#query GoogleBigqueryTable#query}
        '''
        result = self._values.get("query")
        assert result is not None, "Required property 'query' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def enable_refresh(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specifies if BigQuery should automatically refresh materialized view when the base table is updated. The default is true.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#enable_refresh GoogleBigqueryTable#enable_refresh}
        '''
        result = self._values.get("enable_refresh")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def refresh_interval_ms(self) -> typing.Optional[jsii.Number]:
        '''Specifies maximum frequency at which this materialized view will be refreshed. The default is 1800000.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#refresh_interval_ms GoogleBigqueryTable#refresh_interval_ms}
        '''
        result = self._values.get("refresh_interval_ms")
        return typing.cast(typing.Optional[jsii.Number], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryTableMaterializedView(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryTableMaterializedViewOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableMaterializedViewOutputReference",
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
            type_hints = typing.get_type_hints(GoogleBigqueryTableMaterializedViewOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetEnableRefresh")
    def reset_enable_refresh(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetEnableRefresh", []))

    @jsii.member(jsii_name="resetRefreshIntervalMs")
    def reset_refresh_interval_ms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRefreshIntervalMs", []))

    @builtins.property
    @jsii.member(jsii_name="enableRefreshInput")
    def enable_refresh_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "enableRefreshInput"))

    @builtins.property
    @jsii.member(jsii_name="queryInput")
    def query_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="refreshIntervalMsInput")
    def refresh_interval_ms_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "refreshIntervalMsInput"))

    @builtins.property
    @jsii.member(jsii_name="enableRefresh")
    def enable_refresh(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "enableRefresh"))

    @enable_refresh.setter
    def enable_refresh(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTableMaterializedViewOutputReference, "enable_refresh").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "enableRefresh", value)

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "query"))

    @query.setter
    def query(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTableMaterializedViewOutputReference, "query").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "query", value)

    @builtins.property
    @jsii.member(jsii_name="refreshIntervalMs")
    def refresh_interval_ms(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "refreshIntervalMs"))

    @refresh_interval_ms.setter
    def refresh_interval_ms(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTableMaterializedViewOutputReference, "refresh_interval_ms").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "refreshIntervalMs", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleBigqueryTableMaterializedView]:
        return typing.cast(typing.Optional[GoogleBigqueryTableMaterializedView], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryTableMaterializedView],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTableMaterializedViewOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableRangePartitioning",
    jsii_struct_bases=[],
    name_mapping={"field": "field", "range": "range"},
)
class GoogleBigqueryTableRangePartitioning:
    def __init__(
        self,
        *,
        field: builtins.str,
        range: typing.Union["GoogleBigqueryTableRangePartitioningRange", typing.Dict[str, typing.Any]],
    ) -> None:
        '''
        :param field: The field used to determine how to create a range-based partition. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#field GoogleBigqueryTable#field}
        :param range: range block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#range GoogleBigqueryTable#range}
        '''
        if isinstance(range, dict):
            range = GoogleBigqueryTableRangePartitioningRange(**range)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryTableRangePartitioning.__init__)
            check_type(argname="argument field", value=field, expected_type=type_hints["field"])
            check_type(argname="argument range", value=range, expected_type=type_hints["range"])
        self._values: typing.Dict[str, typing.Any] = {
            "field": field,
            "range": range,
        }

    @builtins.property
    def field(self) -> builtins.str:
        '''The field used to determine how to create a range-based partition.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#field GoogleBigqueryTable#field}
        '''
        result = self._values.get("field")
        assert result is not None, "Required property 'field' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def range(self) -> "GoogleBigqueryTableRangePartitioningRange":
        '''range block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#range GoogleBigqueryTable#range}
        '''
        result = self._values.get("range")
        assert result is not None, "Required property 'range' is missing"
        return typing.cast("GoogleBigqueryTableRangePartitioningRange", result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryTableRangePartitioning(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryTableRangePartitioningOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableRangePartitioningOutputReference",
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
            type_hints = typing.get_type_hints(GoogleBigqueryTableRangePartitioningOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putRange")
    def put_range(
        self,
        *,
        end: jsii.Number,
        interval: jsii.Number,
        start: jsii.Number,
    ) -> None:
        '''
        :param end: End of the range partitioning, exclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#end GoogleBigqueryTable#end}
        :param interval: The width of each range within the partition. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#interval GoogleBigqueryTable#interval}
        :param start: Start of the range partitioning, inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#start GoogleBigqueryTable#start}
        '''
        value = GoogleBigqueryTableRangePartitioningRange(
            end=end, interval=interval, start=start
        )

        return typing.cast(None, jsii.invoke(self, "putRange", [value]))

    @builtins.property
    @jsii.member(jsii_name="range")
    def range(self) -> "GoogleBigqueryTableRangePartitioningRangeOutputReference":
        return typing.cast("GoogleBigqueryTableRangePartitioningRangeOutputReference", jsii.get(self, "range"))

    @builtins.property
    @jsii.member(jsii_name="fieldInput")
    def field_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fieldInput"))

    @builtins.property
    @jsii.member(jsii_name="rangeInput")
    def range_input(
        self,
    ) -> typing.Optional["GoogleBigqueryTableRangePartitioningRange"]:
        return typing.cast(typing.Optional["GoogleBigqueryTableRangePartitioningRange"], jsii.get(self, "rangeInput"))

    @builtins.property
    @jsii.member(jsii_name="field")
    def field(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "field"))

    @field.setter
    def field(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTableRangePartitioningOutputReference, "field").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "field", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleBigqueryTableRangePartitioning]:
        return typing.cast(typing.Optional[GoogleBigqueryTableRangePartitioning], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryTableRangePartitioning],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTableRangePartitioningOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableRangePartitioningRange",
    jsii_struct_bases=[],
    name_mapping={"end": "end", "interval": "interval", "start": "start"},
)
class GoogleBigqueryTableRangePartitioningRange:
    def __init__(
        self,
        *,
        end: jsii.Number,
        interval: jsii.Number,
        start: jsii.Number,
    ) -> None:
        '''
        :param end: End of the range partitioning, exclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#end GoogleBigqueryTable#end}
        :param interval: The width of each range within the partition. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#interval GoogleBigqueryTable#interval}
        :param start: Start of the range partitioning, inclusive. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#start GoogleBigqueryTable#start}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryTableRangePartitioningRange.__init__)
            check_type(argname="argument end", value=end, expected_type=type_hints["end"])
            check_type(argname="argument interval", value=interval, expected_type=type_hints["interval"])
            check_type(argname="argument start", value=start, expected_type=type_hints["start"])
        self._values: typing.Dict[str, typing.Any] = {
            "end": end,
            "interval": interval,
            "start": start,
        }

    @builtins.property
    def end(self) -> jsii.Number:
        '''End of the range partitioning, exclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#end GoogleBigqueryTable#end}
        '''
        result = self._values.get("end")
        assert result is not None, "Required property 'end' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def interval(self) -> jsii.Number:
        '''The width of each range within the partition.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#interval GoogleBigqueryTable#interval}
        '''
        result = self._values.get("interval")
        assert result is not None, "Required property 'interval' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def start(self) -> jsii.Number:
        '''Start of the range partitioning, inclusive.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#start GoogleBigqueryTable#start}
        '''
        result = self._values.get("start")
        assert result is not None, "Required property 'start' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryTableRangePartitioningRange(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryTableRangePartitioningRangeOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableRangePartitioningRangeOutputReference",
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
            type_hints = typing.get_type_hints(GoogleBigqueryTableRangePartitioningRangeOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="endInput")
    def end_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "endInput"))

    @builtins.property
    @jsii.member(jsii_name="intervalInput")
    def interval_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "intervalInput"))

    @builtins.property
    @jsii.member(jsii_name="startInput")
    def start_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "startInput"))

    @builtins.property
    @jsii.member(jsii_name="end")
    def end(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "end"))

    @end.setter
    def end(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTableRangePartitioningRangeOutputReference, "end").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "end", value)

    @builtins.property
    @jsii.member(jsii_name="interval")
    def interval(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "interval"))

    @interval.setter
    def interval(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTableRangePartitioningRangeOutputReference, "interval").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "interval", value)

    @builtins.property
    @jsii.member(jsii_name="start")
    def start(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "start"))

    @start.setter
    def start(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTableRangePartitioningRangeOutputReference, "start").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "start", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleBigqueryTableRangePartitioningRange]:
        return typing.cast(typing.Optional[GoogleBigqueryTableRangePartitioningRange], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryTableRangePartitioningRange],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTableRangePartitioningRangeOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableTimePartitioning",
    jsii_struct_bases=[],
    name_mapping={
        "type": "type",
        "expiration_ms": "expirationMs",
        "field": "field",
        "require_partition_filter": "requirePartitionFilter",
    },
)
class GoogleBigqueryTableTimePartitioning:
    def __init__(
        self,
        *,
        type: builtins.str,
        expiration_ms: typing.Optional[jsii.Number] = None,
        field: typing.Optional[builtins.str] = None,
        require_partition_filter: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param type: The supported types are DAY, HOUR, MONTH, and YEAR, which will generate one partition per day, hour, month, and year, respectively. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#type GoogleBigqueryTable#type}
        :param expiration_ms: Number of milliseconds for which to keep the storage for a partition. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#expiration_ms GoogleBigqueryTable#expiration_ms}
        :param field: The field used to determine how to create a time-based partition. If time-based partitioning is enabled without this value, the table is partitioned based on the load time. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#field GoogleBigqueryTable#field}
        :param require_partition_filter: If set to true, queries over this table require a partition filter that can be used for partition elimination to be specified. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#require_partition_filter GoogleBigqueryTable#require_partition_filter}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryTableTimePartitioning.__init__)
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument expiration_ms", value=expiration_ms, expected_type=type_hints["expiration_ms"])
            check_type(argname="argument field", value=field, expected_type=type_hints["field"])
            check_type(argname="argument require_partition_filter", value=require_partition_filter, expected_type=type_hints["require_partition_filter"])
        self._values: typing.Dict[str, typing.Any] = {
            "type": type,
        }
        if expiration_ms is not None:
            self._values["expiration_ms"] = expiration_ms
        if field is not None:
            self._values["field"] = field
        if require_partition_filter is not None:
            self._values["require_partition_filter"] = require_partition_filter

    @builtins.property
    def type(self) -> builtins.str:
        '''The supported types are DAY, HOUR, MONTH, and YEAR, which will generate one partition per day, hour, month, and year, respectively.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#type GoogleBigqueryTable#type}
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def expiration_ms(self) -> typing.Optional[jsii.Number]:
        '''Number of milliseconds for which to keep the storage for a partition.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#expiration_ms GoogleBigqueryTable#expiration_ms}
        '''
        result = self._values.get("expiration_ms")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def field(self) -> typing.Optional[builtins.str]:
        '''The field used to determine how to create a time-based partition.

        If time-based partitioning is enabled without this value, the table is partitioned based on the load time.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#field GoogleBigqueryTable#field}
        '''
        result = self._values.get("field")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def require_partition_filter(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''If set to true, queries over this table require a partition filter that can be used for partition elimination to be specified.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#require_partition_filter GoogleBigqueryTable#require_partition_filter}
        '''
        result = self._values.get("require_partition_filter")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryTableTimePartitioning(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryTableTimePartitioningOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableTimePartitioningOutputReference",
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
            type_hints = typing.get_type_hints(GoogleBigqueryTableTimePartitioningOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetExpirationMs")
    def reset_expiration_ms(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetExpirationMs", []))

    @jsii.member(jsii_name="resetField")
    def reset_field(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetField", []))

    @jsii.member(jsii_name="resetRequirePartitionFilter")
    def reset_require_partition_filter(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRequirePartitionFilter", []))

    @builtins.property
    @jsii.member(jsii_name="expirationMsInput")
    def expiration_ms_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "expirationMsInput"))

    @builtins.property
    @jsii.member(jsii_name="fieldInput")
    def field_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "fieldInput"))

    @builtins.property
    @jsii.member(jsii_name="requirePartitionFilterInput")
    def require_partition_filter_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "requirePartitionFilterInput"))

    @builtins.property
    @jsii.member(jsii_name="typeInput")
    def type_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "typeInput"))

    @builtins.property
    @jsii.member(jsii_name="expirationMs")
    def expiration_ms(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "expirationMs"))

    @expiration_ms.setter
    def expiration_ms(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTableTimePartitioningOutputReference, "expiration_ms").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "expirationMs", value)

    @builtins.property
    @jsii.member(jsii_name="field")
    def field(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "field"))

    @field.setter
    def field(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTableTimePartitioningOutputReference, "field").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "field", value)

    @builtins.property
    @jsii.member(jsii_name="requirePartitionFilter")
    def require_partition_filter(
        self,
    ) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "requirePartitionFilter"))

    @require_partition_filter.setter
    def require_partition_filter(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTableTimePartitioningOutputReference, "require_partition_filter").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "requirePartitionFilter", value)

    @builtins.property
    @jsii.member(jsii_name="type")
    def type(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "type"))

    @type.setter
    def type(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTableTimePartitioningOutputReference, "type").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "type", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleBigqueryTableTimePartitioning]:
        return typing.cast(typing.Optional[GoogleBigqueryTableTimePartitioning], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleBigqueryTableTimePartitioning],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTableTimePartitioningOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableView",
    jsii_struct_bases=[],
    name_mapping={"query": "query", "use_legacy_sql": "useLegacySql"},
)
class GoogleBigqueryTableView:
    def __init__(
        self,
        *,
        query: builtins.str,
        use_legacy_sql: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
    ) -> None:
        '''
        :param query: A query that BigQuery executes when the view is referenced. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#query GoogleBigqueryTable#query}
        :param use_legacy_sql: Specifies whether to use BigQuery's legacy SQL for this view. The default value is true. If set to false, the view will use BigQuery's standard SQL Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#use_legacy_sql GoogleBigqueryTable#use_legacy_sql}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleBigqueryTableView.__init__)
            check_type(argname="argument query", value=query, expected_type=type_hints["query"])
            check_type(argname="argument use_legacy_sql", value=use_legacy_sql, expected_type=type_hints["use_legacy_sql"])
        self._values: typing.Dict[str, typing.Any] = {
            "query": query,
        }
        if use_legacy_sql is not None:
            self._values["use_legacy_sql"] = use_legacy_sql

    @builtins.property
    def query(self) -> builtins.str:
        '''A query that BigQuery executes when the view is referenced.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#query GoogleBigqueryTable#query}
        '''
        result = self._values.get("query")
        assert result is not None, "Required property 'query' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def use_legacy_sql(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Specifies whether to use BigQuery's legacy SQL for this view.

        The default value is true. If set to false, the view will use BigQuery's standard SQL

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_bigquery_table#use_legacy_sql GoogleBigqueryTable#use_legacy_sql}
        '''
        result = self._values.get("use_legacy_sql")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleBigqueryTableView(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleBigqueryTableViewOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleBigqueryTable.GoogleBigqueryTableViewOutputReference",
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
            type_hints = typing.get_type_hints(GoogleBigqueryTableViewOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetUseLegacySql")
    def reset_use_legacy_sql(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetUseLegacySql", []))

    @builtins.property
    @jsii.member(jsii_name="queryInput")
    def query_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryInput"))

    @builtins.property
    @jsii.member(jsii_name="useLegacySqlInput")
    def use_legacy_sql_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "useLegacySqlInput"))

    @builtins.property
    @jsii.member(jsii_name="query")
    def query(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "query"))

    @query.setter
    def query(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTableViewOutputReference, "query").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "query", value)

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
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTableViewOutputReference, "use_legacy_sql").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "useLegacySql", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleBigqueryTableView]:
        return typing.cast(typing.Optional[GoogleBigqueryTableView], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[GoogleBigqueryTableView]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleBigqueryTableViewOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleBigqueryTable",
    "GoogleBigqueryTableConfig",
    "GoogleBigqueryTableEncryptionConfiguration",
    "GoogleBigqueryTableEncryptionConfigurationOutputReference",
    "GoogleBigqueryTableExternalDataConfiguration",
    "GoogleBigqueryTableExternalDataConfigurationCsvOptions",
    "GoogleBigqueryTableExternalDataConfigurationCsvOptionsOutputReference",
    "GoogleBigqueryTableExternalDataConfigurationGoogleSheetsOptions",
    "GoogleBigqueryTableExternalDataConfigurationGoogleSheetsOptionsOutputReference",
    "GoogleBigqueryTableExternalDataConfigurationHivePartitioningOptions",
    "GoogleBigqueryTableExternalDataConfigurationHivePartitioningOptionsOutputReference",
    "GoogleBigqueryTableExternalDataConfigurationOutputReference",
    "GoogleBigqueryTableMaterializedView",
    "GoogleBigqueryTableMaterializedViewOutputReference",
    "GoogleBigqueryTableRangePartitioning",
    "GoogleBigqueryTableRangePartitioningOutputReference",
    "GoogleBigqueryTableRangePartitioningRange",
    "GoogleBigqueryTableRangePartitioningRangeOutputReference",
    "GoogleBigqueryTableTimePartitioning",
    "GoogleBigqueryTableTimePartitioningOutputReference",
    "GoogleBigqueryTableView",
    "GoogleBigqueryTableViewOutputReference",
]

publication.publish()
