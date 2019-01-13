import json

import constants

from math import sin, cos, sqrt, atan2, radians, pi


class Store:
    name = ""
    loc = ""
    address = ""
    city = ""
    state = ""
    zipcode = ""
    lat = 0
    lon = 0
    county = ""

    def __init__(self, store):
        self.name = store[0]
        self.loc = store[1]
        self.address = store[2]
        self.city = store[3]
        self.state = store[4]
        self.zipcode = store[5]
        self.lat = float(store[6])
        self.lon = float(store[7])
        self.county = store[8]

    def _degrees_to_radians(self, degrees):
        return degrees * pi / 180

    def find_distance(self, lat, lon, units):
        """
        https://www.movable-type.co.uk/scripts/latlong.html
        :param lat:
        :param lon:
        :param units:
        :return: distance
        """

        if units == 'km':
            radius = constants.RADIUS_IN_KM
        else:
            radius = constants.RADIUS_IN_MI

        dlat = self._degrees_to_radians(lat - self.lat)
        dlon = self._degrees_to_radians(lon - self.lon)

        lat1 = self._degrees_to_radians(self.lat)
        lat2 = self._degrees_to_radians(lat)

        a = sin(dlat / 2) * sin(dlat / 2) + \
            sin(dlon / 2) * sin(dlon / 2) * cos(lat1) * cos(lat2);
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        return round(radius * c, 1)

    def get_store(self):
        store = ''
        for attr, value in self.__dict__.items():
            store = store + attr + ': ' + str(value) + ', '
        return store

    def __str__(self):
        for attr, value in self.__dict__.items():
            print(attr, value)

    def to_json(self):
        return {key: value for key, value in self.__dict__.items() if not key.startswith('__') and not callable(key)}
