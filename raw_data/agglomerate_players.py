import pandas as pd


def read_file(file: str) -> pd.DataFrame:
    """
    REad file governos
    :return:
    """
    players = pd.read_csv(file)
    return players


def select_country(df_players: pd.DataFrame, country: str) -> pd.DataFrame:
    """
    Select players from country
    :param df_players:
    :param country:
    :return:
    """
    df_players = df_players[["long_name", 'nationality']]
    df_players = df_players[df_players['nationality'] == country].reset_index(drop=True)
    return df_players

def define_first_name_last_name(df_players:pd.DataFrame)->pd.DataFrame:
    """

    :param df_players:
    :return:
    """
    df_players['first_name'], df_players['last_name'] = df_players['long_name'].str.split(' ', 1).str
    df_players['middle_name'], df_players['last_name'] = df_players['last_name'].str.split(' ', 1).str
    df_players = df_players[['first_name', "middle_name", "last_name", "nationality"]]
    return df_players

def write_csv(path:str)->None:
    """

    :param path:
    :return:
    """
    df_players.to_csv(path, index=False, header=True)


df_players = read_file('football/players_20.csv')
df_players = select_country(df_players=df_players, country="United States")
df_players = define_first_name_last_name(df_players)

print(df_players)
