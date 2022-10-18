import unittest
from fin_crawler import FinCrawler
import time
class Test_tw_stock_info_real(unittest.TestCase):

    def test_request(self):
        time.sleep(4)
        result_idx1 = {
            'update_date': '20221015',
            'stock_id': '1102',
            'company_name': '亞洲水泥股份有限公司',
            'stock_name': '亞泥',
            'foreign_register_country': '－ ',
            'industry_type': '01',
            'address': '台北市大安區敦化南路2段207號30、31樓',
            'tax_id': '03244509',
            'chairman': '徐旭東',
            'CEO': '李坤炎',
            'spokesman': '周維崑',
            'spokesman_title': '副總經理',
            'deputy_spokesman': '吳玲綾',
            'phone': '02-2733-8000',
            'establishment_date': '19570321',
            'IPO_date': '19620608',
            'common_shares_price': '新台幣                 10.0000元',
            'paid_in_capital': '35459275570',
            'private_shares_num': '0',
            'special_shares_num': '0',
            'financial_report_type': '1',
            'stock_transfer_agency': '亞東證券股份有限公司',
            'stcok_transfer_phone': '02-7753-1699',
            'stock_transfer_address': '新北市板橋區新站路16號13樓',
            'accounting_firm': '勤業眾信聯合會計師事務所',
            'accountant_1': '戴信維',
            'accountant_2': '陳培德',
            'stock_name_en': 'ACC',
            'address_en': "30-31F., No.207, Sec. 2, Dunhua S. Rd., Da' an Dist., Taipei City 106, TaiwanTAIPEI,TAIWAN,R.O.C",
            'fax': '02-2378-5191',
            'email': 'service@acc.com.tw',
            'website': 'www.acc.com.tw'
        }
        result_idx500 = {
            'update_date': '20221015',
            'stock_id': '2923',
            'company_name': '鼎固控股有限公司',
            'stock_name': '鼎固-KY',
            'foreign_register_country': 'KY 開曼群島                                                    ',
            'industry_type': '14',
            'address': '臺北市信義區基隆路一段420號10樓(臺北聯絡處)',
            'tax_id': '31896684',
            'chairman': '張洪本',
            'CEO': '張能耀',
            'spokesman': '張能耀',
            'spokesman_title': '總經理',
            'deputy_spokesman': '馮安怡',
            'phone': '8621-64332999',
            'establishment_date': '20071205',
            'IPO_date': '20121207',
            'common_shares_price': '新台幣                 10.0000元',
            'paid_in_capital': '17402969820',
            'private_shares_num': '0',
            'special_shares_num': '0',
            'financial_report_type': '1',
            'stock_transfer_agency': '富邦綜合證券(股)公司股務代理部',
            'stcok_transfer_phone': '(02)23611300',
            'stock_transfer_address': '台北市許昌街17號2樓',
            'accounting_firm': '勤業眾信聯合會計師事務所',
            'accountant_1': '鄭旭然',
            'accountant_2': '陳俊宏',
            'stock_name_en': 'Sino Horizon',
            'address_en': '450#, Ruijin 2 road, Huangpu District,Shanghai, PRC',
            'fax': '8621-64332999',
            'email': 'ir@sinohorizon.cn',
            'website': 'http://www.sinohorizon.cn/'
            }
        data = FinCrawler.get('tw_stock_info',{})
        self.assertEqual(data[1],result_idx1)
        self.assertEqual(data[500],result_idx500)

