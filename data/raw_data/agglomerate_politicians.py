import csv
import pandas as pd
import numpy as np

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

def read_file(path_file: str) -> list:
    """
    Read File
    :return:
    """
    list_items = []
    with open(path_file, 'r') as fd:
        reader = csv.reader(fd)
        for row in reader:
            if len(row) > 0:
                list_items.append(row)
    return list_items


def read_file_governors(file: str):
    """
    REad file governos
    :return:
    """
    gov = pd.read_csv(file)
    return gov


def convert_states(list_states: list) -> list:
    """
    Retunr list of states converted
    :param list_states:
    :return:
    """
    list_states_conv = []
    for item in list_states:
        list_states_conv.append(item[0].lower())
    return list_states_conv


def clean_list_string(list_items=list):
    for item in list_items:
        item.lower().replace("'", "").replace(",", "")
    pass


def extract_information(list_polit: list, list_states: list) -> list:
    """

    :param list_polit:
    :param list_states:
    :return:
    """

    items = []
    for i in range(len(list_polit)):

        name = (list_polit[i])
        if i % 2 == 0:
            polit_item = []
            polit_item.append(str(name[0]).lower().replace(" ", ""))
            if len(name) > 2:
                polit_item.append(str(name[1].lower().replace(" ", "")) + " " + str(name[2]).lower().replace(" ", ""))
            else:
                polit_item.append(name[1].lower().replace(" ", ""))
        else:
            for state in list_states:
                if " " + state in name[0].lower():
                    polit_item.append(state)
                    items.append(polit_item)
    return items


def select_data(gov: pd.DataFrame) -> pd.DataFrame:
    """
    Select data
    :param gov:
    :return:
    """
    gov = gov[["last_name", "first_name", "state_name"]]
    gov = gov.values.tolist()
    return gov


def merge_data(gov: pd.DataFrame, polit: pd.DataFrame) -> list:
    gov.extend(polit)
    res = []
    [res.append(x) for x in gov if x not in res]
    return res


def improve_dataframe(list_politicians: list) -> pd.DataFrame:
    df = pd.DataFrame(list_politicians, columns=['first_name', 'last_name', 'state',"none"])
    del df["none"]
    df["middle_name"] = np.nan
    df["country"] = "united states"
    df["continent"] = "america"
    df["lang_primar"] = "en"
    df["lang_secondary"] = np.nan
    df["lang_tertiary"] = np.nan
    df["lang_quaternary"] = np.nan
    df["search_engine"] = np.nan
    df["link"] = np.nan
    df["category"] = "politicians"
    df = df.apply(lambda x: x.astype(str).str.lower())
    return df

def write_csv(path: str, df: pd.DataFrame) -> None:
    """
    Write dataframe to csv file
    :param path:
    :return:
    """
    df.to_csv(path, index=False, header=True)


list_polit = read_file('politicians/politicians.txt')
list_states = read_file('politicians/list_states.csv')

list_states = convert_states(list_states)
list_congressmann = extract_information(list_polit, list_states)
list_governors = read_file_governors('politicians/governors.txt')
list_governors = select_data(list_governors)
list_policians = merge_data(list_governors, list_congressmann)
df = improve_dataframe(list_policians)
write_csv('../clean_data/politicians_usa.csv', df)
# print
