import unittest
from fin_crawler import FinCrawler
import time

from fin_crawler.plugins.tw_stock_info import gen_params_example,gen_params,parse


class TestCase_tw_stock_info(unittest.TestCase):

    def test_gen_params_example(self):
        self.assertEqual({},gen_params_example())

    def test_gen_params(self):

        # test normal case
        params = gen_params(**{})
        self.assertEqual(params['fetch']['url_template'],'https://mopsfin.twse.com.tw/opendata/t187ap03_L.csv')

    def test_parse(self):
        test_data = '\ufeff出表日期,公司代號,公司名稱,公司簡稱,外國企業註冊地國,產業別,住址,營利事業統一編號,董事長,總經理,發言人,發言人職稱,代理發言人,總機電話,成立日期,上市日期,普通股每股面額,實收資本額,私募股數,特別股,編制財務報表類型,股票過戶機構,過戶電話,過戶地址,簽證會計師事務所,簽證會計師1,簽證會計師2,英文簡稱,英文通訊地址,傳真機號碼,電子郵件信箱,網址\r\n"1111014","1101","台灣水泥股份有限公司","台泥","－ ","01","台北市中山北路2段113號","11913502","張安平","張安平","黃健強","資深副總經理","賴家柔","(02)2531-7099","19501229","19620209","新台幣                 10.0000元","69361817420","0","200000000","1","中國信託商業銀行代理部","66365566","台北市重慶南路一段83號5樓","勤業眾信聯合會計師事務所","黃惠敏","郭政弘","TCC","No.113, Sec.2, Zhongshan N. Rd.,Taipei City 104,Taiwan (R.O.C.)","(02)2531-6529","finance@taiwancement.com","http://www.taiwancement.com"'
        test_data = test_data.encode('utf-8')
        formed_data = {
            'website':['http://www.taiwancement.com'],
            'company_name':['台灣水泥股份有限公司'],
            'stock_id':['1101'],
            'stock_name':['台泥']
        }

        result = parse(test_data)

        for col_name,value in formed_data.items():
            self.assertEqual(value,result[col_name])