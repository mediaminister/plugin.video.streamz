# -*- coding: utf-8 -*-
""" Tests for Content API """

# pylint: disable=invalid-name,missing-docstring

from __future__ import absolute_import, division, print_function, unicode_literals

import unittest

from resources.lib import kodiutils
from resources.lib.streamz import STOREFRONT_MAIN, STOREFRONT_MOVIES, STOREFRONT_SERIES
from resources.lib.streamz.api import Api
from resources.lib.streamz.auth import Auth


@unittest.skipUnless(kodiutils.get_setting('username') and kodiutils.get_setting('password'), 'Skipping since we have no credentials.')
class TestApi(unittest.TestCase):
    """ Tests for Streamz API """

    @classmethod
    def setUpClass(cls):
        cls.auth = Auth(kodiutils.get_setting('username'),
                        kodiutils.get_setting('password'),
                        kodiutils.get_setting('loginprovider'),
                        kodiutils.get_setting('profile'),
                        kodiutils.get_tokens_path())
        cls.api = Api(cls.auth)

    def test_catalog(self):
        categories = self.api.get_categories()
        self.assertTrue(categories)

        items = self.api.get_items()
        self.assertTrue(items)

    def test_recommendations(self):
        main_recommendations = self.api.get_recommendations(STOREFRONT_MAIN)
        self.assertIsInstance(main_recommendations, list)

        movie_recommendations = self.api.get_recommendations(STOREFRONT_MOVIES)
        self.assertIsInstance(movie_recommendations, list)

        serie_recommendations = self.api.get_recommendations(STOREFRONT_SERIES)
        self.assertIsInstance(serie_recommendations, list)

    def test_continuewatching(self):
        mylist = self.api.get_swimlane('continue-watching')
        self.assertIsInstance(mylist, list)

    def test_mylist(self):
        mylist = self.api.get_swimlane('my-list')
        self.assertIsInstance(mylist, list)

    def test_search(self):
        results = self.api.do_search('huis')
        self.assertIsInstance(results, list)


if __name__ == '__main__':
    unittest.main()
