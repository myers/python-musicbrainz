#!/usr/bin/env python
"""test_template

A sample unit test file.
"""

__author__   = 'John Shamo'
__revision__ = "$Id: test_exception.py,v 1.1 2003/10/13 13:28:58 myers Exp $"

import unittest

import musicbrainz

class SampleTestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testException1(self):
        mb = musicbrainz.mb()

        try:
            mb.Query('monkey')
        except musicbrainz.MusicBrainzError:
            pass
        else:
            fail("expected a musicbrainz.MusicBrainzError")



def suite():
    suite = unittest.makeSuite(SampleTestCase, 'test')

    # suite2 = module2.TheTestSuite()
    # return unittest.TestSuite((suite1, suite2))

    return suite

if __name__ == "__main__":
    unittest.main()
