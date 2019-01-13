import unittest

from store import Store
from stores import Stores
from find_store import FindStore


class TestStore(unittest.TestCase):

    def setUp(self):
        self.store = Store([
            'East St Paul SWC',
            'I-94 & White Bear Ave',
            '1744 Suburban Ave',
            'Saint Paul',
            'MN',
            '55106-6619',
            '44.9498979',
            '-93.0289915',
            'Ramsey County'
        ])

    def test_find_distance_1(self):
        lat = 44.9498979
        lon = -93.0289915
        self.assertTrue(self.store.find_distance(lat, lon, 'mi') == 0, 'Incorrect distance found between stores')

    def test_find_distance_2(self):
        lat = 38.729245
        lon= -90.444167
        self.assertTrue(self.store.find_distance(lat, lon, 'mi') > 440, 'Distance more than expected')

    def tearDown(self):
        self.store = None


class TestStores(unittest.TestCase):

    def setUp(self):
        self.stores = Stores('../data/store-locations.csv')

    def test_nearest_store(self):
        lat = 38.729245
        lon = -90.444167
        nearest, distance = self.stores.find_nearest(lat, lon, 'mi')
        self.assertTrue(len(self.stores.stores) == 1791, "Could not load all stores")
        self.assertTrue("12275 St Charles Rock Rd" in nearest.to_json()['address'], "Incorrect nearest store")

    def tearDown(self):
        self.stores = None


if __name__ == "__main__":
    unittest.main()
