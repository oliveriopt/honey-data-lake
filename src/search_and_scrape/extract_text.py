from newspaper import Article

import src.search_and_scrape.cons_google_search as cons


class ExtractTextNews:

    def __init__(self, url: str):
        self.url = url
        self.lang = cons.lang
        self.text = ""

    def scrap_news(self):
        """
        Take the main text of the news
        :return:
        """
        article = Article(self.url, self.lang)
        article.download()
        article.parse()
        self.text = (article.text)
