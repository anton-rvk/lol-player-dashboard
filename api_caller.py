
from riotwatcher import LolWatcher, RiotWatcher
import pandas as pd

from summoner import Player

class Watcher():

    def __init__(self, api_key):


        self.riot_watcher = RiotWatcher(api_key)
        self.lol_watcher = LolWatcher(api_key)
        #self.region = region
        #self.region_general = "AMERICAS"

    
    def get_player(self, username, region, general_region):

        split_username = username.split("#")

        game_name = split_username[0]
        tag = split_username[1]

        account = self.riot_watcher.account.by_riot_id(general_region, 
                                                            game_name=game_name, 
                                                            tag_line=tag)
        
        summoner = self.lol_watcher.summoner.by_puuid(region=region, 
                                                      encrypted_puuid=account["puuid"])

        player = Player(account= account, 
                          summoner = summoner,
                          region=region,
                          general_region=general_region)

        return player
    


    def fetch_match_history(self, player, columns = None):

        match_history = self.lol_watcher.match.matchlist_by_puuid(player.general_region,
                                                                  player.puuid)
        
        match_history_list = []

        for match_id in match_history:
            match = self.lol_watcher.match.by_id(region=player.general_region, 
                                                match_id=match_id)
            
            match_df = pd.DataFrame(match["info"]["participants"])

            if columns:
                match_df = match_df[columns]

            match_history_list.append(match_df)

        player.match_history = match_history_list

        return player
    
    def fetch_datadragon(self, region, dataset = 1):

        versions = self.lol_watcher.data_dragon.versions_for_region(region)
        print(versions)

        datadragon = self.lol_watcher.data_dragon
        
        match dataset: #make this an ENUM
            case 1:
                version = versions['n']['champion']

                df = pd.DataFrame(datadragon.champions(version))
                return pd.json_normalize((df["data"]))
            
            case 2: 
                version = versions['n']['item']
                return datadragon.items(version)
            case 3: 
                version = versions['n']['rune']
                return datadragon.runes(version)
            case 4: 
                version = versions['n']['profileicon']
                return datadragon.profile_icons(version)
            case _: 
                return None