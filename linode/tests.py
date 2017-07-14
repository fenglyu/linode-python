import api
import unittest
import os
from getpass import getpass
from pprint import pprint

class ApiTest(unittest.TestCase):

    def setUp(self):
        self.linode = api.Api(os.environ['LINODE_API_KEY'])

    def testAvailLinodeplans(self):
        available_plans = self.linode.avail_linodeplans()
        pprint("available plans")
        map(pprint, available_plans)
        self.assertTrue(isinstance(available_plans, list))

    def testAvailLinodedcs(self):
        available_dc = self.linode.avail_datacenters()
        pprint("available datacenter")
        map(pprint, available_dc)
        self.assertTrue(isinstance(available_dc, list))

    def testEcho(self):
        test_parameters = {'FOO': 'bar', 'FIZZ': 'buzz'}
        response = self.linode.test_echo(**test_parameters)
        self.assertTrue('FOO' in response)
        self.assertTrue('FIZZ' in response)
        self.assertEqual(test_parameters['FOO'], response['FOO'])
        self.assertEqual(test_parameters['FIZZ'], response['FIZZ'])

if __name__ == "__main__":
    if 'LINODE_API_KEY' not in os.environ:
        os.environ['LINODE_API_KEY'] = getpass('Enter API Key: ')
    unittest.main()
