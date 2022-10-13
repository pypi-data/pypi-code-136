class Country:
    name = ''
    aliases = []
    iso2code = ''
    capital = ''
    iso3code = ''
    incomelevel = ''
    capital_longitude = ''
    capital_latitude = ''
    lendingtype = ''
    region = ''
    groups = []
    alias = []
    fao_code = ''
    sdg_code = ''

    def __getitem__(self,key):
        return getattr(self,key)

    #def __repr__(self):
        #return ("****************************\nName: %s\nAliases: %s\n CapitaL %s Iso2code: %s Iso3code: %s Income level: %s Longitude (capital): %s Latitude (capital): %s Lending type: %s-%s\n%s\n%s\n%s\n%s\n" % (self.name, self.aliases, self.iso2code, self.capital, self.iso3code, self.incomelevel, self.capital_longitude, self.capital_latitude, self.lendingtype, self.region, str(self.groups), str(self.alias), self.fao_code, self.sdg_code))

    def as_json(self):
    	# The replacement of (.) is done to avoid issues with key in mongodb
        return dict(name=self.name.replace(".", ""), aliases=self.aliases, iso2code=self.iso2code, capitalcity=self.capitalcity, iso3code=self.iso3code, incomelevel=self.incomelevel, capital_longitude=self.capital_longitude, capital_latitude=self.capital_latitude, lendingtype=self.lendingtype, region=self.region, groups=self.groups)
    
    def as_array(self):
        return([self.name, str(self.aliases), self.iso2code, self.capital, self.iso3code, self.incomelevel, str(self.capital_longitude), str(self.capital_latitude), self.lendingtype, self.region, str(self.groups), str(self.alias), self.fao_code, self.sdg_code])
