from GoogleNews import GoogleNews
from newspaper import Article

import src.search_and_scrape.cons_google_search as cons
import pandas as pd

pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


class GoogleNewsSearchScrap:

    def __init__(self, query: str, lang: str):
        self.googlenews = GoogleNews()
        self.googlenews.setlang(lang)
        self.googlenews.setperiod(cons.period)
        self.googlenews.setTimeRange(cons.start_date, cons.end_date)
        self.googlenews.setencode(cons.decode)
        self.number_page = cons.number_page
        self.lang = cons.lang
        self.query = query
        self.result = None

    def __search_news(self) -> None:
        """
        Runing search news
        :return:
        """
        self.googlenews.search(self.query)
        #self.googlenews.getpage(self.number_page)
        self.result = self.googlenews.result()
        print(self.result)
        self.googlenews.clear()
        self.result = pd.DataFrame(self.result)
        print(self.result)

    def __scrap_news(self, url: str) -> str:
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
        for index, rows in self.result.iterrows():
            self.__scrap_news(rows["link"])
            self.result.at[index, "content_txt"] = self.text
