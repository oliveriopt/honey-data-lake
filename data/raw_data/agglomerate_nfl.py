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
    states_code = states_code.set_index('abbreviation')
    dict_y = states_code['state'].to_dict()
    return dict_y


def select_information(df_players: pd.DataFrame) -> pd.DataFrame:
    """
    Select players from data
    :param df_players:
    :param country:
    :return:
    """
    df_players = df_players[["Birth Place", 'Birthday', "Name"]]
    df_players['Birthday'] = pd.to_datetime(df_players['Birthday'])
    df_players["today"] = date.today().strftime("%Y-%m-%d")
    df_players['today'] = pd.to_datetime(df_players['today'])
    df_players["age"] = (df_players["today"] - df_players['Birthday']).dt.days / 365.
    df_players = df_players[df_players['age'] <= 50].reset_index(drop=True)
    df_players = df_players.dropna(subset=['Birth Place']).reset_index(drop=True)
    return df_players


def clean_information(df_players: pd.DataFrame, states_code: dict) -> pd.DataFrame:
    """
    Clean information
    :param df_players:
    :param states_code:
    :return:
    """
    df_players['city'], df_players['state_code'] = df_players['Birth Place'].str.split(' , ', 1).str
    df_players = df_players.replace({"state_code": states_code})
    df_players['last_name'], df_players['first_name'] = df_players['Name'].str.split(', ', 1).str
    df_players = df_players[["first_name", "last_name", "state_code"]]
    df_players.rename(columns={'state_code': 'state'}, inplace=True)
    df_players = df_players.apply(lambda x: x.astype(str).str.lower())
    df_players["country"] = "united states"
    df_players["continent"] = "america"
    df_players["middle_name"] = np.nan
    df_players["lang_primar"] = "en"
    df_players["lang_secondary"] = np.nan
    df_players["lang_tertiary"] = np.nan
    df_players["lang_quaternary"] = np.nan
    df_players["search_engine"] = np.nan
    df_players["link"] = np.nan
    df_players["category"] = "nfl_players"
    return df_players


def write_csv(path: str, df_players: pd.DataFrame) -> None:
    """
    Write dataframe to csv file
    :param path:
    :return:
    """
    df_players.to_csv(path, index=False, header=True)


df_players = read_file('nfl/Basic_Stats.csv')
dict_states = read_file_convert_dict('nfl/code_states.csv')
df_players = select_information(df_players)
df_players = clean_information(df_players, dict_states)
write_csv("../clean_data/nfl_players_usa.csv", df_players)
