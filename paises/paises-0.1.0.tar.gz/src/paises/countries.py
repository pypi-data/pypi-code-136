import sys
import os
sys.path.append(os.getcwd().split("geo")[0])
from country import Country
from texttable import Texttable
from cache import *

from data import ldcs2025, ldcs2019, ldcs2018, ldcs2017, lldcs, mics, mics_lower, \
	mics_upper, oecd, sids, africa, asia, \
	america, north_america, central_america, south_america, \
	europe, oecd, pacific_islands, asia_and_the_pacific, \
	developing_excluding_ldcs, \
	country_alias

cache_folder = os.getcwd().split('geo')[0] + 'datascrapper2/countries/cache'

class Countries(list):

	def __init__(self):
		if len(self) == 0:
			pass

	def __iter__(self):
		self.idx = 0
		return self

	def __next__(self):
		if self.idx < len(self):
			self.idx += 1
			return self[self.idx - 1]
		else:
			raise StopIteration

	# prints the dataframe
	def print(self, **kwargs):		
		table = Texttable()

		for r in self:
			table.add_row(r.as_array())
		table_s = table.draw()

	#def __repr__(self):
		# table = Texttable()

		#for r in self:
		#	table.add_row(r.as_array())
		
		#table_s = table.draw()

		#return str(table_s)
	#	yield

	# Get a country object using the name
	def get(self, n):
		for c in self:
			if n == c.name or n in c.alias:
				return c
		return None

	# Return countries belonging to a group
	def get_group(self, g):		
		ctrs = Countries()	
		if (isinstance(g, str)):
			for c in self:
				for group in c.groups:	
					if group == g: 										
						ctrs.append(c)
		else:
			for c in self:
				if set(g).issubset(c.groups):				
					ctrs.append(c)

		return ctrs


	# Return this list as ISO2
	def get_as_iso2(self):
		iso2_list = []
		for c in self:
			iso2_list.append(c.iso2code)
		return iso2_list

	# Return this list as ISO3
	def get_as_iso3(self):
		iso3_list = []
		for country in countries:
			if (self.get_iso3_from_country_name(country) != None):
				iso3_list.append(self.get_iso3_from_country_name(country))
		return iso3_list

	# Return this lsit as fao code
	def get_as_fao_code(self):
		fao_code_list = []
		for country in self:
			fao_code_list.append(country.fao_code)	
		return fao_code_list		

	# Return the name of a country using the iso2 code
	def get_name_from_iso2(self, iso2code):
		for c in self:
			if c.iso2code == iso2code:
				return c.name
	
	# Return the name of a country using the iso3 code
	def get_name_from_iso3(self, iso3code):
		for c in self:
			if c.iso3code == iso3code:
				return c.name

	# Add the corresponding group to each country in items
	def add_group(self, group, items):
		for c in self:
			if c.name in items:
				c.groups.append(groups)

	# Return an array with country names on this list
	def get_names(self):

		names = []
		for c in self:
			names.append(c.name)
			
		return(names)

	# Return the list of names and aliases
	def get_names_and_aliases(self):
		names = []
		for c in self:
			names.append(c.name)
			for i in c.alias:
				names.append(i)
		return(names)

	# Add group information to country in list
	# based on data stored in lists
	def get_country_groups(self, country):

		groups = []

		if country in ldcs2025:
			groups.append("LDCs2025")

		if country in ldcs2019:
			groups.append("LDCs2019")

		if country in ldcs2018:
			groups.append("LDCs")

		if country in ldcs2017:
			groups.append("LDCs2017")
		
		if country in lldcs:
			groups.append("LLDCs")

		if country in mics:
			groups.append("MICs")

		if country in mics_lower:
			groups.append("LMICs")

		if country in mics_upper:
			groups.append("UMICs")

		if country in oecd:
			groups.append("OECD")

		if country in sids:
			groups.append("SIDS")

		if country in pacific_islands:
			groups.append("Pacific islands")

		if country in asia_and_the_pacific:
			groups.append("Asia and the Pacific")

		if country in africa:
			groups.append("Africa")

		if country in asia:
			groups.append("Asia")

		if country in america:
			groups.append("America")

		if country in developing_excluding_ldcs:
			groups.append("Developing excluding LDCs")

		return groups

	# Check if a country belongs to a group

	def is_in_group(self, name):
		for c in self:
			if c.name == name or name in c.groups:
				return True
		return False

	# Check if a country belongs to a region
	def is_in_region(self, name):

		if name in africa:
			return "Africa"

		if name in asia:
			return "Asia"

		if name in north_america:
			return "North America"

		if name in central_america:
			return "Central America"

		if name in south_america:
			return "South America"

		if name in europe:
			return "Europe"

	# Get a list of country names that is in the specified groups
	def get_country_names_from_groups(self, groups):
		ctrs = self.get_countries_in_group(groups)
		country_names = []
		for ctr in ctrs:
			if ctr.name not in country_names:
				country_names.append(ctr.name)
		
		return country_names

	# Return country names on this list as json
	def as_json(self):
		ctrs = {}
		for w in self:
			ctrs[w.name] = w.as_json()

		return ctrs
	
	
	# Set an alias for a country

	def set_country_alias(self, c, a):
		for ctry in self:
			if ctry.name == c:
				ctry.alias = a

	# load aliases for countries

	def load_country_alias(self):
		for k in country_alias:
			self.set_country_alias(k,country_alias[k])
	
	# Load country data from the worldbank
	# We fetch data from the World Bank
	# We use a cache system
	def load_wb(self):
		
		file_name = 'countries'
		p = get_file_path(file_name)
		if check_cache(p) == False:
			retrieve_and_cache(name=file_name)	
		else:
			check_age(file_name)    	
		
		cached_data = load_cache(p)
		
		# Store data in array
		for item in cached_data[1]:
			c = Country()
			c.name = item['name']
			c.iso2code = item['iso2Code']
			c.capitalcity = item['capitalCity']
			c.iso3code = item['id']
			c.incomelevel = item['incomeLevel']['value']
			c.capital_longitude = item['longitude']
			c.capital_latitude = item['latitude']
			c.lendingtype = item['lendingType']['value']
			c.groups = self.get_country_groups(c.name)
			c.region = self.is_in_region(c.name)
			self.append(c)

		# Now we add aliases of countries
		self.load_country_alias()

	# Load the codes used by the FAO
	def load_fao_code(self):
		fao_countries = sources.fao.data.load_countries()
		for ctr in self:			
			if (fao_countries.search('label', ctr.name).count() > 0):
				f_c = fao_countries.search('label', ctr.name).rows[0].get_cell('code').get_value()
				ctr.fao_code = f_c
			else:
				for al in ctr.alias:
					if (fao_countries.search('label', al).count() > 0):
						f_c = fao_countries.search('label', al).rows[0].get_cell('code').get_value()
						ctr.fao_code = f_c	
				

	# Load the codes use by the FAO
	def load_sdg_code(self):
		areas = sources.sdgs.areas.load_areas()
		for a in areas:
			if (self.get_cell(a.get_cell('geoAreaName').get_value()) is not None):
				self.get_cell(a.get_cell('geoAreaName').get_value()).sdg_code = str(a.get_cell('geoAreaCode').get_value()).split(".")[0]
