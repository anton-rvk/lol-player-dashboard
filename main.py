

"""
player = Player("na1", "Comrarius#1984")

print(player.fetch_match(columns=["championName", "kills", "deaths", "assists", "challenges"], 
                         challenges_columns=["firstTurretKilledTime", 
                                             "earliestDragonTakedown",
                                             "kda"]))#.to_csv("match_0.csv")
"""

from api_caller import Watcher



watcher = Watcher(api_key="RGAPI-330dbbc3-e5c6-4af0-8850-c0afdc6dfc0c")

player = watcher.get_player(username="Comrarius#1984",
                            region="na1",
                            general_region="AMERICAS")

player = watcher.fetch_match_history(player=player,
                                     columns=["championName", "role", "kills", "deaths", "assists"])


#print(player.match_history)

champions = watcher.fetch_datadragon(region="na1", dataset=1)
print(champions)