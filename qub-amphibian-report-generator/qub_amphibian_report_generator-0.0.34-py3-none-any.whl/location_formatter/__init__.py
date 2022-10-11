"""# Location Formatter.

This is a package intended to help to organise and categorise the GeographicRegion data from the dataset. The database is set up with Continent, Country and GeographicRegion but do to formatting of the dataset it is not possible to determining which part of the location string belongs in which table.

It is made up of the following modules:

- clean_data.py: Cleans the data passed into it
- location_finder.py:  Searches location.json and location.db to identify location type
- location_updater.py: Updates the location string
- location.py: Class to represent data associated with a location
- locations_setup.py: Runs initial setup for locations.json file
- main.py: Not called anywhere else in the project but allows for the location finder to be run on a dataset and return an updated excel file.

"""
