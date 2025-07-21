from data.player import Player

DEFAULT_COLUMNS = [

]


player = Player("na1", "Comrarius#1984")

print(player.fetch_match(columns=["championName", "kills", "deaths", "assists", "challenges"], 
                         challenges_columns=["firstTurretKilledTime", 
                                             "earliestDragonTakedown",
                                             "kda"]))#.to_csv("match_0.csv")