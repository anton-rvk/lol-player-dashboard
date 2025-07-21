from riotwatcher import LolWatcher, RiotWatcher, ApiError
import pandas as pd

API_KEY = "RGAPI-8e260593-a23a-4f84-9e64-7d345c762be9"

lol_watcher = LolWatcher(API_KEY)
riot_watcher = RiotWatcher(API_KEY)

region = "na1"

account = riot_watcher.account.by_riot_id('AMERICAS', game_name='Comrarius', tag_line='1984')

summoner = lol_watcher.summoner.by_puuid(region, account['puuid'])

matches = lol_watcher.match.matchlist_by_puuid('AMERICAS', 
                                               puuid = account['puuid'],
                                               count=100)

match_1 = lol_watcher.match.by_id('AMERICAS', match_id=matches[0])

#print(pd.DataFrame.from_dict(match_1))

print(pd.DataFrame(match_1["info"]["participants"]))