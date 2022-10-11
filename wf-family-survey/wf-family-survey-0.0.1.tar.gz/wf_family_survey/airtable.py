import wf_core_data
import pandas as pd
from collections import OrderedDict
import datetime
import logging

logger = logging.getLogger(__name__)

class FamilySurveyAirtableClient(wf_core_data.AirtableClient):

    def fetch_school_inputs(
        self,
        pull_datetime=None,
        params=None,
        base_id=wf_core_data.SCHOOLS_BASE_ID,
        format='dataframe',
        delay=wf_core_data.DEFAULT_DELAY,
        max_requests=wf_core_data.DEFAULT_MAX_REQUESTS
    ):
        pull_datetime = wf_core_data.utils.to_datetime(pull_datetime)
        if pull_datetime is None:
            pull_datetime = datetime.datetime.now(tz=datetime.timezone.utc)
        logger.info('Fetching family survey school inputs from Airtable')
        records = self.bulk_get(
            base_id=base_id,
            endpoint='Family survey - school inputs',
            params=params
        )
        school_inputs=list()
        for record in records:
            fields = record.get('fields', {})
            datum = OrderedDict([
                ('school_input_id_at', record.get('id')),
                ('school_input_created_datetime_at', wf_core_data.utils.to_datetime(record.get('createdTime'))),
                ('pull_datetime', pull_datetime),
                ('school_id_at', fields.get('Schools')),
                ('include_school_in_data', fields.get('Include in data')),
                ('include_school_in_reporting', fields.get('Include in reporting')),
                ('school_data_pending', fields.get('Data pending')),
                ('school_report_language', fields.get('Report language')),
                ('num_students', fields.get('Number of students')),
                ('num_forms_sent', fields.get('Number of forms sent'))
            ])
            school_inputs.append(datum)
        if format == 'dataframe':
            school_inputs = convert_school_inputs_to_df(school_inputs)
        elif format == 'list':
            pass
        else:
            raise ValueError('Data format \'{}\' not recognized'.format(format))
        return school_inputs

    def fetch_hub_inputs(
        self,
        pull_datetime=None,
        params=None,
        base_id=wf_core_data.SCHOOLS_BASE_ID,
        format='dataframe',
        delay=wf_core_data.DEFAULT_DELAY,
        max_requests=wf_core_data.DEFAULT_MAX_REQUESTS
    ):
        pull_datetime = wf_core_data.utils.to_datetime(pull_datetime)
        if pull_datetime is None:
            pull_datetime = datetime.datetime.now(tz=datetime.timezone.utc)
        logger.info('Fetching family survey hub inputs from Airtable')
        records = self.bulk_get(
            base_id=base_id,
            endpoint='Family survey - hub inputs',
            params=params
        )
        hub_inputs=list()
        for record in records:
            fields = record.get('fields', {})
            datum = OrderedDict([
                ('hub_input_id_at', record.get('id')),
                ('hub_input_created_datetime_at', wf_core_data.utils.to_datetime(record.get('createdTime'))),
                ('pull_datetime', pull_datetime),
                ('hub_id_at', fields.get('Hubs')),
                ('include_hub_in_reporting', fields.get('Include in reporting')),
                ('hub_data_pending', fields.get('Data pending'))
            ])
            hub_inputs.append(datum)
        if format == 'dataframe':
            hub_inputs = convert_hub_inputs_to_df(hub_inputs)
        elif format == 'list':
            pass
        else:
            raise ValueError('Data format \'{}\' not recognized'.format(format))
        return hub_inputs

    def fetch_excluded_classroom_inputs(
        self,
        pull_datetime=None,
        params=None,
        base_id=wf_core_data.SCHOOLS_BASE_ID,
        format='dataframe',
        delay=wf_core_data.DEFAULT_DELAY,
        max_requests=wf_core_data.DEFAULT_MAX_REQUESTS
    ):
        pull_datetime = wf_core_data.utils.to_datetime(pull_datetime)
        if pull_datetime is None:
            pull_datetime = datetime.datetime.now(tz=datetime.timezone.utc)
        logger.info('Fetching family survey excluded classroom inputs from Airtable')
        records = self.bulk_get(
            base_id=base_id,
            endpoint='Family survey - excluded classroom inputs',
            params=params
        )
        excluded_classroom_inputs = list()
        for record in records:
            fields = record.get('fields', {})
            datum = OrderedDict([
                ('excluded_classroom_input_id_at', record.get('id')),
                ('excluded_classroom_input_created_datetime_at', wf_core_data.utils.to_datetime(record.get('createdTime'))),
                ('pull_datetime', pull_datetime),
                ('school_id_tc', fields.get('TC school ID')),
                ('classroom_id_tc', fields.get('TC classroom ID'))
            ])
            excluded_classroom_inputs.append(datum)
        if format == 'dataframe':
            excluded_classroom_inputs = convert_excluded_classroom_inputs_to_df(excluded_classroom_inputs)
        elif format == 'list':
            pass
        else:
            raise ValueError('Data format \'{}\' not recognized'.format(format))
        return excluded_classroom_inputs

    def fetch_excluded_student_inputs(
        self,
        pull_datetime=None,
        params=None,
        base_id=wf_core_data.SCHOOLS_BASE_ID,
        format='dataframe',
        delay=wf_core_data.DEFAULT_DELAY,
        max_requests=wf_core_data.DEFAULT_MAX_REQUESTS
    ):
        pull_datetime = wf_core_data.utils.to_datetime(pull_datetime)
        if pull_datetime is None:
            pull_datetime = datetime.datetime.now(tz=datetime.timezone.utc)
        logger.info('Fetching family survey excluded student inputs from Airtable')
        records = self.bulk_get(
            base_id=base_id,
            endpoint='Family survey - excluded student inputs',
            params=params
        )
        excluded_student_inputs = list()
        for record in records:
            fields = record.get('fields', {})
            datum = OrderedDict([
                ('excluded_student_input_id_at', record.get('id')),
                ('excluded_student_input_created_datetime_at', wf_core_data.utils.to_datetime(record.get('createdTime'))),
                ('pull_datetime', pull_datetime),
                ('school_id_tc', fields.get('TC school ID')),
                ('student_id_tc', fields.get('TC student ID'))
            ])
            excluded_student_inputs.append(datum)
        if format == 'dataframe':
            excluded_student_inputs = convert_excluded_student_inputs_to_df(excluded_student_inputs)
        elif format == 'list':
            pass
        else:
            raise ValueError('Data format \'{}\' not recognized'.format(format))
        return excluded_student_inputs

    def fetch_field_name_inputs(
        self,
        pull_datetime=None,
        params=None,
        base_id=wf_core_data.SCHOOLS_BASE_ID,
        format='dataframe',
        delay=wf_core_data.DEFAULT_DELAY,
        max_requests=wf_core_data.DEFAULT_MAX_REQUESTS
    ):
        pull_datetime = wf_core_data.utils.to_datetime(pull_datetime)
        if pull_datetime is None:
            pull_datetime = datetime.datetime.now(tz=datetime.timezone.utc)
        logger.info('Fetching family survey field name inputs from Airtable')
        records = self.bulk_get(
            base_id=base_id,
            endpoint='Family survey - field name inputs',
            params=params
        )
        field_name_inputs = list()
        for record in records:
            fields = record.get('fields', {})
            datum = OrderedDict([
                ('field_name_input_id_at', record.get('id')),
                ('field_name_input_created_datetime_at', wf_core_data.utils.to_datetime(record.get('createdTime'))),
                ('pull_datetime', pull_datetime),
                ('source_field_name', fields.get('Source field name')),
                ('target_field_name', fields.get('Target field name'))
            ])
            field_name_inputs.append(datum)
        if format == 'dataframe':
            field_name_inputs = convert_field_name_inputs_to_df(field_name_inputs)
        elif format == 'list':
            pass
        else:
            raise ValueError('Data format \'{}\' not recognized'.format(format))
        return field_name_inputs

    def fetch_non_tc_form_data(
        self,
        pull_datetime=None,
        params=None,
        base_id=wf_core_data.SCHOOLS_BASE_ID,
        format='dataframe',
        delay=wf_core_data.DEFAULT_DELAY,
        max_requests=wf_core_data.DEFAULT_MAX_REQUESTS
    ):
        pull_datetime = wf_core_data.utils.to_datetime(pull_datetime)
        if pull_datetime is None:
            pull_datetime = datetime.datetime.now(tz=datetime.timezone.utc)
        logger.info('Fetching family survey paper form data from Airtable')
        records = self.bulk_get(
            base_id=base_id,
            endpoint='Family survey non-TC data 2021-22',
            params=params
        )
        non_tc_form_data=list()
        for record in records:
            fields = record.get('fields', {})
            datum = OrderedDict([
                ('non_tc_form_id_at', record.get('id')),
                ('non_tc_form_created_datetime_at', wf_core_data.utils.to_datetime(record.get('createdTime'))),
                ('pull_datetime', pull_datetime),
                ('school_id_at', fields.get('school_id_at')),
                ('student_id_at_auto', wf_core_data.utils.extract_int(fields.get('student_id_at_auto'))),
                ('student_first_name_at', fields.get('student_first_name_at')),
                ('student_last_name_at', fields.get('student_last_name_at')),
                ('ethnicity_category_id_at_list', fields.get('ethnicity_list')),
                ('language_response', fields.get('language_response')),
                ('household_income_category_id_at', fields.get('household_income')),
                ('frl_boolean_category_id_at', fields.get('frl')),
                ('nps_response', wf_core_data.utils.extract_int(fields.get('nps_response'))),
                ('marketing_opt_out_boolean_category_id_at', fields.get('marketing_opt_out')),
                ('feedback_response', fields.get('feedback_response'))
            ])
            non_tc_form_data.append(datum)
        if format == 'dataframe':
            non_tc_form_data = convert_non_tc_form_data_to_df(non_tc_form_data)
        elif format == 'list':
            pass
        else:
            raise ValueError('Data format \'{}\' not recognized'.format(format))
        return non_tc_form_data

def convert_school_inputs_to_df(school_inputs):
    if len(school_inputs) == 0:
        return pd.DataFrame()
    school_inputs_df = pd.DataFrame(
        school_inputs,
        dtype='object'
    )
    school_inputs_df['pull_datetime'] = pd.to_datetime(school_inputs_df['pull_datetime'])
    school_inputs_df['school_input_created_datetime_at'] = pd.to_datetime(school_inputs_df['school_input_created_datetime_at'])
    school_inputs_df['school_id_at'] = school_inputs_df['school_id_at'].apply(wf_core_data.utils.to_singleton)
    school_inputs_df = school_inputs_df.astype({
        'school_input_id_at': 'string',
        'school_id_at': 'string',
        'include_school_in_data': 'bool',
        'include_school_in_reporting': 'bool',
        'school_data_pending': 'bool',
        'num_students': 'Int64',
        'num_forms_sent': 'Int64'
    })
    school_inputs_df.set_index('school_input_id_at', inplace=True)
    return school_inputs_df

def convert_hub_inputs_to_df(hub_inputs):
    if len(hub_inputs) == 0:
        return pd.DataFrame()
    hub_inputs_df = pd.DataFrame(
        hub_inputs,
        dtype='object'
    )
    hub_inputs_df['pull_datetime'] = pd.to_datetime(hub_inputs_df['pull_datetime'])
    hub_inputs_df['hub_input_created_datetime_at'] = pd.to_datetime(hub_inputs_df['hub_input_created_datetime_at'])
    hub_inputs_df['hub_id_at'] = hub_inputs_df['hub_id_at'].apply(wf_core_data.utils.to_singleton)
    hub_inputs_df = hub_inputs_df.astype({
        'hub_input_id_at': 'string',
        'hub_id_at': 'string',
        'include_hub_in_reporting': 'bool',
        'hub_data_pending': 'bool'
    })
    hub_inputs_df.set_index('hub_input_id_at', inplace=True)
    return hub_inputs_df

def convert_excluded_classroom_inputs_to_df(excluded_classroom_inputs):
    if len(excluded_classroom_inputs) == 0:
        return pd.DataFrame()
    excluded_classroom_inputs_df = pd.DataFrame(
        excluded_classroom_inputs,
        dtype='object'
    )
    excluded_classroom_inputs_df['pull_datetime'] = pd.to_datetime(excluded_classroom_inputs_df['pull_datetime'])
    excluded_classroom_inputs_df['excluded_classroom_input_created_datetime_at'] = pd.to_datetime(excluded_classroom_inputs_df['excluded_classroom_input_created_datetime_at'])
    excluded_classroom_inputs_df = excluded_classroom_inputs_df.astype({
        'excluded_classroom_input_id_at': 'string',
        'school_id_tc': 'int',
        'classroom_id_tc': 'int'
    })
    excluded_classroom_inputs_df.set_index('excluded_classroom_input_id_at', inplace=True)
    return excluded_classroom_inputs_df

def convert_excluded_student_inputs_to_df(excluded_student_inputs):
    if len(excluded_student_inputs) == 0:
        return pd.DataFrame()
    excluded_student_inputs_df = pd.DataFrame(
        excluded_student_inputs,
        dtype='object'
    )
    excluded_student_inputs_df['pull_datetime'] = pd.to_datetime(excluded_student_inputs_df['pull_datetime'])
    excluded_student_inputs_df['excluded_student_input_created_datetime_at'] = pd.to_datetime(excluded_student_inputs_df['excluded_student_input_created_datetime_at'])
    excluded_student_inputs_df = excluded_student_inputs_df.astype({
        'excluded_student_input_id_at': 'string',
        'school_id_tc': 'int',
        'student_id_tc': 'int'
    })
    excluded_student_inputs_df.set_index('excluded_student_input_id_at', inplace=True)
    return excluded_student_inputs_df

def convert_field_name_inputs_to_df(field_name_inputs):
    if len(field_name_inputs) == 0:
        return pd.DataFrame()
    field_name_inputs_df = pd.DataFrame(
        field_name_inputs,
        dtype='object'
    )
    field_name_inputs_df['pull_datetime'] = pd.to_datetime(field_name_inputs_df['pull_datetime'])
    field_name_inputs_df['field_name_input_created_datetime_at'] = pd.to_datetime(field_name_inputs_df['field_name_input_created_datetime_at'])
    field_name_inputs_df = field_name_inputs_df.astype({
        'field_name_input_id_at': 'string',
        'source_field_name': 'string',
        'target_field_name': 'string'
    })
    field_name_inputs_df.set_index('field_name_input_id_at', inplace=True)
    return field_name_inputs_df

def convert_non_tc_form_data_to_df(non_tc_form_data):
    if len(non_tc_form_data) == 0:
        return pd.DataFrame()
    non_tc_form_data_df = pd.DataFrame(
        non_tc_form_data,
        dtype='object'
    )
    non_tc_form_data_df['pull_datetime'] = pd.to_datetime(non_tc_form_data_df['pull_datetime'])
    non_tc_form_data_df['non_tc_form_created_datetime_at'] = pd.to_datetime(non_tc_form_data_df['non_tc_form_created_datetime_at'])
    non_tc_form_data_df['school_id_at'] = non_tc_form_data_df['school_id_at'].apply(wf_core_data.utils.to_singleton)
    non_tc_form_data_df['household_income_category_id_at'] = non_tc_form_data_df['household_income_category_id_at'].apply(wf_core_data.utils.to_singleton)
    non_tc_form_data_df['frl_boolean_category_id_at'] = non_tc_form_data_df['frl_boolean_category_id_at'].apply(wf_core_data.utils.to_singleton)
    non_tc_form_data_df['marketing_opt_out_boolean_category_id_at'] = non_tc_form_data_df['marketing_opt_out_boolean_category_id_at'].apply(wf_core_data.utils.to_singleton)
    non_tc_form_data_df = non_tc_form_data_df.astype({
        'school_id_at': 'string',
        'student_id_at_auto': 'int',
        'student_first_name_at': 'string',
        'student_last_name_at': 'string',
        'language_response': 'string',
        'household_income_category_id_at': 'string',
        'frl_boolean_category_id_at': 'string',
        'nps_response': 'Int64',
        'marketing_opt_out_boolean_category_id_at': 'string',
        'feedback_response': 'string'
    })
    non_tc_form_data_df.set_index('non_tc_form_id_at', inplace=True)
    return non_tc_form_data_df
