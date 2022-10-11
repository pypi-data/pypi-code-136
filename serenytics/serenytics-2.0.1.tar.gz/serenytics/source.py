import json
import logging
import requests
import shutil
import tempfile
import gzip
from uuid import uuid4

import pandas as pd

from serenytics.task import Task
from .helpers import SerenyticsException, make_request, HTTP_201_CREATED
from . import settings

logger = logging.getLogger(__name__)


class UnknownDataSource(SerenyticsException):
    def __init__(self, uuid_or_name):
        super(UnknownDataSource, self).__init__(u'Source with uuid or name "{}" does not exist'.format(uuid_or_name))


class DataSource(object):
    """
    Serenytics data source
    """

    def __init__(self, config, client):
        self._config = config
        self._client = client
        self._headers = client._headers

    def _check_is_storage_source(self):
        if self._config['type'] != 'Storage':
            raise SerenyticsException('Error: You can only reload the data of a storage data source.')

    @property
    def name(self):
        return self._config['name']

    @property
    def uuid(self):
        return self._config['uuid']

    @property
    def type(self):
        return self._config['type']

    @property
    def _measures(self):
        return self._config['jsonContent'].get('measures')

    def reload_data(self, new_data, force_types=None):
        """
        Reset data of a Storage data source.

        It erases old data and loads new data instead.

        :param new_data: list of dicts, each dict is a row
        :param force_types: dict to force the type of a column in the output storage.

        Notes:
            - current data source must be a Storage data source
            - new data doesn't have to have the same structure as old data.
        """
        self._check_is_storage_source()

        # create a pandas dataframe from this data
        df = pd.DataFrame(new_data)

        self.reload_data_from_dataframe(df, force_types=force_types)

    def reload_data_from_array(self, columns, rows, force_types=None):
        """
        Reset data of a Storage data source.

        It erases old data and loads new data instead.

        :param columns: list of string, each string is a column name
        :param rows: list of list of values, each list of values is a row
        :param force_types: dict to force the type of a column in the output storage.

        Notes:
            - current data source must be a Storage data source
            - new data doesn't have to have the same structure as old data.
        """
        self._check_is_storage_source()

        # create a pandas dataframe from this data
        df = pd.DataFrame(rows, columns=columns)

        self.reload_data_from_dataframe(df, force_types=force_types)

    def reload_data_from_dataframe(self, df, force_types=None):
        """
        Reset data of a Storage data source.

        It erases old data and loads new data instead.
        :param df: pandas dataframe to load in the source
        :param force_types: dict to force the type of a column in the output storage.

        Notes:
            - current data source must be a Storage data source
            - new data doesn't have to have the same structure as old data.
        """
        self._check_is_storage_source()

        temp_directory = tempfile.mkdtemp()

        try:
            local_filename = temp_directory + '/' + str(uuid4()) + ".pd025_pickle"
            df.to_pickle(local_filename, compression="gzip")

            # -- upload the file (as source attached file)
            self._upload_attached_file(local_filename, separator=None, force_types=force_types)

            # -- reload the content of the file in the storage
            self._load_attached_file_into_storage()

            shutil.rmtree(temp_directory)
        except Exception as e:
            shutil.rmtree(temp_directory)
            raise e

    def reload_data_from_file(self, filename, separator=',', force_types=None):
        """
        Reset data of a Storage data source.

        It erases old data and loads new data from the given file instead.

        :param filename: path of the file to load. The file must be a csv file (.csv) and can be gzipped (.csv.gz) for
        better transfer speed and shorter script execution times.
        :param separator: CSV field separator, usually a comma or a semicolon.
        :param force_types: Dict of column names with types ('int', 'float', 'datetime', 'str') to force column type in
        our storage.

        Notes:
            - current data source must be a Storage data source
            - new data doesn't have to have the same structure as old data.
        """
        self._check_is_storage_source()

        if not filename.endswith(('.csv', '.csv.gz')):
            raise SerenyticsException('filename must end with ".csv" or ".csv.gz"')

        self._upload_attached_file(filename, separator, force_types)
        self._load_attached_file_into_storage()

    def reload_data_from_s3_file(self, s3_bucket, s3_key, s3_csv_separator=None, s3_region=None, s3_credentials=None,
                                 force_types=None):
        """
        Reset data of a Storage data source.

        It erases old data and loads new data from the given S3 file instead.

        :param s3_bucket: S3 bucket of the object to load
        :param s3_key: S3 key of the object to load
        :param s3_csv_separator: Optional, CSV field separator, usually a comma or a semicolon.
        :param s3_region: Optional, must be provided if region is different from the redshift region
        :param s3_credentials: Optional, must be provided if the object is not public (must be a string with such as
        "aws_access_key_id=my_aws_access_key_id;aws_secret_access_key=my_aws_secret_access_key"
        :param force_types: force some column types

        Notes:
            - current data source must be a Storage data source
            - new data doesn't have to have the same structure as old data.
        """
        self._check_is_storage_source()
        self._load_data_from_s3_file(s3_bucket, s3_key, s3_csv_separator, s3_region, s3_credentials, force_types)

    def update_data_from_file(self, filename, primary_key, separator=','):
        """
        Update data of a Storage data source.

        Inserts new data from filename in current source and replace rows with same primary key as in given file.

        :param filename: path of the file to load. The file must be a csv file (.csv) and can be gzipped (.csv.gz) for
        better transfer speed and shorter script execution times.
        :param primary_key: column name of the primary key (the key used to uniquely define the data rows, such as an id
        or a guid).
        :param separator: CSV field separator, usually a comma or a semicolon.

        Notes:
            - current data source must be a Storage data source
            - new data has to have the same structure as old data
        """
        self._check_is_storage_source()

        if not filename.endswith(('.csv', '.csv.gz')):
            raise SerenyticsException('filename must end with ".csv" or ".csv.gz"')

        self._upload_attached_file(filename, separator=separator)
        self._update_data_from_file(primary_key)

    def _upload_attached_file(self, filename, separator=None, force_types=None):
        """
        Each datasource can have one attached file. This function uploads a local file to the backend as
        the attached file for this datasource.
        If the datasource is a storage, this attached file can then be loaded in the storage with the function
         _load_attached_file_into_storage.
        :param filename: local filepath to load
        :param separator: separator to use when loading this file (only usefull for CSV files)
        :param force_types: types to force when reloading this datasource.
        :return:
        """
        self._config['originalFileName'] = filename

        if separator is not None:
            self._config['jsonContent']['separator'] = separator

        if force_types is not None:
            self._config['jsonContent']['advanced_options'] = json.dumps({'force_types': force_types})

        self.save()

        response = make_request('GET', settings.SERENYTICS_API_DOMAIN + '/api/data_source/sign_s3/',
                                params={'s3_object_type': 'csv/gz', 's3_object_name': self.uuid},
                                headers=self._headers)
        response_content = response.json()

        with open(filename, 'rb') as file_to_upload:
            data = file_to_upload.read()

        if response_content['status'] == 'error':
            # the server doesn't use S3
            make_request('POST', settings.SERENYTICS_API_DOMAIN + '/api/data_source/' + self.uuid + '/file',
                         data=data, headers=self._headers, expected_status_code=HTTP_201_CREATED)
        else:
            make_request('PUT', response_content['signed_request'], data=data,
                         headers={'Content-Type': 'csv/gz', 'x-amz-acl': 'private'})

    def _load_attached_file_into_storage(self):
        response = make_request('POST',
                                settings.SERENYTICS_API_DOMAIN + '/api/data_source/' + self.uuid + '/reload_from_file',
                                data=json.dumps({'async': True}),
                                headers=self._headers)

        task = Task(task_id=response.json()['task_id'], description="Reload data from file", headers=self._headers)
        task.wait()
        task.raise_on_error()
        logger.info('import status: %s' % task.result)

    def _load_data_from_s3_file(self, s3_bucket, s3_key, s3_csv_separator, s3_region, s3_credentials, force_types):
        payload = {
            'async': True,
            's3_bucket': s3_bucket,
            's3_key': s3_key
        }
        if s3_csv_separator:
            payload['s3_csv_separator'] = s3_csv_separator
        if s3_region:
            payload['s3_region'] = s3_region
        if s3_credentials:
            payload['s3_credentials'] = s3_credentials
        if force_types is not None:
            payload['force_types'] = force_types

        response = make_request('POST',
                                settings.SERENYTICS_API_DOMAIN + '/api/data_source/' + self.uuid + '/reload_from_s3',
                                data=json.dumps(payload),
                                headers=self._headers)
        task = Task(task_id=response.json()['task_id'], description="Reload data from S3", headers=self._headers)
        task.wait()
        task.raise_on_error()
        logger.info('import status: %s' % task.result)

    def _update_data_from_file(self, primary_key):
        response = make_request('POST',
                                settings.SERENYTICS_API_DOMAIN + '/api/data_source/' + self.uuid + '/update_from_file',
                                data=json.dumps({'primary_key': primary_key, 'async': True}),
                                headers=self._headers)
        task = Task(task_id=response.json()['task_id'], description="Update data from file", headers=self._headers)
        task.wait()
        task.raise_on_error()

    def batch(self,
              rows_to_insert=None,
              rows_to_insert_or_update=None,
              rows_to_delete=None,
              primary_key=None,
              async_=False):
        """
        Run batch operations on data source (insert/update/delete).

        Note: either `rows_to_insert`, `rows_to_insert_or_update` or `rows_to_delete` must be supplied to the function
        as a list of rows.

        Notes:
            - current data source must be a Storage data source
            - new data has to have the same structure as old data.
        """
        self._check_is_storage_source()

        def _check_argument(arg, name):
            if arg and not isinstance(arg, (list, tuple)):
                raise SerenyticsException('%s must be a list or a tuple, and it was: %r' % (name, arg))

        _check_argument(rows_to_insert, 'rows_to_insert')
        _check_argument(rows_to_insert_or_update, 'rows_to_insert_or_update')
        _check_argument(rows_to_delete, 'rows_to_delete')

        if rows_to_insert is None and rows_to_insert_or_update is None and rows_to_delete is None:
            raise SerenyticsException('at least one argument in `rows_to_insert`, `rows_to_insert_or_update` and'
                                      ' `rows_to_delete` must be not None')
        if (rows_to_insert_or_update or rows_to_delete) and primary_key is None:
            raise SerenyticsException('`primary_key`argument must be not None when updating or deleting rows')

        operations = []

        if rows_to_insert:
            operations.append({
                'action': 'insert',
                'rows': rows_to_insert
            })

        if rows_to_insert_or_update:
            operations.append({
                'action': 'insertOrUpdate',
                'rows': rows_to_insert_or_update,
                'primaryKey': primary_key
            })

        if rows_to_delete:
            operations.append({
                'action': 'delete',
                'rows': rows_to_delete,
                'primaryKey': primary_key
            })

        batch_url = settings.SERENYTICS_API_DOMAIN + '/api/data_source/' + self.uuid + '/batch'
        make_request('post', batch_url, headers=self._headers,
                     data=json.dumps({
                         'async': async_,
                         'operations': operations
                     }),
                     expected_json_status='ok')

    def push_data(self, data):
        """
        Append `data` to current storage data source.

        Warning: this call is not blocking and doesn't wait for the data to be imported into serenytics datawarehouse.
        Then you won't have any guarantee that the data has really been imported. If you need a guarantee, at the
        expense of a longer function call, please use method `batch` and regroup all your rows of data
        in a list.
        """
        self._check_is_storage_source()
        token = self._config['token']
        push_url = settings.SERENYTICS_API_DOMAIN + '/api/data_source/' + self.uuid + '/push/' + token
        make_request('post', push_url, data=json.dumps(data), headers=self._headers)

    def get_value_formula(self, formula_name):
        options = {
            'order': 'row_by_row',
            'data_processing_pipeline': [{
                'select': [{'name': formula_name}]
            }]
        }
        data = self.get_data(options=options)
        if len(data.rows) == 1 and len(data.rows[0]) == 1:
            return data.rows[0][0]
        else:
            raise SerenyticsException("Error: the value formula didn't return a single numeric value.")

    def get_data(self, options=None):
        """
        Extract data from the data source
        """
        no_options = options is None

        if no_options:
            options = {'only_headers': True}

        self._add_measure_uuid_when_needed(options)

        response = make_request('post', settings.SERENYTICS_API_DOMAIN + '/api/formatted_data/' + self.uuid,
                                data=json.dumps(options),
                                headers=self._headers)
        response_content = response.json()

        if response_content['status'] == 'error':
            raise SerenyticsException(response_content['errors'][0])

        if not no_options:
            return Data(response_content)

        # make second API call to retrieve actual data
        headers = response_content['columns_titles']
        new_options = {
            'order': 'row_by_row',
            'data_processing_pipeline': [{
                'select': [header['name'] for header in headers]
            }]
        }
        response = make_request('post', settings.SERENYTICS_API_DOMAIN + '/api/formatted_data/' + self.uuid,
                                data=json.dumps(new_options),
                                headers=self._headers)
        response_content = response.json()

        if response_content['status'] == 'error':
            raise SerenyticsException(response_content['errors'][0])

        return Data(response_content)

    def get_dataset(self):
        """
        Extract dataset from a source into a pandas dataframe (by downloading a file and loading it into a df)
        :return:
        """

        response = make_request('post', settings.SERENYTICS_API_DOMAIN + '/api/data_source/' + self.uuid +
                                '/export_source_data',
                                data=json.dumps({'send_email': False}),
                                headers=self._headers)
        response_content = response.json()
        csv_url = response_content.get('csv_url')
        if not csv_url:
            err = response_content.get('errors', 'Unknown error')
            raise SerenyticsException('Failed to download dataset. %s' % str(err))

        # download the file
        try:
            temp_directory = tempfile.mkdtemp()
            r = requests.get(csv_url, stream=True)
            filename_from_backend = r.headers.get('Content-Disposition')
            if '.csv.gz' in filename_from_backend:
                extension = '.csv.gz'
            else:
                extension = '.csv'
            local_filename = temp_directory + '/' + self.uuid + '.' + extension
            r.raise_for_status()
            with open(local_filename, 'wb') as f:
                for chunk in r.iter_content(chunk_size=8192):
                    if chunk:  # filter out keep-alive new chunks
                        f.write(chunk)

            data_array = pd.read_csv(local_filename)
            shutil.rmtree(temp_directory)

        except Exception as e:
            shutil.rmtree(temp_directory)
            raise e

        return data_array

    def _rename_df_columns_for_joins(self, df):
        join_config = self._config["jsonContent"].get("joinConfig", [])
        renaming_dict = {}
        for c in df.columns:
            for child_ds in join_config:
                new_prefix = child_ds.get("prefix")

                redshift_prefix = "push_" + child_ds.get("uuid", "undefined_uuid").replace("-", "_") + "_"
                if new_prefix and c.startswith(redshift_prefix):
                    new_col_name = c.replace(redshift_prefix, new_prefix + ".")
                    renaming_dict[c] = new_col_name

                default_prefix = child_ds.get("uuid", "undefined_uuid") + "."
                if new_prefix and c.startswith(default_prefix):
                    new_col_name = c.replace(default_prefix, new_prefix + ".")
                    renaming_dict[c] = new_col_name

        df.rename(columns=renaming_dict, inplace=True)

    def _download_file(self, temp_directory, csv_url, generated_file_format):

        r = requests.get(csv_url, stream=True)
        local_filename_to_read = temp_directory + '/' + self.uuid + '.' + generated_file_format
        r.raise_for_status()
        with open(local_filename_to_read, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)
        return local_filename_to_read

    def _load_file(self, temp_directory, generated_file_format, local_filename_to_read, csv_separator):
        if generated_file_format == "csv":
            data_array = pd.read_csv(local_filename_to_read, sep=csv_separator)
        elif generated_file_format == "csv.gz":
            unzipped_file = temp_directory + '/' + self.uuid + '.csv'
            with gzip.open(local_filename_to_read, 'rb') as f_in:
                with open(unzipped_file, 'wb') as f_out:
                    shutil.copyfileobj(f_in, f_out)
            data_array = pd.read_csv(unzipped_file, sep=csv_separator)
        elif generated_file_format == "pickle":
            data_array = pd.read_pickle(local_filename_to_read, compression="gzip")
        elif generated_file_format == "parquet":
            data_array = pd.read_parquet(local_filename_to_read)
        else:
            raise SerenyticsException(f'Unknown format obtained from a datasource export: {generated_file_format}')

        return data_array

    def get_dataset_as_dataframe(self, exchange_format='auto', csv_separator="|", add_quotes_in_csv=False):
        """
        Extract dataset from a source into a pandas dataframe (by downloading a file and loading it into a df).
        This function will replace the function source.get_data().get_as_dataframe().

        :param exchange_format: the file type used to transfer the data.
        Must be in ('auto', 'csv', 'csv.gz', 'parquet'). Default is auto. In auto mode, it choose the best format
        according to the datasource type: parquet for Redshift storage (or a join of Redshift storages) and
        pandas pickle for all other datasource types.
        :param csv_separator: csv separator to use if format csv or csv.gz is used.
        :param add_quotes_in_csv: specify if quotes must be added if format is csv or csv.gz is used.
        :return:
        """

        response = make_request('post', settings.SERENYTICS_API_DOMAIN + '/api/data_source/' + self.uuid +
                                '/export_source_data',
                                data=json.dumps(
                                    {
                                        'export_format': exchange_format,
                                        'send_email': False,
                                        'csv_separator': csv_separator,
                                        'add_quotes': add_quotes_in_csv
                                    }),
                                headers=self._headers)

        response_content = response.json()
        if response_content.get('status', 'ok') == 'error':
            err_str = response_content.get('errors', 'Unknown error')
            raise SerenyticsException('Failed to download dataset. %s' % str(err_str))

        csv_url = response_content.get('csv_url')
        generated_file_format = response_content.get('output_file_format')

        if not csv_url:
            err = response_content.get('errors', 'Unknown error')
            raise SerenyticsException('Failed to download dataset. %s' % str(err))

        try:
            temp_directory = tempfile.mkdtemp()

            # -- download the file
            local_filename_to_read = self._download_file(temp_directory, csv_url, generated_file_format)

            # -- load the file
            data_array = self._load_file(temp_directory, generated_file_format, local_filename_to_read, csv_separator)

            shutil.rmtree(temp_directory)

            # -- rename columns prefixes if the exported datasource is a join
            if self.type == "InnerJoin":
                self._rename_df_columns_for_joins(data_array)

        except Exception as e:
            shutil.rmtree(temp_directory)
            raise e

        return data_array

    def get_columns(self):
        """
        :return: The list of columns of the datasource
        """

        options = {'only_headers': True}

        response = make_request('post', settings.SERENYTICS_API_DOMAIN + '/api/formatted_data/' + self.uuid,
                                data=json.dumps(options),
                                headers=self._headers)
        response_content = response.json()

        if response_content['status'] == 'error':
            raise SerenyticsException(response_content['errors'][0])

        return response_content['columns_titles']

    def get_nb_rows(self):
        """
            Return the nb of rows of the data source
        """
        options = {
            'order': 'row_by_row',
            'data_processing_pipeline': [{
                'select': [{'name': '$$count$$', 'agg_function': 'sum'}],
            }]
        }
        try:
            data = self.get_data(options=options)
            return data.rows[0][0]
        except SerenyticsException as srn_exception:
            if 'Storage source is empty' in str(srn_exception):
                return 0
            else:
                raise srn_exception

    def _add_measure_uuid_when_needed(self, options):
        if 'data_processing_pipeline' not in options:
            return

        measures = self._measures
        if not measures:
            return

        measure_uuid_by_name = {measures[uuid]['name']: uuid for uuid in measures}

        headers_to_process = [
            header
            for header_list in ('select', 'where', 'group_by', 'order_by')
            for step in options['data_processing_pipeline']
            if header_list in step
            for header in step[header_list]
        ]

        for header in headers_to_process:
            if isinstance(header, dict) and 'name' in header:
                name = header['name']
                if name in measure_uuid_by_name:
                    header['measureUuid'] = measure_uuid_by_name[name]

    # for backward compatibility only
    def _save(self):
        self.save()

    def save(self):
        make_request('PUT', settings.SERENYTICS_API_DOMAIN + '/api/data_source/' + self.uuid,
                     data=json.dumps(self._config),
                     headers=self._headers)

    def invalidate_cache(self):
        """
        Invalidate data source cache.

        All get_data() calls or calls made when loading a dashboard using this source won't use current cache.
        Works whatever the cache config of the source (i.e. if the source is static, or cached for 24h, or another
        duration).
        """
        url = settings.SERENYTICS_API_DOMAIN + '/api/data_source/' + self.uuid + '/invalidate_cache'
        make_request('post', url, headers=self._headers)

    def reload_users_metadata(self):
        """
        Reload users metadata with the data from this source.

        The data source should have a first column named login with one row by user in the organization. Other
        columns will be stored as user metadata.

        Note:
        - The user authenticated must be admin of this organization.
        """
        url = settings.SERENYTICS_API_DOMAIN + '/api/data_source/' + self.uuid + '/reload_users_metadata'
        make_request('post', url, headers=self._headers)

    def set_property(self, property_name, value):
        """
        Set a property of this source.
        Contact support@serenytics.com for the list of properties you can set for a given data source type.
        """
        self._config['jsonContent'][property_name] = value


class Data(object):
    """
    Handles data extracted from a data source
    """

    def __init__(self, raw_data):
        self._raw_data = raw_data

    @property
    def headers(self):
        return self._raw_data.get('columns_titles', [])

    @property
    def columns(self):
        return [header['name'] for header in self.headers]

    @property
    def rows(self):
        return self._raw_data.get('data', [])

    def get_as_dataframe(self):
        return pd.DataFrame(self.rows, columns=self.columns)
