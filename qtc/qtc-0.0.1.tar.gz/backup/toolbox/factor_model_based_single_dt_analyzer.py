import pandas as pd
import quant_common.utils.datetime_utils as dtu
import quant_common.utils.misc_utils as mu
import quant_common.data.biz_entity as be
from quant_common.ext.configurable import Configurable
from quant_common.consts.enums import DataSource

# import bamrisk_equity.utils.datetime_utils as edtu
# import bamrisk_equity.data.static_data as esd
from quant_common.calendar.factor_model_calendar import FactorModelCalendar
import quant_common.data.dal.factor_model as dalfm
import quant_common.data.positions as epos
import quant_common.data.factor_model as fm
from quant_common.consts.enums import PositionType, CrossSectionalDataFormat, Symbology, FactorIdentifier, TradingRegion
from quant_common.ext.logging import set_logger
logger = set_logger()


class FactorModelBasedSingleDTAnalyzer(Configurable):
    DEFAULT_CONFIG = {'timezone': None, 'symbology': 'SecurityId',
                      # 'factor_model_code': None,
                      'acug_codes': None, 'acu_codes': None, 'strat_codes': None,
                      'positions_data_sources': 'DB', 'positions_type': 'UCA_V2', 'risk_region_on': True, 'lookthru_baskets': False, 'log_details': False,
                      'factor_identifier': 'FactorDesc',
                      'factor_loadings.data_format': 'MATRIX', 'factor_loadings.attach_factor_type': True,
                      'factor_portfolios.data_format': 'MATRIX', 'factor_portfolios.attach_factor_type': True,
                      'security_risk_attributes_cols': None, 'security_risk_attributes.date_type': 'DateId', 'security_risk_attributes.decimal_unit': 'DECIMAL'}

    @property
    def factor_model_code(self):
        return self.__factor_model_code

    @factor_model_code.setter
    def factor_model_code(self, factor_model_code):
        self.__factor_model_code = factor_model_code

    @property
    def factor_model_id(self):
        return self.__factor_model_id

    @factor_model_id.setter
    def factor_model_id(self, factor_model_id):
        self.__factor_model_id = factor_model_id

    @property
    def risk_region(self):
        return self.__risk_region

    @risk_region.setter
    def risk_region(self, risk_region):
        self.__risk_region = risk_region

    @property
    def pnl_dateid(self):
        return self.__pnl_dateid

    @pnl_dateid.setter
    def pnl_dateid(self, pnl_dateid):
        self.__pnl_dateid = pnl_dateid

    @property
    def position_dateid(self):
        return self.__position_dateid

    @position_dateid.setter
    def position_dateid(self, position_dateid):
        self.__position_dateid = position_dateid

    @property
    def factor_model_dateid(self):
        return self.__factor_model_dateid

    @factor_model_dateid.setter
    def factor_model_dateid(self, factor_model_dateid):
        self.__factor_model_dateid = factor_model_dateid

    # @property
    # def acug_codes(self):
    #     return self.__acug_codes
    #
    # @acug_codes.setter
    # def acug_codes(self, acug_codes):
    #     self.__acug_codes = acug_codes
    #
    # @property
    # def acu_codes(self):
    #     return self.__acu_codes
    #
    # @acu_codes.setter
    # def acu_codes(self, acu_codes):
    #     self.__acu_codes = acu_codes
    #
    # @property
    # def strat_codes(self):
    #     return self.__strat_codes
    #
    # @strat_codes.setter
    # def strat_codes(self, strat_codes):
    #     self.__strat_codes = strat_codes
    #
    # @property
    # def trading_region(self):
    #     return self.__trading_region
    #
    # @trading_region.setter
    # def trading_region(self, trading_region):
    #     self.__trading_region = trading_region

    @property
    def symbology(self):
        return self.__symbology

    @symbology.setter
    def symbology(self, symbology):
        self.__symbology = symbology

    @property
    def positions(self):
        return self.__positions

    @positions.setter
    def positions(self, positions):
        self.__positions = positions

    @property
    def factor_identifier(self):
        return self.__factor_identifier

    @factor_identifier.setter
    def factor_identifier(self, factor_identifier):
        self.__factor_identifier = factor_identifier

    @property
    def factor_loadings_rd_factors(self):
        return self.__factor_loadings_rd_factors

    @factor_loadings_rd_factors.setter
    def factor_loadings_rd_factors(self, factor_loadings_rd_factors):
        self.__factor_loadings_rd_factors = factor_loadings_rd_factors

    @property
    def factor_portfolios_rd_factors(self):
        return self.__factor_portfolios_rd_factors

    @factor_portfolios_rd_factors.setter
    def factor_portfolios_rd_factors(self, factor_portfolios_rd_factors):
        self.__factor_portfolios_rd_factors = factor_portfolios_rd_factors

    @property
    def security_risk_attributes(self):
        return self.__security_risk_attributes

    @security_risk_attributes.setter
    def security_risk_attributes(self, security_risk_attributes):
        self.__security_risk_attributes = security_risk_attributes

    @property
    def security_factor_exps_rd_factors(self):
        return self.__security_factor_exps_rd_factors

    @security_factor_exps_rd_factors.setter
    def security_factor_exps_rd_factors(self, security_factor_exps_rd_factors):
        self.__security_factor_exps_rd_factors = security_factor_exps_rd_factors

    def _normalize_dateids(self,
                           pnl_dateid=None, position_dateid=None, factor_model_dateid=None,
                           timezone=None):
        if pnl_dateid is None and position_dateid is None and factor_model_dateid is None:
            pnl_dateid = FactorModelCalendar.get_best_trading_dateid(risk_region=self.risk_region, timezone=timezone)
            logger.warn(f'pnl_dateid is set to {pnl_dateid} since '
                        f'none of (pnl_dateid, position_dateid, factor_model_dateid) is explicitly provided!')

        model_date_offset = -2 if dalfm.is_attribution_model(factor_model_id=self.factor_model_id) else -1

        if pnl_dateid is not None:
            self.pnl_dateid = pnl_dateid
        else:
            if position_dateid is not None:
                self.pnl_dateid = FactorModelCalendar.next_trading_dateid(risk_region=self.risk_region, dateid=position_dateid)
            else:
                self.pnl_dateid = FactorModelCalendar.shift_trading_days(risk_region=self.risk_region,
                                                                         dateid=factor_model_dateid,
                                                                         offset=-model_date_offset)

        self.position_dateid = FactorModelCalendar.prev_trading_dateid(risk_region=self.risk_region,
                                                                       dateid=self.pnl_dateid)
        self.factor_model_dateid = FactorModelCalendar.shift_trading_days(risk_region=self.risk_region,
                                                                          dateid=self.pnl_dateid,
                                                                          offset=model_date_offset)

    def __init__(self,
                 pnl_dateid=None, position_dateid=None, factor_model_dateid=None,
                 factor_model_code=None,
                 config=dict(),
                 **kwargs):
        super().__init__(config=config, **kwargs)

        # self._normalize_books()
        # self._infer_trading_region()

        if factor_model_code is None:
            raise Exception(f'Please provide "factor_model_code" either in the constructor or in the config file !')

        self.factor_model_code = factor_model_code
        self.factor_model_id = fm.get_static_data().FACTOR_MODEL_CODE2ID[self.factor_model_code]
        risk_region = fm.get_static_data().FACTOR_MODEL_CODE_TO_RISK_REGION[self.factor_model_code]
        if risk_region=='AP':
            risk_region = 'Asia'

        self.risk_region = risk_region

        self._normalize_dateids(pnl_dateid=pnl_dateid, position_dateid=position_dateid, factor_model_dateid=factor_model_dateid,
                                timezone=self.config.get('timezone', None))

        symbology = self.config.get('symbology', 'SecurityId')
        self.symbology = Symbology.retrieve(value=symbology)

        factor_identifier = self.config.get('factor_identifier', 'FactorDesc')
        self.factor_identifier = FactorIdentifier.retrieve(value=factor_identifier)

        self.positions = None
        self.factor_loadings_rd_factors = None
        self.factor_portfolios_rd_factors = None
        self.security_factor_exps_rd_factors = None

    def load_positions(self):
        raise Exception(f'Not implenented yot !')

    # def attach_trading_regions_to_positions(self):
    #     acugs = self.positions[self.positions['EntityTypeCode']=='ACUG']
    #     if len(acugs)>0:
    #         acug_trading_region = csd.get_static_data().ACUGS[['ACUGCode','TradingRegionCode']]
    #         acug_trading_region.columns = ['EntityCode','TradingRegion']
    #         if self.symbology.value not in acugs.columns:
    #             acugs.reset_index(inplace=True)
    #         #
    #         acugs = pd.merge(acugs, acug_trading_region, on='EntityCode', how='left', sort=False)
    #     #
    #
    #     acus = self.positions[self.positions['EntityTypeCode']=='ACU']
    #     acus['ACUCode'] = acus['EntityCode']
    #     if self.symbology.value not in acus.columns:
    #         acus.reset_index(inplace=True)
    #     #
    #
    #     strats = self.positions[self.positions['EntityTypeCode']=='STRAT']
    #     if len(strats)>0:
    #         acu_strategy = csd.get_static_data().ACU_STRATEGY_RELATIONS
    #         date = dtu.parse_datetime(dt=self.pnl_dateid, format='%Y%m%d')
    #         acu_strategy = acu_strategy[(acu_strategy['EffectiveStartDate']<=date) &
    #                                     ((acu_strategy['EffectiveEndDate'].isnull()) | (acu_strategy['EffectiveEndDate']>date))]
    #
    #         if self.symbology.value not in strats.columns:
    #             strats.reset_index(inplace=True)
    #         #
    #         strats = pd.merge(strats, acu_strategy[['ACUCode','STRATCode']].rename(columns={'STRATCode':'EntityCode'}),
    #                           on='EntityCode', how='left', sort=False)
    #         acus = pd.concat([acus, strats], sort=False)
    #     #
    #     if len(acus)>0:
    #         acu_trading_region = csd.get_static_data().ACUS[['ACUCode', 'TradingRegionCode']]
    #         acu_trading_region.columns = ['ACUCode', 'TradingRegion']
    #         acus = pd.merge(acus, acu_trading_region, on='ACUCode', how='left', sort=False)
    #     #
    #     acus = acus.drop(columns=['ACUCode'])
    #
    #     positions = pd.concat([acugs, acus], sort=False)
    #
    #     if self.symbology.value not in self.positions.columns:
    #         positions.set_index(self.symbology.value, inplace=True)
    #     #
    #
    #     self.positions = positions
    # #

    def load_factor_loadings_rd_factors(self):
        factor_loadings_attach_factor_type = self.config.get('factor_loadings.attach_factor_type', False)
        factor_loadings_data_format = self.config.get('factor_loadings.data_format', 'MATRIX')

        dalfm.request_factor_loadings(metadata_fields='AssetId,FactorId',
                                      start_datestr=None, end_datestr=None,
                            scope_type_code=None, scope_identifier_codes=None,
                            factor_model_ids=None, factor_model_codes=None,
                            factor_model_type_ids=None, factor_model_type_codes=None,
                            factor_ids=None, factor_codes=None,
                            include_custom_factors=False, consistent_custom_factors=False,
                            asset_id_type_code=None,
                            asset_ids=None,
                            is_best_date=False,
                            knowledge_datestr=None,
                            max_retry=0, retry_interval=60)



        trading_region = 'RAW' if self.symbology==Symbology.AXIOMA_ID else self.trading_region

        factor_loadings_data_format = CrossSectionalDataFormat.retrieve(value=factor_loadings_data_format)
        if factor_loadings_data_format == CrossSectionalDataFormat.MATRIX:
            self.factor_loadings_rd_factors = fm.load_factor_loadings_matrix_rd_factors(date=self.factor_model_dateid,
                                                                                        factor_model_code=self.factor_model_code,
                                                                                        trading_region=trading_region,
                                                                                        symbology=self.symbology,
                                                                                        factor_identifier=self.factor_identifier)
        else:
            self.factor_loadings_rd_factors = fm.load_factor_loadings_rd_factors(date=self.factor_model_dateid,
                                                                                 factor_model_code=self.factor_model_code,
                                                                                 trading_region=trading_region,
                                                                                 symbology=self.symbology,
                                                                                 factor_identifier=self.factor_identifier,
                                                                                 attach_factor_type=factor_loadings_attach_factor_type)
        #
        # return self.factor_loadings_rd_factors
    #

    def load_factor_portfolios_rd_factors(self):
        factor_portfolios_attach_factor_type = self.config.get('factor_portfolios.attach_factor_type', False)
        factor_portfolios_data_format = self.config.get('factor_portfolios.data_format', 'MATRIX')

        trading_region = 'RAW' if self.symbology==Symbology.AXIOMA_ID else self.trading_region

        factor_portfolios_data_format = CrossSectionalDataFormat.retrieve(value=factor_portfolios_data_format)
        if factor_portfolios_data_format == CrossSectionalDataFormat.MATRIX:
            self.factor_portfolios_rd_factors = fm.load_factor_portfolios_matrix_rd_factors(date=self.factor_model_dateid,
                                                                                            factor_model_code=self.factor_model_code,
                                                                                            symbology=self.symbology,
                                                                                            factor_identifier=self.factor_identifier)
        else:
            self.factor_portfolios_rd_factors = fm.load_factor_portfolios_rd_factors(date=self.factor_model_dateid,
                                                                                     factor_model_code=self.factor_model_code,
                                                                                     symbology=self.symbology,
                                                                                     factor_identifier=self.factor_identifier,
                                                                                     attach_factor_type=factor_portfolios_attach_factor_type)
        #
        # return self.factor_loadings_rd_factors
    #

    def load_security_risk_attributes(self):
        security_risk_attributes_date_type = self.config.get('security_risk_attributes.date_type', 'DateId')
        security_risk_attributes_cols = self.config.get('security_risk_attributes_cols', None)

        trading_region = 'RAW' if self.symbology==Symbology.AXIOMA_ID else self.trading_region
        self.security_risk_attributes = fm.load_security_risk_attributes(factor_model_codes=self.factor_model_code,
                                                                         trading_region=trading_region,
                                                                         dates=self.pnl_dateid,
                                                                         symbology=self.symbology,
                                                                         cols=security_risk_attributes_cols,
                                                                         keep_id_cols=False,
                                                                         date_type=security_risk_attributes_date_type)
    #

    def _calc_security_factor_exps(self, factor_loadings_matrix):
        trading_region = TradingRegion.RAW if self.symbology == Symbology.AXIOMA_ID else self.trading_region

        merge_cols = [self.symbology.value]
        if trading_region!=TradingRegion.RAW:
            merge_cols += ['TradingRegion']
            if 'TradingRegion' not in self.positions.columns:
                self.attach_trading_regions_to_positions()
            #
        #

        if self.symbology.value in self.positions.columns:
            security_factor_exps = pd.merge(self.positions, factor_loadings_matrix.reset_index(),
                                            on=merge_cols, how='left', sort=False)
        else:
            security_factor_exps = pd.merge(self.positions.reset_index(), factor_loadings_matrix.reset_index(),
                                            on=merge_cols, how='left', sort=False)
            security_factor_exps.set_index(self.symbology.value, inplace=True)
        #

        # if factors is not None:
        #     factors = mu.iterable_to_tuple(factors, raw_type='str')
        #     factors = [factor for factor in factors if factor in factor_loadings_matrix.columns]
        # #

        for col in factor_loadings_matrix.columns:
            security_factor_exps[col] *= security_factor_exps['NMV']
        #
        security_factor_exps = security_factor_exps.drop(columns=['NMV'])

        return security_factor_exps
    #

    def calc_security_factor_exps_rd_factors(self):
        logger.info(f'Calculating per Security/Factor exposures ...')

        factor_loadings_data_format = self.config.get('factor_loadings.data_format', 'MATRIX')
        trading_region = TradingRegion.RAW if self.symbology == Symbology.AXIOMA_ID else self.trading_region

        factor_loadings_data_format = CrossSectionalDataFormat.retrieve(value=factor_loadings_data_format)
        if factor_loadings_data_format == CrossSectionalDataFormat.MATRIX:
            factor_loadings_matrix = self.factor_loadings_rd_factors
        else:
            index_cols = [self.symbology.value, self.factor_identifier.value]
            append = trading_region != TradingRegion.RAW
            factor_loadings_matrix = self.factor_loadings_rd_factors.set_index(index_cols, append=append)['Loading'].unstack().fillna(0.0)
        #

        self.security_factor_exps_rd_factors = self._calc_security_factor_exps(factor_loadings_matrix=factor_loadings_matrix)
    #

    def initialize(self):
        raise Exception(f'Not implemented yet!')
    #
#
