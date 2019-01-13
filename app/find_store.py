#!/usr/bin/env python

"""
Find Store
  find_store will locate the nearest store (as the crow flies) from
  store-locations.csv, print the matching store address, as well as
  the distance to that store.

Usage:
  find_store --address="<address>"
  find_store --address="<address>" [--units=(mi|km)] [--output=text|json]
  find_store --zip=<zip>
  find_store --zip=<zip> [--units=(mi|km)] [--output=text|json]

Options:
  --zip=<zip>          Find nearest store to this zip code. If there are multiple best-matches, return the first.
  --address=(address)  Find nearest store to this address. If there are multiple best-matches, return the first.
  --units=(mi|km)      Display units in miles or kilometers [default: mi]
  --output=(text|json) Output in human-readable text, or in JSON (e.g. machine-readable) [default: text]

Example
  find_store --address="1770 Union St, San Francisco, CA 94123"
  find_store --zip=94115 --units=km
"""

import os

import googlemaps

import constants

from docopt import docopt
from stores import Stores


class FindStore:

    args = ''
    store = None
    distance = 0
    stores = None

    def __init__(self, arguments):
        self.args = arguments
        self.gmaps = googlemaps.Client(key=constants.GMAP_API_KEY)
        self.stores = Stores('../data/store-locations.csv')

    def get_coordinates(self):
        if self.args['--address'] is None:
            location = self.gmaps.geocode(self.args['--zip'])
        else:
            location = self.gmaps.geocode(self.args['--address'])
        lat = location[0]['geometry']['location']['lat']
        lon = location[0]['geometry']['location']['lng']
        return lat, lon

    def find_store(self):
        (lat, lon) = self.get_coordinates()
        (self.store, self.distance) = self.stores.find_nearest(lat, lon, self.args['--units'])
        return self.parse_store()

    def parse_store(self):
        if self.args['--output'] == 'json':
            rep = self.store.to_json()
            rep['distance'] = self.distance
            return rep
        else:
            store = self.store.get_store()
            return store + 'Distance: ' + str(self.distance)


if __name__ == '__main__':
    args = docopt(__doc__, version='0.0.1')
    find_store = FindStore(args)
    print(find_store.find_store())
