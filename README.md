# Grove:find_store
A command-line utility to find nearest store for a given address or zip code from a list of available stores.
The app uses [googlemaps](https://github.com/googlemaps/google-maps-services-python) api for geocoding an address (street address or zipcode) and uses the latitude and longitude from the google maps platform.
Each store is represented by the [`store.py`](grove/app/store.py) class. It also provides a utility api to calculate the distance between store's location and given latitude and longitude. The api supports both `miles` and `kilometers` for calculating the distance. 

Please refer to **Haversine** calculation as outlined in 
* [calculate distance, bearing and more between latitude/longitude points](https://www.movable-type.co.uk/scripts/latlong.html)

![picture alt](https://ttarnawski.usermd.net/wp-content/uploads/2017/08/Bez-nazwy.png "Title is optional")

The driver program is presented with the output in two possible formats: text (default) and json. The store class provides both json and string representation of the store object. This allows the driver program or any wrapper to interpret the syntax and process the object as necessary.

# Usage
```
Find Store
  find_store will locate the nearest store (as the vrow flies) from
  store-locations.csv, print the matching store address, as well as
  the distance to that store.

Usage:
  find_store --address="<address>"
  find_store --address="<address>" [--units=(mi|km)] [--output=text|json]
  find_store --zip=<zip>
  find_store --zip=<zip> [--units=(mi|km)] [--output=text|json]

Options:
  --zip=<zip>          Find nearest store to this zip code. If there are multiple best-matches, return the first.
  --address            Find nearest store to this address. If there are multiple best-matches, return the first.
  --units=(mi|km)      Display units in miles or kilometers [default: mi]
  --output=(text|json) Output in human-readable text, or in JSON (e.g. machine-readable) [default: text]

Example
  find_store --address="1770 Union St, San Francisco, CA 94123"
  find_store --zip=94115 --units=km
```

# Deployment
* Install `python3.7`
* Clone the repository
* Install the requirements: `pip install -r requirements`
* Update the `GMAP_API_KEY` in [`constants.py`](grove/app/constants.py)
  * use the steps mentioned in [google maps developer quick start guide](https://developers.google.com/maps/documentation/geocoding/get-api-key)
  * Requires setting up billing and enabling maps platform api
* Run the app: `python3.7 find_store`

# Testing
* Tests provided for each of the class
* Uses assertions to ensure data validity and distance calculation accuracy
* Test execution
  * Automated
    * `python3.7 test_basic.py`
  * Manual
    * done using a number of addresses and verified against [gps distance calculator](http://boulter.com/gps/distance/) and [distance between gps coordinates](https://gps-coordinates.org/distance-between-coordinates.php)

# Issues
* The [`geopy`](https://geopy.readthedocs.io/en/stable/) library did not work well for some of the locations, so i had to search for a more reliable geocoding service, and, thus, switched to using googlemaps
* The distance obtained by the calculation has approx. 5% of variation when compared to some other geocoding services

# Acknowledgements
* Using the [googlemaps](https://github.com/googlemaps/google-maps-services-python) api made it very simple to use the service to geocode any latitude and longitude coordinates
* A good primer on [lat-long distance calculation explained](https://www.sisense.com/blog/latitude-longitude-distance-calculation-explained/)
* Calculation code [stackoverflow](https://stackoverflow.com/questions/365826/calculate-distance-between-2-gps-coordinates)
