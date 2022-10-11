import wf_core_data
import pandas as pd
import numpy as np
from collections import OrderedDict
import datetime
import re
import logging

logger = logging.getLogger(__name__)

class FamilySurveyTransparentClassroomClient(wf_core_data.TransparentClassroomClient):

    def fetch_family_survey_form_data(
        self,
        field_name_lookup,
        family_survey_school_form_template_ids=None,
        family_survey_network_form_template_ids=None,
        template_name_re=None,
        school_ids=None
    ):
        if family_survey_school_form_template_ids is None:
            logger.info('Family survey school form template IDs not specified. Fetching.')
            family_survey_school_form_template_ids = self.fetch_family_survey_school_form_template_ids(
                family_survey_network_form_template_ids=family_survey_network_form_template_ids,
                template_name_re=template_name_re,
                school_ids=school_ids
            )
        form_data=list()
        for school_id, form_template_id in family_survey_school_form_template_ids:
            logger.info('Fetching data for school ID {} and form template ID {}'.format(
                school_id,
                form_template_id
            ))
            form_data_school = self.fetch_form_data_school(
                school_id=school_id,
                form_template_id=form_template_id,
                format='list'
            )
            for form_datum in form_data_school:
                fields = form_datum.pop('form_fields')
                for key, value in fields.items():
                    form_datum[field_name_lookup[key]] = value
                form_data.append(form_datum)
        form_data = pd.DataFrame(form_data)
        form_data['pull_datetime'] = pd.to_datetime(form_data['pull_datetime'], utc=True)
        form_data['form_created'] = pd.to_datetime(form_data['form_created'], utc=True)
        form_data['form_updated'] = pd.to_datetime(form_data['form_updated'], utc=True)
        form_data['form_last_emailed'] = pd.to_datetime(form_data['form_last_emailed'], utc=True)
        form_data['form_due_date'] = pd.to_datetime(form_data['form_due_date'], utc=True)
        type_dict_all = {
            'school_id_tc': 'int',
            'form_id_tc': 'int',
            'student_id_tc': 'int',
            'form_template_id_tc': 'int',
            'form_state': 'string',
            'nps_response': 'string',
            'feedback_response': 'string',
            'language_response': 'string',
            'household_size_response': 'string',
            'household_income_response': 'string',
            'frl_response': 'string',
            'marketing_opt_out_response': 'string'
        }
        type_dict = {column: type_dict_all[column] for column in form_data.columns if column in type_dict_all.keys()}
        form_data = form_data.astype(type_dict)
        form_data.set_index(['school_id_tc', 'form_id_tc'], inplace=True)
        return form_data

    def fetch_family_survey_school_form_template_ids(
        self,
        family_survey_network_form_template_ids=None,
        template_name_re=None,
        school_ids=None
    ):
        school_form_template_data = self.fetch_family_survey_school_form_template_data(
            family_survey_network_form_template_ids=family_survey_network_form_template_ids,
            template_name_re=template_name_re,
            school_ids=school_ids
        )
        family_survey_school_form_template_ids = list(
            school_form_template_data.index[school_form_template_data['is_family_survey_template']]
        )
        return family_survey_school_form_template_ids

    def fetch_family_survey_school_form_template_data(
        self,
        family_survey_network_form_template_ids=None,
        template_name_re=None,
        school_ids=None
    ):
        if family_survey_network_form_template_ids is None:
            if template_name_re is None:
                raise ValueError('Must specify either a set of family survey network form template IDs or regular expression which matchs family survey network form names')
            family_survey_network_form_template_ids = self.fetch_family_survey_network_form_template_ids(template_name_re)
        form_template_data = self.fetch_form_template_data(
            school_ids=school_ids,
            format='dataframe'
        )
        form_template_data['is_family_survey_template'] = form_template_data['widgets'].apply(
            lambda widgets: np.any([
                (widget.get('type') == 'EmbeddedForm') and (int(widget.get('embedded_form_id')) in family_survey_network_form_template_ids)
                for widget in widgets
            ])
        )
        form_template_data['is_family_survey_template'] = form_template_data['is_family_survey_template'].astype('bool')
        form_template_data = form_template_data.reindex(columns=[
            'form_template_name',
            'is_family_survey_template'
        ])
        form_template_data.sort_values('is_family_survey_template', ascending = False, inplace = True)
        return form_template_data

    def fetch_family_survey_network_form_template_ids(
        self,
        template_name_re
    ):
        network_form_template_data = self.fetch_family_survey_network_form_template_data(
            template_name_re=template_name_re
        )
        family_survey_network_form_template_ids = list(
            network_form_template_data.index[network_form_template_data['is_family_survey_template']]
        )
        return family_survey_network_form_template_ids

    def fetch_family_survey_network_form_template_data(
        self,
        template_name_re
    ):
        network_form_template_data = self.fetch_network_form_template_data(format='dataframe')
        template_name_re_compiled = re.compile(template_name_re)
        network_form_template_data['is_family_survey_template'] = network_form_template_data['form_template_name'].apply(
            lambda x: template_name_re_compiled.match(x) is not None
        )
        network_form_template_data['is_family_survey_template'] = network_form_template_data['is_family_survey_template'].astype('bool')
        network_form_template_data = network_form_template_data.reindex(columns=[
            'form_template_name',
            'is_family_survey_template'
        ])
        network_form_template_data.sort_values('is_family_survey_template', ascending = False, inplace = True)
        return network_form_template_data
