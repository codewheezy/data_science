from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder
import pandas as pd
nba_teams = teams.get_teams()

def one_dict(list_dict):
    """we use this function to spilt the data into rows and colums"""
    keys=list_dict[0].keys()
    out_dict={key:[] for key in keys}
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
    return out_dict


dict_nba_team=one_dict(nba_teams)
df_teams=pd.DataFrame(dict_nba_team)
df_teams.head()

df_warriors=df_teams[df_teams['nickname']=='Warriors']
df_warriors

id_warriors=df_warriors[['id']].values[0][0]
id_warriors


gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=id_warriors)
gamefinder.get_json()
games = gamefinder.get_data_frames()[0]
print(games.head())
