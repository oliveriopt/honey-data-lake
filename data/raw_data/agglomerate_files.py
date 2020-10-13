import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

def read_file(file: str) -> pd.DataFrame:
    """
    REad file governos
    :return:
    """
    df = pd.read_csv(file)
    return df

def write_csv(path: str, df: pd.DataFrame) -> None:
    """
    Write dataframe to csv file
    :param path:
    :return:
    """
    df.to_csv(path, index=False, header=True)

df = read_file('../clean_data/politicians_usa.csv')
df1 = read_file('../clean_data/nba_players_usa.csv')
df2 = read_file('../clean_data/nfl_players_usa.csv')
df3 = read_file('../clean_data/football_players_usa.csv')

result = pd.concat([df, df1, df2, df3])
write_csv('../normalization_data/personas.csv', result)

print(result.head())
print(result.shape)