import pyodbc
print(pyodbc.drivers())


class FootballAPI:
    def __init__(self, base_url="https://api.football-data.org/v4/"):
        self.base_url = base_url

    def get_endpoint(self, path):
        return self.base_url + path

    def describe(self):
        print(f"api connected to {self.base_url}")
