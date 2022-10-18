from acceldata_sdk.errors import TorchSdkException
from acceldata_sdk.models.pipeline import CreatePipeline, Pipeline, PipelineRun
from acceldata_sdk.torch_http_client import TorchHttpClient
from acceldata_sdk.models.datasource import CreateDataSource
from acceldata_sdk.constants import RuleExecutionStatus, FailureStrategy, PolicyType, AssetSourceType, \
    SDK_MIN_VERSION_SUPPORT, SdkSupportedVersions
from acceldata_sdk.models.rule import RuleResource
from typing import List
from acceldata_sdk.models.ruleExecutionResult import RuleResult, PolicyFilter, RuleType
from semantic_version import Version, SimpleSpec
import logging
import distutils


class TorchClient:
    logger = logging.getLogger('torch')
    logger.setLevel(logging.INFO)

    """
            Description : Torch user client is used to send data to catalog server.

            :param url: (String) url of the catalog server
            :param timeout_ms: (Integer) timeout of the requests sending to catalog
            :param access_key: (String) Access key of API key. You can generate API key from torch UI's setting
            :param secret_key: (String) Secret key of API key.
            :param do_version_check: (bool) Enable version compatibility check between sdk and torch.


            Ex.  TorchClient = TorchUserClient(url='https://torch.acceldata.local:5443', access_key='OY2VVIN2N6LJ', secret_key='da6bDBimQfXSMsyyhlPVJJfk7Zc2gs')
    """

    def __init__(self, url, timeout_ms=10000, access_key: str = None, secret_key: str = None,
                 do_version_check: bool = True):
        """
                Description : Torch user client is used to send data to catalog server.

                :param url: (String) url of the catalog server
                :param timeout_ms: (Integer) timeout of the requests sending to catalog
                :param access_key: (String) Access key of API key. You can generate API key from torch UI's setting
                :param secret_key: (String) Secret key of API key.
                :param do_version_check: (bool) Enable version compatibility check between sdk and torch.


                Ex.  TorchClient = TorchUserClient(url='https://torch.acceldata.local:5443', access_key='OY2VVIN2N6LJ', secret_key='da6bDBimQfXSMsyyhlPVJJfk7Zc2gs')
        """
        if access_key is None and secret_key is None:
            raise Exception('Access key and secret key - required')
        self.client = TorchHttpClient(url=url, access_key=access_key, secret_key=secret_key, timeout_ms=timeout_ms)
        if isinstance(do_version_check, str):
            self.do_version_check = bool(distutils.util.strtobool(do_version_check))
        else:
            self.do_version_check = do_version_check
        if self.do_version_check:
            supported_versions = self.get_supported_sdk_versions()
            ver_comparator = SimpleSpec(f'>={supported_versions.minVersion},<={supported_versions.maxVersion}')
            if Version(SDK_MIN_VERSION_SUPPORT) not in ver_comparator:
                raise Exception(f'Torch supports sdk versions between {supported_versions.minVersion} and '
                                f'{supported_versions.maxVersion}')
        else:
            self.logger.info('Skipping version check')

    def get_supported_sdk_versions(self) -> SdkSupportedVersions:
        """
        Description:
            To get supported sdk versions
        :return: (SdkSupportedVersions) newly created SdkSupportedVersions class instance
        """
        return self.client.get_supported_sdk_versions()

    def create_pipeline(self, pipeline: CreatePipeline) -> Pipeline:
        """
        Description:
            To create pipeline in torch catalog service
        :param pipeline: (CreatePipeline) class instance of the pipeline to be created
        :return: (Pipeline) newly created pipeline class instance
        """
        if pipeline.uid is None or pipeline.name is None:
            raise Exception('To create a pipeline, pipeline uid/name is required')
        return self.client.create_pipeline(pipeline)

    def get_pipeline(self, pipeline_identity) -> Pipeline:
        """
        Description:
            To get an existing pipeline from torch catalog
        :param pipeline_identity: uid or id of the pipeline
        :return:(Pipeline) pipeline class instance
        """
        return self.client.get_pipeline(pipeline_identity)

    def get_pipelines(self):
        """
        Description:
            To get an all pipelines from torch catalog
        :return:(List[PipelineInfo]) pipeline class instance
        """
        return self.client.get_pipelines()

    def get_spans(self, pipeline_run_id):
        """
        Description:
            To get an all spans from torch catalog
        :param pipeline_run_id: run_id of the pipeline
        :return:(List[Span]) pipeline class instance
        """
        return self.client.get_spans(pipeline_run_id)

    def get_pipeline_run(self, pipeline_run_id: str) -> PipelineRun:
        """
        Description:
            To get an existing pipeline from torch catalog
        :param pipeline_run_id: continuation id or run id of the pipeline run
        :return:(PipelineRun) pipeline run class instance
        """
        return self.client.get_pipeline_run(pipeline_run_id)

    def get_pipeline_runs(self, pipeline_id) -> List[PipelineRun]:
        """
        Description:
            To get an all pipeline runs for a pipeline id from torch catalog
        :param pipeline_id: id of the pipeline
        :return:(List[PipelineRun]) List of pipeline run class instance
        """
        return self.client.get_pipeline_runs(pipeline_id)

    def create_datasource(self, datasource: CreateDataSource):
        """
        Description:
            To create datasource in torch catalog
        :param datasource: (CreateDataSource) class instance of the datasource to be created
        :return: (DataSource) newly created datasource
        """
        return self.client.create_datasource(datasource)

    def get_datasource(self, assembly_identifier, properties=False):
        """
        Description:
            Find datasource by it's name or id in torch catalog
        :param assembly_identifier: name or id of the datasource given in torch
        :param properties: optional parameter, bool, to get datasource properties as well
        :return: (DataSource) datasource
        """
        return self.client.get_datasource(assembly_identifier, properties)

    def get_datasource_by_id(self, id: int, properties: bool = False):
        """
        Description:
            Find datasource by its id in torch catalog
        :param id: id of the datasource given in torch
        :return: (DataSource) datasource
        """
        return self.client.get_datasource_by_id(id, properties)

    def get_datasources(self, type: AssetSourceType = None):
        """
        Description:
            Find datasources by its type in torch catalog
        :param type: type of the datasource given in torch, optional
        :return: list(DataSource) datasource
        """
        return self.client.get_datasources(type)

    def get_all_datasources(self):
        """
        Description:
            list all datasources in torch catalog
        :return: (DataSource) list of datasource
        """
        return self.client.get_all_datasources()

    def start_crawler(self, datasource_name: str):
        """
        Description:
            Start crawler for datasource
        :param datasource_name: name of the datasource given in torch
        :return: (CrawlerStatus) CrawlerStatus
        """
        return self.client.start_crawler(datasource_name)

    def get_crawler_status(self, datasource_name: str):
        """
        Description:
            Get crawler status for datasource
        :param datasource_name: name of the datasource given in torch
        :return: (CrawlerStatus) CrawlerStatus
        """
        return self.client.get_crawler_status(datasource_name)

    def get_asset_types(self):
        """
        Description:
            get all asset types supported in torch catalog
        :return: list of asset types
        """
        return self.client.get_all_asset_types()

    def get_profile_status(self, asset_id: int, req_id: int):
        """
        Description:
            get status of asset profile for given request id
        :return: profiling status
        """
        return self.client.get_profile_request_details(asset_id=asset_id, req_id=req_id)

    def get_all_source_types(self):
        """
        Description:
            get all source types supported in torch catalog
        :return: list of all source type
        """
        return self.client.get_all_source_types()

    def get_property_templates(self):
        pass

    def get_connection_types(self):
        """
        Description:
            get all connection types supported in torch catalog
        :return: list of all connection types
        """
        return self.client.get_connection_types()

    def get_tags(self):
        return self.client.get_tags()

    def delete_tag(self, tag: str):
        return self.client.delete_tag(tag)

    def update_data_protection(self, tag: str, is_protected: bool):
        return self.client.update_data_protection(tag, is_protected)

    def discover(self):
        # add filters in discover api & more details in asset class
        return self.client.discover()

    def list_all_snapshots(self):
        return self.client.list_all_snapshots()

    def get_user(self, user_id=None, username=None):
        if user_id is None and username is None:
            raise TorchSdkException('Either provide uid or id to find an asset')
        if user_id is not None:
            return self.client.get_user_by_id(id=user_id)
        if username is not None:
            return self.client.get_user_by_name(username=username)

    def create_api_key(self):
        return self.client.create_api_keys()

    def get_api_keys(self):
        return self.client.get_api_keys()

    def delete_api_key(self, access_key: str):
        return self.client.delete_api_key(access_key)

    def get_notifications(self):
        return self.client.get_notifications()

    def get_incidents(self):
        return self.client.get_incidents()

    def list_all_analysis_pipelines(self):
        return self.client.list_all_analysis_pipelines()

    def get_analysis_pipeline(self, id: int):
        return self.client.get_analysis_pipeline(id)

    def get_all_auto_profile_configurations(self):
        return self.client.get_all_auto_profile_configurations()

    def get_asset(self, identifier):
        """"
            Description:
                Find an asset of the datasource
            :param identifier: uid or ID of the asset
        """
        return self.client.get_asset(identifier)

    def get_policy(self, type: PolicyType, identifier) -> RuleResource:
        """"
            Description:
                Find policy
            :param identifier: ID or name of the policy
            :param type: type of the policy
        """
        if type.value == PolicyType.DATA_QUALITY.value:
            return self.client.get_dq_rule(identifier)
        elif type.value == PolicyType.RECONCILIATION.value:
            return self.client.get_reconciliation_rule(identifier)
        else:
            raise TorchSdkException('Invalid policy type passed.')

    def list_all_policies(self, filter: PolicyFilter, page=0, size=25, withLatestExecution=True, sortBy='updatedAt:DESC'):
        """
        Description:
            To list all policies based on filter
        :param filter: (Enum PolicyFilter) Type of policies to be executed.
        PolicyFilter can have the following parameters
        period: Time period for which list should be filtered. It is an enum ExecutionPeriod
        tags: tags on which list should be filtered
        lastExecutionResult: lastExecution result on which list should be filtered
        asset: Assets for which policies should be filtered. This list should be of objects of type Asset returned by get_asset
        data_source:  Datasource for which policies should be filtered. This list should be of objects of type Datasource
        returned by get_datasource
        policyType: Type of policy policies should be filtered. This is an enum of type RuleType
        enable: To filter only for enabled policies set enable to True
        active: : To filter only for active policies set active to True
        :param page: (Int) page number of query output
        :param size: (Int) Size of each page
        :param sortBy: (Str) sorting order
        """
        return self.client.get_all_rules(filter=filter, page=page, size=size, sortBy=sortBy,
                                         withLatestExecution=withLatestExecution)

    def list_all_classification_configurations(self):
        return self.client.list_all_classification_configurations()

    def create_classification_configuration(self, classification_config):
        return self.client.create_classification_configuration(classification_config)

    def update_classification_configuration(self, classification_config):
        return self.client.update_classification_configuration(classification_config)

    def get_classification_configuration(self, name: str):
        return self.client.get_classification_configuration(name)

    def delete_classification_configuration(self, name: str):
        return self.client.delete_classification_configuration(name)

    def list_setting_groups(self):
        return self.client.list_setting_groups()

    def find_settings_by_group(self, setting_group_name: str):
        return self.client.find_settings_by_group(setting_group_name)

    def get_setting(self, key: str):
        return self.client.get_setting(key)

    def update_setting_value(self, key: str, value: str):
        return self.client.update_setting_value(key, value)

    def reset_setting_value(self, key:str):
        return self.client.reset_setting_value(key)

    def list_all_connections(self):
        return self.client.list_all_connections()

    def create_connection(self, create_connection):
        return self.client.create_connection(create_connection)

    def update_connection(self, update_connection):
        if update_connection.name is None:
            raise TorchSdkException('Update connection should have name of the connection. (update_connection : '
                                    'CreateConnection class instance)')
        return self.client.update_connection(update_connection.name, update_connection)

    def delete_connection(self, id):
        return self.client.delete_connection(id)

    def check_connection(self, connection):
        return self.client.check_connection(connection)

    def get_connection(self, name):
        return self.client.get_connection(name)

    def execute_dq_rule(self, rule_id, incremental=False):
        return self.client.execute_dq_rule(rule_id, incremental)

    def execute_reconciliation_rule(self, rule_id, incremental=False):
        return self.client.execute_reconciliation_rule(rule_id, incremental)

    def get_dq_rule_execution_details(self, execution_id):
        return self.client.get_dq_rule_execution_details(execution_id)

    def get_reconciliation_rule_execution_details(self, execution_id):
        return self.client.get_reconciliation_rule_execution_details(execution_id)

    def cancel_rule_execution(self, execution_id):
        return self.client.cancel_rule_execution(execution_id)

    def enable_rule(self, rule_id):
        return self.client.enable_rule(rule_id)

    def disable_rule(self, rule_id):
        return self.client.disable_rule(rule_id)

    def get_reconciliation_rule_result(self, execution_id) -> RuleResult:
        return self.client.get_reconciliation_rule_result(execution_id)

    def get_dq_rule_result(self, execution_id) -> RuleResult:
        return self.client.get_dq_rule_result(execution_id)

    def execute_policy(self, policy_type: PolicyType, policy_id, sync=True, incremental=False, failure_strategy: FailureStrategy = FailureStrategy.DoNotFail):
        """
        Description:
            To execute policies synchronously and asynchronously
        :param policy_type: (PolicyType) Type of rule to be executed
        :param policy_id: (String) id of the rule to be executed
        :param sync: (bool) optional Set it to False if asynchronous execution has to be done
        :param incremental: (bool) optional Set it to True if full execution has to be done
        :param failure_strategy: (enum) optional Set it to decide if it should fail at error,
            fail at warning or never fail
        """
        return self.client.execute_rule(policy_type, policy_id, sync, incremental, failure_strategy)

    def get_policy_status(self, policy_type, execution_id) -> RuleExecutionStatus:
        """
        Description:
            To get status of rule execution
        :param policy_type: (PolicyType) Type of rule to be executed
        :param execution_id: (String) ID of execution of the rule previously executed.
        """
        return self.client.get_rule_status(policy_type, execution_id)

    def get_policy_execution_result(self, policy_type: PolicyType, execution_id,
                                    failure_strategy: FailureStrategy = FailureStrategy.DoNotFail):
        """
        Description:
            To get result of rule execution
        :param policy_type: (PolicyType) Type of rule to be executed
        :param execution_id: (String) ID of execution of the rule previously executed.
        :param failure_strategy: (enum) optional Set it to decide if it should fail at error,
            fail at warning or never fail
        """
        return self.client.get_rule_execution_result(policy_type, execution_id, failure_strategy)

    def policy_executions(self, identifier, policy_type: RuleType, page=0, size=25, sortBy='finishedAt:DESC'):
        """
        Description:
            To list rule executions
        :param identifier: id or name of executed rule
        :param policy_type: (Enum RuleType) Type of executed rule
        :param page: (Int) page number of query output
        :param size: (Int) Size of each page
        :param sortBy: (Str) sorting order
        """
        return self.client.policy_executions(identifier, policy_type, page, size, sortBy)
