from src.pipeline.inject_data import SelectInsertUpdateDataSQL
from src.search_and_scrape.google_query import GoogleNewsSearch
from src.search_and_scrape.extract_text import ExtractTextNews
import src.pipeline.cons_pipeline as cons


class ProcessPipelineInjectionSelection:

    def __init__(self, insert_table: str, select_table: str, select_join_table: str):
        self.file = cons.path_data_normalisation + insert_table + cons.csv
        self.insert_table = insert_table
        self.select_table = select_table
        self.select_join_table = select_join_table

    def inject_data_sql_from_file(self):
        inject = SelectInsertUpdateDataSQL(path_file=self.file, insert_table=self.insert_table, insert_values=None,
                                           select_table=None, select_join_table=None)
        inject.process_inject_query_using_file()

    def select_data_sql(self):
        inject = SelectInsertUpdateDataSQL(path_file=None, insert_table=None, insert_values=None,
                                           select_table=None, select_join_table=None)
        inject.process_select_query()


class ProcessPipelineNewsContent:

    def __init__(self):
        pass

    def google_news_search(self, query_search: str):
        news = GoogleNewsSearch(query=query_search)
        news.search_news()
        print(news.result)

    def extract_content(self):
        scrap = ExtractTextNews(url=url3)
        scrap.scrap_news()
        print(scrap.text)


insert_table = "persona"
pipeline = ProcessPipelineInjectionSelection(insert_table=insert_table)
pipeline.inject_data_sql_from_file()
