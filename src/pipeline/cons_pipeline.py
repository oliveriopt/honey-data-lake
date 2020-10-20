import os
import platform
from pathlib import Path

pth = os.path.abspath(os.getcwd())
PATH = str(Path(pth).parents[1])
csv = ".csv"

logfile = PATH + "/log/logfile.txt"

# VARIABLES FOR OUTPUTS
if platform.system() == "Darwin":
    path_data_normalisation = PATH + "/data/data_normalization/"
else:
    path_data_normalisation = PATH + "\\data\\data_normalization\\"

tables = ["category", "geographic_zone", "category", "language", "persona"]
columns_sql = ["persona_id", "first_name", "middle_name", "last_name", "geographic_zone_id", "state", "country",
               "continent", "category_id", "category", "language_id", "language"]
columns_news = ["persona_id", "title", "media", "date", "desc", "link", "content_txt", "source_search"]
columns_news_extended = ["persona_id", "title", "media", "date", "desc", "link", "content_txt", "source_search"]

news_content = "newscontent"
