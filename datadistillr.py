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
    projectDistillry = base_url + "projectDistillry"
    queryBarrels = base_url + "queryBarrels"

    def __init__(self):
        self.session  = requests.Session()
        
        self.proj_token_dict = {}
        self.barrel_token_dict = {}
        self.query_token_dict = {}

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
        """Converts response to JSON"""
        login_resp_json = login_response.json()
        #print(login_response.status_code)
        """Parses the JSON response into a python dictionary"""
        return login_resp_json 

    def logout(self):
        """Gets logout page"""
        logout_response = self.session.get(url = self.logout_page, cookies = self.jar, verify = False)
        """Converts response to JSON"""
        logout_resp_json = logout_response.json()
        #print(logout_response.status_code)
        """Parses the JSON response into a python dictionary"""
        return logout_resp_json

    def get_projects(self):
        """Gets projects page"""
        projects_response = self.session.get(url = self.projects_page, cookies = self.jar, verify = False)
        """Converts response to JSON"""
        proj_resp_json = projects_response.json()
        """Gets the projects list"""
        proj_list = proj_resp_json["projects"]

        for i in range(len(proj_list)):
            self.proj_token_dict[proj_list[i]["name"]] = [proj_list[i]["token"]]

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

    def project_details(self, project_token):  
        details_page = self.projectDistillry + "/" + str(project_token)
        details = self.session.get(url = details_page) 
        details_json = details.json()

        details_json_barrels = details_json["project"]["queryBarrels"]

        for i in range(len(details_json_barrels)):
            self.barrel_token_dict[details_json_barrels[i]["name"]] = [details_json_barrels[i]["token"]]

        return details_json
        
    def queries(self, barrel_token):
        queries_page = self.queryBarrels + "/" + str(barrel_token)
        queries_list = self.session.get(url = queries_page)
        queries_list_json = queries_list.json()
        queries_list2 = queries_list_json["queryBarrel"]["queries"]

        for i in range(len(queries_list2)):
            if queries_list2[i]["query"] in self.query_token_dict:
                self.query_token_dict[queries_list2[i]["query"]].append(queries_list2[i]["token"])
            else:
                self.query_token_dict[queries_list2[i]["query"]] = [queries_list2[i]["token"]]


        return queries_list_json
        
    def query_details(self, barrel_token, query_token):
        query_details_page = self.queryBarrels + "/" + str(barrel_token) + "/query/" + str(query_token)
        query_details_get = self.session.get(url = query_details_page)
        query_details_get_json = query_details_get.json()
        return query_details_get_json

    def query_results(self, barrel_token, query_token):
        query_run_page = self.queryBarrels + "/" + str(barrel_token) + "/query/" + str(query_token) + "/run"
        query_run = self.session.get(url = query_run_page)
        query_run_json = query_run.json()
        return query_run_json
    


    









