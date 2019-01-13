import csv

import constants

from store import Store


class Stores:

    stores = []

    def __init__(self, data):
        self.load_stores(data)

    def load_stores(self, path):
        with open(path, 'r') as f:
            reader = csv.reader(f)
            next(f, None)
            for store in reader:
                self.stores.append(Store(store))

    def find_nearest(self, lat, lon, units='mi'):
        distance = float("inf")
        nearest = self.stores[0]
        for store in self.stores:
            d = store.find_distance(lat, lon, units)
            if d < distance:
                nearest = store
                distance = d
        return nearest, distance
