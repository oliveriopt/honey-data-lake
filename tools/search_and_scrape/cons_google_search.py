from time import gmtime, strftime
max_chars = 20000
period = "d"
tmb = "nws"
gl = "us"
start_date = '20/10/2019'
api_key = "29714c89070e1853d4834ddd74ce3a1a99b5e1a896bbba50e7110a547478ae68"
end_date =  strftime("%d/%m/%Y", gmtime())
number_search = 30
decode = 'utf-8'
keys_news = ["position","link","title","source","date","snippet"]

