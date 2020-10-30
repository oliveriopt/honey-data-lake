logfile = "logfile.txt"
news_content = "newscontent"
columns_sql = ["persona_id", "first_name", "middle_name", "last_name", "geographic_zone_id", "state", "country",
               "continent", "category_id", "category", "language_id", "language"]
colummn_news_change = {"persona_id": "persona_id", "position": "position_search", "title": "title", "source": "media",
                       "date": "date",
                       "snippet": "desc", \
                       "link": "link", "content_txt": "content_txt", "source_search": "source_search"}
columns_news_reshape = ["persona_id", "position_search", "title", "media", "date", "desc", "link", "content_txt",
                        "source_search"]