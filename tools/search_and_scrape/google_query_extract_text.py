from serpapi.google_search_results import GoogleSearchResults
from newspaper import Article

import tools.search_and_scrape.cons_google_search as cons
import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


class GoogleNewsSearchScrap:

    def __init__(self, query: str, lang: str, location: str):
        self.__params = {}
        self.lang = lang
        self.__params["q"] = query
        self.__params["tbm"] = cons.tmb
        self.__params["gl"] = cons.gl
        self.__params["hl"] = self.lang
        self.__params["location"] = location
        self.__params["num"] = cons.number_search
        self.__params["api_key"] = cons.api_key
        self.result = None

    def __reshape_news_result(self) -> None:
        """
        Reshape the data from SERPAPI to transform for dataframe
        :return:
        """
        news_results_norm = []
        for item in self.result:
            item_norm = {your_key: item[your_key] for your_key in cons.keys_news}
            news_results_norm.append(item_norm)
        self.result = pd.DataFrame(news_results_norm)

    def __search_news(self) -> None:
        """
        Runing search news
        :return:
        """
        client = GoogleSearchResults(self.__params)
        self.result = client.get_dict()['news_results']
        self.__reshape_news_result()

    def __scrap_news(self, url: str) -> None:
        """
        Take the main text of the news
        :return:
        """
        try:
            article = Article(url, self.lang)
            article.download()
            article.parse()
            self.text = repr(article.text)

        except:
            self.text = "ERROR DOWNLOAD ARTICLE"

    def process_search_scrap_news(self):
        self.__search_news()
        # for index, rows in self.result.iterrows():
        #    self.__scrap_news(rows["link"])
        #    self.result.at[index, "content_txt"] = self.text
