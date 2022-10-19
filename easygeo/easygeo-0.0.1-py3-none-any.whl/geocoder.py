from geopy.geocoders import Nominatim, GoogleV3
from geopy.extra.rate_limiter import RateLimiter
import json

# Wrapper for geocoding api's, previous results are cached.
class GeoCode(object):
    """
    Wrapper for geopy's geocoding library,
    It simplifies the process of geocoding into two simple steps:
    1. Initialization (class instance creation)
    2. Geocoding (built in method within the class to transform an address into coordinates)

    This class has some perks such as a simple cache that can be used
    to avoid repetition of API calls into expensive services such as Google API, or just to improve speed.
    It has been tested with a cache size of around 6M unique addresses, which just work.
    Some optimization can be made, but if ain't broken don't fix it.
    (unless for some strange reason this becomes like the backbone of the internet, from which I'm sure 
    people far more versed coding will have their eyes bleed out first, and then try to improve on this c:)
    """
    def __init__(self, method:str = "GoogleV3", domain:str = "maps.google.cl", api_key:str = None, cache_file:str = None, min_delay:float = None):
        """ 
        Class constructor:
        Method -> string: Current options are: GoogleV3, Nominatim
        domain -> string: Address on which requests will be sent.
        api_key -> string: Needed for GoogleV3 API.
        cache_file -> string: File where requests and responses can be saved.
                              Default: adddress_cache.json on current directory. 
        min_delay -> float: Time interval between requests
                              By default it's 0.02 seconds (50 requests/second) on Google's API and 1 second on Nominatim.
        """
        self.method = method
        self.domain = domain
        self.api_key = api_key
        self.min_delay_seconds = None
        if min_delay is not None:
            self.min_delay_seconds = min_delay
        self.geolocator = self.set_geolocator()
        self.geocoder = RateLimiter(self.geolocator.geocode, min_delay_seconds=self.min_delay_seconds)
        
        # Cache file
        if cache_file is None:
            self.cache_file = "address_cache.json"
        else: 
            self.cache_file = cache_file
        
        self.cache = dict()
        
        # Cache loading
        try:
            self.load_cache()
        except:
            print("Creating cache file: "+self.cache_file)
            self.save_cache()
        
    def set_geolocator(self):
        """
        set_geolocator: Generates a geolocator based on Google Maps or Nominatim request type API
        returns a geopy geocoder.
        """
        if self.method == "GoogleV3":
            geolocator = GoogleV3(user_agent="LT", 
                                  domain = self.domain, 
                                  api_key = self.api_key)
            if self.min_delay_seconds is None:
                self.min_delay_seconds = 0.02 # Maximum of 50 requests per second.
        else:
            geolocator = Nominatim(user_agent="LT")
            if self.min_delay_seconds is None:
                self.min_delay_seconds = 1
        return geolocator
    
    # Obtains the saved address -> coordinates cache
    def get_cache(self):
        """
        get_cache corresponds to the cache attribute getter.
        returns a dictionary with the cache contents.
        """
        return self.cache
    
    # Loads a cache file.
    def load_cache(self):
        """
        load_cache corresponds to the cache attribute loader.
        It loads a previously saved cache file into memory. 
        """
        with open(self.cache_file, 'r') as f:
            self.cache = json.load(f)
    
    # Saves the cache in ram into the hard drive.
    def save_cache(self, verbose = True):
        """
        save_cache corresponds to the cache attribute dump.
        It saves the memory cache contents into a permanent location. 
        """
        if verbose:
            print("Saved in cache")
        with open(self.cache_file, 'w') as f:
            json.dump(self.cache, f)
            
    # Geocode transforms the address into coordinates using the selected geolocation engine.
    # When a request was already queried, it searches it in the cache, to save resources.
    def geocode(self, address, debug = False, save = False):
        if address not in self.cache:
            try:
                location = self.geocoder(address).raw
            except:
                location = "error"
                return location
            if debug: 
                return location
            # Address, coordinates in a json way
            location_coordinates = dict()
            if self.method == "GoogleV3":
                #in_rm = (location["formatted_address"].find("Metropolitana") != -1)
                location_coordinates["formatted_address"] = location["formatted_address"]
                location_coordinates["location"] = location["geometry"]["location"]
                location_coordinates["is_valid"] = (location["address_components"][0]["types"][0] == 'street_number') #& (in_rm) 
            else:
                location_coordinates["formatted_address"] = location["display_name"]
                coordinates = dict()
                coordinates["lat"] = location["lat"]
                coordinates["long"] = location["lon"]
                location_coordinates["location"] = coordinates
            self.cache[address] = location_coordinates
            if save:
                self.save_cache()
            
        return self.cache[address]

