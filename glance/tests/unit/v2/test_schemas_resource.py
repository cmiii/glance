# Copyright 2012 OpenStack LLC.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the 'License'); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an 'AS IS' BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import glance.api.v2.schemas
import glance.tests.unit.utils as unit_test_utils
import glance.tests.utils as test_utils


class TestSchemasController(test_utils.BaseTestCase):

    def setUp(self):
        super(TestSchemasController, self).setUp()
        self.controller = glance.api.v2.schemas.Controller()

    def test_image(self):
        req = unit_test_utils.get_fake_request()
        output = self.controller.image(req)
        self.assertEqual(output['name'], 'image')
        self.assertTrue('status' in output['properties'],
                        "'status' key missing from image schema")

    def test_images(self):
        req = unit_test_utils.get_fake_request()
        output = self.controller.images(req)
        self.assertEqual(output['name'], 'images')
        expected = set(['images', 'schema', 'first', 'next'])
        self.assertEqual(set(output['properties'].keys()), expected)
        expected = set(['{schema}', '{first}', '{next}'])
        actual = set([link['href'] for link in output['links']])
        self.assertEqual(actual, expected)

    def test_access(self):
        req = unit_test_utils.get_fake_request()
        output = self.controller.access(req)
        self.assertEqual(output['name'], 'access')
        expected = set(['tenant_id', 'can_share', 'schema', 'self', 'image'])
        self.assertEqual(set(output['properties'].keys()), expected)
        expected = set(['{schema}', '{self}', '{image}'])
        actual = set([link['href'] for link in output['links']])
        self.assertEqual(actual, expected)

    def test_accesses(self):
        req = unit_test_utils.get_fake_request()
        output = self.controller.accesses(req)
        self.assertEqual(output['name'], 'accesses')
        expected = set(['accesses', 'schema', 'first', 'next'])
        self.assertEqual(set(output['properties'].keys()), expected)
        expected = set(['{schema}', '{first}', '{next}'])
        actual = set([link['href'] for link in output['links']])
        self.assertEqual(actual, expected)
