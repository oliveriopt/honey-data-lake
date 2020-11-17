from datetime import date

import pandas as pd
import numpy as np
import warnings
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
warnings.simplefilter(action='ignore', category=FutureWarning)

def read_file(file: str) -> pd.DataFrame:
    """
    REad file governos
    :return:
    """
    players = pd.read_csv(file)
    return players

def read_file_convert_dict(file: str) -> dict:
    """
    Read states codes for mapping
    :param file:
    :return:
    """
    states_code = pd.read_csv(file)
    states_code = states_code[["prefix_1","city"]]
    states_code = states_code.set_index('prefix_1')
    dict_y = states_code['city'].to_dict()
    return dict_y

def select_information(df_players: pd.DataFrame,dict_teams:dict) -> pd.DataFrame:
    """
    Select players from data
    :param df_players:
    :param country:
    :return:
    """
    df_players = df_players[["player_name","team_abbreviation",'season']]
    df_players['year'] = df_players['season'].astype(str).str[0:4]
    df_players['year'] = df_players['year'].astype(int)
    df_players = df_players[df_players['year'] >= 2010].reset_index(drop=True)
    df_players['first_name'], df_players['last_name'] = df_players['player_name'].str.split(' ', 1).str
    df_players = df_players.apply(lambda x: x.astype(str).str.lower())
    df_players = df_players.replace({"team_abbreviation": dict_teams})
    df_players['count'] = df_players['team_abbreviation'].str.len()
    df_players = df_players[df_players['count'] > 3].reset_index(drop=True)
    df_players = df_players[["first_name","last_name","team_abbreviation"]]
    df_players.rename({'team_abbreviation': 'state'}, axis=1, inplace=True)
    df_players = df_players.apply(lambda x: x.astype(str).str.lower())
    df_players["middle_name"] = np.nan
    df_players["country"] = "united states"
    df_players["continent"] = "america"
    df_players["lang_primar"] = "en"
    df_players["lang_secondary"] = np.nan
    df_players["lang_tertiary"] = np.nan
    df_players["lang_quaternary"] = np.nan
    df_players["search_engine"] = np.nan
    df_players["link"] = np.nan
    df_players["category"] = "nba_players"
    df_players = df_players.apply(lambda x: x.astype(str).str.lower())
    return df_players

def write_csv(path: str, df_players: pd.DataFrame) -> None:
    """
    Write dataframe to csv file
    :param path:
    :return:
    """
    df_players.to_csv(path, index=False, header=True)

df_players = read_file('nba/nba_players_1.csv')
dict_teams = read_file_convert_dict('nba/teams_code.csv')
df_players = select_information(df_players,dict_teams)
write_csv("../clean_data/nba_players_usa.csv", df_players)