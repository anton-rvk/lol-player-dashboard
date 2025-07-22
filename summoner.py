
class Player():

    def __init__(self, 
                 account, 
                 summoner,
                 region, 
                 general_region):

        self._region = region
        self._general_region = general_region

        self._account = account
        
        self._puuid = self._account["puuid"]

        self._summoner = summoner

        self._match_history = None


    @property
    def match_history(self):
        return self._match_history

    @match_history.setter
    def match_history(self, value):
        self._match_history = value
    
    @property
    def general_region(self):
        return self._general_region
    
    @property
    def region(self):
        return self._region
    
    @property
    def puuid(self):
        return self._puuid