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
        self.session  = requests.Session()

        pass


    def login(self, email, password):
        """Takes in email and password, converts to dictionary, then converts to JSON, and posts the user info to the login page"""
        user_info = {
            "email": email, 
            "password": password,
            "invitations":{
             "organizationInvitationToken":None,
             "projectInvitationToken":None,
             "teamInvitationToken":None}
            }
        
        #json_user_info = json.dumps(user_info)

        login_response = self.session.post(url = self.login_page, json = user_info, cookies = self.jar, verify= False)
        login_resp_json = login_response.json()
        #print(login_response.status_code)
        return login_resp_json 

    def logout(self):
        """Gets logout page"""
        logout_response = self.session.get(url = self.logout_page, cookies = self.jar, verify = False)
        logout_resp_json = logout_response.json()
        #print(logout_response.status_code)
        return logout_resp_json

    def get_projects(self):
        """Gets projects page"""
        projects_response = self.session.get(url = self.projects_page, cookies = self.jar, verify = False)
        proj_resp_json = projects_response.json()
        proj_list = proj_resp_json["projects"]
        proj_token = proj_list[0]["token"]
        #print(projects_response.status_code)
        return proj_list
    
    def create_project(self, name, desc = "", icon = "glass whiskey", color = "blend", active = 1, tags = []):
        """Function to create a new project in Datadistillr from python"""
        """Takes in name, with all other parameters set to default"""
        new_proj_payload = {
            "name" : name,
            "desc" : desc,
            "icon" : icon,
            "color" : color,
            "active" : active,
            "tags" : tags
        }
        """Creates a dictionary from the parameters"""

        new_proj = self.session.post(self.projects_page, json = new_proj_payload)
        """Posts the payload to the projects page to create new project"""
        return new_proj











