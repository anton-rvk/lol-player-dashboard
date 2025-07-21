
from riotwatcher import LolWatcher, RiotWatcher

import pandas as pd


API_KEY = "RGAPI-8e260593-a23a-4f84-9e64-7d345c762be9"

class Player():

    def __init__(self, region, username):

        self.riot_watcher = RiotWatcher(API_KEY)
        self.lol_watcher = LolWatcher(API_KEY)

        self.region = region
        self.region_general = "AMERICAS"


        split_username = username.split("#")

        self.game_name = split_username[0]
        self.tag = split_username[1]

        self.account = self.riot_watcher.account.by_riot_id(self.region_general, 
                                                            game_name=self.game_name, 
                                                            tag_line=self.tag)
        
        self.puuid = self.account["puuid"]

        self.summoner = self.lol_watcher.summoner.by_puuid(self.region,
                                                           self.puuid)

        self.match_history = self.lol_watcher.match.matchlist_by_puuid(self.region_general,
                                                                       self.puuid)

    def fetch_match(self, 
                    match_age = 0,
                    challenges_columns = [],
                    columns = None):
        
        my_match_id = self.match_history[match_age]
        my_match = self.lol_watcher.match.by_id(region=self.region_general, 
                                                match_id=my_match_id)

        match_df = pd.DataFrame(my_match["info"]["participants"])
        
        if columns:

            if "challenges" in columns:
                expanded_challenges =  pd.json_normalize(match_df["challenges"]).reset_index(drop=True)[challenges_columns]
                columns.remove("challenges")
                print(expanded_challenges.shape)
                print(match_df[columns].shape)

                match_df =  pd.concat([match_df[columns], 
                                       expanded_challenges], axis=1)

                columns.extend(list(expanded_challenges.columns))


            print(columns)
            print("HA")
            return match_df[columns]
         
        return match_df