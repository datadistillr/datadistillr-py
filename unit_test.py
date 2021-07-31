import unittest
import datadistillr

class TestDataDistillrMethods(unittest.TestCase):
    
    def test_login(self):
        self.assertEqual(datadistillr.login(), "", msg= "Login successful") 

    def test_logout(self):
        self.assertEqual(datadistillr.logout(), "", msg= "Logout successful")

    def test_get_projects(self):
        self.assertEqual(datadistillr.get_projects, "", msg= "Getting projects successful")

    def test_project_details(self):
        self.assertEqual(datadistillr.project_details, "")

    def test_queries(self):
        self.assertEqual(datadistillr.queries(), "")

    def test_query_results(self):
        self.assertEqual(datadistillr.query_results(), "")

    def test_create_project(self):
        self.assertEqual(datadistillr.create_project(), "")
