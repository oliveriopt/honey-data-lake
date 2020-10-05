import pandas as pd

def read_file():
    """
    REad file governos
    :return:
    """
    gov = pd.read_csv('governors.txt')
    return gov

def select_data()


gov = read_file()
print(gov.columns.values)