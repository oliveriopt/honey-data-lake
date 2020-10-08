from googlesearch import search
from GoogleNews import GoogleNews
import google_search.src.cons_google_search as cons


class GoogleSearch:
    def __init__(self, query: str, tld: str):
        self.query = query
        self.tld = tld  # The top level domain
        self.lang = cons.lang  # The language
        self.num = cons.num  # Number of results per page
        self.start = 0  # First result to retrieve
        self.stop = 40  # Last result to retrieve
        self.pause = 2.0
        self.result = []

    def google_search(self):
        """
        Return list of links in google search
        :return:
        """

        for i in search(query,
                        tld=self.tld,
                        lang=self.lang,
                        num=self.num,
                        start=self.start,
                        stop=self.stop,
                        pause=self.pause,
                        ):
            print(i)
            self.result.append(i)


class GoogleNewsSearch:

    def __init__(self, query: str):
        self.googlenews = GoogleNews()
        print(self.googlenews)
        self.googlenews.setlang(cons.lang)
        self.googlenews.setperiod(cons.period)
        self.googlenews.setTimeRange(cons.start_date, cons.end_date)
        self.googlenews.setencode(cons.decode)
        self.number_page = cons.number_page
        self.query = query
        self.result = []

    def search_news(self) -> list:
        """
        Runing search news
        :return:
        """
        print(self.query)
        self.googlenews.search(self.query)
        self.googlenews.getpage(self.number_page)
        self.result = self.googlenews.result()
        self.googlenews.clear()


query = "wexton,jennifer,virginia"
news = GoogleNewsSearch(query=query)
news.search_news()
print(news.result)
