import unittest
import datadistillr
import json

class TestDataDistillrMethods(unittest.TestCase):
    def __init__(self, methodName: str) -> None:
        super().__init__(methodName=methodName)
        pass

    
    def test_login(self):
        loginresponse = {
            "env":"production",
            "buildNumber":"1626204389575",
            "messages":None,
            "loggedIn":True,
            "landing_page":"/projects",
            "error":None,
            "userToken":1393626227,
            "activeOrganization":{
            "name":"hidden",
            "level":"personal",
            "domain":None,
            "logo":None,
            "role":"admin",
            "token":1135197221,
            "created_by_token":1393626227},
            "gravatarUrl":"https://www.gravatar.com/avatar/cd1649a417cafdef00d4b85674c0eb97?d=https://cdn4.iconfinder.com/data/icons/avatars-xmas-giveaway/128/pilot_traveller_person_avatar-512.png",
            "hasOrganizationInvitation":False,
            "userSetupOrganization":True,
            "user":{
            "email":"",
            "last_activity":{
            "date":"",
            "timezone_type":3,
            "timezone":""},
            "last_ip_address":"",
            "last_login":{
            "date":"",
            "timezone_type":3,
            "timezone":""},
            "organizations":[{
            "name":"hidden",
            "level":"personal",
            "domain":None,
            "logo":None,
            "role":"admin",
            "createdBy":"",
            "token":1135197221,
            "created_by_token":1393626227}],
            "vars":{"name":""},
            "token":1393626227,
            "defaultOrgToken":1135197221,
            "active":None,
            "loading":False,
            "activityString":"Active Just now",
            "gravatarUrl":"https://www.gravatar.com/avatar/cd1649a417cafdef00d4b85674c0eb97?d=https://cdn4.iconfinder.com/data/icons/avatars-xmas-giveaway/128/pilot_traveller_person_avatar-512.png"},
            "webSocketUrl":"wss://jw5kcbx4sd.execute-api.us-east-1.amazonaws.com/production",
            "notificationCount":0}
        self.assertEqual(datadistillr.login(), loginresponse, msg= "Login successful") 
        self.assertNotEqual(datadistillr.login(), loginresponse, msg= "Login failed") 

    def test_logout(self):
        logoutreponse = {"env":"production","buildNumber":"1626204389575","messages":None,"loggedIn":False,"message":"You are logged out.","session_destroyed":True}
        self.assertEqual(datadistillr.logout(), logoutreponse, msg= "Logout successful")

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
