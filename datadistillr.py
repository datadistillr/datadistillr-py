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
        """Creates session"""
        self.session  = requests.Session()
        """Dictionaries for the project tokens, barrel tokens, and query tokens that are updated when you get the project, query barrels, or queries respectively"""
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
        

        login_response = self.session.post(url = self.login_page, json = user_info, cookies = self.jar, verify= False)
        """Converts response to JSON"""
        login_resp_json = login_response.json()
        """Parses the JSON response into a python dictionary"""
        return login_resp_json 

    def logout(self):
        """Gets logout page"""
        logout_response = self.session.get(url = self.logout_page, cookies = self.jar, verify = False)
        """Converts response to JSON"""
        logout_resp_json = logout_response.json()
        """Parses the JSON response into a python dictionary"""
        return logout_resp_json

    def get_projects(self):
        """Gets projects page"""
        projects_response = self.session.get(url = self.projects_page, cookies = self.jar, verify = False)
        """Converts response to JSON"""
        proj_resp_json = projects_response.json()
        """Gets the projects list"""
        proj_list = proj_resp_json["projects"]
        """Creates a dictionary of all projects and their tokens"""
        for i in range(len(proj_list)):
            self.proj_token_dict[proj_list[i]["name"]] = [proj_list[i]["token"]]
        """Returns the parsed JSON"""
        return proj_list

    def create_project(self, name, desc = "", icon = "glass whiskey", color = "blend", active = 1, tags = []):
        """Function to create a new project in Datadistillr from python"""
        """Takes in name, with all other parameters set to default"""

        """Creates a dictionary from the parameters"""
        new_proj_payload = {
            "name" : name,
            "desc" : desc,
            "icon" : icon,
            "color" : color,
            "active" : active,
            "tags" : tags
        }

        """Posts the payload to the projects page to create new project"""
        new_proj = self.session.post(self.projects_page, json = new_proj_payload)
        """Returns the status code which should be 201"""
        return new_proj

    def project_details(self, project_token):
        """Creates the details page through the project Distillry url + the project token"""  
        details_page = self.projectDistillry + "/" + str(project_token)
        """Gets the url"""
        details = self.session.get(url = details_page) 
        """Parses the response from JSON to a python dictionary"""
        details_json = details.json()
        """Finds the part regarding query barrels"""
        details_json_barrels = details_json["project"]["queryBarrels"]
        """Creates a dictionary of all the query barrels and their tokens"""
        for i in range(len(details_json_barrels)):
            self.barrel_token_dict[details_json_barrels[i]["name"]] = [details_json_barrels[i]["token"]]
        """Returns the parsed JSON"""
        return details_json
        
    def queries(self, barrel_token):
        """Creates the queries page through the query barrels url + the barrel token"""
        queries_page = self.queryBarrels + "/" + str(barrel_token)
        """Gets the url"""
        queries_response = self.session.get(url = queries_page)
        """Parses the response from JSON to a python dictionary"""
        queries_response_json = queries_response.json()
        """Finds the part regarding the queries"""
        queries_list = queries_response_json["queryBarrel"]["queries"]
        """Creates a dictionary of all the queries and their tokens. If the query is already in the dictionary, appends the new token"""
        for i in range(len(queries_list)):
            if queries_list[i]["query"] in self.query_token_dict:
                self.query_token_dict[queries_list[i]["query"]].append(queries_list[i]["token"])
            else:
                self.query_token_dict[queries_list[i]["query"]] = [queries_list[i]["token"]]
        """Returns the parsed JSON"""
        return queries_response_json
        
    def query_details(self, barrel_token, query_token):
        """Creates the query details page through the query barrels url + the barrel token + the query token"""
        query_details_page = self.queryBarrels + "/" + str(barrel_token) + "/query/" + str(query_token)
        """Gets the url"""
        query_details_get = self.session.get(url = query_details_page)
        """Parses the response from a JSON to a python dictionary"""
        query_details_get_json = query_details_get.json()
        """Returns the parsed JSON"""
        return query_details_get_json

    def query_results(self, barrel_token, query_token):
        """Creates the query details page through the query barrels url + the barrel token + the query token"""
        query_run_page = self.queryBarrels + "/" + str(barrel_token) + "/query/" + str(query_token) + "/run"
        """Gets the url"""
        query_run = self.session.get(url = query_run_page)
        """Parses the response from a JSON to a python dictionary"""
        query_run_json = query_run.json()
        """Returns the parsed JSON"""
        return query_run_json
    


    









