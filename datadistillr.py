class datadistillr:
    def datadistillr():
            import requests

            login = "https://devapp.datadistillr.io/api/login"
            logininfo = {"email":"forrest@datadistillr.com","password":"abcd1234"}
            logout = "https://devapp.datadistillr.io/api/logout"
            projects = "https://devapp.datadistillr.io/api/projects"

            requests.post(url = login,params = logininfo)
            requests.get(url = logout)
            requests.get(url = projects)


