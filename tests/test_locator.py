import unittest
from fsopxpy_loc.locator import get_asset_url, FSOLocateExcetion


class TestStringMethods(unittest.TestCase):

    def test_get_asset_url_found(self):
        """Is output valid RDF?"""
        pxid = 'px-x-0102020204_102'
        asset_url_expected = 'https://www.bfs.admin.ch/bfsstatic/dam/assets/22724379/master'
        asset_url_derived = get_asset_url(pxid)
        assert asset_url_expected == asset_url_derived

    def test_get_asset_url_not_found(self):
        """Is output valid RDF?"""
        pxid = 'px-x-0102020204'
        with self.assertRaises(FSOLocateExcetion):
            get_asset_url(pxid)
