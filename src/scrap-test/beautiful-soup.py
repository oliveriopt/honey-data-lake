from serpapi.google_search_results import GoogleSearchResults

try:
    params = {
        "q": "kirk hinrich",
        "tbm": "nws",
        "gl": "us",
        "hl": "en",
        "location": "atlanta",
        "num": 20,
        "api_key": "29714c89070e1853d4834ddd74ce3a1a99b5e1a896bbba50e7110a547478ae68"
    }

    client = GoogleSearchResults(params)
    results = client.get_dict()
    news_results = results['news_results']
    print(news_results)

except:
    pass




