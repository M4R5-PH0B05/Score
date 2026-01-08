class Score:
    # A score instance is a ranking created by a user.
    def __init__(self,name: str,created_by: str,created_at: str,instances: list,ranking_system: int):
        self.name = name
        self.created_by = created_by
        self.created_at = created_at
        self.instances = instances
        self.ranking_system = ranking_system

class User:
    # A user 
    def __init__(self,username: str,first_name: str,second_name: str,email: str,passhash: str):
        self.username = username
        self.first_name = first_name
        self.second_name = second_name
        self.email = email
        self.passhash = passhash

    def register(self):
        pass

    def login(self):
        pass

class Instance:
    def __init__(self,title: str,artist: str,length: int,released: str,art: str):
        self.title = title
        self.artist = artist
        self.length = length
        self.released = released
        self.art = art