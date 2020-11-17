import pandas as pd
import itertools
import numpy as np

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


def normalyze_categories(df: pd.DataFrame) -> list:
    """
    Select unique values of categories
    :param df:
    :return:
    """
    categ = df["category"].unique()

    return categ


def normalize_description_zone(df: pd.DataFrame) -> list:
    """
    Select unique values of geo localisation
    :param df:
    :return:
    """
    geo_s = df["state"].unique()
    geo_c = df["country"].unique()
    geo_cont = df["continent"].unique()
    a = [geo_s, geo_c, geo_cont]
    comb = list(itertools.product(*a))
    return comb


def normalize_lang(df: pd.DataFrame) -> list:
    """
    Select combinations of language
    :param df:
    :return:
    """
    lang_1 = df["lang_primar"].unique()
    lang_2 = df["lang_secondary"].unique()
    lang_3 = df["lang_tertiary"].unique()
    lang_4 = df["lang_quaternary"].unique()
    a = [lang_1, lang_2, lang_3, lang_4]
    comb = list(itertools.product(*a))

    return comb


def create_df_from_list(export: list, column: list) -> pd.DataFrame:
    """
    Create df from list
    :param export:
    :param column:
    :return:
    """
    df = pd.DataFrame(export, columns=column)
    df.index.names = ["id"]
    return df


def write_list(path: str, df: pd.DataFrame) -> None:
    """
    Write dataframe to csv file
    :param path:
    :return:
    """
    df.to_csv(path, na_rep='NULL')


def define_personas(df: pd.DataFrame, df_merge: pd.DataFrame, columns: list, name_id: str) -> pd.DataFrame:
    """
    Define main personas database
    :param df: df with personas source
    :param df_merge: data to merge to put the id
    :param columns: 
    :param name_id: 
    :return: 
    """""
    df_merge.reset_index(inplace=True)
    result = pd.merge(df, df_merge, on=columns)
    result = result.rename(columns={"id": name_id})
    del df_merge["id"]
    return result


df = read_file('../data_normalization/personas_source.csv')

categ = create_df_from_list(normalyze_categories(df), ["category"])
geo = create_df_from_list(normalize_description_zone(df), ["state", "country", "continent"])
lang = create_df_from_list(normalize_lang(df), ["lang_primar", "lang_secondary", "lang_tertiary", "lang_quaternary"])

df_personas = define_personas(df, geo, ["state", "country", "continent"], "geographic_zone_id")
df_personas = define_personas(df_personas, categ, ["category"], "category_id")
df_personas = define_personas(df_personas, lang, ["lang_primar", "lang_secondary", "lang_tertiary", "lang_quaternary"], "language_id")

write_list('../data_normalization/category.csv', categ)
write_list('../data_normalization/geographic_zone.csv', geo)
write_list('../data_normalization/language.csv', lang)

df_personas = df_personas[["first_name","middle_name","last_name","language_id","geographic_zone_id","category_id"]]

write_list('../data_normalization/persona.csv', df_personas)

print(df_personas)
