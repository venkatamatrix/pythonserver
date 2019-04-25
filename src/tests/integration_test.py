""" src/tests/test_subscribers.py"""
from ..app import create_app, db
import unittest
import json


class ResourceTest(unittest.TestCase):
    """workflow Test Case"""

    def setUp(self):
        """Test Setup"""
        self.app = create_app("test")
        self.client = self.app.test_client

        self.resourcetypes = {
            "loggedInUser": "sowjanya",
            "resourceCategoryLevel1": "",
            "resourceCategoryLevel2": "",
            "resourceTypeIsActive": True,
            "resourceTypeDesc": "",
            "resourceTypeRemarks":"",
            "resourceTypeName": "sowjanya123"
        }


        with self.app.app_context():
            # create all tables
            db.create_all()

    def test_resource_creation(self):
        """ test resource creation """
        self.client().post('/resourceTypes/data', headers={'Content-Type': 'application/json'})
        res = self.client().post('/resourceTypes', headers={'Content-Type': 'application/json'},
                                 data=json.dumps(self.resourcetypes))
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 201)

    def test_get_resource(self):
        """ Test resource Get all """
        self.client().post('/resourceTypes/data', headers={'Content-Type': 'application/json'})
        res = self.client().post('/resourceTypes', headers={'Content-Type': 'application/json'},
                                 data=json.dumps(self.resourcetypes))
        json_data = json.loads(res.data)
        self.assertEqual(res.status_code, 201)
        res = self.client().get('/resourceTypes', headers={'Content-Type': 'application/json'},
                                data=json.dumps(self.resourcetypes))
        self.assertEqual(res.status_code, 200)

    def test_resource_update(self):
        """ Test Update resource """
        self.client().post('/resourceTypes/data', headers={'Content-Type': 'application/json'})
        res = self.client().post('/resourceTypes', headers={'Content-Type': 'application/json'},
                                 data=json.dumps(self.resourcetypes))
        json_data = json.loads(res.data)
        res = self.client().put('/resourceTypes/' + str(1),
                                headers={'Content-Type': 'application/json'},
                                data=json.dumps(self.resourcetypes))
        self.assertEqual(res.status_code, 200)

    def test_delete_resource(self):
        """ Test resource soft Delete """
        self.client().post('/resourceTypes/data', headers={'Content-Type': 'application/json'})
        res = self.client().post('/resourceTypes', headers={'Content-Type': 'application/json'},
                                 data=json.dumps(self.resourcetypes))
        json_data = json.loads(res.data)

        res = self.client().delete('/resourceTypes/' + str(1) + "/sowjanya",
                                   headers={'Content-Type': 'application/json'},
                                   data=json.dumps(dict(loggedInUser="sowjanya")))
        self.assertEqual(res.status_code, 200)

    def tearDown(self):
        """ Tear Down"""
        with self.app.app_context():
            db.session.remove()
            db.drop_all()


if __name__ == "__main__":
    unittest.main()
