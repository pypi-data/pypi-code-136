import inspect
import pandas as pd
from joblib import Parallel, delayed
import qtc.utils.misc_utils as mu
from qtc.ext.multiprocessing import infer_joblib_backend, run_multi_dateids_joblib
from qtc.consts.enums import DateDataType
import qtc.utils.datetime_utils as dtu
from backup.calendar.factor_model_calendar import FactorModelCalendar
import qtc.data.factor_model as fm
from qtc.ext.logging import set_logger
logger = set_logger()


class TaskExecutor:
    @classmethod
    def run_tasks_single_model_multi_dates(cls, run_tasks_single_date_func,
                                           risk_region=None, factor_model_code=None,
                                           start_date=None, end_date=None, date_range_mode='SINGLE_DATE',
                                           concat_axis=None,
                                           n_jobs=1,
                                           **kwargs):
        dateids, start_dateid, end_dateid = \
            FactorModelCalendar.infer_trading_dateids(risk_region=risk_region, factor_model_code=factor_model_code,
                                                      start_date=start_date, end_date=end_date,
                                                      date_range_mode=date_range_mode)

        func_arg_names = set(inspect.signature(run_tasks_single_date_func).parameters.keys())

        kwargs = {key:value for key,value in kwargs.items() if key in func_arg_names}
        for arg_name in ['risk_region','factor_model_code']:
            if arg_name in func_arg_names:
                kwargs[arg_name] = eval(arg_name)

        ret = list()
        if n_jobs!=1:
            ret = run_multi_dateids_joblib(dateids=dateids, func=run_tasks_single_date_func,
                                           concat_axis=concat_axis,
                                           n_jobs=n_jobs,
                                           **kwargs)
        else:
            for dateid in dateids:
                data = run_tasks_single_date_func(dateid=dateid, **kwargs)
                if data is not None and concat_axis is not None:
                    ret.append(data)

            if concat_axis is not None:
                ret = pd.concat(ret, axis=concat_axis, sort=False)

        return dateids, start_dateid, end_dateid, ret

    @classmethod
    def run_tasks_multi_dates(cls, run_tasks_single_date_func,
                              start_date=None, end_date=None, date_range_mode='SINGLE_DATE',
                              concat_axis=None,
                              n_jobs=1,
                              **kwargs):
        return TaskExecutor.run_tasks_single_model_multi_dates(
            run_tasks_single_date_func=run_tasks_single_date_func,
            risk_region='WW',
            start_date=start_date, end_date=end_date, date_range_mode=date_range_mode,
            concat_axis=concat_axis,
            n_jobs=n_jobs,
            **kwargs)

    @classmethod
    def _run_single_model_single_dt(cls,
                                    run_tasks_single_model_single_dt_func,
                                    dt,
                                    factor_model_code,
                                    dt_arg,
                                    concat_axis=None,
                                    **kwargs):
        dateid = dtu.normalize_date_to_dateid(date=dt)

        if not FactorModelCalendar.is_trading_date(factor_model_code=factor_model_code, dateid=dateid):
            return None

        kwargs.update({dt_arg: dt})
        data = run_tasks_single_model_single_dt_func(factor_model_code=factor_model_code,
                                                     **kwargs)
        if data is not None and concat_axis is not None:
            data['FactorModel'] = factor_model_code

        return data

    @classmethod
    def run_multi_models_single_dt(cls, run_tasks_single_model_single_dt_func,
                                   factor_model_codes,
                                   dt=None, dateid=None,
                                   concat_axis=None,
                                   n_jobs=1,
                                   use_default_backend=False,
                                   **kwargs):
        if dt is None:
            dt = dateid

        func_arg_names = set(inspect.signature(run_tasks_single_model_single_dt_func).parameters.keys())
        found_dt_arg = False
        for dt_arg in ['dateid','calendar','dt']:
            if dt_arg in func_arg_names:
                found_dt_arg = True
                break

        if not found_dt_arg:
            logger.warn(f'Failed to find datetime like argument [dateid|calendar|dt] in the signature of'
                        f' run_tasks_single_model_single_dt_func={run_tasks_single_model_single_dt_func} !')
            return None

        factor_model_codes = mu.iterable_to_tuple(factor_model_codes, raw_type='str')
        ret = list()
        if n_jobs==1 or len(factor_model_codes)<=2:
            for factor_model_code in factor_model_codes:
                data = TaskExecutor._run_single_model_single_dt(run_tasks_single_model_single_dt_func=run_tasks_single_model_single_dt_func,
                                                                dt=dt,
                                                                factor_model_code=factor_model_code,
                                                                dt_arg=dt_arg,
                                                                concat_axis=concat_axis,
                                                                **kwargs)
                if data is not None and concat_axis is not None:
                    ret.append(data)
        else:
            backend = infer_joblib_backend(use_default=use_default_backend)
            ret = Parallel(n_jobs=n_jobs, backend=backend)(delayed(function=TaskExecutor._run_single_model_single_dt)
                                                           (run_tasks_single_model_single_dt_func=run_tasks_single_model_single_dt_func,
                                                            dt=dt,
                                                            factor_model_code=factor_model_code,
                                                            dt_arg=dt_arg,
                                                            concat_axis=concat_axis,
                                                            **kwargs)
                                                           for factor_model_code in factor_model_codes)

        if concat_axis is not None:
            ret = pd.concat(ret, axis=concat_axis, sort=False)

        if dateid is not None and isinstance(ret, pd.DataFrame):
            ret['DateId'] = dateid

        return ret

    @classmethod
    def run_tasks_multi_models_multi_dates(cls, run_tasks_single_model_single_date_func,
                                           factor_model_codes,
                                           start_date=None, end_date=None, date_range_mode='SINGLE_DATE',
                                           concat_axis=None,
                                           date_type='DateId',
                                           n_jobs_models=1,
                                           n_jobs_dates=1,
                                           **kwargs):

        factor_model_codes = list(mu.iterable_to_tuple(factor_model_codes, raw_type='str'))
        risk_regions = set(fm.get_static_data().FACTOR_MODEL_CODE_TO_RISK_REGION[factor_model_code]
                           for factor_model_code in factor_model_codes)

        dateids, start_dateid, end_dateid = \
            FactorModelCalendar.infer_trading_dateids(risk_region=list(risk_regions)[0] if len(risk_regions)==1 else 'WW',
                                                      start_date=start_date, end_date=end_date,
                                                      date_range_mode=date_range_mode)

        factor_model_codes = list(mu.iterable_to_tuple(factor_model_codes, raw_type='str'))
        if len(factor_model_codes)>2 and n_jobs_dates!=1:
            logger.warn(f'There are more than 2 factor models. Force looping dates without multiprocessing !')
            n_jobs_dates = 1

        ret = list()
        if n_jobs_dates==1 or len(dateids)<=2:
            for dateid in dateids:
                data = TaskExecutor.run_multi_models_single_dt(
                    run_tasks_single_model_single_dt_func=run_tasks_single_model_single_date_func,
                    dateid=dateid, factor_model_codes=factor_model_codes,
                    concat_axis=concat_axis,
                    n_jobs=n_jobs_models,
                    **kwargs)

                if isinstance(data, pd.DataFrame):
                    data['DateId'] = dateid
                if data is not None and concat_axis is not None:
                    ret.append(data)
        else:
            backend = infer_joblib_backend()
            ret = Parallel(n_jobs=n_jobs_dates, backend=backend)(delayed(function=TaskExecutor.run_multi_models_single_dt)
                                                                 (run_tasks_single_model_single_dt_func=run_tasks_single_model_single_date_func,
                                                                  dateid=dateid, factor_model_codes=factor_model_codes,
                                                                  concat_axis=concat_axis,
                                                                  n_jobs=n_jobs_models,
                                                                  **kwargs)
                                                                 for dateid in dateids)

        if concat_axis is not None:
            ret = pd.concat(ret, axis=concat_axis, sort=False)

            if isinstance(date_type, str):
                date_type = DateDataType.retrieve(value=date_type)
            if date_type!=DateDataType.DATEID:
                ret = dtu.convert_data_type_for_date_col(df=ret, date_col='DateId',
                                                         from_data_type='DateId', to_data_type=date_type,
                                                         to_date_col_idx=0)
                ret.drop(columns=['DateId'], inplace=True)

        return dateids, start_dateid, end_dateid, ret