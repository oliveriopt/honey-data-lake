from serpapi.google_search_results import GoogleSearchResults
from newspaper import Article

import src.search_and_scrape.cons_google_search as cons
import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


class GoogleNewsSearchScrap:

    def __init__(self, query: str, lang: str, location: str):
        self.params = {}
        self.lang = lang
        self.params["q"] = query
        self.params["tbm"] = cons.tmb
        self.params["gl"] = cons.gl
        self.params["hl"] = self.lang
        self.params["location"] = location
        self.params["num"] = cons.number_search
        self.params["api_key"] = cons.api_key
        self.result = None



    def __search_news(self) -> None:
        """
        Runing search news
        :return:
        """
        client = GoogleSearchResults(self.params)
        results = client.get_dict()
        news_results = results['news_results']
        news_results_norm = []
        for item in news_results:
            item_norm = {your_key: item[your_key] for your_key in cons.keys_news}
            news_results_norm.append(item_norm)
        self.result = pd.DataFrame(news_results_norm)
        print(self.result)

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
        #for index, rows in self.result.iterrows():
        #    self.__scrap_news(rows["link"])
        #    self.result.at[index, "content_txt"] = self.text
