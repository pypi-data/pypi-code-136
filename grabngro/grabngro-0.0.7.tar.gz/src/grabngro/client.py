import requests

class GenericClient:
	"""
	This client class has some generic constants/methods that we inherit in the specific client classes, e.g. ApiClient or FuturesClient.
	"""
	def __init__(self):
		self.API_ENDPOINT = 'http://10.20.25.249:8000/' # internal private ip
		self.CONNECT_ERROR = 'Unable to connect to the API.\nThe IP may have changed, try updating grabngro with `pip install --upgrade grabngro`'
	
	# Generic function for simple "fetch this json and return" style requests
	def simple_get_request(self, endpoint: str):
		try:
			res = requests.get(self.API_ENDPOINT + endpoint)
		except requests.exceptions.ConnectionError:
			raise Exception(self.CONNECT_ERROR)
		res.raise_for_status()
		json = res.json()
		if isinstance(json, dict) and 'error' in json.keys():
			raise Exception(json['error'])
		return json

class ApiClient(GenericClient):
	"""
	`ApiClient` is a wrapper for the pyarrow API.

	Example:

	```
	client = ApiClient()

	# lists available datasets
	datasets = client.get_datasets()
	print(datasets) # ex: ['ndvi_8day', 'gdi_daily', 'lst_daily']

	# query ndvi data for a district in 2019
	client.get_by_district(district_id=140360, dataset='ndvi_8day', year=2019)

	# query gdi data for Illinois in December 2017
	client.get_by_province(province_id=13064, dataset='gdi_daily', year=2017, month=12)

	# query lst data for France from January 2017 to March 2020, inclusive
	x = client.get_by_country(country_id=1070, dataset='lst_daily', year=2017, month=1, year_until=2020, month_until=3)

	# load the result into a pandas DataFrame
	df = pd.DataFrame(x).T
	```
	"""
	
	def get_datasets(self):
		return self.simple_get_request('datasets')
	
	def get_by_district(self, district_id, **kwargs):
		return self.query('&district=%s' % district_id, **kwargs)

	def get_by_province(self, province_id, **kwargs):
		return self.query('&province=%s' % province_id, **kwargs)

	def get_by_country(self, country_id, **kwargs):
		return self.query('&country=%s' % country_id, **kwargs)

	def query(self, area_selector, dataset, year, month=None, year_until=None, month_until=None):
		year = int(year)
		end_mo = 12
		start_mo = int(month or 1)
		end_yr = int(year_until or year)
		querystring = '?file=%s%s' % (dataset, area_selector)
		for yr in range(year, end_yr + 1):
			if yr == end_yr:
				end_mo = int(month_until or month or 12)
			for mo in range(start_mo, end_mo + 1):
				if start_mo == 1 and end_mo == 12:
					querystring += '&months=%s' % yr
					break
				querystring += '&months=%s-%s' % (yr, mo)
			start_mo = 1
		return self.simple_get_request(querystring) 



class FuturesClient(GenericClient):
	"""
	`FuturesClient` is a wrapper for the grabngro API, specifically for functions that pull futures data.

	Example:

	```
	futures_client = FuturesClient()

	# lists available datasets
	datasets = futures_client.get_datasets()
	print(datasets) # ex: ['cme_daily']

	# lists month codes
	month_codes = futures_client.get_month_codes()
	
	# returns available contract codes and codes
	product_codes = futures_client.get_product_codes()
		
	# query futures data for corn/december 2022, using industry codes
	x = futures_client.get_by_code('CZ22')
	futures_client.get_by_code('CZ2022')
	futures_client.get_by_code('CZ2')

	# query futures data for corn/december 2022, using Gro IDs
	futures_client.get_by_ids(file='cme_daily', region_id=1215, item_id=274, start_date='2022-12-01')

	# load the result into a pandas DataFrame
	df = pd.DataFrame(x).T
	```
	"""

	def get_datasets(self):
		return self.simple_get_request('futures_datasets')
	
	def get_month_codes(self):
		return self.simple_get_request('futures_month_codes')
	
	def get_product_codes(self):
		return self.simple_get_request('futures_product_codes')

	def search_products(self, query: str, num_results: int = 3):
		querystring: str = f"?query={query}"
		results = self.simple_get_request('futures_product_search/'+querystring)
		# Return first N key/value pairs in a dictionary
		return {k: results[k] for k in list(results.keys())[:num_results]}

	# Get futures data for a specific contract, specified with Gro IDs
	def get_by_ids(self, file: str, region_id: int, item_id: int, start_date: str):
		querystring: str = f"?file={file}&region_id={region_id}&item_id={item_id}&start_date={start_date}"
		return self.simple_get_request('futures/'+querystring)

	# Get futures data using a specific contract code
	def get_by_code(self, code: str):
		querystring: str = f"?code={code}"
		return self.simple_get_request('futures_by_code/'+querystring)

