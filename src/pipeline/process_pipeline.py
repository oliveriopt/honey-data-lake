from src.pipeline.inject_data import SelectInsertUpdateDataSQL
from tools.search_and_scrape.google_query_extract_text import GoogleNewsSearchScrap

import src.pipeline.cons_pipeline as cons
import pandas as pd
import logging
import dateparser
import numpy as np

pd.set_option('display.max_rows', 1000)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


class ProcessPipelineInjectionSelection:

    def __init__(self, insert_table: str or None, select_table: str or None, select_table_join: str or None,
                 select_table_join_2: str or None, select_table_join_3: str or None):
        if insert_table is not None:
            self.file = cons.path_data_normalisation + insert_table + cons.csv
        self.insert_table = insert_table
        self.select_table = select_table
        self.select_table_join = select_table_join
        self.select_table_join_2 = select_table_join_2
        self.select_table_join_3 = select_table_join_3

        self.result_sql = None
        self.result_search_google_news = None
        self.result_news = pd.DataFrame()

    def inject_data_sql_from_file(self) -> None:
        """
        Inject data to posgres database
        :return:
        """
        inject = SelectInsertUpdateDataSQL(path_file=self.file, insert_table=self.insert_table, insert_values=None,
                                           select_table=None, select_table_join=None, select_table_join_2=None,
                                           select_table_join_3=None)
        inject.process_inject_query_using_file()

    def __update_data_sql(self, table_update: str) -> None:
        """
        Update data to posgres database
        :return:
        """
        inject = SelectInsertUpdateDataSQL(path_file=None, insert_table=table_update, insert_values=self.result_news,
                                           select_table=None, select_table_join=None, select_table_join_2=None,
                                           select_table_join_3=None)
        inject.process_update_query()

    def __select_data_sql(self, limit: int, offset: int) -> None:
        """
        Select data from sql database
        :return:
        """

        inject = SelectInsertUpdateDataSQL(path_file=None, insert_table=None, insert_values=None,
                                           select_table=self.select_table, select_table_join=self.select_table_join,
                                           select_table_join_2=self.select_table_join_2,
                                           select_table_join_3=self.select_table_join_3)
        self.result_sql = inject.process_select_query(limit=limit, offset=offset)
        self.result_sql = pd.DataFrame.from_records(self.result_sql, columns=cons.columns_sql)

    def __google_news_search(self, query_search: str, lang: str, location: str) -> None:
        """
        Search into google news
        :param query_search:
        :param lang:
        :return:
        """
        news = GoogleNewsSearchScrap(query=query_search, lang=lang, location=location)
        news.process_search_scrap_news()
        self.result_search_google_news = news.result

    def __change_none_type(self, value_change: str) -> None or str:
        """
        Change NONE type for blank space
        :param value_change:
        :return:
        """
        if value_change is None:
            return ""
        return value_change

    def __crete_string_search(self, row) -> tuple:
        """
        Create string search from dataframe
        :param index:
        :param row:
        :return:
        """
        fn = self.__change_none_type(row["first_name"])
        mn = self.__change_none_type(row["middle_name"])
        ln = self.__change_none_type(row["last_name"])
        st = self.__change_none_type(row["state"])
        lang = self.__change_none_type(row["language"])
        string_search = fn + " " + mn + " " + ln
        info = "String search: " + string_search + "\tState: " + st + "\tLanguage: " + \
               lang
        logging.info(info)
        return string_search, st, lang

    def __change_date(self) -> None:
        """
        Change date from "X weeks ago" to date format using year, month, day
        :return:
        """
        for index_date, row_date in self.result_search_google_news.iterrows():
            date = row_date["date"]
            self.result_search_google_news.at[index_date, "date"] = dateparser.parse(date).strftime("%Y-%m-%d")

    def __reshape_data(self, row) -> None:
        """
        Reshape data, introducing persona_id and other columns
        :param row:
        :return:
        """
        self.result_search_google_news["persona_id"] = row["persona_id"]
        self.result_search_google_news["source_search"] = "GOOG_NEWS"
        self.result_search_google_news["content_txt"] = None
        self.__change_date()
        self.result_search_google_news = self.result_search_google_news.rename(columns=cons.colummn_news_change)
        self.result_search_google_news = self.result_search_google_news[cons.columns_news_reshape]

    def process_searching(self, limit: int, offset: int) -> None:
        """
        Process searching
        :return:
        """
        logging.basicConfig(filename=cons.logfile, level=logging.INFO, format='%(asctime)s - %(message)s')
        self.__select_data_sql(limit=limit, offset=offset)
        for index, row in self.result_sql.iterrows():
            string_search, st, lang = self.__crete_string_search(index, row)
            self.__google_news_search(str(string_search), str(lang), str(st))
            self.__reshape_data(row)
            self.result_news = self.result_news.append(self.result_search_google_news, ignore_index=True)
        self.result_news.reset_index(drop=True)
        self.result_news.index = np.arange(offset*20, offset*20 +  limit*20)
        self.result_news = self.result_news.to_records(index=True)
        self.result_news = list(self.result_news)
        self.__update_data_sql(cons.news_content)
