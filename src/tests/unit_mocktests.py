from ..app import create_app, db
import unittest
import json
# from ..models.resourcetypemodel import TemplateGroupModel, TemplateGroupSchema
# from ..templateviews.templategroupview import get_all_activetemplategroup,get_all_templates

templategroups = {
        "loggedInUser": "puppala",
        "applicationId": "ww",
        "applicationVersionId": "ddd",
        "businessGroupId": 1,
        "businessUnitId": 1,
        "resourceTypeId": 1,
        "templateGroupDesc": "icpa",
        "templateGroupIsActive": True,
        "templateGroupName": "sowjanya",
        "templateGroupRemarks": "eed",
        "templateGroupType": "ee",
        "templateSource": "aa",
        "templateThresholdCategory": "icpqqq",
    }
class SelfDrivingCarTest(unittest.TestCase):

    def getdata(self):
        print("hello")
        # self.assertEqual(get_all_templates(templategroups), 200)

if __name__ == "__main__":
    unittest.main()

