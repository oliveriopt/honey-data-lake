from newspaper import Article

import search_and_scrape.src.cons_google_search as cons


class ExtractTextNews:

    def __init__(self, url:str):
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


url = "https://thehill.com/homenews/campaign/415221-james-comey-knocks-on-door-for-democrat-jennifer-wexton"
url2 = "https://www.businessinsider.com/democrat-jennifer-wexton-unseats-barbara-comstock-in-virginia-2018-11"
url3 = "https://www.ft.com/content/93cffd8f-84ce-4160-a22e-b7d168620875"

scrap = ExtractTextNews(url=url3)
scrap.scrap_news()
print(scrap.text)
