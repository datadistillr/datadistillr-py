import requests
import http.cookiejar
import json


class datadistillr:
    """Cookie Jar and the url pages based off the base url"""
    jar = http.cookiejar.CookieJar()
    base_url = "https://devapp.datadistillr.io/api/"
    login_page = base_url + "login"
    logout_page = base_url + "logout"
    projects_page = base_url + "projects"

    def __init__(self):
        #self.login_page = "https://devapp.datadistillr.io/api/login"
        #self.logout_page = "https://devapp.datadistillr.io/api/logout"
        #self.projects_page = "https://devapp.datadistillr.io/api/projects"
        pass


    def login(self, email, password):
        """Takes in email and password, converts to dictionary, then converts to JSON, and posts the user info to the login page"""
        user_info = {
            "email": str(email), 
            "password": str(password),
            }
        
        json_user_info = json.dumps(user_info)
        
        return requests.post(url = self.login_page, params = json_user_info, cookies = self.jar)

    def logout(self):
        """Gets logout page"""
        return requests.get(url = self.logout_page, cookies = self.jar)

    def get_projects(self):
        """Gets projects page"""
        return requests.get(url = self.projects_page, cookies = self.jar)







