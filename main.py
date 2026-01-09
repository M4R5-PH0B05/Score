class Score:
    # A score instance is a ranking created by a user.
    def __init__(self,id: int,name: str,created_by: str,created_at: str,ranking_system: int,
                 visibility: str,tier_count: int,instance_type: str):
        self.id = id
        self.name = name
        self.created_by = created_by
        self.created_at = created_at
        self.ranking_system = ranking_system
        self.visibility = visibility
        self.tier_count = tier_count
        self.instance_type = instance_type
        self.instances = None

    # Adds a new instance to the list
    def addInstance(self):
        pass

    # Removes an instance from the list
    def removeInstance(self):
        pass

    # Changes an instances rank
    def changeInstanceRank(self):
        pass

    # Creates a shareable link to the score
    def shareScore(self):
        pass

    # Renames the score
    def renameScore(self):
        pass

    # Deletes the score
    def deleteScore(self):
        pass

    # Saves the Score to the database
    def saveScore(self):
        pass

    # Changes ranking system, e.g. 1,2,3,4,5 > S,A,B,C,D
    def changeRankingSystem(self):
        pass

    # Changes the visibility of the score
    def changeVisibility(self):
        pass

    # Adds a new tier
    def addTier(self):
        pass

    # Remove a tier
    def removeTier(self):
        pass

    # Loads instances from DB
    def loadInstances(self):
        self.instances = []



class User:
    def __init__(self,username: str,first_name: str,second_name: str,email,UUID: str):
        self.username = username
        self.first_name = first_name
        self.second_name = second_name
        self.email = email
        self.UUID = UUID

class Album:
    def __init__(self,title: str,artist: str,length: int,released: str,art: str):
        self.title = title
        self.artist = artist
        self.length = length
        self.released = released
        self.art = art

class Song:
    def __init__(self,title: str,artist: str,length: int,released: str,art: str):
        self.title = title
        self.artist = artist
        self.length = length
        self.released = released
        self.art = art

class Artist:
    def __init__(self,first_name: str, second_name:str,art: str):
        self.first_name = first_name
        self.second_name = second_name
        self.art = art


def registerUser():
    # Take in details, return new user object
    # Commit to DB

    pass

def loginUser():
    # take in details, return user object
    pass

