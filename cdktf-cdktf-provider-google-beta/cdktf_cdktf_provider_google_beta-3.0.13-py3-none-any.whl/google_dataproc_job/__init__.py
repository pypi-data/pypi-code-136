'''
# `google_dataproc_job`

Refer to the Terraform Registory for docs: [`google_dataproc_job`](https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job).
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


class GoogleDataprocJob(
    cdktf.TerraformResource,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocJob.GoogleDataprocJob",
):
    '''Represents a {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job google_dataproc_job}.'''

    def __init__(
        self,
        scope: constructs.Construct,
        id_: builtins.str,
        *,
        placement: typing.Union["GoogleDataprocJobPlacement", typing.Dict[str, typing.Any]],
        force_delete: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        hadoop_config: typing.Optional[typing.Union["GoogleDataprocJobHadoopConfig", typing.Dict[str, typing.Any]]] = None,
        hive_config: typing.Optional[typing.Union["GoogleDataprocJobHiveConfig", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        pig_config: typing.Optional[typing.Union["GoogleDataprocJobPigConfig", typing.Dict[str, typing.Any]]] = None,
        presto_config: typing.Optional[typing.Union["GoogleDataprocJobPrestoConfig", typing.Dict[str, typing.Any]]] = None,
        project: typing.Optional[builtins.str] = None,
        pyspark_config: typing.Optional[typing.Union["GoogleDataprocJobPysparkConfig", typing.Dict[str, typing.Any]]] = None,
        reference: typing.Optional[typing.Union["GoogleDataprocJobReference", typing.Dict[str, typing.Any]]] = None,
        region: typing.Optional[builtins.str] = None,
        scheduling: typing.Optional[typing.Union["GoogleDataprocJobScheduling", typing.Dict[str, typing.Any]]] = None,
        spark_config: typing.Optional[typing.Union["GoogleDataprocJobSparkConfig", typing.Dict[str, typing.Any]]] = None,
        sparksql_config: typing.Optional[typing.Union["GoogleDataprocJobSparksqlConfig", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["GoogleDataprocJobTimeouts", typing.Dict[str, typing.Any]]] = None,
        connection: typing.Optional[typing.Union[typing.Union[cdktf.SSHProvisionerConnection, typing.Dict[str, typing.Any]], typing.Union[cdktf.WinrmProvisionerConnection, typing.Dict[str, typing.Any]]]] = None,
        count: typing.Optional[jsii.Number] = None,
        depends_on: typing.Optional[typing.Sequence[cdktf.ITerraformDependable]] = None,
        for_each: typing.Optional[cdktf.ITerraformIterator] = None,
        lifecycle: typing.Optional[typing.Union[cdktf.TerraformResourceLifecycle, typing.Dict[str, typing.Any]]] = None,
        provider: typing.Optional[cdktf.TerraformProvider] = None,
        provisioners: typing.Optional[typing.Sequence[typing.Union[typing.Union[cdktf.FileProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.LocalExecProvisioner, typing.Dict[str, typing.Any]], typing.Union[cdktf.RemoteExecProvisioner, typing.Dict[str, typing.Any]]]]] = None,
    ) -> None:
        '''Create a new {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job google_dataproc_job} Resource.

        :param scope: The scope in which to define this construct.
        :param id_: The scoped construct ID. Must be unique amongst siblings in the same scope
        :param placement: placement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#placement GoogleDataprocJob#placement}
        :param force_delete: By default, you can only delete inactive jobs within Dataproc. Setting this to true, and calling destroy, will ensure that the job is first cancelled before issuing the delete. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#force_delete GoogleDataprocJob#force_delete}
        :param hadoop_config: hadoop_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#hadoop_config GoogleDataprocJob#hadoop_config}
        :param hive_config: hive_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#hive_config GoogleDataprocJob#hive_config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#id GoogleDataprocJob#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: Optional. The labels to associate with this job. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#labels GoogleDataprocJob#labels}
        :param pig_config: pig_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#pig_config GoogleDataprocJob#pig_config}
        :param presto_config: presto_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#presto_config GoogleDataprocJob#presto_config}
        :param project: The project in which the cluster can be found and jobs subsequently run against. If it is not provided, the provider project is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#project GoogleDataprocJob#project}
        :param pyspark_config: pyspark_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#pyspark_config GoogleDataprocJob#pyspark_config}
        :param reference: reference block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#reference GoogleDataprocJob#reference}
        :param region: The Cloud Dataproc region. This essentially determines which clusters are available for this job to be submitted to. If not specified, defaults to global. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#region GoogleDataprocJob#region}
        :param scheduling: scheduling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#scheduling GoogleDataprocJob#scheduling}
        :param spark_config: spark_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#spark_config GoogleDataprocJob#spark_config}
        :param sparksql_config: sparksql_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#sparksql_config GoogleDataprocJob#sparksql_config}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#timeouts GoogleDataprocJob#timeouts}
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocJob.__init__)
            check_type(argname="argument scope", value=scope, expected_type=type_hints["scope"])
            check_type(argname="argument id_", value=id_, expected_type=type_hints["id_"])
        config = GoogleDataprocJobConfig(
            placement=placement,
            force_delete=force_delete,
            hadoop_config=hadoop_config,
            hive_config=hive_config,
            id=id,
            labels=labels,
            pig_config=pig_config,
            presto_config=presto_config,
            project=project,
            pyspark_config=pyspark_config,
            reference=reference,
            region=region,
            scheduling=scheduling,
            spark_config=spark_config,
            sparksql_config=sparksql_config,
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

    @jsii.member(jsii_name="putHadoopConfig")
    def put_hadoop_config(
        self,
        *,
        archive_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        file_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        jar_file_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        logging_config: typing.Optional[typing.Union["GoogleDataprocJobHadoopConfigLoggingConfig", typing.Dict[str, typing.Any]]] = None,
        main_class: typing.Optional[builtins.str] = None,
        main_jar_file_uri: typing.Optional[builtins.str] = None,
        properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param archive_uris: HCFS URIs of archives to be extracted in the working directory of .jar, .tar, .tar.gz, .tgz, and .zip. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#archive_uris GoogleDataprocJob#archive_uris}
        :param args: The arguments to pass to the driver. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#args GoogleDataprocJob#args}
        :param file_uris: HCFS URIs of files to be copied to the working directory of Spark drivers and distributed tasks. Useful for naively parallel tasks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#file_uris GoogleDataprocJob#file_uris}
        :param jar_file_uris: HCFS URIs of jar files to add to the CLASSPATHs of the Spark driver and tasks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#jar_file_uris GoogleDataprocJob#jar_file_uris}
        :param logging_config: logging_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#logging_config GoogleDataprocJob#logging_config}
        :param main_class: The class containing the main method of the driver. Must be in a provided jar or jar that is already on the classpath. Conflicts with main_jar_file_uri Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#main_class GoogleDataprocJob#main_class}
        :param main_jar_file_uri: The HCFS URI of jar file containing the driver jar. Conflicts with main_class. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#main_jar_file_uri GoogleDataprocJob#main_jar_file_uri}
        :param properties: A mapping of property names to values, used to configure Spark. Properties that conflict with values set by the Cloud Dataproc API may be overwritten. Can include properties set in /etc/spark/conf/spark-defaults.conf and classes in user code. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#properties GoogleDataprocJob#properties}
        '''
        value = GoogleDataprocJobHadoopConfig(
            archive_uris=archive_uris,
            args=args,
            file_uris=file_uris,
            jar_file_uris=jar_file_uris,
            logging_config=logging_config,
            main_class=main_class,
            main_jar_file_uri=main_jar_file_uri,
            properties=properties,
        )

        return typing.cast(None, jsii.invoke(self, "putHadoopConfig", [value]))

    @jsii.member(jsii_name="putHiveConfig")
    def put_hive_config(
        self,
        *,
        continue_on_failure: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        jar_file_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        query_file_uri: typing.Optional[builtins.str] = None,
        query_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        script_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param continue_on_failure: Whether to continue executing queries if a query fails. The default value is false. Setting to true can be useful when executing independent parallel queries. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#continue_on_failure GoogleDataprocJob#continue_on_failure}
        :param jar_file_uris: HCFS URIs of jar files to add to the CLASSPATH of the Hive server and Hadoop MapReduce (MR) tasks. Can contain Hive SerDes and UDFs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#jar_file_uris GoogleDataprocJob#jar_file_uris}
        :param properties: A mapping of property names and values, used to configure Hive. Properties that conflict with values set by the Cloud Dataproc API may be overwritten. Can include properties set in /etc/hadoop/conf/*-site.xml, /etc/hive/conf/hive-site.xml, and classes in user code. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#properties GoogleDataprocJob#properties}
        :param query_file_uri: HCFS URI of file containing Hive script to execute as the job. Conflicts with query_list. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#query_file_uri GoogleDataprocJob#query_file_uri}
        :param query_list: The list of Hive queries or statements to execute as part of the job. Conflicts with query_file_uri. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#query_list GoogleDataprocJob#query_list}
        :param script_variables: Mapping of query variable names to values (equivalent to the Hive command: SET name="value";). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#script_variables GoogleDataprocJob#script_variables}
        '''
        value = GoogleDataprocJobHiveConfig(
            continue_on_failure=continue_on_failure,
            jar_file_uris=jar_file_uris,
            properties=properties,
            query_file_uri=query_file_uri,
            query_list=query_list,
            script_variables=script_variables,
        )

        return typing.cast(None, jsii.invoke(self, "putHiveConfig", [value]))

    @jsii.member(jsii_name="putPigConfig")
    def put_pig_config(
        self,
        *,
        continue_on_failure: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        jar_file_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        logging_config: typing.Optional[typing.Union["GoogleDataprocJobPigConfigLoggingConfig", typing.Dict[str, typing.Any]]] = None,
        properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        query_file_uri: typing.Optional[builtins.str] = None,
        query_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        script_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param continue_on_failure: Whether to continue executing queries if a query fails. The default value is false. Setting to true can be useful when executing independent parallel queries. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#continue_on_failure GoogleDataprocJob#continue_on_failure}
        :param jar_file_uris: HCFS URIs of jar files to add to the CLASSPATH of the Pig Client and Hadoop MapReduce (MR) tasks. Can contain Pig UDFs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#jar_file_uris GoogleDataprocJob#jar_file_uris}
        :param logging_config: logging_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#logging_config GoogleDataprocJob#logging_config}
        :param properties: A mapping of property names to values, used to configure Pig. Properties that conflict with values set by the Cloud Dataproc API may be overwritten. Can include properties set in /etc/hadoop/conf/*-site.xml, /etc/pig/conf/pig.properties, and classes in user code. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#properties GoogleDataprocJob#properties}
        :param query_file_uri: HCFS URI of file containing Hive script to execute as the job. Conflicts with query_list. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#query_file_uri GoogleDataprocJob#query_file_uri}
        :param query_list: The list of Hive queries or statements to execute as part of the job. Conflicts with query_file_uri. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#query_list GoogleDataprocJob#query_list}
        :param script_variables: Mapping of query variable names to values (equivalent to the Pig command: name=[value]). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#script_variables GoogleDataprocJob#script_variables}
        '''
        value = GoogleDataprocJobPigConfig(
            continue_on_failure=continue_on_failure,
            jar_file_uris=jar_file_uris,
            logging_config=logging_config,
            properties=properties,
            query_file_uri=query_file_uri,
            query_list=query_list,
            script_variables=script_variables,
        )

        return typing.cast(None, jsii.invoke(self, "putPigConfig", [value]))

    @jsii.member(jsii_name="putPlacement")
    def put_placement(self, *, cluster_name: builtins.str) -> None:
        '''
        :param cluster_name: The name of the cluster where the job will be submitted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#cluster_name GoogleDataprocJob#cluster_name}
        '''
        value = GoogleDataprocJobPlacement(cluster_name=cluster_name)

        return typing.cast(None, jsii.invoke(self, "putPlacement", [value]))

    @jsii.member(jsii_name="putPrestoConfig")
    def put_presto_config(
        self,
        *,
        client_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        continue_on_failure: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        logging_config: typing.Optional[typing.Union["GoogleDataprocJobPrestoConfigLoggingConfig", typing.Dict[str, typing.Any]]] = None,
        output_format: typing.Optional[builtins.str] = None,
        properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        query_file_uri: typing.Optional[builtins.str] = None,
        query_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param client_tags: Presto client tags to attach to this query. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#client_tags GoogleDataprocJob#client_tags}
        :param continue_on_failure: Whether to continue executing queries if a query fails. Setting to true can be useful when executing independent parallel queries. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#continue_on_failure GoogleDataprocJob#continue_on_failure}
        :param logging_config: logging_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#logging_config GoogleDataprocJob#logging_config}
        :param output_format: The format in which query output will be displayed. See the Presto documentation for supported output formats. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#output_format GoogleDataprocJob#output_format}
        :param properties: A mapping of property names to values. Used to set Presto session properties Equivalent to using the --session flag in the Presto CLI. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#properties GoogleDataprocJob#properties}
        :param query_file_uri: The HCFS URI of the script that contains SQL queries. Conflicts with query_list. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#query_file_uri GoogleDataprocJob#query_file_uri}
        :param query_list: The list of SQL queries or statements to execute as part of the job. Conflicts with query_file_uri. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#query_list GoogleDataprocJob#query_list}
        '''
        value = GoogleDataprocJobPrestoConfig(
            client_tags=client_tags,
            continue_on_failure=continue_on_failure,
            logging_config=logging_config,
            output_format=output_format,
            properties=properties,
            query_file_uri=query_file_uri,
            query_list=query_list,
        )

        return typing.cast(None, jsii.invoke(self, "putPrestoConfig", [value]))

    @jsii.member(jsii_name="putPysparkConfig")
    def put_pyspark_config(
        self,
        *,
        main_python_file_uri: builtins.str,
        archive_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        file_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        jar_file_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        logging_config: typing.Optional[typing.Union["GoogleDataprocJobPysparkConfigLoggingConfig", typing.Dict[str, typing.Any]]] = None,
        properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        python_file_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param main_python_file_uri: Required. The HCFS URI of the main Python file to use as the driver. Must be a .py file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#main_python_file_uri GoogleDataprocJob#main_python_file_uri}
        :param archive_uris: Optional. HCFS URIs of archives to be extracted in the working directory of .jar, .tar, .tar.gz, .tgz, and .zip. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#archive_uris GoogleDataprocJob#archive_uris}
        :param args: Optional. The arguments to pass to the driver. Do not include arguments, such as --conf, that can be set as job properties, since a collision may occur that causes an incorrect job submission Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#args GoogleDataprocJob#args}
        :param file_uris: Optional. HCFS URIs of files to be copied to the working directory of Python drivers and distributed tasks. Useful for naively parallel tasks Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#file_uris GoogleDataprocJob#file_uris}
        :param jar_file_uris: Optional. HCFS URIs of jar files to add to the CLASSPATHs of the Python driver and tasks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#jar_file_uris GoogleDataprocJob#jar_file_uris}
        :param logging_config: logging_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#logging_config GoogleDataprocJob#logging_config}
        :param properties: Optional. A mapping of property names to values, used to configure PySpark. Properties that conflict with values set by the Cloud Dataproc API may be overwritten. Can include properties set in /etc/spark/conf/spark-defaults.conf and classes in user code Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#properties GoogleDataprocJob#properties}
        :param python_file_uris: Optional. HCFS file URIs of Python files to pass to the PySpark framework. Supported file types: .py, .egg, and .zip Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#python_file_uris GoogleDataprocJob#python_file_uris}
        '''
        value = GoogleDataprocJobPysparkConfig(
            main_python_file_uri=main_python_file_uri,
            archive_uris=archive_uris,
            args=args,
            file_uris=file_uris,
            jar_file_uris=jar_file_uris,
            logging_config=logging_config,
            properties=properties,
            python_file_uris=python_file_uris,
        )

        return typing.cast(None, jsii.invoke(self, "putPysparkConfig", [value]))

    @jsii.member(jsii_name="putReference")
    def put_reference(self, *, job_id: typing.Optional[builtins.str] = None) -> None:
        '''
        :param job_id: The job ID, which must be unique within the project. The job ID is generated by the server upon job submission or provided by the user as a means to perform retries without creating duplicate jobs Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#job_id GoogleDataprocJob#job_id}
        '''
        value = GoogleDataprocJobReference(job_id=job_id)

        return typing.cast(None, jsii.invoke(self, "putReference", [value]))

    @jsii.member(jsii_name="putScheduling")
    def put_scheduling(
        self,
        *,
        max_failures_per_hour: jsii.Number,
        max_failures_total: jsii.Number,
    ) -> None:
        '''
        :param max_failures_per_hour: Maximum number of times per hour a driver may be restarted as a result of driver exiting with non-zero code before job is reported failed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#max_failures_per_hour GoogleDataprocJob#max_failures_per_hour}
        :param max_failures_total: Maximum number of times in total a driver may be restarted as a result of driver exiting with non-zero code before job is reported failed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#max_failures_total GoogleDataprocJob#max_failures_total}
        '''
        value = GoogleDataprocJobScheduling(
            max_failures_per_hour=max_failures_per_hour,
            max_failures_total=max_failures_total,
        )

        return typing.cast(None, jsii.invoke(self, "putScheduling", [value]))

    @jsii.member(jsii_name="putSparkConfig")
    def put_spark_config(
        self,
        *,
        archive_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        file_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        jar_file_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        logging_config: typing.Optional[typing.Union["GoogleDataprocJobSparkConfigLoggingConfig", typing.Dict[str, typing.Any]]] = None,
        main_class: typing.Optional[builtins.str] = None,
        main_jar_file_uri: typing.Optional[builtins.str] = None,
        properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param archive_uris: HCFS URIs of archives to be extracted in the working directory of .jar, .tar, .tar.gz, .tgz, and .zip. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#archive_uris GoogleDataprocJob#archive_uris}
        :param args: The arguments to pass to the driver. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#args GoogleDataprocJob#args}
        :param file_uris: HCFS URIs of files to be copied to the working directory of Spark drivers and distributed tasks. Useful for naively parallel tasks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#file_uris GoogleDataprocJob#file_uris}
        :param jar_file_uris: HCFS URIs of jar files to add to the CLASSPATHs of the Spark driver and tasks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#jar_file_uris GoogleDataprocJob#jar_file_uris}
        :param logging_config: logging_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#logging_config GoogleDataprocJob#logging_config}
        :param main_class: The class containing the main method of the driver. Must be in a provided jar or jar that is already on the classpath. Conflicts with main_jar_file_uri Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#main_class GoogleDataprocJob#main_class}
        :param main_jar_file_uri: The HCFS URI of jar file containing the driver jar. Conflicts with main_class. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#main_jar_file_uri GoogleDataprocJob#main_jar_file_uri}
        :param properties: A mapping of property names to values, used to configure Spark. Properties that conflict with values set by the Cloud Dataproc API may be overwritten. Can include properties set in /etc/spark/conf/spark-defaults.conf and classes in user code. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#properties GoogleDataprocJob#properties}
        '''
        value = GoogleDataprocJobSparkConfig(
            archive_uris=archive_uris,
            args=args,
            file_uris=file_uris,
            jar_file_uris=jar_file_uris,
            logging_config=logging_config,
            main_class=main_class,
            main_jar_file_uri=main_jar_file_uri,
            properties=properties,
        )

        return typing.cast(None, jsii.invoke(self, "putSparkConfig", [value]))

    @jsii.member(jsii_name="putSparksqlConfig")
    def put_sparksql_config(
        self,
        *,
        jar_file_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        logging_config: typing.Optional[typing.Union["GoogleDataprocJobSparksqlConfigLoggingConfig", typing.Dict[str, typing.Any]]] = None,
        properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        query_file_uri: typing.Optional[builtins.str] = None,
        query_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        script_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param jar_file_uris: HCFS URIs of jar files to be added to the Spark CLASSPATH. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#jar_file_uris GoogleDataprocJob#jar_file_uris}
        :param logging_config: logging_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#logging_config GoogleDataprocJob#logging_config}
        :param properties: A mapping of property names to values, used to configure Spark SQL's SparkConf. Properties that conflict with values set by the Cloud Dataproc API may be overwritten. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#properties GoogleDataprocJob#properties}
        :param query_file_uri: The HCFS URI of the script that contains SQL queries. Conflicts with query_list. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#query_file_uri GoogleDataprocJob#query_file_uri}
        :param query_list: The list of SQL queries or statements to execute as part of the job. Conflicts with query_file_uri. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#query_list GoogleDataprocJob#query_list}
        :param script_variables: Mapping of query variable names to values (equivalent to the Spark SQL command: SET name="value";). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#script_variables GoogleDataprocJob#script_variables}
        '''
        value = GoogleDataprocJobSparksqlConfig(
            jar_file_uris=jar_file_uris,
            logging_config=logging_config,
            properties=properties,
            query_file_uri=query_file_uri,
            query_list=query_list,
            script_variables=script_variables,
        )

        return typing.cast(None, jsii.invoke(self, "putSparksqlConfig", [value]))

    @jsii.member(jsii_name="putTimeouts")
    def put_timeouts(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#create GoogleDataprocJob#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#delete GoogleDataprocJob#delete}.
        '''
        value = GoogleDataprocJobTimeouts(create=create, delete=delete)

        return typing.cast(None, jsii.invoke(self, "putTimeouts", [value]))

    @jsii.member(jsii_name="resetForceDelete")
    def reset_force_delete(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetForceDelete", []))

    @jsii.member(jsii_name="resetHadoopConfig")
    def reset_hadoop_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHadoopConfig", []))

    @jsii.member(jsii_name="resetHiveConfig")
    def reset_hive_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetHiveConfig", []))

    @jsii.member(jsii_name="resetId")
    def reset_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetId", []))

    @jsii.member(jsii_name="resetLabels")
    def reset_labels(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLabels", []))

    @jsii.member(jsii_name="resetPigConfig")
    def reset_pig_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPigConfig", []))

    @jsii.member(jsii_name="resetPrestoConfig")
    def reset_presto_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPrestoConfig", []))

    @jsii.member(jsii_name="resetProject")
    def reset_project(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProject", []))

    @jsii.member(jsii_name="resetPysparkConfig")
    def reset_pyspark_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPysparkConfig", []))

    @jsii.member(jsii_name="resetReference")
    def reset_reference(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetReference", []))

    @jsii.member(jsii_name="resetRegion")
    def reset_region(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetRegion", []))

    @jsii.member(jsii_name="resetScheduling")
    def reset_scheduling(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScheduling", []))

    @jsii.member(jsii_name="resetSparkConfig")
    def reset_spark_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSparkConfig", []))

    @jsii.member(jsii_name="resetSparksqlConfig")
    def reset_sparksql_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetSparksqlConfig", []))

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
    @jsii.member(jsii_name="driverControlsFilesUri")
    def driver_controls_files_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "driverControlsFilesUri"))

    @builtins.property
    @jsii.member(jsii_name="driverOutputResourceUri")
    def driver_output_resource_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "driverOutputResourceUri"))

    @builtins.property
    @jsii.member(jsii_name="hadoopConfig")
    def hadoop_config(self) -> "GoogleDataprocJobHadoopConfigOutputReference":
        return typing.cast("GoogleDataprocJobHadoopConfigOutputReference", jsii.get(self, "hadoopConfig"))

    @builtins.property
    @jsii.member(jsii_name="hiveConfig")
    def hive_config(self) -> "GoogleDataprocJobHiveConfigOutputReference":
        return typing.cast("GoogleDataprocJobHiveConfigOutputReference", jsii.get(self, "hiveConfig"))

    @builtins.property
    @jsii.member(jsii_name="pigConfig")
    def pig_config(self) -> "GoogleDataprocJobPigConfigOutputReference":
        return typing.cast("GoogleDataprocJobPigConfigOutputReference", jsii.get(self, "pigConfig"))

    @builtins.property
    @jsii.member(jsii_name="placement")
    def placement(self) -> "GoogleDataprocJobPlacementOutputReference":
        return typing.cast("GoogleDataprocJobPlacementOutputReference", jsii.get(self, "placement"))

    @builtins.property
    @jsii.member(jsii_name="prestoConfig")
    def presto_config(self) -> "GoogleDataprocJobPrestoConfigOutputReference":
        return typing.cast("GoogleDataprocJobPrestoConfigOutputReference", jsii.get(self, "prestoConfig"))

    @builtins.property
    @jsii.member(jsii_name="pysparkConfig")
    def pyspark_config(self) -> "GoogleDataprocJobPysparkConfigOutputReference":
        return typing.cast("GoogleDataprocJobPysparkConfigOutputReference", jsii.get(self, "pysparkConfig"))

    @builtins.property
    @jsii.member(jsii_name="reference")
    def reference(self) -> "GoogleDataprocJobReferenceOutputReference":
        return typing.cast("GoogleDataprocJobReferenceOutputReference", jsii.get(self, "reference"))

    @builtins.property
    @jsii.member(jsii_name="scheduling")
    def scheduling(self) -> "GoogleDataprocJobSchedulingOutputReference":
        return typing.cast("GoogleDataprocJobSchedulingOutputReference", jsii.get(self, "scheduling"))

    @builtins.property
    @jsii.member(jsii_name="sparkConfig")
    def spark_config(self) -> "GoogleDataprocJobSparkConfigOutputReference":
        return typing.cast("GoogleDataprocJobSparkConfigOutputReference", jsii.get(self, "sparkConfig"))

    @builtins.property
    @jsii.member(jsii_name="sparksqlConfig")
    def sparksql_config(self) -> "GoogleDataprocJobSparksqlConfigOutputReference":
        return typing.cast("GoogleDataprocJobSparksqlConfigOutputReference", jsii.get(self, "sparksqlConfig"))

    @builtins.property
    @jsii.member(jsii_name="status")
    def status(self) -> "GoogleDataprocJobStatusList":
        return typing.cast("GoogleDataprocJobStatusList", jsii.get(self, "status"))

    @builtins.property
    @jsii.member(jsii_name="timeouts")
    def timeouts(self) -> "GoogleDataprocJobTimeoutsOutputReference":
        return typing.cast("GoogleDataprocJobTimeoutsOutputReference", jsii.get(self, "timeouts"))

    @builtins.property
    @jsii.member(jsii_name="forceDeleteInput")
    def force_delete_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "forceDeleteInput"))

    @builtins.property
    @jsii.member(jsii_name="hadoopConfigInput")
    def hadoop_config_input(self) -> typing.Optional["GoogleDataprocJobHadoopConfig"]:
        return typing.cast(typing.Optional["GoogleDataprocJobHadoopConfig"], jsii.get(self, "hadoopConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="hiveConfigInput")
    def hive_config_input(self) -> typing.Optional["GoogleDataprocJobHiveConfig"]:
        return typing.cast(typing.Optional["GoogleDataprocJobHiveConfig"], jsii.get(self, "hiveConfigInput"))

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
    @jsii.member(jsii_name="pigConfigInput")
    def pig_config_input(self) -> typing.Optional["GoogleDataprocJobPigConfig"]:
        return typing.cast(typing.Optional["GoogleDataprocJobPigConfig"], jsii.get(self, "pigConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="placementInput")
    def placement_input(self) -> typing.Optional["GoogleDataprocJobPlacement"]:
        return typing.cast(typing.Optional["GoogleDataprocJobPlacement"], jsii.get(self, "placementInput"))

    @builtins.property
    @jsii.member(jsii_name="prestoConfigInput")
    def presto_config_input(self) -> typing.Optional["GoogleDataprocJobPrestoConfig"]:
        return typing.cast(typing.Optional["GoogleDataprocJobPrestoConfig"], jsii.get(self, "prestoConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="projectInput")
    def project_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "projectInput"))

    @builtins.property
    @jsii.member(jsii_name="pysparkConfigInput")
    def pyspark_config_input(self) -> typing.Optional["GoogleDataprocJobPysparkConfig"]:
        return typing.cast(typing.Optional["GoogleDataprocJobPysparkConfig"], jsii.get(self, "pysparkConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="referenceInput")
    def reference_input(self) -> typing.Optional["GoogleDataprocJobReference"]:
        return typing.cast(typing.Optional["GoogleDataprocJobReference"], jsii.get(self, "referenceInput"))

    @builtins.property
    @jsii.member(jsii_name="regionInput")
    def region_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "regionInput"))

    @builtins.property
    @jsii.member(jsii_name="schedulingInput")
    def scheduling_input(self) -> typing.Optional["GoogleDataprocJobScheduling"]:
        return typing.cast(typing.Optional["GoogleDataprocJobScheduling"], jsii.get(self, "schedulingInput"))

    @builtins.property
    @jsii.member(jsii_name="sparkConfigInput")
    def spark_config_input(self) -> typing.Optional["GoogleDataprocJobSparkConfig"]:
        return typing.cast(typing.Optional["GoogleDataprocJobSparkConfig"], jsii.get(self, "sparkConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="sparksqlConfigInput")
    def sparksql_config_input(
        self,
    ) -> typing.Optional["GoogleDataprocJobSparksqlConfig"]:
        return typing.cast(typing.Optional["GoogleDataprocJobSparksqlConfig"], jsii.get(self, "sparksqlConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="timeoutsInput")
    def timeouts_input(
        self,
    ) -> typing.Optional[typing.Union["GoogleDataprocJobTimeouts", cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union["GoogleDataprocJobTimeouts", cdktf.IResolvable]], jsii.get(self, "timeoutsInput"))

    @builtins.property
    @jsii.member(jsii_name="forceDelete")
    def force_delete(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "forceDelete"))

    @force_delete.setter
    def force_delete(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJob, "force_delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "forceDelete", value)

    @builtins.property
    @jsii.member(jsii_name="id")
    def id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "id"))

    @id.setter
    def id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJob, "id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "id", value)

    @builtins.property
    @jsii.member(jsii_name="labels")
    def labels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "labels"))

    @labels.setter
    def labels(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJob, "labels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "labels", value)

    @builtins.property
    @jsii.member(jsii_name="project")
    def project(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "project"))

    @project.setter
    def project(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJob, "project").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "project", value)

    @builtins.property
    @jsii.member(jsii_name="region")
    def region(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "region"))

    @region.setter
    def region(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJob, "region").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "region", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocJob.GoogleDataprocJobConfig",
    jsii_struct_bases=[cdktf.TerraformMetaArguments],
    name_mapping={
        "connection": "connection",
        "count": "count",
        "depends_on": "dependsOn",
        "for_each": "forEach",
        "lifecycle": "lifecycle",
        "provider": "provider",
        "provisioners": "provisioners",
        "placement": "placement",
        "force_delete": "forceDelete",
        "hadoop_config": "hadoopConfig",
        "hive_config": "hiveConfig",
        "id": "id",
        "labels": "labels",
        "pig_config": "pigConfig",
        "presto_config": "prestoConfig",
        "project": "project",
        "pyspark_config": "pysparkConfig",
        "reference": "reference",
        "region": "region",
        "scheduling": "scheduling",
        "spark_config": "sparkConfig",
        "sparksql_config": "sparksqlConfig",
        "timeouts": "timeouts",
    },
)
class GoogleDataprocJobConfig(cdktf.TerraformMetaArguments):
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
        placement: typing.Union["GoogleDataprocJobPlacement", typing.Dict[str, typing.Any]],
        force_delete: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        hadoop_config: typing.Optional[typing.Union["GoogleDataprocJobHadoopConfig", typing.Dict[str, typing.Any]]] = None,
        hive_config: typing.Optional[typing.Union["GoogleDataprocJobHiveConfig", typing.Dict[str, typing.Any]]] = None,
        id: typing.Optional[builtins.str] = None,
        labels: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        pig_config: typing.Optional[typing.Union["GoogleDataprocJobPigConfig", typing.Dict[str, typing.Any]]] = None,
        presto_config: typing.Optional[typing.Union["GoogleDataprocJobPrestoConfig", typing.Dict[str, typing.Any]]] = None,
        project: typing.Optional[builtins.str] = None,
        pyspark_config: typing.Optional[typing.Union["GoogleDataprocJobPysparkConfig", typing.Dict[str, typing.Any]]] = None,
        reference: typing.Optional[typing.Union["GoogleDataprocJobReference", typing.Dict[str, typing.Any]]] = None,
        region: typing.Optional[builtins.str] = None,
        scheduling: typing.Optional[typing.Union["GoogleDataprocJobScheduling", typing.Dict[str, typing.Any]]] = None,
        spark_config: typing.Optional[typing.Union["GoogleDataprocJobSparkConfig", typing.Dict[str, typing.Any]]] = None,
        sparksql_config: typing.Optional[typing.Union["GoogleDataprocJobSparksqlConfig", typing.Dict[str, typing.Any]]] = None,
        timeouts: typing.Optional[typing.Union["GoogleDataprocJobTimeouts", typing.Dict[str, typing.Any]]] = None,
    ) -> None:
        '''
        :param connection: 
        :param count: 
        :param depends_on: 
        :param for_each: 
        :param lifecycle: 
        :param provider: 
        :param provisioners: 
        :param placement: placement block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#placement GoogleDataprocJob#placement}
        :param force_delete: By default, you can only delete inactive jobs within Dataproc. Setting this to true, and calling destroy, will ensure that the job is first cancelled before issuing the delete. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#force_delete GoogleDataprocJob#force_delete}
        :param hadoop_config: hadoop_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#hadoop_config GoogleDataprocJob#hadoop_config}
        :param hive_config: hive_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#hive_config GoogleDataprocJob#hive_config}
        :param id: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#id GoogleDataprocJob#id}. Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2. If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        :param labels: Optional. The labels to associate with this job. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#labels GoogleDataprocJob#labels}
        :param pig_config: pig_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#pig_config GoogleDataprocJob#pig_config}
        :param presto_config: presto_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#presto_config GoogleDataprocJob#presto_config}
        :param project: The project in which the cluster can be found and jobs subsequently run against. If it is not provided, the provider project is used. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#project GoogleDataprocJob#project}
        :param pyspark_config: pyspark_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#pyspark_config GoogleDataprocJob#pyspark_config}
        :param reference: reference block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#reference GoogleDataprocJob#reference}
        :param region: The Cloud Dataproc region. This essentially determines which clusters are available for this job to be submitted to. If not specified, defaults to global. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#region GoogleDataprocJob#region}
        :param scheduling: scheduling block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#scheduling GoogleDataprocJob#scheduling}
        :param spark_config: spark_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#spark_config GoogleDataprocJob#spark_config}
        :param sparksql_config: sparksql_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#sparksql_config GoogleDataprocJob#sparksql_config}
        :param timeouts: timeouts block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#timeouts GoogleDataprocJob#timeouts}
        '''
        if isinstance(lifecycle, dict):
            lifecycle = cdktf.TerraformResourceLifecycle(**lifecycle)
        if isinstance(placement, dict):
            placement = GoogleDataprocJobPlacement(**placement)
        if isinstance(hadoop_config, dict):
            hadoop_config = GoogleDataprocJobHadoopConfig(**hadoop_config)
        if isinstance(hive_config, dict):
            hive_config = GoogleDataprocJobHiveConfig(**hive_config)
        if isinstance(pig_config, dict):
            pig_config = GoogleDataprocJobPigConfig(**pig_config)
        if isinstance(presto_config, dict):
            presto_config = GoogleDataprocJobPrestoConfig(**presto_config)
        if isinstance(pyspark_config, dict):
            pyspark_config = GoogleDataprocJobPysparkConfig(**pyspark_config)
        if isinstance(reference, dict):
            reference = GoogleDataprocJobReference(**reference)
        if isinstance(scheduling, dict):
            scheduling = GoogleDataprocJobScheduling(**scheduling)
        if isinstance(spark_config, dict):
            spark_config = GoogleDataprocJobSparkConfig(**spark_config)
        if isinstance(sparksql_config, dict):
            sparksql_config = GoogleDataprocJobSparksqlConfig(**sparksql_config)
        if isinstance(timeouts, dict):
            timeouts = GoogleDataprocJobTimeouts(**timeouts)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocJobConfig.__init__)
            check_type(argname="argument connection", value=connection, expected_type=type_hints["connection"])
            check_type(argname="argument count", value=count, expected_type=type_hints["count"])
            check_type(argname="argument depends_on", value=depends_on, expected_type=type_hints["depends_on"])
            check_type(argname="argument for_each", value=for_each, expected_type=type_hints["for_each"])
            check_type(argname="argument lifecycle", value=lifecycle, expected_type=type_hints["lifecycle"])
            check_type(argname="argument provider", value=provider, expected_type=type_hints["provider"])
            check_type(argname="argument provisioners", value=provisioners, expected_type=type_hints["provisioners"])
            check_type(argname="argument placement", value=placement, expected_type=type_hints["placement"])
            check_type(argname="argument force_delete", value=force_delete, expected_type=type_hints["force_delete"])
            check_type(argname="argument hadoop_config", value=hadoop_config, expected_type=type_hints["hadoop_config"])
            check_type(argname="argument hive_config", value=hive_config, expected_type=type_hints["hive_config"])
            check_type(argname="argument id", value=id, expected_type=type_hints["id"])
            check_type(argname="argument labels", value=labels, expected_type=type_hints["labels"])
            check_type(argname="argument pig_config", value=pig_config, expected_type=type_hints["pig_config"])
            check_type(argname="argument presto_config", value=presto_config, expected_type=type_hints["presto_config"])
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
            check_type(argname="argument pyspark_config", value=pyspark_config, expected_type=type_hints["pyspark_config"])
            check_type(argname="argument reference", value=reference, expected_type=type_hints["reference"])
            check_type(argname="argument region", value=region, expected_type=type_hints["region"])
            check_type(argname="argument scheduling", value=scheduling, expected_type=type_hints["scheduling"])
            check_type(argname="argument spark_config", value=spark_config, expected_type=type_hints["spark_config"])
            check_type(argname="argument sparksql_config", value=sparksql_config, expected_type=type_hints["sparksql_config"])
            check_type(argname="argument timeouts", value=timeouts, expected_type=type_hints["timeouts"])
        self._values: typing.Dict[str, typing.Any] = {
            "placement": placement,
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
        if force_delete is not None:
            self._values["force_delete"] = force_delete
        if hadoop_config is not None:
            self._values["hadoop_config"] = hadoop_config
        if hive_config is not None:
            self._values["hive_config"] = hive_config
        if id is not None:
            self._values["id"] = id
        if labels is not None:
            self._values["labels"] = labels
        if pig_config is not None:
            self._values["pig_config"] = pig_config
        if presto_config is not None:
            self._values["presto_config"] = presto_config
        if project is not None:
            self._values["project"] = project
        if pyspark_config is not None:
            self._values["pyspark_config"] = pyspark_config
        if reference is not None:
            self._values["reference"] = reference
        if region is not None:
            self._values["region"] = region
        if scheduling is not None:
            self._values["scheduling"] = scheduling
        if spark_config is not None:
            self._values["spark_config"] = spark_config
        if sparksql_config is not None:
            self._values["sparksql_config"] = sparksql_config
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
    def placement(self) -> "GoogleDataprocJobPlacement":
        '''placement block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#placement GoogleDataprocJob#placement}
        '''
        result = self._values.get("placement")
        assert result is not None, "Required property 'placement' is missing"
        return typing.cast("GoogleDataprocJobPlacement", result)

    @builtins.property
    def force_delete(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''By default, you can only delete inactive jobs within Dataproc.

        Setting this to true, and calling destroy, will ensure that the job is first cancelled before issuing the delete.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#force_delete GoogleDataprocJob#force_delete}
        '''
        result = self._values.get("force_delete")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def hadoop_config(self) -> typing.Optional["GoogleDataprocJobHadoopConfig"]:
        '''hadoop_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#hadoop_config GoogleDataprocJob#hadoop_config}
        '''
        result = self._values.get("hadoop_config")
        return typing.cast(typing.Optional["GoogleDataprocJobHadoopConfig"], result)

    @builtins.property
    def hive_config(self) -> typing.Optional["GoogleDataprocJobHiveConfig"]:
        '''hive_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#hive_config GoogleDataprocJob#hive_config}
        '''
        result = self._values.get("hive_config")
        return typing.cast(typing.Optional["GoogleDataprocJobHiveConfig"], result)

    @builtins.property
    def id(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#id GoogleDataprocJob#id}.

        Please be aware that the id field is automatically added to all resources in Terraform providers using a Terraform provider SDK version below 2.
        If you experience problems setting this value it might not be settable. Please take a look at the provider documentation to ensure it should be settable.
        '''
        result = self._values.get("id")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def labels(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Optional. The labels to associate with this job.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#labels GoogleDataprocJob#labels}
        '''
        result = self._values.get("labels")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def pig_config(self) -> typing.Optional["GoogleDataprocJobPigConfig"]:
        '''pig_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#pig_config GoogleDataprocJob#pig_config}
        '''
        result = self._values.get("pig_config")
        return typing.cast(typing.Optional["GoogleDataprocJobPigConfig"], result)

    @builtins.property
    def presto_config(self) -> typing.Optional["GoogleDataprocJobPrestoConfig"]:
        '''presto_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#presto_config GoogleDataprocJob#presto_config}
        '''
        result = self._values.get("presto_config")
        return typing.cast(typing.Optional["GoogleDataprocJobPrestoConfig"], result)

    @builtins.property
    def project(self) -> typing.Optional[builtins.str]:
        '''The project in which the cluster can be found and jobs subsequently run against.

        If it is not provided, the provider project is used.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#project GoogleDataprocJob#project}
        '''
        result = self._values.get("project")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pyspark_config(self) -> typing.Optional["GoogleDataprocJobPysparkConfig"]:
        '''pyspark_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#pyspark_config GoogleDataprocJob#pyspark_config}
        '''
        result = self._values.get("pyspark_config")
        return typing.cast(typing.Optional["GoogleDataprocJobPysparkConfig"], result)

    @builtins.property
    def reference(self) -> typing.Optional["GoogleDataprocJobReference"]:
        '''reference block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#reference GoogleDataprocJob#reference}
        '''
        result = self._values.get("reference")
        return typing.cast(typing.Optional["GoogleDataprocJobReference"], result)

    @builtins.property
    def region(self) -> typing.Optional[builtins.str]:
        '''The Cloud Dataproc region.

        This essentially determines which clusters are available for this job to be submitted to. If not specified, defaults to global.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#region GoogleDataprocJob#region}
        '''
        result = self._values.get("region")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def scheduling(self) -> typing.Optional["GoogleDataprocJobScheduling"]:
        '''scheduling block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#scheduling GoogleDataprocJob#scheduling}
        '''
        result = self._values.get("scheduling")
        return typing.cast(typing.Optional["GoogleDataprocJobScheduling"], result)

    @builtins.property
    def spark_config(self) -> typing.Optional["GoogleDataprocJobSparkConfig"]:
        '''spark_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#spark_config GoogleDataprocJob#spark_config}
        '''
        result = self._values.get("spark_config")
        return typing.cast(typing.Optional["GoogleDataprocJobSparkConfig"], result)

    @builtins.property
    def sparksql_config(self) -> typing.Optional["GoogleDataprocJobSparksqlConfig"]:
        '''sparksql_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#sparksql_config GoogleDataprocJob#sparksql_config}
        '''
        result = self._values.get("sparksql_config")
        return typing.cast(typing.Optional["GoogleDataprocJobSparksqlConfig"], result)

    @builtins.property
    def timeouts(self) -> typing.Optional["GoogleDataprocJobTimeouts"]:
        '''timeouts block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#timeouts GoogleDataprocJob#timeouts}
        '''
        result = self._values.get("timeouts")
        return typing.cast(typing.Optional["GoogleDataprocJobTimeouts"], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocJobConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocJob.GoogleDataprocJobHadoopConfig",
    jsii_struct_bases=[],
    name_mapping={
        "archive_uris": "archiveUris",
        "args": "args",
        "file_uris": "fileUris",
        "jar_file_uris": "jarFileUris",
        "logging_config": "loggingConfig",
        "main_class": "mainClass",
        "main_jar_file_uri": "mainJarFileUri",
        "properties": "properties",
    },
)
class GoogleDataprocJobHadoopConfig:
    def __init__(
        self,
        *,
        archive_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        file_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        jar_file_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        logging_config: typing.Optional[typing.Union["GoogleDataprocJobHadoopConfigLoggingConfig", typing.Dict[str, typing.Any]]] = None,
        main_class: typing.Optional[builtins.str] = None,
        main_jar_file_uri: typing.Optional[builtins.str] = None,
        properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param archive_uris: HCFS URIs of archives to be extracted in the working directory of .jar, .tar, .tar.gz, .tgz, and .zip. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#archive_uris GoogleDataprocJob#archive_uris}
        :param args: The arguments to pass to the driver. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#args GoogleDataprocJob#args}
        :param file_uris: HCFS URIs of files to be copied to the working directory of Spark drivers and distributed tasks. Useful for naively parallel tasks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#file_uris GoogleDataprocJob#file_uris}
        :param jar_file_uris: HCFS URIs of jar files to add to the CLASSPATHs of the Spark driver and tasks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#jar_file_uris GoogleDataprocJob#jar_file_uris}
        :param logging_config: logging_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#logging_config GoogleDataprocJob#logging_config}
        :param main_class: The class containing the main method of the driver. Must be in a provided jar or jar that is already on the classpath. Conflicts with main_jar_file_uri Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#main_class GoogleDataprocJob#main_class}
        :param main_jar_file_uri: The HCFS URI of jar file containing the driver jar. Conflicts with main_class. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#main_jar_file_uri GoogleDataprocJob#main_jar_file_uri}
        :param properties: A mapping of property names to values, used to configure Spark. Properties that conflict with values set by the Cloud Dataproc API may be overwritten. Can include properties set in /etc/spark/conf/spark-defaults.conf and classes in user code. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#properties GoogleDataprocJob#properties}
        '''
        if isinstance(logging_config, dict):
            logging_config = GoogleDataprocJobHadoopConfigLoggingConfig(**logging_config)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocJobHadoopConfig.__init__)
            check_type(argname="argument archive_uris", value=archive_uris, expected_type=type_hints["archive_uris"])
            check_type(argname="argument args", value=args, expected_type=type_hints["args"])
            check_type(argname="argument file_uris", value=file_uris, expected_type=type_hints["file_uris"])
            check_type(argname="argument jar_file_uris", value=jar_file_uris, expected_type=type_hints["jar_file_uris"])
            check_type(argname="argument logging_config", value=logging_config, expected_type=type_hints["logging_config"])
            check_type(argname="argument main_class", value=main_class, expected_type=type_hints["main_class"])
            check_type(argname="argument main_jar_file_uri", value=main_jar_file_uri, expected_type=type_hints["main_jar_file_uri"])
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
        self._values: typing.Dict[str, typing.Any] = {}
        if archive_uris is not None:
            self._values["archive_uris"] = archive_uris
        if args is not None:
            self._values["args"] = args
        if file_uris is not None:
            self._values["file_uris"] = file_uris
        if jar_file_uris is not None:
            self._values["jar_file_uris"] = jar_file_uris
        if logging_config is not None:
            self._values["logging_config"] = logging_config
        if main_class is not None:
            self._values["main_class"] = main_class
        if main_jar_file_uri is not None:
            self._values["main_jar_file_uri"] = main_jar_file_uri
        if properties is not None:
            self._values["properties"] = properties

    @builtins.property
    def archive_uris(self) -> typing.Optional[typing.List[builtins.str]]:
        '''HCFS URIs of archives to be extracted in the working directory of .jar, .tar, .tar.gz, .tgz, and .zip.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#archive_uris GoogleDataprocJob#archive_uris}
        '''
        result = self._values.get("archive_uris")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def args(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The arguments to pass to the driver.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#args GoogleDataprocJob#args}
        '''
        result = self._values.get("args")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def file_uris(self) -> typing.Optional[typing.List[builtins.str]]:
        '''HCFS URIs of files to be copied to the working directory of Spark drivers and distributed tasks.

        Useful for naively parallel tasks.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#file_uris GoogleDataprocJob#file_uris}
        '''
        result = self._values.get("file_uris")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def jar_file_uris(self) -> typing.Optional[typing.List[builtins.str]]:
        '''HCFS URIs of jar files to add to the CLASSPATHs of the Spark driver and tasks.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#jar_file_uris GoogleDataprocJob#jar_file_uris}
        '''
        result = self._values.get("jar_file_uris")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def logging_config(
        self,
    ) -> typing.Optional["GoogleDataprocJobHadoopConfigLoggingConfig"]:
        '''logging_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#logging_config GoogleDataprocJob#logging_config}
        '''
        result = self._values.get("logging_config")
        return typing.cast(typing.Optional["GoogleDataprocJobHadoopConfigLoggingConfig"], result)

    @builtins.property
    def main_class(self) -> typing.Optional[builtins.str]:
        '''The class containing the main method of the driver.

        Must be in a provided jar or jar that is already on the classpath. Conflicts with main_jar_file_uri

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#main_class GoogleDataprocJob#main_class}
        '''
        result = self._values.get("main_class")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def main_jar_file_uri(self) -> typing.Optional[builtins.str]:
        '''The HCFS URI of jar file containing the driver jar. Conflicts with main_class.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#main_jar_file_uri GoogleDataprocJob#main_jar_file_uri}
        '''
        result = self._values.get("main_jar_file_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def properties(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A mapping of property names to values, used to configure Spark.

        Properties that conflict with values set by the Cloud Dataproc API may be overwritten. Can include properties set in /etc/spark/conf/spark-defaults.conf and classes in user code.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#properties GoogleDataprocJob#properties}
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocJobHadoopConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocJob.GoogleDataprocJobHadoopConfigLoggingConfig",
    jsii_struct_bases=[],
    name_mapping={"driver_log_levels": "driverLogLevels"},
)
class GoogleDataprocJobHadoopConfigLoggingConfig:
    def __init__(
        self,
        *,
        driver_log_levels: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        '''
        :param driver_log_levels: Optional. The per-package log levels for the driver. This may include 'root' package name to configure rootLogger. Examples: 'com.google = FATAL', 'root = INFO', 'org.apache = DEBUG'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#driver_log_levels GoogleDataprocJob#driver_log_levels}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocJobHadoopConfigLoggingConfig.__init__)
            check_type(argname="argument driver_log_levels", value=driver_log_levels, expected_type=type_hints["driver_log_levels"])
        self._values: typing.Dict[str, typing.Any] = {
            "driver_log_levels": driver_log_levels,
        }

    @builtins.property
    def driver_log_levels(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''Optional.

        The per-package log levels for the driver. This may include 'root' package name to configure rootLogger. Examples: 'com.google = FATAL', 'root = INFO', 'org.apache = DEBUG'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#driver_log_levels GoogleDataprocJob#driver_log_levels}
        '''
        result = self._values.get("driver_log_levels")
        assert result is not None, "Required property 'driver_log_levels' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocJobHadoopConfigLoggingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocJobHadoopConfigLoggingConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocJob.GoogleDataprocJobHadoopConfigLoggingConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocJobHadoopConfigLoggingConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="driverLogLevelsInput")
    def driver_log_levels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "driverLogLevelsInput"))

    @builtins.property
    @jsii.member(jsii_name="driverLogLevels")
    def driver_log_levels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "driverLogLevels"))

    @driver_log_levels.setter
    def driver_log_levels(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobHadoopConfigLoggingConfigOutputReference, "driver_log_levels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "driverLogLevels", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocJobHadoopConfigLoggingConfig]:
        return typing.cast(typing.Optional[GoogleDataprocJobHadoopConfigLoggingConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocJobHadoopConfigLoggingConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobHadoopConfigLoggingConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDataprocJobHadoopConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocJob.GoogleDataprocJobHadoopConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocJobHadoopConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putLoggingConfig")
    def put_logging_config(
        self,
        *,
        driver_log_levels: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        '''
        :param driver_log_levels: Optional. The per-package log levels for the driver. This may include 'root' package name to configure rootLogger. Examples: 'com.google = FATAL', 'root = INFO', 'org.apache = DEBUG'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#driver_log_levels GoogleDataprocJob#driver_log_levels}
        '''
        value = GoogleDataprocJobHadoopConfigLoggingConfig(
            driver_log_levels=driver_log_levels
        )

        return typing.cast(None, jsii.invoke(self, "putLoggingConfig", [value]))

    @jsii.member(jsii_name="resetArchiveUris")
    def reset_archive_uris(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArchiveUris", []))

    @jsii.member(jsii_name="resetArgs")
    def reset_args(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArgs", []))

    @jsii.member(jsii_name="resetFileUris")
    def reset_file_uris(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFileUris", []))

    @jsii.member(jsii_name="resetJarFileUris")
    def reset_jar_file_uris(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJarFileUris", []))

    @jsii.member(jsii_name="resetLoggingConfig")
    def reset_logging_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoggingConfig", []))

    @jsii.member(jsii_name="resetMainClass")
    def reset_main_class(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMainClass", []))

    @jsii.member(jsii_name="resetMainJarFileUri")
    def reset_main_jar_file_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMainJarFileUri", []))

    @jsii.member(jsii_name="resetProperties")
    def reset_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProperties", []))

    @builtins.property
    @jsii.member(jsii_name="loggingConfig")
    def logging_config(
        self,
    ) -> GoogleDataprocJobHadoopConfigLoggingConfigOutputReference:
        return typing.cast(GoogleDataprocJobHadoopConfigLoggingConfigOutputReference, jsii.get(self, "loggingConfig"))

    @builtins.property
    @jsii.member(jsii_name="archiveUrisInput")
    def archive_uris_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "archiveUrisInput"))

    @builtins.property
    @jsii.member(jsii_name="argsInput")
    def args_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "argsInput"))

    @builtins.property
    @jsii.member(jsii_name="fileUrisInput")
    def file_uris_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "fileUrisInput"))

    @builtins.property
    @jsii.member(jsii_name="jarFileUrisInput")
    def jar_file_uris_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "jarFileUrisInput"))

    @builtins.property
    @jsii.member(jsii_name="loggingConfigInput")
    def logging_config_input(
        self,
    ) -> typing.Optional[GoogleDataprocJobHadoopConfigLoggingConfig]:
        return typing.cast(typing.Optional[GoogleDataprocJobHadoopConfigLoggingConfig], jsii.get(self, "loggingConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="mainClassInput")
    def main_class_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mainClassInput"))

    @builtins.property
    @jsii.member(jsii_name="mainJarFileUriInput")
    def main_jar_file_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mainJarFileUriInput"))

    @builtins.property
    @jsii.member(jsii_name="propertiesInput")
    def properties_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "propertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="archiveUris")
    def archive_uris(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "archiveUris"))

    @archive_uris.setter
    def archive_uris(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobHadoopConfigOutputReference, "archive_uris").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "archiveUris", value)

    @builtins.property
    @jsii.member(jsii_name="args")
    def args(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "args"))

    @args.setter
    def args(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobHadoopConfigOutputReference, "args").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "args", value)

    @builtins.property
    @jsii.member(jsii_name="fileUris")
    def file_uris(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "fileUris"))

    @file_uris.setter
    def file_uris(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobHadoopConfigOutputReference, "file_uris").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileUris", value)

    @builtins.property
    @jsii.member(jsii_name="jarFileUris")
    def jar_file_uris(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "jarFileUris"))

    @jar_file_uris.setter
    def jar_file_uris(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobHadoopConfigOutputReference, "jar_file_uris").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jarFileUris", value)

    @builtins.property
    @jsii.member(jsii_name="mainClass")
    def main_class(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mainClass"))

    @main_class.setter
    def main_class(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobHadoopConfigOutputReference, "main_class").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mainClass", value)

    @builtins.property
    @jsii.member(jsii_name="mainJarFileUri")
    def main_jar_file_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mainJarFileUri"))

    @main_jar_file_uri.setter
    def main_jar_file_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobHadoopConfigOutputReference, "main_jar_file_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mainJarFileUri", value)

    @builtins.property
    @jsii.member(jsii_name="properties")
    def properties(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "properties"))

    @properties.setter
    def properties(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobHadoopConfigOutputReference, "properties").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "properties", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleDataprocJobHadoopConfig]:
        return typing.cast(typing.Optional[GoogleDataprocJobHadoopConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocJobHadoopConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobHadoopConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocJob.GoogleDataprocJobHiveConfig",
    jsii_struct_bases=[],
    name_mapping={
        "continue_on_failure": "continueOnFailure",
        "jar_file_uris": "jarFileUris",
        "properties": "properties",
        "query_file_uri": "queryFileUri",
        "query_list": "queryList",
        "script_variables": "scriptVariables",
    },
)
class GoogleDataprocJobHiveConfig:
    def __init__(
        self,
        *,
        continue_on_failure: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        jar_file_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        query_file_uri: typing.Optional[builtins.str] = None,
        query_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        script_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param continue_on_failure: Whether to continue executing queries if a query fails. The default value is false. Setting to true can be useful when executing independent parallel queries. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#continue_on_failure GoogleDataprocJob#continue_on_failure}
        :param jar_file_uris: HCFS URIs of jar files to add to the CLASSPATH of the Hive server and Hadoop MapReduce (MR) tasks. Can contain Hive SerDes and UDFs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#jar_file_uris GoogleDataprocJob#jar_file_uris}
        :param properties: A mapping of property names and values, used to configure Hive. Properties that conflict with values set by the Cloud Dataproc API may be overwritten. Can include properties set in /etc/hadoop/conf/*-site.xml, /etc/hive/conf/hive-site.xml, and classes in user code. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#properties GoogleDataprocJob#properties}
        :param query_file_uri: HCFS URI of file containing Hive script to execute as the job. Conflicts with query_list. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#query_file_uri GoogleDataprocJob#query_file_uri}
        :param query_list: The list of Hive queries or statements to execute as part of the job. Conflicts with query_file_uri. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#query_list GoogleDataprocJob#query_list}
        :param script_variables: Mapping of query variable names to values (equivalent to the Hive command: SET name="value";). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#script_variables GoogleDataprocJob#script_variables}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocJobHiveConfig.__init__)
            check_type(argname="argument continue_on_failure", value=continue_on_failure, expected_type=type_hints["continue_on_failure"])
            check_type(argname="argument jar_file_uris", value=jar_file_uris, expected_type=type_hints["jar_file_uris"])
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument query_file_uri", value=query_file_uri, expected_type=type_hints["query_file_uri"])
            check_type(argname="argument query_list", value=query_list, expected_type=type_hints["query_list"])
            check_type(argname="argument script_variables", value=script_variables, expected_type=type_hints["script_variables"])
        self._values: typing.Dict[str, typing.Any] = {}
        if continue_on_failure is not None:
            self._values["continue_on_failure"] = continue_on_failure
        if jar_file_uris is not None:
            self._values["jar_file_uris"] = jar_file_uris
        if properties is not None:
            self._values["properties"] = properties
        if query_file_uri is not None:
            self._values["query_file_uri"] = query_file_uri
        if query_list is not None:
            self._values["query_list"] = query_list
        if script_variables is not None:
            self._values["script_variables"] = script_variables

    @builtins.property
    def continue_on_failure(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to continue executing queries if a query fails.

        The default value is false. Setting to true can be useful when executing independent parallel queries. Defaults to false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#continue_on_failure GoogleDataprocJob#continue_on_failure}
        '''
        result = self._values.get("continue_on_failure")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def jar_file_uris(self) -> typing.Optional[typing.List[builtins.str]]:
        '''HCFS URIs of jar files to add to the CLASSPATH of the Hive server and Hadoop MapReduce (MR) tasks.

        Can contain Hive SerDes and UDFs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#jar_file_uris GoogleDataprocJob#jar_file_uris}
        '''
        result = self._values.get("jar_file_uris")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def properties(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A mapping of property names and values, used to configure Hive.

        Properties that conflict with values set by the Cloud Dataproc API may be overwritten. Can include properties set in /etc/hadoop/conf/*-site.xml, /etc/hive/conf/hive-site.xml, and classes in user code.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#properties GoogleDataprocJob#properties}
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def query_file_uri(self) -> typing.Optional[builtins.str]:
        '''HCFS URI of file containing Hive script to execute as the job. Conflicts with query_list.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#query_file_uri GoogleDataprocJob#query_file_uri}
        '''
        result = self._values.get("query_file_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def query_list(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of Hive queries or statements to execute as part of the job. Conflicts with query_file_uri.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#query_list GoogleDataprocJob#query_list}
        '''
        result = self._values.get("query_list")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def script_variables(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Mapping of query variable names to values (equivalent to the Hive command: SET name="value";).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#script_variables GoogleDataprocJob#script_variables}
        '''
        result = self._values.get("script_variables")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocJobHiveConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocJobHiveConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocJob.GoogleDataprocJobHiveConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocJobHiveConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetContinueOnFailure")
    def reset_continue_on_failure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContinueOnFailure", []))

    @jsii.member(jsii_name="resetJarFileUris")
    def reset_jar_file_uris(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJarFileUris", []))

    @jsii.member(jsii_name="resetProperties")
    def reset_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProperties", []))

    @jsii.member(jsii_name="resetQueryFileUri")
    def reset_query_file_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryFileUri", []))

    @jsii.member(jsii_name="resetQueryList")
    def reset_query_list(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryList", []))

    @jsii.member(jsii_name="resetScriptVariables")
    def reset_script_variables(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScriptVariables", []))

    @builtins.property
    @jsii.member(jsii_name="continueOnFailureInput")
    def continue_on_failure_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "continueOnFailureInput"))

    @builtins.property
    @jsii.member(jsii_name="jarFileUrisInput")
    def jar_file_uris_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "jarFileUrisInput"))

    @builtins.property
    @jsii.member(jsii_name="propertiesInput")
    def properties_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "propertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="queryFileUriInput")
    def query_file_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryFileUriInput"))

    @builtins.property
    @jsii.member(jsii_name="queryListInput")
    def query_list_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "queryListInput"))

    @builtins.property
    @jsii.member(jsii_name="scriptVariablesInput")
    def script_variables_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "scriptVariablesInput"))

    @builtins.property
    @jsii.member(jsii_name="continueOnFailure")
    def continue_on_failure(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "continueOnFailure"))

    @continue_on_failure.setter
    def continue_on_failure(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobHiveConfigOutputReference, "continue_on_failure").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "continueOnFailure", value)

    @builtins.property
    @jsii.member(jsii_name="jarFileUris")
    def jar_file_uris(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "jarFileUris"))

    @jar_file_uris.setter
    def jar_file_uris(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobHiveConfigOutputReference, "jar_file_uris").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jarFileUris", value)

    @builtins.property
    @jsii.member(jsii_name="properties")
    def properties(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "properties"))

    @properties.setter
    def properties(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobHiveConfigOutputReference, "properties").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "properties", value)

    @builtins.property
    @jsii.member(jsii_name="queryFileUri")
    def query_file_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "queryFileUri"))

    @query_file_uri.setter
    def query_file_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobHiveConfigOutputReference, "query_file_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryFileUri", value)

    @builtins.property
    @jsii.member(jsii_name="queryList")
    def query_list(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "queryList"))

    @query_list.setter
    def query_list(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobHiveConfigOutputReference, "query_list").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryList", value)

    @builtins.property
    @jsii.member(jsii_name="scriptVariables")
    def script_variables(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "scriptVariables"))

    @script_variables.setter
    def script_variables(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobHiveConfigOutputReference, "script_variables").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scriptVariables", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleDataprocJobHiveConfig]:
        return typing.cast(typing.Optional[GoogleDataprocJobHiveConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocJobHiveConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobHiveConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocJob.GoogleDataprocJobPigConfig",
    jsii_struct_bases=[],
    name_mapping={
        "continue_on_failure": "continueOnFailure",
        "jar_file_uris": "jarFileUris",
        "logging_config": "loggingConfig",
        "properties": "properties",
        "query_file_uri": "queryFileUri",
        "query_list": "queryList",
        "script_variables": "scriptVariables",
    },
)
class GoogleDataprocJobPigConfig:
    def __init__(
        self,
        *,
        continue_on_failure: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        jar_file_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        logging_config: typing.Optional[typing.Union["GoogleDataprocJobPigConfigLoggingConfig", typing.Dict[str, typing.Any]]] = None,
        properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        query_file_uri: typing.Optional[builtins.str] = None,
        query_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        script_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param continue_on_failure: Whether to continue executing queries if a query fails. The default value is false. Setting to true can be useful when executing independent parallel queries. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#continue_on_failure GoogleDataprocJob#continue_on_failure}
        :param jar_file_uris: HCFS URIs of jar files to add to the CLASSPATH of the Pig Client and Hadoop MapReduce (MR) tasks. Can contain Pig UDFs. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#jar_file_uris GoogleDataprocJob#jar_file_uris}
        :param logging_config: logging_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#logging_config GoogleDataprocJob#logging_config}
        :param properties: A mapping of property names to values, used to configure Pig. Properties that conflict with values set by the Cloud Dataproc API may be overwritten. Can include properties set in /etc/hadoop/conf/*-site.xml, /etc/pig/conf/pig.properties, and classes in user code. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#properties GoogleDataprocJob#properties}
        :param query_file_uri: HCFS URI of file containing Hive script to execute as the job. Conflicts with query_list. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#query_file_uri GoogleDataprocJob#query_file_uri}
        :param query_list: The list of Hive queries or statements to execute as part of the job. Conflicts with query_file_uri. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#query_list GoogleDataprocJob#query_list}
        :param script_variables: Mapping of query variable names to values (equivalent to the Pig command: name=[value]). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#script_variables GoogleDataprocJob#script_variables}
        '''
        if isinstance(logging_config, dict):
            logging_config = GoogleDataprocJobPigConfigLoggingConfig(**logging_config)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocJobPigConfig.__init__)
            check_type(argname="argument continue_on_failure", value=continue_on_failure, expected_type=type_hints["continue_on_failure"])
            check_type(argname="argument jar_file_uris", value=jar_file_uris, expected_type=type_hints["jar_file_uris"])
            check_type(argname="argument logging_config", value=logging_config, expected_type=type_hints["logging_config"])
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument query_file_uri", value=query_file_uri, expected_type=type_hints["query_file_uri"])
            check_type(argname="argument query_list", value=query_list, expected_type=type_hints["query_list"])
            check_type(argname="argument script_variables", value=script_variables, expected_type=type_hints["script_variables"])
        self._values: typing.Dict[str, typing.Any] = {}
        if continue_on_failure is not None:
            self._values["continue_on_failure"] = continue_on_failure
        if jar_file_uris is not None:
            self._values["jar_file_uris"] = jar_file_uris
        if logging_config is not None:
            self._values["logging_config"] = logging_config
        if properties is not None:
            self._values["properties"] = properties
        if query_file_uri is not None:
            self._values["query_file_uri"] = query_file_uri
        if query_list is not None:
            self._values["query_list"] = query_list
        if script_variables is not None:
            self._values["script_variables"] = script_variables

    @builtins.property
    def continue_on_failure(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to continue executing queries if a query fails.

        The default value is false. Setting to true can be useful when executing independent parallel queries. Defaults to false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#continue_on_failure GoogleDataprocJob#continue_on_failure}
        '''
        result = self._values.get("continue_on_failure")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def jar_file_uris(self) -> typing.Optional[typing.List[builtins.str]]:
        '''HCFS URIs of jar files to add to the CLASSPATH of the Pig Client and Hadoop MapReduce (MR) tasks.

        Can contain Pig UDFs.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#jar_file_uris GoogleDataprocJob#jar_file_uris}
        '''
        result = self._values.get("jar_file_uris")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def logging_config(
        self,
    ) -> typing.Optional["GoogleDataprocJobPigConfigLoggingConfig"]:
        '''logging_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#logging_config GoogleDataprocJob#logging_config}
        '''
        result = self._values.get("logging_config")
        return typing.cast(typing.Optional["GoogleDataprocJobPigConfigLoggingConfig"], result)

    @builtins.property
    def properties(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A mapping of property names to values, used to configure Pig.

        Properties that conflict with values set by the Cloud Dataproc API may be overwritten. Can include properties set in /etc/hadoop/conf/*-site.xml, /etc/pig/conf/pig.properties, and classes in user code.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#properties GoogleDataprocJob#properties}
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def query_file_uri(self) -> typing.Optional[builtins.str]:
        '''HCFS URI of file containing Hive script to execute as the job. Conflicts with query_list.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#query_file_uri GoogleDataprocJob#query_file_uri}
        '''
        result = self._values.get("query_file_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def query_list(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of Hive queries or statements to execute as part of the job. Conflicts with query_file_uri.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#query_list GoogleDataprocJob#query_list}
        '''
        result = self._values.get("query_list")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def script_variables(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Mapping of query variable names to values (equivalent to the Pig command: name=[value]).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#script_variables GoogleDataprocJob#script_variables}
        '''
        result = self._values.get("script_variables")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocJobPigConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocJob.GoogleDataprocJobPigConfigLoggingConfig",
    jsii_struct_bases=[],
    name_mapping={"driver_log_levels": "driverLogLevels"},
)
class GoogleDataprocJobPigConfigLoggingConfig:
    def __init__(
        self,
        *,
        driver_log_levels: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        '''
        :param driver_log_levels: Optional. The per-package log levels for the driver. This may include 'root' package name to configure rootLogger. Examples: 'com.google = FATAL', 'root = INFO', 'org.apache = DEBUG'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#driver_log_levels GoogleDataprocJob#driver_log_levels}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocJobPigConfigLoggingConfig.__init__)
            check_type(argname="argument driver_log_levels", value=driver_log_levels, expected_type=type_hints["driver_log_levels"])
        self._values: typing.Dict[str, typing.Any] = {
            "driver_log_levels": driver_log_levels,
        }

    @builtins.property
    def driver_log_levels(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''Optional.

        The per-package log levels for the driver. This may include 'root' package name to configure rootLogger. Examples: 'com.google = FATAL', 'root = INFO', 'org.apache = DEBUG'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#driver_log_levels GoogleDataprocJob#driver_log_levels}
        '''
        result = self._values.get("driver_log_levels")
        assert result is not None, "Required property 'driver_log_levels' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocJobPigConfigLoggingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocJobPigConfigLoggingConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocJob.GoogleDataprocJobPigConfigLoggingConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocJobPigConfigLoggingConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="driverLogLevelsInput")
    def driver_log_levels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "driverLogLevelsInput"))

    @builtins.property
    @jsii.member(jsii_name="driverLogLevels")
    def driver_log_levels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "driverLogLevels"))

    @driver_log_levels.setter
    def driver_log_levels(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobPigConfigLoggingConfigOutputReference, "driver_log_levels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "driverLogLevels", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocJobPigConfigLoggingConfig]:
        return typing.cast(typing.Optional[GoogleDataprocJobPigConfigLoggingConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocJobPigConfigLoggingConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobPigConfigLoggingConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDataprocJobPigConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocJob.GoogleDataprocJobPigConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocJobPigConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putLoggingConfig")
    def put_logging_config(
        self,
        *,
        driver_log_levels: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        '''
        :param driver_log_levels: Optional. The per-package log levels for the driver. This may include 'root' package name to configure rootLogger. Examples: 'com.google = FATAL', 'root = INFO', 'org.apache = DEBUG'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#driver_log_levels GoogleDataprocJob#driver_log_levels}
        '''
        value = GoogleDataprocJobPigConfigLoggingConfig(
            driver_log_levels=driver_log_levels
        )

        return typing.cast(None, jsii.invoke(self, "putLoggingConfig", [value]))

    @jsii.member(jsii_name="resetContinueOnFailure")
    def reset_continue_on_failure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContinueOnFailure", []))

    @jsii.member(jsii_name="resetJarFileUris")
    def reset_jar_file_uris(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJarFileUris", []))

    @jsii.member(jsii_name="resetLoggingConfig")
    def reset_logging_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoggingConfig", []))

    @jsii.member(jsii_name="resetProperties")
    def reset_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProperties", []))

    @jsii.member(jsii_name="resetQueryFileUri")
    def reset_query_file_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryFileUri", []))

    @jsii.member(jsii_name="resetQueryList")
    def reset_query_list(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryList", []))

    @jsii.member(jsii_name="resetScriptVariables")
    def reset_script_variables(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScriptVariables", []))

    @builtins.property
    @jsii.member(jsii_name="loggingConfig")
    def logging_config(self) -> GoogleDataprocJobPigConfigLoggingConfigOutputReference:
        return typing.cast(GoogleDataprocJobPigConfigLoggingConfigOutputReference, jsii.get(self, "loggingConfig"))

    @builtins.property
    @jsii.member(jsii_name="continueOnFailureInput")
    def continue_on_failure_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "continueOnFailureInput"))

    @builtins.property
    @jsii.member(jsii_name="jarFileUrisInput")
    def jar_file_uris_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "jarFileUrisInput"))

    @builtins.property
    @jsii.member(jsii_name="loggingConfigInput")
    def logging_config_input(
        self,
    ) -> typing.Optional[GoogleDataprocJobPigConfigLoggingConfig]:
        return typing.cast(typing.Optional[GoogleDataprocJobPigConfigLoggingConfig], jsii.get(self, "loggingConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="propertiesInput")
    def properties_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "propertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="queryFileUriInput")
    def query_file_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryFileUriInput"))

    @builtins.property
    @jsii.member(jsii_name="queryListInput")
    def query_list_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "queryListInput"))

    @builtins.property
    @jsii.member(jsii_name="scriptVariablesInput")
    def script_variables_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "scriptVariablesInput"))

    @builtins.property
    @jsii.member(jsii_name="continueOnFailure")
    def continue_on_failure(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "continueOnFailure"))

    @continue_on_failure.setter
    def continue_on_failure(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobPigConfigOutputReference, "continue_on_failure").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "continueOnFailure", value)

    @builtins.property
    @jsii.member(jsii_name="jarFileUris")
    def jar_file_uris(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "jarFileUris"))

    @jar_file_uris.setter
    def jar_file_uris(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobPigConfigOutputReference, "jar_file_uris").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jarFileUris", value)

    @builtins.property
    @jsii.member(jsii_name="properties")
    def properties(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "properties"))

    @properties.setter
    def properties(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobPigConfigOutputReference, "properties").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "properties", value)

    @builtins.property
    @jsii.member(jsii_name="queryFileUri")
    def query_file_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "queryFileUri"))

    @query_file_uri.setter
    def query_file_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobPigConfigOutputReference, "query_file_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryFileUri", value)

    @builtins.property
    @jsii.member(jsii_name="queryList")
    def query_list(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "queryList"))

    @query_list.setter
    def query_list(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobPigConfigOutputReference, "query_list").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryList", value)

    @builtins.property
    @jsii.member(jsii_name="scriptVariables")
    def script_variables(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "scriptVariables"))

    @script_variables.setter
    def script_variables(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobPigConfigOutputReference, "script_variables").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scriptVariables", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleDataprocJobPigConfig]:
        return typing.cast(typing.Optional[GoogleDataprocJobPigConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocJobPigConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobPigConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocJob.GoogleDataprocJobPlacement",
    jsii_struct_bases=[],
    name_mapping={"cluster_name": "clusterName"},
)
class GoogleDataprocJobPlacement:
    def __init__(self, *, cluster_name: builtins.str) -> None:
        '''
        :param cluster_name: The name of the cluster where the job will be submitted. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#cluster_name GoogleDataprocJob#cluster_name}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocJobPlacement.__init__)
            check_type(argname="argument cluster_name", value=cluster_name, expected_type=type_hints["cluster_name"])
        self._values: typing.Dict[str, typing.Any] = {
            "cluster_name": cluster_name,
        }

    @builtins.property
    def cluster_name(self) -> builtins.str:
        '''The name of the cluster where the job will be submitted.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#cluster_name GoogleDataprocJob#cluster_name}
        '''
        result = self._values.get("cluster_name")
        assert result is not None, "Required property 'cluster_name' is missing"
        return typing.cast(builtins.str, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocJobPlacement(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocJobPlacementOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocJob.GoogleDataprocJobPlacementOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocJobPlacementOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="clusterUuid")
    def cluster_uuid(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterUuid"))

    @builtins.property
    @jsii.member(jsii_name="clusterNameInput")
    def cluster_name_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "clusterNameInput"))

    @builtins.property
    @jsii.member(jsii_name="clusterName")
    def cluster_name(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "clusterName"))

    @cluster_name.setter
    def cluster_name(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobPlacementOutputReference, "cluster_name").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clusterName", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleDataprocJobPlacement]:
        return typing.cast(typing.Optional[GoogleDataprocJobPlacement], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocJobPlacement],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobPlacementOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocJob.GoogleDataprocJobPrestoConfig",
    jsii_struct_bases=[],
    name_mapping={
        "client_tags": "clientTags",
        "continue_on_failure": "continueOnFailure",
        "logging_config": "loggingConfig",
        "output_format": "outputFormat",
        "properties": "properties",
        "query_file_uri": "queryFileUri",
        "query_list": "queryList",
    },
)
class GoogleDataprocJobPrestoConfig:
    def __init__(
        self,
        *,
        client_tags: typing.Optional[typing.Sequence[builtins.str]] = None,
        continue_on_failure: typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]] = None,
        logging_config: typing.Optional[typing.Union["GoogleDataprocJobPrestoConfigLoggingConfig", typing.Dict[str, typing.Any]]] = None,
        output_format: typing.Optional[builtins.str] = None,
        properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        query_file_uri: typing.Optional[builtins.str] = None,
        query_list: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param client_tags: Presto client tags to attach to this query. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#client_tags GoogleDataprocJob#client_tags}
        :param continue_on_failure: Whether to continue executing queries if a query fails. Setting to true can be useful when executing independent parallel queries. Defaults to false. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#continue_on_failure GoogleDataprocJob#continue_on_failure}
        :param logging_config: logging_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#logging_config GoogleDataprocJob#logging_config}
        :param output_format: The format in which query output will be displayed. See the Presto documentation for supported output formats. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#output_format GoogleDataprocJob#output_format}
        :param properties: A mapping of property names to values. Used to set Presto session properties Equivalent to using the --session flag in the Presto CLI. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#properties GoogleDataprocJob#properties}
        :param query_file_uri: The HCFS URI of the script that contains SQL queries. Conflicts with query_list. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#query_file_uri GoogleDataprocJob#query_file_uri}
        :param query_list: The list of SQL queries or statements to execute as part of the job. Conflicts with query_file_uri. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#query_list GoogleDataprocJob#query_list}
        '''
        if isinstance(logging_config, dict):
            logging_config = GoogleDataprocJobPrestoConfigLoggingConfig(**logging_config)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocJobPrestoConfig.__init__)
            check_type(argname="argument client_tags", value=client_tags, expected_type=type_hints["client_tags"])
            check_type(argname="argument continue_on_failure", value=continue_on_failure, expected_type=type_hints["continue_on_failure"])
            check_type(argname="argument logging_config", value=logging_config, expected_type=type_hints["logging_config"])
            check_type(argname="argument output_format", value=output_format, expected_type=type_hints["output_format"])
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument query_file_uri", value=query_file_uri, expected_type=type_hints["query_file_uri"])
            check_type(argname="argument query_list", value=query_list, expected_type=type_hints["query_list"])
        self._values: typing.Dict[str, typing.Any] = {}
        if client_tags is not None:
            self._values["client_tags"] = client_tags
        if continue_on_failure is not None:
            self._values["continue_on_failure"] = continue_on_failure
        if logging_config is not None:
            self._values["logging_config"] = logging_config
        if output_format is not None:
            self._values["output_format"] = output_format
        if properties is not None:
            self._values["properties"] = properties
        if query_file_uri is not None:
            self._values["query_file_uri"] = query_file_uri
        if query_list is not None:
            self._values["query_list"] = query_list

    @builtins.property
    def client_tags(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Presto client tags to attach to this query.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#client_tags GoogleDataprocJob#client_tags}
        '''
        result = self._values.get("client_tags")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def continue_on_failure(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        '''Whether to continue executing queries if a query fails.

        Setting to true can be useful when executing independent parallel queries. Defaults to false.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#continue_on_failure GoogleDataprocJob#continue_on_failure}
        '''
        result = self._values.get("continue_on_failure")
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], result)

    @builtins.property
    def logging_config(
        self,
    ) -> typing.Optional["GoogleDataprocJobPrestoConfigLoggingConfig"]:
        '''logging_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#logging_config GoogleDataprocJob#logging_config}
        '''
        result = self._values.get("logging_config")
        return typing.cast(typing.Optional["GoogleDataprocJobPrestoConfigLoggingConfig"], result)

    @builtins.property
    def output_format(self) -> typing.Optional[builtins.str]:
        '''The format in which query output will be displayed. See the Presto documentation for supported output formats.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#output_format GoogleDataprocJob#output_format}
        '''
        result = self._values.get("output_format")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def properties(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A mapping of property names to values.

        Used to set Presto session properties Equivalent to using the --session flag in the Presto CLI.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#properties GoogleDataprocJob#properties}
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def query_file_uri(self) -> typing.Optional[builtins.str]:
        '''The HCFS URI of the script that contains SQL queries. Conflicts with query_list.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#query_file_uri GoogleDataprocJob#query_file_uri}
        '''
        result = self._values.get("query_file_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def query_list(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of SQL queries or statements to execute as part of the job. Conflicts with query_file_uri.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#query_list GoogleDataprocJob#query_list}
        '''
        result = self._values.get("query_list")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocJobPrestoConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocJob.GoogleDataprocJobPrestoConfigLoggingConfig",
    jsii_struct_bases=[],
    name_mapping={"driver_log_levels": "driverLogLevels"},
)
class GoogleDataprocJobPrestoConfigLoggingConfig:
    def __init__(
        self,
        *,
        driver_log_levels: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        '''
        :param driver_log_levels: Optional. The per-package log levels for the driver. This may include 'root' package name to configure rootLogger. Examples: 'com.google = FATAL', 'root = INFO', 'org.apache = DEBUG'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#driver_log_levels GoogleDataprocJob#driver_log_levels}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocJobPrestoConfigLoggingConfig.__init__)
            check_type(argname="argument driver_log_levels", value=driver_log_levels, expected_type=type_hints["driver_log_levels"])
        self._values: typing.Dict[str, typing.Any] = {
            "driver_log_levels": driver_log_levels,
        }

    @builtins.property
    def driver_log_levels(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''Optional.

        The per-package log levels for the driver. This may include 'root' package name to configure rootLogger. Examples: 'com.google = FATAL', 'root = INFO', 'org.apache = DEBUG'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#driver_log_levels GoogleDataprocJob#driver_log_levels}
        '''
        result = self._values.get("driver_log_levels")
        assert result is not None, "Required property 'driver_log_levels' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocJobPrestoConfigLoggingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocJobPrestoConfigLoggingConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocJob.GoogleDataprocJobPrestoConfigLoggingConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocJobPrestoConfigLoggingConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="driverLogLevelsInput")
    def driver_log_levels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "driverLogLevelsInput"))

    @builtins.property
    @jsii.member(jsii_name="driverLogLevels")
    def driver_log_levels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "driverLogLevels"))

    @driver_log_levels.setter
    def driver_log_levels(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobPrestoConfigLoggingConfigOutputReference, "driver_log_levels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "driverLogLevels", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocJobPrestoConfigLoggingConfig]:
        return typing.cast(typing.Optional[GoogleDataprocJobPrestoConfigLoggingConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocJobPrestoConfigLoggingConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobPrestoConfigLoggingConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDataprocJobPrestoConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocJob.GoogleDataprocJobPrestoConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocJobPrestoConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putLoggingConfig")
    def put_logging_config(
        self,
        *,
        driver_log_levels: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        '''
        :param driver_log_levels: Optional. The per-package log levels for the driver. This may include 'root' package name to configure rootLogger. Examples: 'com.google = FATAL', 'root = INFO', 'org.apache = DEBUG'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#driver_log_levels GoogleDataprocJob#driver_log_levels}
        '''
        value = GoogleDataprocJobPrestoConfigLoggingConfig(
            driver_log_levels=driver_log_levels
        )

        return typing.cast(None, jsii.invoke(self, "putLoggingConfig", [value]))

    @jsii.member(jsii_name="resetClientTags")
    def reset_client_tags(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetClientTags", []))

    @jsii.member(jsii_name="resetContinueOnFailure")
    def reset_continue_on_failure(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetContinueOnFailure", []))

    @jsii.member(jsii_name="resetLoggingConfig")
    def reset_logging_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoggingConfig", []))

    @jsii.member(jsii_name="resetOutputFormat")
    def reset_output_format(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetOutputFormat", []))

    @jsii.member(jsii_name="resetProperties")
    def reset_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProperties", []))

    @jsii.member(jsii_name="resetQueryFileUri")
    def reset_query_file_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryFileUri", []))

    @jsii.member(jsii_name="resetQueryList")
    def reset_query_list(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryList", []))

    @builtins.property
    @jsii.member(jsii_name="loggingConfig")
    def logging_config(
        self,
    ) -> GoogleDataprocJobPrestoConfigLoggingConfigOutputReference:
        return typing.cast(GoogleDataprocJobPrestoConfigLoggingConfigOutputReference, jsii.get(self, "loggingConfig"))

    @builtins.property
    @jsii.member(jsii_name="clientTagsInput")
    def client_tags_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "clientTagsInput"))

    @builtins.property
    @jsii.member(jsii_name="continueOnFailureInput")
    def continue_on_failure_input(
        self,
    ) -> typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[builtins.bool, cdktf.IResolvable]], jsii.get(self, "continueOnFailureInput"))

    @builtins.property
    @jsii.member(jsii_name="loggingConfigInput")
    def logging_config_input(
        self,
    ) -> typing.Optional[GoogleDataprocJobPrestoConfigLoggingConfig]:
        return typing.cast(typing.Optional[GoogleDataprocJobPrestoConfigLoggingConfig], jsii.get(self, "loggingConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="outputFormatInput")
    def output_format_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "outputFormatInput"))

    @builtins.property
    @jsii.member(jsii_name="propertiesInput")
    def properties_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "propertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="queryFileUriInput")
    def query_file_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryFileUriInput"))

    @builtins.property
    @jsii.member(jsii_name="queryListInput")
    def query_list_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "queryListInput"))

    @builtins.property
    @jsii.member(jsii_name="clientTags")
    def client_tags(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "clientTags"))

    @client_tags.setter
    def client_tags(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobPrestoConfigOutputReference, "client_tags").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "clientTags", value)

    @builtins.property
    @jsii.member(jsii_name="continueOnFailure")
    def continue_on_failure(self) -> typing.Union[builtins.bool, cdktf.IResolvable]:
        return typing.cast(typing.Union[builtins.bool, cdktf.IResolvable], jsii.get(self, "continueOnFailure"))

    @continue_on_failure.setter
    def continue_on_failure(
        self,
        value: typing.Union[builtins.bool, cdktf.IResolvable],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobPrestoConfigOutputReference, "continue_on_failure").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "continueOnFailure", value)

    @builtins.property
    @jsii.member(jsii_name="outputFormat")
    def output_format(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "outputFormat"))

    @output_format.setter
    def output_format(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobPrestoConfigOutputReference, "output_format").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "outputFormat", value)

    @builtins.property
    @jsii.member(jsii_name="properties")
    def properties(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "properties"))

    @properties.setter
    def properties(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobPrestoConfigOutputReference, "properties").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "properties", value)

    @builtins.property
    @jsii.member(jsii_name="queryFileUri")
    def query_file_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "queryFileUri"))

    @query_file_uri.setter
    def query_file_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobPrestoConfigOutputReference, "query_file_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryFileUri", value)

    @builtins.property
    @jsii.member(jsii_name="queryList")
    def query_list(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "queryList"))

    @query_list.setter
    def query_list(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobPrestoConfigOutputReference, "query_list").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryList", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleDataprocJobPrestoConfig]:
        return typing.cast(typing.Optional[GoogleDataprocJobPrestoConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocJobPrestoConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobPrestoConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocJob.GoogleDataprocJobPysparkConfig",
    jsii_struct_bases=[],
    name_mapping={
        "main_python_file_uri": "mainPythonFileUri",
        "archive_uris": "archiveUris",
        "args": "args",
        "file_uris": "fileUris",
        "jar_file_uris": "jarFileUris",
        "logging_config": "loggingConfig",
        "properties": "properties",
        "python_file_uris": "pythonFileUris",
    },
)
class GoogleDataprocJobPysparkConfig:
    def __init__(
        self,
        *,
        main_python_file_uri: builtins.str,
        archive_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        file_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        jar_file_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        logging_config: typing.Optional[typing.Union["GoogleDataprocJobPysparkConfigLoggingConfig", typing.Dict[str, typing.Any]]] = None,
        properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        python_file_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param main_python_file_uri: Required. The HCFS URI of the main Python file to use as the driver. Must be a .py file. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#main_python_file_uri GoogleDataprocJob#main_python_file_uri}
        :param archive_uris: Optional. HCFS URIs of archives to be extracted in the working directory of .jar, .tar, .tar.gz, .tgz, and .zip. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#archive_uris GoogleDataprocJob#archive_uris}
        :param args: Optional. The arguments to pass to the driver. Do not include arguments, such as --conf, that can be set as job properties, since a collision may occur that causes an incorrect job submission Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#args GoogleDataprocJob#args}
        :param file_uris: Optional. HCFS URIs of files to be copied to the working directory of Python drivers and distributed tasks. Useful for naively parallel tasks Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#file_uris GoogleDataprocJob#file_uris}
        :param jar_file_uris: Optional. HCFS URIs of jar files to add to the CLASSPATHs of the Python driver and tasks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#jar_file_uris GoogleDataprocJob#jar_file_uris}
        :param logging_config: logging_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#logging_config GoogleDataprocJob#logging_config}
        :param properties: Optional. A mapping of property names to values, used to configure PySpark. Properties that conflict with values set by the Cloud Dataproc API may be overwritten. Can include properties set in /etc/spark/conf/spark-defaults.conf and classes in user code Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#properties GoogleDataprocJob#properties}
        :param python_file_uris: Optional. HCFS file URIs of Python files to pass to the PySpark framework. Supported file types: .py, .egg, and .zip Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#python_file_uris GoogleDataprocJob#python_file_uris}
        '''
        if isinstance(logging_config, dict):
            logging_config = GoogleDataprocJobPysparkConfigLoggingConfig(**logging_config)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocJobPysparkConfig.__init__)
            check_type(argname="argument main_python_file_uri", value=main_python_file_uri, expected_type=type_hints["main_python_file_uri"])
            check_type(argname="argument archive_uris", value=archive_uris, expected_type=type_hints["archive_uris"])
            check_type(argname="argument args", value=args, expected_type=type_hints["args"])
            check_type(argname="argument file_uris", value=file_uris, expected_type=type_hints["file_uris"])
            check_type(argname="argument jar_file_uris", value=jar_file_uris, expected_type=type_hints["jar_file_uris"])
            check_type(argname="argument logging_config", value=logging_config, expected_type=type_hints["logging_config"])
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument python_file_uris", value=python_file_uris, expected_type=type_hints["python_file_uris"])
        self._values: typing.Dict[str, typing.Any] = {
            "main_python_file_uri": main_python_file_uri,
        }
        if archive_uris is not None:
            self._values["archive_uris"] = archive_uris
        if args is not None:
            self._values["args"] = args
        if file_uris is not None:
            self._values["file_uris"] = file_uris
        if jar_file_uris is not None:
            self._values["jar_file_uris"] = jar_file_uris
        if logging_config is not None:
            self._values["logging_config"] = logging_config
        if properties is not None:
            self._values["properties"] = properties
        if python_file_uris is not None:
            self._values["python_file_uris"] = python_file_uris

    @builtins.property
    def main_python_file_uri(self) -> builtins.str:
        '''Required. The HCFS URI of the main Python file to use as the driver. Must be a .py file.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#main_python_file_uri GoogleDataprocJob#main_python_file_uri}
        '''
        result = self._values.get("main_python_file_uri")
        assert result is not None, "Required property 'main_python_file_uri' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def archive_uris(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional. HCFS URIs of archives to be extracted in the working directory of .jar, .tar, .tar.gz, .tgz, and .zip.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#archive_uris GoogleDataprocJob#archive_uris}
        '''
        result = self._values.get("archive_uris")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def args(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional.

        The arguments to pass to the driver. Do not include arguments, such as --conf, that can be set as job properties, since a collision may occur that causes an incorrect job submission

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#args GoogleDataprocJob#args}
        '''
        result = self._values.get("args")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def file_uris(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional.

        HCFS URIs of files to be copied to the working directory of Python drivers and distributed tasks. Useful for naively parallel tasks

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#file_uris GoogleDataprocJob#file_uris}
        '''
        result = self._values.get("file_uris")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def jar_file_uris(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional. HCFS URIs of jar files to add to the CLASSPATHs of the Python driver and tasks.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#jar_file_uris GoogleDataprocJob#jar_file_uris}
        '''
        result = self._values.get("jar_file_uris")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def logging_config(
        self,
    ) -> typing.Optional["GoogleDataprocJobPysparkConfigLoggingConfig"]:
        '''logging_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#logging_config GoogleDataprocJob#logging_config}
        '''
        result = self._values.get("logging_config")
        return typing.cast(typing.Optional["GoogleDataprocJobPysparkConfigLoggingConfig"], result)

    @builtins.property
    def properties(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Optional.

        A mapping of property names to values, used to configure PySpark. Properties that conflict with values set by the Cloud Dataproc API may be overwritten. Can include properties set in /etc/spark/conf/spark-defaults.conf and classes in user code

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#properties GoogleDataprocJob#properties}
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def python_file_uris(self) -> typing.Optional[typing.List[builtins.str]]:
        '''Optional.

        HCFS file URIs of Python files to pass to the PySpark framework. Supported file types: .py, .egg, and .zip

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#python_file_uris GoogleDataprocJob#python_file_uris}
        '''
        result = self._values.get("python_file_uris")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocJobPysparkConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocJob.GoogleDataprocJobPysparkConfigLoggingConfig",
    jsii_struct_bases=[],
    name_mapping={"driver_log_levels": "driverLogLevels"},
)
class GoogleDataprocJobPysparkConfigLoggingConfig:
    def __init__(
        self,
        *,
        driver_log_levels: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        '''
        :param driver_log_levels: Optional. The per-package log levels for the driver. This may include 'root' package name to configure rootLogger. Examples: 'com.google = FATAL', 'root = INFO', 'org.apache = DEBUG'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#driver_log_levels GoogleDataprocJob#driver_log_levels}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocJobPysparkConfigLoggingConfig.__init__)
            check_type(argname="argument driver_log_levels", value=driver_log_levels, expected_type=type_hints["driver_log_levels"])
        self._values: typing.Dict[str, typing.Any] = {
            "driver_log_levels": driver_log_levels,
        }

    @builtins.property
    def driver_log_levels(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''Optional.

        The per-package log levels for the driver. This may include 'root' package name to configure rootLogger. Examples: 'com.google = FATAL', 'root = INFO', 'org.apache = DEBUG'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#driver_log_levels GoogleDataprocJob#driver_log_levels}
        '''
        result = self._values.get("driver_log_levels")
        assert result is not None, "Required property 'driver_log_levels' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocJobPysparkConfigLoggingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocJobPysparkConfigLoggingConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocJob.GoogleDataprocJobPysparkConfigLoggingConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocJobPysparkConfigLoggingConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="driverLogLevelsInput")
    def driver_log_levels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "driverLogLevelsInput"))

    @builtins.property
    @jsii.member(jsii_name="driverLogLevels")
    def driver_log_levels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "driverLogLevels"))

    @driver_log_levels.setter
    def driver_log_levels(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobPysparkConfigLoggingConfigOutputReference, "driver_log_levels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "driverLogLevels", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocJobPysparkConfigLoggingConfig]:
        return typing.cast(typing.Optional[GoogleDataprocJobPysparkConfigLoggingConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocJobPysparkConfigLoggingConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobPysparkConfigLoggingConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDataprocJobPysparkConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocJob.GoogleDataprocJobPysparkConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocJobPysparkConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putLoggingConfig")
    def put_logging_config(
        self,
        *,
        driver_log_levels: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        '''
        :param driver_log_levels: Optional. The per-package log levels for the driver. This may include 'root' package name to configure rootLogger. Examples: 'com.google = FATAL', 'root = INFO', 'org.apache = DEBUG'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#driver_log_levels GoogleDataprocJob#driver_log_levels}
        '''
        value = GoogleDataprocJobPysparkConfigLoggingConfig(
            driver_log_levels=driver_log_levels
        )

        return typing.cast(None, jsii.invoke(self, "putLoggingConfig", [value]))

    @jsii.member(jsii_name="resetArchiveUris")
    def reset_archive_uris(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArchiveUris", []))

    @jsii.member(jsii_name="resetArgs")
    def reset_args(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArgs", []))

    @jsii.member(jsii_name="resetFileUris")
    def reset_file_uris(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFileUris", []))

    @jsii.member(jsii_name="resetJarFileUris")
    def reset_jar_file_uris(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJarFileUris", []))

    @jsii.member(jsii_name="resetLoggingConfig")
    def reset_logging_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoggingConfig", []))

    @jsii.member(jsii_name="resetProperties")
    def reset_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProperties", []))

    @jsii.member(jsii_name="resetPythonFileUris")
    def reset_python_file_uris(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetPythonFileUris", []))

    @builtins.property
    @jsii.member(jsii_name="loggingConfig")
    def logging_config(
        self,
    ) -> GoogleDataprocJobPysparkConfigLoggingConfigOutputReference:
        return typing.cast(GoogleDataprocJobPysparkConfigLoggingConfigOutputReference, jsii.get(self, "loggingConfig"))

    @builtins.property
    @jsii.member(jsii_name="archiveUrisInput")
    def archive_uris_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "archiveUrisInput"))

    @builtins.property
    @jsii.member(jsii_name="argsInput")
    def args_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "argsInput"))

    @builtins.property
    @jsii.member(jsii_name="fileUrisInput")
    def file_uris_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "fileUrisInput"))

    @builtins.property
    @jsii.member(jsii_name="jarFileUrisInput")
    def jar_file_uris_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "jarFileUrisInput"))

    @builtins.property
    @jsii.member(jsii_name="loggingConfigInput")
    def logging_config_input(
        self,
    ) -> typing.Optional[GoogleDataprocJobPysparkConfigLoggingConfig]:
        return typing.cast(typing.Optional[GoogleDataprocJobPysparkConfigLoggingConfig], jsii.get(self, "loggingConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="mainPythonFileUriInput")
    def main_python_file_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mainPythonFileUriInput"))

    @builtins.property
    @jsii.member(jsii_name="propertiesInput")
    def properties_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "propertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="pythonFileUrisInput")
    def python_file_uris_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "pythonFileUrisInput"))

    @builtins.property
    @jsii.member(jsii_name="archiveUris")
    def archive_uris(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "archiveUris"))

    @archive_uris.setter
    def archive_uris(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobPysparkConfigOutputReference, "archive_uris").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "archiveUris", value)

    @builtins.property
    @jsii.member(jsii_name="args")
    def args(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "args"))

    @args.setter
    def args(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobPysparkConfigOutputReference, "args").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "args", value)

    @builtins.property
    @jsii.member(jsii_name="fileUris")
    def file_uris(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "fileUris"))

    @file_uris.setter
    def file_uris(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobPysparkConfigOutputReference, "file_uris").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileUris", value)

    @builtins.property
    @jsii.member(jsii_name="jarFileUris")
    def jar_file_uris(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "jarFileUris"))

    @jar_file_uris.setter
    def jar_file_uris(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobPysparkConfigOutputReference, "jar_file_uris").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jarFileUris", value)

    @builtins.property
    @jsii.member(jsii_name="mainPythonFileUri")
    def main_python_file_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mainPythonFileUri"))

    @main_python_file_uri.setter
    def main_python_file_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobPysparkConfigOutputReference, "main_python_file_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mainPythonFileUri", value)

    @builtins.property
    @jsii.member(jsii_name="properties")
    def properties(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "properties"))

    @properties.setter
    def properties(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobPysparkConfigOutputReference, "properties").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "properties", value)

    @builtins.property
    @jsii.member(jsii_name="pythonFileUris")
    def python_file_uris(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "pythonFileUris"))

    @python_file_uris.setter
    def python_file_uris(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobPysparkConfigOutputReference, "python_file_uris").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "pythonFileUris", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleDataprocJobPysparkConfig]:
        return typing.cast(typing.Optional[GoogleDataprocJobPysparkConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocJobPysparkConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobPysparkConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocJob.GoogleDataprocJobReference",
    jsii_struct_bases=[],
    name_mapping={"job_id": "jobId"},
)
class GoogleDataprocJobReference:
    def __init__(self, *, job_id: typing.Optional[builtins.str] = None) -> None:
        '''
        :param job_id: The job ID, which must be unique within the project. The job ID is generated by the server upon job submission or provided by the user as a means to perform retries without creating duplicate jobs Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#job_id GoogleDataprocJob#job_id}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocJobReference.__init__)
            check_type(argname="argument job_id", value=job_id, expected_type=type_hints["job_id"])
        self._values: typing.Dict[str, typing.Any] = {}
        if job_id is not None:
            self._values["job_id"] = job_id

    @builtins.property
    def job_id(self) -> typing.Optional[builtins.str]:
        '''The job ID, which must be unique within the project.

        The job ID is generated by the server upon job submission or provided by the user as a means to perform retries without creating duplicate jobs

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#job_id GoogleDataprocJob#job_id}
        '''
        result = self._values.get("job_id")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocJobReference(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocJobReferenceOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocJob.GoogleDataprocJobReferenceOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocJobReferenceOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="resetJobId")
    def reset_job_id(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJobId", []))

    @builtins.property
    @jsii.member(jsii_name="jobIdInput")
    def job_id_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "jobIdInput"))

    @builtins.property
    @jsii.member(jsii_name="jobId")
    def job_id(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "jobId"))

    @job_id.setter
    def job_id(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobReferenceOutputReference, "job_id").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jobId", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleDataprocJobReference]:
        return typing.cast(typing.Optional[GoogleDataprocJobReference], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocJobReference],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobReferenceOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocJob.GoogleDataprocJobScheduling",
    jsii_struct_bases=[],
    name_mapping={
        "max_failures_per_hour": "maxFailuresPerHour",
        "max_failures_total": "maxFailuresTotal",
    },
)
class GoogleDataprocJobScheduling:
    def __init__(
        self,
        *,
        max_failures_per_hour: jsii.Number,
        max_failures_total: jsii.Number,
    ) -> None:
        '''
        :param max_failures_per_hour: Maximum number of times per hour a driver may be restarted as a result of driver exiting with non-zero code before job is reported failed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#max_failures_per_hour GoogleDataprocJob#max_failures_per_hour}
        :param max_failures_total: Maximum number of times in total a driver may be restarted as a result of driver exiting with non-zero code before job is reported failed. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#max_failures_total GoogleDataprocJob#max_failures_total}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocJobScheduling.__init__)
            check_type(argname="argument max_failures_per_hour", value=max_failures_per_hour, expected_type=type_hints["max_failures_per_hour"])
            check_type(argname="argument max_failures_total", value=max_failures_total, expected_type=type_hints["max_failures_total"])
        self._values: typing.Dict[str, typing.Any] = {
            "max_failures_per_hour": max_failures_per_hour,
            "max_failures_total": max_failures_total,
        }

    @builtins.property
    def max_failures_per_hour(self) -> jsii.Number:
        '''Maximum number of times per hour a driver may be restarted as a result of driver exiting with non-zero code before job is reported failed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#max_failures_per_hour GoogleDataprocJob#max_failures_per_hour}
        '''
        result = self._values.get("max_failures_per_hour")
        assert result is not None, "Required property 'max_failures_per_hour' is missing"
        return typing.cast(jsii.Number, result)

    @builtins.property
    def max_failures_total(self) -> jsii.Number:
        '''Maximum number of times in total a driver may be restarted as a result of driver exiting with non-zero code before job is reported failed.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#max_failures_total GoogleDataprocJob#max_failures_total}
        '''
        result = self._values.get("max_failures_total")
        assert result is not None, "Required property 'max_failures_total' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocJobScheduling(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocJobSchedulingOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocJob.GoogleDataprocJobSchedulingOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocJobSchedulingOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="maxFailuresPerHourInput")
    def max_failures_per_hour_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxFailuresPerHourInput"))

    @builtins.property
    @jsii.member(jsii_name="maxFailuresTotalInput")
    def max_failures_total_input(self) -> typing.Optional[jsii.Number]:
        return typing.cast(typing.Optional[jsii.Number], jsii.get(self, "maxFailuresTotalInput"))

    @builtins.property
    @jsii.member(jsii_name="maxFailuresPerHour")
    def max_failures_per_hour(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxFailuresPerHour"))

    @max_failures_per_hour.setter
    def max_failures_per_hour(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobSchedulingOutputReference, "max_failures_per_hour").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxFailuresPerHour", value)

    @builtins.property
    @jsii.member(jsii_name="maxFailuresTotal")
    def max_failures_total(self) -> jsii.Number:
        return typing.cast(jsii.Number, jsii.get(self, "maxFailuresTotal"))

    @max_failures_total.setter
    def max_failures_total(self, value: jsii.Number) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobSchedulingOutputReference, "max_failures_total").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "maxFailuresTotal", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleDataprocJobScheduling]:
        return typing.cast(typing.Optional[GoogleDataprocJobScheduling], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocJobScheduling],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobSchedulingOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocJob.GoogleDataprocJobSparkConfig",
    jsii_struct_bases=[],
    name_mapping={
        "archive_uris": "archiveUris",
        "args": "args",
        "file_uris": "fileUris",
        "jar_file_uris": "jarFileUris",
        "logging_config": "loggingConfig",
        "main_class": "mainClass",
        "main_jar_file_uri": "mainJarFileUri",
        "properties": "properties",
    },
)
class GoogleDataprocJobSparkConfig:
    def __init__(
        self,
        *,
        archive_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        file_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        jar_file_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        logging_config: typing.Optional[typing.Union["GoogleDataprocJobSparkConfigLoggingConfig", typing.Dict[str, typing.Any]]] = None,
        main_class: typing.Optional[builtins.str] = None,
        main_jar_file_uri: typing.Optional[builtins.str] = None,
        properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param archive_uris: HCFS URIs of archives to be extracted in the working directory of .jar, .tar, .tar.gz, .tgz, and .zip. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#archive_uris GoogleDataprocJob#archive_uris}
        :param args: The arguments to pass to the driver. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#args GoogleDataprocJob#args}
        :param file_uris: HCFS URIs of files to be copied to the working directory of Spark drivers and distributed tasks. Useful for naively parallel tasks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#file_uris GoogleDataprocJob#file_uris}
        :param jar_file_uris: HCFS URIs of jar files to add to the CLASSPATHs of the Spark driver and tasks. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#jar_file_uris GoogleDataprocJob#jar_file_uris}
        :param logging_config: logging_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#logging_config GoogleDataprocJob#logging_config}
        :param main_class: The class containing the main method of the driver. Must be in a provided jar or jar that is already on the classpath. Conflicts with main_jar_file_uri Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#main_class GoogleDataprocJob#main_class}
        :param main_jar_file_uri: The HCFS URI of jar file containing the driver jar. Conflicts with main_class. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#main_jar_file_uri GoogleDataprocJob#main_jar_file_uri}
        :param properties: A mapping of property names to values, used to configure Spark. Properties that conflict with values set by the Cloud Dataproc API may be overwritten. Can include properties set in /etc/spark/conf/spark-defaults.conf and classes in user code. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#properties GoogleDataprocJob#properties}
        '''
        if isinstance(logging_config, dict):
            logging_config = GoogleDataprocJobSparkConfigLoggingConfig(**logging_config)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocJobSparkConfig.__init__)
            check_type(argname="argument archive_uris", value=archive_uris, expected_type=type_hints["archive_uris"])
            check_type(argname="argument args", value=args, expected_type=type_hints["args"])
            check_type(argname="argument file_uris", value=file_uris, expected_type=type_hints["file_uris"])
            check_type(argname="argument jar_file_uris", value=jar_file_uris, expected_type=type_hints["jar_file_uris"])
            check_type(argname="argument logging_config", value=logging_config, expected_type=type_hints["logging_config"])
            check_type(argname="argument main_class", value=main_class, expected_type=type_hints["main_class"])
            check_type(argname="argument main_jar_file_uri", value=main_jar_file_uri, expected_type=type_hints["main_jar_file_uri"])
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
        self._values: typing.Dict[str, typing.Any] = {}
        if archive_uris is not None:
            self._values["archive_uris"] = archive_uris
        if args is not None:
            self._values["args"] = args
        if file_uris is not None:
            self._values["file_uris"] = file_uris
        if jar_file_uris is not None:
            self._values["jar_file_uris"] = jar_file_uris
        if logging_config is not None:
            self._values["logging_config"] = logging_config
        if main_class is not None:
            self._values["main_class"] = main_class
        if main_jar_file_uri is not None:
            self._values["main_jar_file_uri"] = main_jar_file_uri
        if properties is not None:
            self._values["properties"] = properties

    @builtins.property
    def archive_uris(self) -> typing.Optional[typing.List[builtins.str]]:
        '''HCFS URIs of archives to be extracted in the working directory of .jar, .tar, .tar.gz, .tgz, and .zip.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#archive_uris GoogleDataprocJob#archive_uris}
        '''
        result = self._values.get("archive_uris")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def args(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The arguments to pass to the driver.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#args GoogleDataprocJob#args}
        '''
        result = self._values.get("args")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def file_uris(self) -> typing.Optional[typing.List[builtins.str]]:
        '''HCFS URIs of files to be copied to the working directory of Spark drivers and distributed tasks.

        Useful for naively parallel tasks.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#file_uris GoogleDataprocJob#file_uris}
        '''
        result = self._values.get("file_uris")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def jar_file_uris(self) -> typing.Optional[typing.List[builtins.str]]:
        '''HCFS URIs of jar files to add to the CLASSPATHs of the Spark driver and tasks.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#jar_file_uris GoogleDataprocJob#jar_file_uris}
        '''
        result = self._values.get("jar_file_uris")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def logging_config(
        self,
    ) -> typing.Optional["GoogleDataprocJobSparkConfigLoggingConfig"]:
        '''logging_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#logging_config GoogleDataprocJob#logging_config}
        '''
        result = self._values.get("logging_config")
        return typing.cast(typing.Optional["GoogleDataprocJobSparkConfigLoggingConfig"], result)

    @builtins.property
    def main_class(self) -> typing.Optional[builtins.str]:
        '''The class containing the main method of the driver.

        Must be in a provided jar or jar that is already on the classpath. Conflicts with main_jar_file_uri

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#main_class GoogleDataprocJob#main_class}
        '''
        result = self._values.get("main_class")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def main_jar_file_uri(self) -> typing.Optional[builtins.str]:
        '''The HCFS URI of jar file containing the driver jar. Conflicts with main_class.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#main_jar_file_uri GoogleDataprocJob#main_jar_file_uri}
        '''
        result = self._values.get("main_jar_file_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def properties(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A mapping of property names to values, used to configure Spark.

        Properties that conflict with values set by the Cloud Dataproc API may be overwritten. Can include properties set in /etc/spark/conf/spark-defaults.conf and classes in user code.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#properties GoogleDataprocJob#properties}
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocJobSparkConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocJob.GoogleDataprocJobSparkConfigLoggingConfig",
    jsii_struct_bases=[],
    name_mapping={"driver_log_levels": "driverLogLevels"},
)
class GoogleDataprocJobSparkConfigLoggingConfig:
    def __init__(
        self,
        *,
        driver_log_levels: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        '''
        :param driver_log_levels: Optional. The per-package log levels for the driver. This may include 'root' package name to configure rootLogger. Examples: 'com.google = FATAL', 'root = INFO', 'org.apache = DEBUG'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#driver_log_levels GoogleDataprocJob#driver_log_levels}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocJobSparkConfigLoggingConfig.__init__)
            check_type(argname="argument driver_log_levels", value=driver_log_levels, expected_type=type_hints["driver_log_levels"])
        self._values: typing.Dict[str, typing.Any] = {
            "driver_log_levels": driver_log_levels,
        }

    @builtins.property
    def driver_log_levels(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''Optional.

        The per-package log levels for the driver. This may include 'root' package name to configure rootLogger. Examples: 'com.google = FATAL', 'root = INFO', 'org.apache = DEBUG'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#driver_log_levels GoogleDataprocJob#driver_log_levels}
        '''
        result = self._values.get("driver_log_levels")
        assert result is not None, "Required property 'driver_log_levels' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocJobSparkConfigLoggingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocJobSparkConfigLoggingConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocJob.GoogleDataprocJobSparkConfigLoggingConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocJobSparkConfigLoggingConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="driverLogLevelsInput")
    def driver_log_levels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "driverLogLevelsInput"))

    @builtins.property
    @jsii.member(jsii_name="driverLogLevels")
    def driver_log_levels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "driverLogLevels"))

    @driver_log_levels.setter
    def driver_log_levels(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobSparkConfigLoggingConfigOutputReference, "driver_log_levels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "driverLogLevels", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocJobSparkConfigLoggingConfig]:
        return typing.cast(typing.Optional[GoogleDataprocJobSparkConfigLoggingConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocJobSparkConfigLoggingConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobSparkConfigLoggingConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDataprocJobSparkConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocJob.GoogleDataprocJobSparkConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocJobSparkConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putLoggingConfig")
    def put_logging_config(
        self,
        *,
        driver_log_levels: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        '''
        :param driver_log_levels: Optional. The per-package log levels for the driver. This may include 'root' package name to configure rootLogger. Examples: 'com.google = FATAL', 'root = INFO', 'org.apache = DEBUG'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#driver_log_levels GoogleDataprocJob#driver_log_levels}
        '''
        value = GoogleDataprocJobSparkConfigLoggingConfig(
            driver_log_levels=driver_log_levels
        )

        return typing.cast(None, jsii.invoke(self, "putLoggingConfig", [value]))

    @jsii.member(jsii_name="resetArchiveUris")
    def reset_archive_uris(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArchiveUris", []))

    @jsii.member(jsii_name="resetArgs")
    def reset_args(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetArgs", []))

    @jsii.member(jsii_name="resetFileUris")
    def reset_file_uris(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetFileUris", []))

    @jsii.member(jsii_name="resetJarFileUris")
    def reset_jar_file_uris(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJarFileUris", []))

    @jsii.member(jsii_name="resetLoggingConfig")
    def reset_logging_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoggingConfig", []))

    @jsii.member(jsii_name="resetMainClass")
    def reset_main_class(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMainClass", []))

    @jsii.member(jsii_name="resetMainJarFileUri")
    def reset_main_jar_file_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetMainJarFileUri", []))

    @jsii.member(jsii_name="resetProperties")
    def reset_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProperties", []))

    @builtins.property
    @jsii.member(jsii_name="loggingConfig")
    def logging_config(
        self,
    ) -> GoogleDataprocJobSparkConfigLoggingConfigOutputReference:
        return typing.cast(GoogleDataprocJobSparkConfigLoggingConfigOutputReference, jsii.get(self, "loggingConfig"))

    @builtins.property
    @jsii.member(jsii_name="archiveUrisInput")
    def archive_uris_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "archiveUrisInput"))

    @builtins.property
    @jsii.member(jsii_name="argsInput")
    def args_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "argsInput"))

    @builtins.property
    @jsii.member(jsii_name="fileUrisInput")
    def file_uris_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "fileUrisInput"))

    @builtins.property
    @jsii.member(jsii_name="jarFileUrisInput")
    def jar_file_uris_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "jarFileUrisInput"))

    @builtins.property
    @jsii.member(jsii_name="loggingConfigInput")
    def logging_config_input(
        self,
    ) -> typing.Optional[GoogleDataprocJobSparkConfigLoggingConfig]:
        return typing.cast(typing.Optional[GoogleDataprocJobSparkConfigLoggingConfig], jsii.get(self, "loggingConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="mainClassInput")
    def main_class_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mainClassInput"))

    @builtins.property
    @jsii.member(jsii_name="mainJarFileUriInput")
    def main_jar_file_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "mainJarFileUriInput"))

    @builtins.property
    @jsii.member(jsii_name="propertiesInput")
    def properties_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "propertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="archiveUris")
    def archive_uris(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "archiveUris"))

    @archive_uris.setter
    def archive_uris(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobSparkConfigOutputReference, "archive_uris").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "archiveUris", value)

    @builtins.property
    @jsii.member(jsii_name="args")
    def args(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "args"))

    @args.setter
    def args(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobSparkConfigOutputReference, "args").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "args", value)

    @builtins.property
    @jsii.member(jsii_name="fileUris")
    def file_uris(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "fileUris"))

    @file_uris.setter
    def file_uris(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobSparkConfigOutputReference, "file_uris").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "fileUris", value)

    @builtins.property
    @jsii.member(jsii_name="jarFileUris")
    def jar_file_uris(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "jarFileUris"))

    @jar_file_uris.setter
    def jar_file_uris(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobSparkConfigOutputReference, "jar_file_uris").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jarFileUris", value)

    @builtins.property
    @jsii.member(jsii_name="mainClass")
    def main_class(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mainClass"))

    @main_class.setter
    def main_class(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobSparkConfigOutputReference, "main_class").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mainClass", value)

    @builtins.property
    @jsii.member(jsii_name="mainJarFileUri")
    def main_jar_file_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "mainJarFileUri"))

    @main_jar_file_uri.setter
    def main_jar_file_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobSparkConfigOutputReference, "main_jar_file_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "mainJarFileUri", value)

    @builtins.property
    @jsii.member(jsii_name="properties")
    def properties(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "properties"))

    @properties.setter
    def properties(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobSparkConfigOutputReference, "properties").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "properties", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleDataprocJobSparkConfig]:
        return typing.cast(typing.Optional[GoogleDataprocJobSparkConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocJobSparkConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobSparkConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocJob.GoogleDataprocJobSparksqlConfig",
    jsii_struct_bases=[],
    name_mapping={
        "jar_file_uris": "jarFileUris",
        "logging_config": "loggingConfig",
        "properties": "properties",
        "query_file_uri": "queryFileUri",
        "query_list": "queryList",
        "script_variables": "scriptVariables",
    },
)
class GoogleDataprocJobSparksqlConfig:
    def __init__(
        self,
        *,
        jar_file_uris: typing.Optional[typing.Sequence[builtins.str]] = None,
        logging_config: typing.Optional[typing.Union["GoogleDataprocJobSparksqlConfigLoggingConfig", typing.Dict[str, typing.Any]]] = None,
        properties: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
        query_file_uri: typing.Optional[builtins.str] = None,
        query_list: typing.Optional[typing.Sequence[builtins.str]] = None,
        script_variables: typing.Optional[typing.Mapping[builtins.str, builtins.str]] = None,
    ) -> None:
        '''
        :param jar_file_uris: HCFS URIs of jar files to be added to the Spark CLASSPATH. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#jar_file_uris GoogleDataprocJob#jar_file_uris}
        :param logging_config: logging_config block. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#logging_config GoogleDataprocJob#logging_config}
        :param properties: A mapping of property names to values, used to configure Spark SQL's SparkConf. Properties that conflict with values set by the Cloud Dataproc API may be overwritten. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#properties GoogleDataprocJob#properties}
        :param query_file_uri: The HCFS URI of the script that contains SQL queries. Conflicts with query_list. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#query_file_uri GoogleDataprocJob#query_file_uri}
        :param query_list: The list of SQL queries or statements to execute as part of the job. Conflicts with query_file_uri. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#query_list GoogleDataprocJob#query_list}
        :param script_variables: Mapping of query variable names to values (equivalent to the Spark SQL command: SET name="value";). Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#script_variables GoogleDataprocJob#script_variables}
        '''
        if isinstance(logging_config, dict):
            logging_config = GoogleDataprocJobSparksqlConfigLoggingConfig(**logging_config)
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocJobSparksqlConfig.__init__)
            check_type(argname="argument jar_file_uris", value=jar_file_uris, expected_type=type_hints["jar_file_uris"])
            check_type(argname="argument logging_config", value=logging_config, expected_type=type_hints["logging_config"])
            check_type(argname="argument properties", value=properties, expected_type=type_hints["properties"])
            check_type(argname="argument query_file_uri", value=query_file_uri, expected_type=type_hints["query_file_uri"])
            check_type(argname="argument query_list", value=query_list, expected_type=type_hints["query_list"])
            check_type(argname="argument script_variables", value=script_variables, expected_type=type_hints["script_variables"])
        self._values: typing.Dict[str, typing.Any] = {}
        if jar_file_uris is not None:
            self._values["jar_file_uris"] = jar_file_uris
        if logging_config is not None:
            self._values["logging_config"] = logging_config
        if properties is not None:
            self._values["properties"] = properties
        if query_file_uri is not None:
            self._values["query_file_uri"] = query_file_uri
        if query_list is not None:
            self._values["query_list"] = query_list
        if script_variables is not None:
            self._values["script_variables"] = script_variables

    @builtins.property
    def jar_file_uris(self) -> typing.Optional[typing.List[builtins.str]]:
        '''HCFS URIs of jar files to be added to the Spark CLASSPATH.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#jar_file_uris GoogleDataprocJob#jar_file_uris}
        '''
        result = self._values.get("jar_file_uris")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def logging_config(
        self,
    ) -> typing.Optional["GoogleDataprocJobSparksqlConfigLoggingConfig"]:
        '''logging_config block.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#logging_config GoogleDataprocJob#logging_config}
        '''
        result = self._values.get("logging_config")
        return typing.cast(typing.Optional["GoogleDataprocJobSparksqlConfigLoggingConfig"], result)

    @builtins.property
    def properties(self) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''A mapping of property names to values, used to configure Spark SQL's SparkConf.

        Properties that conflict with values set by the Cloud Dataproc API may be overwritten.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#properties GoogleDataprocJob#properties}
        '''
        result = self._values.get("properties")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    @builtins.property
    def query_file_uri(self) -> typing.Optional[builtins.str]:
        '''The HCFS URI of the script that contains SQL queries. Conflicts with query_list.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#query_file_uri GoogleDataprocJob#query_file_uri}
        '''
        result = self._values.get("query_file_uri")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def query_list(self) -> typing.Optional[typing.List[builtins.str]]:
        '''The list of SQL queries or statements to execute as part of the job. Conflicts with query_file_uri.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#query_list GoogleDataprocJob#query_list}
        '''
        result = self._values.get("query_list")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def script_variables(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        '''Mapping of query variable names to values (equivalent to the Spark SQL command: SET name="value";).

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#script_variables GoogleDataprocJob#script_variables}
        '''
        result = self._values.get("script_variables")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocJobSparksqlConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocJob.GoogleDataprocJobSparksqlConfigLoggingConfig",
    jsii_struct_bases=[],
    name_mapping={"driver_log_levels": "driverLogLevels"},
)
class GoogleDataprocJobSparksqlConfigLoggingConfig:
    def __init__(
        self,
        *,
        driver_log_levels: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        '''
        :param driver_log_levels: Optional. The per-package log levels for the driver. This may include 'root' package name to configure rootLogger. Examples: 'com.google = FATAL', 'root = INFO', 'org.apache = DEBUG'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#driver_log_levels GoogleDataprocJob#driver_log_levels}
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocJobSparksqlConfigLoggingConfig.__init__)
            check_type(argname="argument driver_log_levels", value=driver_log_levels, expected_type=type_hints["driver_log_levels"])
        self._values: typing.Dict[str, typing.Any] = {
            "driver_log_levels": driver_log_levels,
        }

    @builtins.property
    def driver_log_levels(self) -> typing.Mapping[builtins.str, builtins.str]:
        '''Optional.

        The per-package log levels for the driver. This may include 'root' package name to configure rootLogger. Examples: 'com.google = FATAL', 'root = INFO', 'org.apache = DEBUG'.

        Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#driver_log_levels GoogleDataprocJob#driver_log_levels}
        '''
        result = self._values.get("driver_log_levels")
        assert result is not None, "Required property 'driver_log_levels' is missing"
        return typing.cast(typing.Mapping[builtins.str, builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocJobSparksqlConfigLoggingConfig(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocJobSparksqlConfigLoggingConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocJob.GoogleDataprocJobSparksqlConfigLoggingConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocJobSparksqlConfigLoggingConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @builtins.property
    @jsii.member(jsii_name="driverLogLevelsInput")
    def driver_log_levels_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "driverLogLevelsInput"))

    @builtins.property
    @jsii.member(jsii_name="driverLogLevels")
    def driver_log_levels(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "driverLogLevels"))

    @driver_log_levels.setter
    def driver_log_levels(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobSparksqlConfigLoggingConfigOutputReference, "driver_log_levels").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "driverLogLevels", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[GoogleDataprocJobSparksqlConfigLoggingConfig]:
        return typing.cast(typing.Optional[GoogleDataprocJobSparksqlConfigLoggingConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocJobSparksqlConfigLoggingConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobSparksqlConfigLoggingConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


class GoogleDataprocJobSparksqlConfigOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocJob.GoogleDataprocJobSparksqlConfigOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocJobSparksqlConfigOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute])

    @jsii.member(jsii_name="putLoggingConfig")
    def put_logging_config(
        self,
        *,
        driver_log_levels: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        '''
        :param driver_log_levels: Optional. The per-package log levels for the driver. This may include 'root' package name to configure rootLogger. Examples: 'com.google = FATAL', 'root = INFO', 'org.apache = DEBUG'. Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#driver_log_levels GoogleDataprocJob#driver_log_levels}
        '''
        value = GoogleDataprocJobSparksqlConfigLoggingConfig(
            driver_log_levels=driver_log_levels
        )

        return typing.cast(None, jsii.invoke(self, "putLoggingConfig", [value]))

    @jsii.member(jsii_name="resetJarFileUris")
    def reset_jar_file_uris(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetJarFileUris", []))

    @jsii.member(jsii_name="resetLoggingConfig")
    def reset_logging_config(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetLoggingConfig", []))

    @jsii.member(jsii_name="resetProperties")
    def reset_properties(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetProperties", []))

    @jsii.member(jsii_name="resetQueryFileUri")
    def reset_query_file_uri(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryFileUri", []))

    @jsii.member(jsii_name="resetQueryList")
    def reset_query_list(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetQueryList", []))

    @jsii.member(jsii_name="resetScriptVariables")
    def reset_script_variables(self) -> None:
        return typing.cast(None, jsii.invoke(self, "resetScriptVariables", []))

    @builtins.property
    @jsii.member(jsii_name="loggingConfig")
    def logging_config(
        self,
    ) -> GoogleDataprocJobSparksqlConfigLoggingConfigOutputReference:
        return typing.cast(GoogleDataprocJobSparksqlConfigLoggingConfigOutputReference, jsii.get(self, "loggingConfig"))

    @builtins.property
    @jsii.member(jsii_name="jarFileUrisInput")
    def jar_file_uris_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "jarFileUrisInput"))

    @builtins.property
    @jsii.member(jsii_name="loggingConfigInput")
    def logging_config_input(
        self,
    ) -> typing.Optional[GoogleDataprocJobSparksqlConfigLoggingConfig]:
        return typing.cast(typing.Optional[GoogleDataprocJobSparksqlConfigLoggingConfig], jsii.get(self, "loggingConfigInput"))

    @builtins.property
    @jsii.member(jsii_name="propertiesInput")
    def properties_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "propertiesInput"))

    @builtins.property
    @jsii.member(jsii_name="queryFileUriInput")
    def query_file_uri_input(self) -> typing.Optional[builtins.str]:
        return typing.cast(typing.Optional[builtins.str], jsii.get(self, "queryFileUriInput"))

    @builtins.property
    @jsii.member(jsii_name="queryListInput")
    def query_list_input(self) -> typing.Optional[typing.List[builtins.str]]:
        return typing.cast(typing.Optional[typing.List[builtins.str]], jsii.get(self, "queryListInput"))

    @builtins.property
    @jsii.member(jsii_name="scriptVariablesInput")
    def script_variables_input(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, builtins.str]]:
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, builtins.str]], jsii.get(self, "scriptVariablesInput"))

    @builtins.property
    @jsii.member(jsii_name="jarFileUris")
    def jar_file_uris(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "jarFileUris"))

    @jar_file_uris.setter
    def jar_file_uris(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobSparksqlConfigOutputReference, "jar_file_uris").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "jarFileUris", value)

    @builtins.property
    @jsii.member(jsii_name="properties")
    def properties(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "properties"))

    @properties.setter
    def properties(self, value: typing.Mapping[builtins.str, builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobSparksqlConfigOutputReference, "properties").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "properties", value)

    @builtins.property
    @jsii.member(jsii_name="queryFileUri")
    def query_file_uri(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "queryFileUri"))

    @query_file_uri.setter
    def query_file_uri(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobSparksqlConfigOutputReference, "query_file_uri").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryFileUri", value)

    @builtins.property
    @jsii.member(jsii_name="queryList")
    def query_list(self) -> typing.List[builtins.str]:
        return typing.cast(typing.List[builtins.str], jsii.get(self, "queryList"))

    @query_list.setter
    def query_list(self, value: typing.List[builtins.str]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobSparksqlConfigOutputReference, "query_list").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "queryList", value)

    @builtins.property
    @jsii.member(jsii_name="scriptVariables")
    def script_variables(self) -> typing.Mapping[builtins.str, builtins.str]:
        return typing.cast(typing.Mapping[builtins.str, builtins.str], jsii.get(self, "scriptVariables"))

    @script_variables.setter
    def script_variables(
        self,
        value: typing.Mapping[builtins.str, builtins.str],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobSparksqlConfigOutputReference, "script_variables").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "scriptVariables", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleDataprocJobSparksqlConfig]:
        return typing.cast(typing.Optional[GoogleDataprocJobSparksqlConfig], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[GoogleDataprocJobSparksqlConfig],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobSparksqlConfigOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocJob.GoogleDataprocJobStatus",
    jsii_struct_bases=[],
    name_mapping={},
)
class GoogleDataprocJobStatus:
    def __init__(self) -> None:
        self._values: typing.Dict[str, typing.Any] = {}

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocJobStatus(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocJobStatusList(
    cdktf.ComplexList,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocJob.GoogleDataprocJobStatusList",
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
            type_hints = typing.get_type_hints(GoogleDataprocJobStatusList.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument wraps_set", value=wraps_set, expected_type=type_hints["wraps_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, wraps_set])

    @jsii.member(jsii_name="get")
    def get(self, index: jsii.Number) -> "GoogleDataprocJobStatusOutputReference":
        '''
        :param index: the index of the item to return.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocJobStatusList.get)
            check_type(argname="argument index", value=index, expected_type=type_hints["index"])
        return typing.cast("GoogleDataprocJobStatusOutputReference", jsii.invoke(self, "get", [index]))

    @builtins.property
    @jsii.member(jsii_name="terraformAttribute")
    def _terraform_attribute(self) -> builtins.str:
        '''The attribute on the parent resource this class is referencing.'''
        return typing.cast(builtins.str, jsii.get(self, "terraformAttribute"))

    @_terraform_attribute.setter
    def _terraform_attribute(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobStatusList, "_terraform_attribute").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobStatusList, "_terraform_resource").fset)
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
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobStatusList, "_wraps_set").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "wrapsSet", value)


class GoogleDataprocJobStatusOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocJob.GoogleDataprocJobStatusOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocJobStatusOutputReference.__init__)
            check_type(argname="argument terraform_resource", value=terraform_resource, expected_type=type_hints["terraform_resource"])
            check_type(argname="argument terraform_attribute", value=terraform_attribute, expected_type=type_hints["terraform_attribute"])
            check_type(argname="argument complex_object_index", value=complex_object_index, expected_type=type_hints["complex_object_index"])
            check_type(argname="argument complex_object_is_from_set", value=complex_object_is_from_set, expected_type=type_hints["complex_object_is_from_set"])
        jsii.create(self.__class__, self, [terraform_resource, terraform_attribute, complex_object_index, complex_object_is_from_set])

    @builtins.property
    @jsii.member(jsii_name="details")
    def details(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "details"))

    @builtins.property
    @jsii.member(jsii_name="state")
    def state(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "state"))

    @builtins.property
    @jsii.member(jsii_name="stateStartTime")
    def state_start_time(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "stateStartTime"))

    @builtins.property
    @jsii.member(jsii_name="substate")
    def substate(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "substate"))

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(self) -> typing.Optional[GoogleDataprocJobStatus]:
        return typing.cast(typing.Optional[GoogleDataprocJobStatus], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(self, value: typing.Optional[GoogleDataprocJobStatus]) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobStatusOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


@jsii.data_type(
    jsii_type="@cdktf/provider-google-beta.googleDataprocJob.GoogleDataprocJobTimeouts",
    jsii_struct_bases=[],
    name_mapping={"create": "create", "delete": "delete"},
)
class GoogleDataprocJobTimeouts:
    def __init__(
        self,
        *,
        create: typing.Optional[builtins.str] = None,
        delete: typing.Optional[builtins.str] = None,
    ) -> None:
        '''
        :param create: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#create GoogleDataprocJob#create}.
        :param delete: Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#delete GoogleDataprocJob#delete}.
        '''
        if __debug__:
            type_hints = typing.get_type_hints(GoogleDataprocJobTimeouts.__init__)
            check_type(argname="argument create", value=create, expected_type=type_hints["create"])
            check_type(argname="argument delete", value=delete, expected_type=type_hints["delete"])
        self._values: typing.Dict[str, typing.Any] = {}
        if create is not None:
            self._values["create"] = create
        if delete is not None:
            self._values["delete"] = delete

    @builtins.property
    def create(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#create GoogleDataprocJob#create}.'''
        result = self._values.get("create")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def delete(self) -> typing.Optional[builtins.str]:
        '''Docs at Terraform Registry: {@link https://www.terraform.io/docs/providers/google-beta/r/google_dataproc_job#delete GoogleDataprocJob#delete}.'''
        result = self._values.get("delete")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "GoogleDataprocJobTimeouts(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class GoogleDataprocJobTimeoutsOutputReference(
    cdktf.ComplexObject,
    metaclass=jsii.JSIIMeta,
    jsii_type="@cdktf/provider-google-beta.googleDataprocJob.GoogleDataprocJobTimeoutsOutputReference",
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
            type_hints = typing.get_type_hints(GoogleDataprocJobTimeoutsOutputReference.__init__)
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
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobTimeoutsOutputReference, "create").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "create", value)

    @builtins.property
    @jsii.member(jsii_name="delete")
    def delete(self) -> builtins.str:
        return typing.cast(builtins.str, jsii.get(self, "delete"))

    @delete.setter
    def delete(self, value: builtins.str) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobTimeoutsOutputReference, "delete").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "delete", value)

    @builtins.property
    @jsii.member(jsii_name="internalValue")
    def internal_value(
        self,
    ) -> typing.Optional[typing.Union[GoogleDataprocJobTimeouts, cdktf.IResolvable]]:
        return typing.cast(typing.Optional[typing.Union[GoogleDataprocJobTimeouts, cdktf.IResolvable]], jsii.get(self, "internalValue"))

    @internal_value.setter
    def internal_value(
        self,
        value: typing.Optional[typing.Union[GoogleDataprocJobTimeouts, cdktf.IResolvable]],
    ) -> None:
        if __debug__:
            type_hints = typing.get_type_hints(getattr(GoogleDataprocJobTimeoutsOutputReference, "internal_value").fset)
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
        jsii.set(self, "internalValue", value)


__all__ = [
    "GoogleDataprocJob",
    "GoogleDataprocJobConfig",
    "GoogleDataprocJobHadoopConfig",
    "GoogleDataprocJobHadoopConfigLoggingConfig",
    "GoogleDataprocJobHadoopConfigLoggingConfigOutputReference",
    "GoogleDataprocJobHadoopConfigOutputReference",
    "GoogleDataprocJobHiveConfig",
    "GoogleDataprocJobHiveConfigOutputReference",
    "GoogleDataprocJobPigConfig",
    "GoogleDataprocJobPigConfigLoggingConfig",
    "GoogleDataprocJobPigConfigLoggingConfigOutputReference",
    "GoogleDataprocJobPigConfigOutputReference",
    "GoogleDataprocJobPlacement",
    "GoogleDataprocJobPlacementOutputReference",
    "GoogleDataprocJobPrestoConfig",
    "GoogleDataprocJobPrestoConfigLoggingConfig",
    "GoogleDataprocJobPrestoConfigLoggingConfigOutputReference",
    "GoogleDataprocJobPrestoConfigOutputReference",
    "GoogleDataprocJobPysparkConfig",
    "GoogleDataprocJobPysparkConfigLoggingConfig",
    "GoogleDataprocJobPysparkConfigLoggingConfigOutputReference",
    "GoogleDataprocJobPysparkConfigOutputReference",
    "GoogleDataprocJobReference",
    "GoogleDataprocJobReferenceOutputReference",
    "GoogleDataprocJobScheduling",
    "GoogleDataprocJobSchedulingOutputReference",
    "GoogleDataprocJobSparkConfig",
    "GoogleDataprocJobSparkConfigLoggingConfig",
    "GoogleDataprocJobSparkConfigLoggingConfigOutputReference",
    "GoogleDataprocJobSparkConfigOutputReference",
    "GoogleDataprocJobSparksqlConfig",
    "GoogleDataprocJobSparksqlConfigLoggingConfig",
    "GoogleDataprocJobSparksqlConfigLoggingConfigOutputReference",
    "GoogleDataprocJobSparksqlConfigOutputReference",
    "GoogleDataprocJobStatus",
    "GoogleDataprocJobStatusList",
    "GoogleDataprocJobStatusOutputReference",
    "GoogleDataprocJobTimeouts",
    "GoogleDataprocJobTimeoutsOutputReference",
]

publication.publish()
