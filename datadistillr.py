import requests
import http.cookiejar
import json
jar = http.cookiejar.CookieJar()

class datadistillr:

    def __init__(self):
        self.session = requests.session()

        self.login_page = "https://devapp.datadistillr.io/api/login"
        self.logout_page = "https://devapp.datadistillr.io/api/logout"
        self.projects_page = "https://devapp.datadistillr.io/api/projects"


    def login(self, email, password):
        user_info = {
            "email": str(email), 
            "password": str(password),
            }
        
        json_user_info = json.dumps(user_info)
        
        requests.post(url = self.login_page, params = json_user_info, cookies = jar)

    def logout(self):
        requests.get(url = self.logout_page, cookies = jar)

    def get_projects(self):
        requests.get(url = self.projects_page, cookies = jar)




