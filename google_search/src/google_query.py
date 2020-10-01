from googlesearch import search


class GoogleSearch:
    def __init__(self, query: str, tld: str, lang: str, num=int):
        self.query = query
        self.tld = tld  # The top level domain
        self.lang = lang  # The language
        self.num = num  # Number of results per page
        self.start = 0  # First result to retrieve
        self.stop = 40  # Last result to retrieve
        self.pause = 2.0
        self.result = []

    def google_search(self):
        """
        Return list of links in google search
        :return:
        """

        for i in search(query,  # The query you want to run
                        tld=self.tld,  # The top level domain
                        lang=self.lang,  # The language
                        num=self.num,  # Number of results per page
                        start=self.start,  # First result to retrieve
                        stop=self.stop,  # Last result to retrieve
                        pause=self.pause,  # Lapse between HTTP requests
                        ):
            print(i)
            self.result.append(i)


query = "politians texas"
goo = GoogleSearch(query, 'com', 'en', 20)
goo.google_search()
