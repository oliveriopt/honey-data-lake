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


def define_first_name_last_name(df_players: pd.DataFrame) -> pd.DataFrame:
    """

    :param df_players:
    :return:
    """
    df_players['first_name'], df_players['name'] = df_players['long_name'].str.split(' ', 1).str
    df_players['last_name'] = df_players['long_name'].str.split().str[-1]
    df_players['middle_name'] = df_players['name'].str.split().str[0]
    df_players.loc[df_players['last_name'] == df_players['middle_name'], 'middle_name'] = None
    df_players = df_players[['first_name','middle_name','last_name','nationality']]
    return df_players


def write_csv(path: str, df_players: pd.DataFrame) -> None:
    """
    Write dataframe to csv file
    :param path:
    :return:
    """
    df_players.to_csv(path, index=False, header=True)


df_players = read_file('football/players_20.csv')
df_players = select_country(df_players=df_players, country="United States")
df_players = define_first_name_last_name(df_players)
write_csv('football/players_usa.csv', df_players)
print(df_players.head())
