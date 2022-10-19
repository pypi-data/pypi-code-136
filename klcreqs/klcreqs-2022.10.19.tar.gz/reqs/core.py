''' created 10/19/2022 '''

from .constants import *

class formula_api:
    http_headers = {"Content-type": "application/json", "Accept": "application/json"}
    time_series_url = 'https://api.factset.com/formula-api/v1/time-series'
    cross_sectional_url = 'https://api.factset.com/formula-api/v1/cross-sectional'
    batch_status_url = 'https://api.factset.com/formula-api/v1/batch-status'
    batch_results_url = 'https://api.factset.com/formula-api/v1/batch-result'
    def __init__(self, formulas, ep, ids=None, uni=None, batch=False, dnames=None, bof=False):
        self.batch = batch
        self.st = time.time()
        self.formulas = formulas
        self.ids = ids
        self.uni = uni
        self.dnames = dnames
        self.ep = ep
        req = formula_api.make_request(self)
        if self.batch == True:
            batch_id_request_json = json.dumps({"data": {"id": json.loads(req.text)['data']['id']}})
            req = formula_api.__poll_return_batch(batch_id_request_json)
        self.status_code = req.status_code
        if self.status_code > 202:
            print(req.text)
        if req.status_code != 200 and bof == True:
            self.ep = 'ts'
            self.batch == True
            req = formula_api.make_request(self)
            self.status_code = req.status_code
            # print(self.status_code)
            if self.status_code == 429:
                sleep(600)
                req = formula_api.make_request(self)
            try:
                batch_id_request_json = json.dumps({"data": {"id": json.loads(req.text)['data']['id']}})
            except:
                print(self.status_code, req.text)
            req = formula_api.__poll_return_batch(batch_id_request_json)
        try:
            self.response = json.loads(req.text)
        except:
            print(self.status_code)
            print(req)
            print('error text response', req.text)
        self.ft = time.time()
        # formula_api.log_request()
        return

    def generate_meta(self):
        df_log = pd.DataFrame()
        df_log['name'] = [self.dnames]
        df_log['form'] = [self.formulas]
        df_log['ep'] = [self.ep]
        df_log['size'] = [sys.getsizeof(self.df.iloc[0,1])]
        df_log['time'] = [self.runtime]
        df_log['time/id'] = [self.runtime/len(self.ids)]
        if self.ids != None:
            df_log['n_ids'] = len(self.ids)
        elif self.uni != None:
            df_log['n_ids'] = len(formula_api(formulas=[f'{self.uni}'], uni=self.uni, ep='ts').df())
        return df_log


    def log_request(self):
        df_log = formula_api.generate_meta()
        db = mysql.connector.connect(
            host='localhost',
            user='append',
            password='Appendaccess1!',
            database='request_logs')
        df_log.to_sql('request_log', con=db, if_exists='append', method='multi')


    def status_code(self):
        return self.status_code

    def df(self):
        self.df = pd.json_normalize(self.response['data'])
        return self.df

    @property
    def runtime(self):
        self.rt = (self.ft - self.st)
        return self.rt

    def make_request(self):
        if self.batch == True:
            self.ep = 'ts'
        request_json = formula_api.__create_request_json(self.ids, self.uni, self.formulas, self.batch, self.dnames)
        if self.ep in ['ts', 'time', 'timeseries', 'time_series', 'time series']:
            return formula_api.time_series_request(
                request_json=request_json
            )
        if self.ep in ['cs', 'cross', 'crosssectional', 'cross_sectional', 'cross sectional']:
            return formula_api.cross_sectional_request(
                request_json=request_json
            )
        else:
            raise 'Exception no valid endpoint provided, use \"ts\" or \"cs\"'

    @staticmethod
    def __poll_return_batch(batch_id_request_json):
        while True:
            sleep(5)
            batch_status_response = requests.post(url=status_endpoint,
                                                  data=batch_id_request_json,
                                                  auth=authorization,
                                                  headers=headers,
                                                  verify=False)
            try:
                batch_status_data = json.loads(batch_status_response.text)
            except:
                print(batch_status_response.text)
            if batch_status_data['data']['status'] == 'DONE':
                batch_result_response = requests.post(url=result_endpoint,
                                                      data=batch_id_request_json,
                                                      auth=authorization,
                                                      headers=headers,
                                                      verify=False)
                if batch_result_response.status_code == 200:
                    return batch_result_response
                elif batch_result_response.status_code >= 400:
                    print('HTTP Status: {}'.format(batch_result_response.status_code))
                    return

    @staticmethod
    def time_series_request(request_json):
        return formula_api.__http_post(
            URL=formula_api.time_series_url,
            json_string=request_json
        )

    @staticmethod
    def cross_sectional_request(request_json):
        return formula_api.__http_post(
            URL=formula_api.cross_sectional_url,
            json_string=request_json
        )

    @staticmethod
    def __create_request_json(ids, uni, formulas, batch, dnames):
        request = {
            "data": {
                "formulas": formulas,
                "flatten": "Y"
            }
        }
        if ids is not None:
            request['data']['ids'] = ids
        elif uni is not None:
            request['data']['universe'] = uni
        elif uni == None and ids == None:
            request['data']['ids'] = ['dummy']
        if batch == True:
            request['data']['batch'] = 'Y'
        if dnames is not None:
            request['data']['displayName'] = dnames
        return json.dumps(request)

    @staticmethod
    def __http_post(URL, json_string):
        try:
            r = requests.post(
                URL,
                auth=authorization,
                headers=formula_api.http_headers,
                data=json_string,
                verify=False,
            )
            return r
        except Exception as e:
            return False, str(e)

class ofdb_api:
    def __init__(self, path):
        self.host = "https://api.factset.com/analytics/ofdb/v1/database/"
        self.path = path
        self.uri = urllib.parse.quote(self.path, safe="")
        return

    def get_dates(self):
        url = f'{self.host}{self.uri}/dates'
        r = requests.get(url, auth=authorization, headers=headers)
        if r.status_code >= 400:
            print(r)
            print(r.text)
            return
        response = json.loads(r.text)
        return response

    def delete_date(self, d):
        url = f"{self.host}{self.uri}/dates/{d}"
        r = requests.delete(url, auth=authorization, headers=headers)
        if r.status_code >= 400:
            print(r)
            print(r.text)
        return

    def delete_symbol(self, symbol, d=None):
        if d is None:
            url = f'{self.host}{self.uri}/symbols/{symbol}'
        elif d is not None:
            url = f'{self.host}{self.uri}/dates/{d}/symbols/{symbol}'
        r = requests.delete(url, auth=authorization, headers=headers)
        if r.status_code > 204:
            print(r)
            print(r.text)
        return

    def parse_upload(self, df):
        df.fillna(0, inplace=True)
        df_dict = df.to_dict(orient='index')
        body = {'data': []}
        for i, j in df_dict.items():
            body['data'].append(j)
        url = f"{self.host}{self.uri}/dates/{self.d}"
        n = 0
        k = len(body['data']) / 200
        if k >= 1:
            body_temp = {'data': []}
            while n < len(body['data']):
                m = int(min(200, len(body['data']) - n))
                body_temp['data'] = body['data'][n:(n + m)]
                r = requests.put(url, auth=authorization, headers=headers, data=body_temp)
                if r.status_code >= 400:
                    print(r)
                    print(r.text)
        else:
            body = json.dumps(body)
            r = requests.put(url, auth=authorization, headers=headers, data=body)
            if r.status_code >= 400:
                print(r)
                print(r.text)
        return r, r.text

    def parse_upload_datewise(self, df):
        df.fillna(0, inplace=True)
        zz = list(set(df.index.to_list()))
        for i in tqdm(zz, total=len(zz), desc='uploading data: ', ncols=100):
            df_temp = df[df.index == i]
            df_temp.index = [j for j in range(len(df_temp.index.to_list()))]
            df_dict = df_temp.to_dict(orient='index')
            body = {'data': []}
            for z, j in df_dict.items():
                body['data'].append(j)
            for i in range(len(body['data'])):
                e = list(body['data'][i].values())
                if None in e:
                    del body['data'][i]
            url = f"{self.host}{self.uri}/dates/{i}"
            n = 0
            k = len(body['data']) / 200
            if k >= 1:
                while n < len(body['data']):
                    body_temp = {'data': []}
                    m = int(min(200, len(body['data']) - n))
                    body_temp['data'] = body['data'][n:(n + m)]
                    n += 200
                    body_temp = json.dumps(body_temp)
                    r = requests.put(url, auth=authorization, headers=headers, data=body_temp)
                    if r.status_code >= 400:
                        print(r)
                        print(r.text)
            else:
                body = json.dumps(body)
                r = requests.put(url, auth=authorization, headers=headers, data=body)
                if r.status_code >= 400:
                    print(r)
                    print(r.text)
        return r, r.text