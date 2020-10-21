import os
import platform
from pathlib import Path

pth = os.path.abspath(os.getcwd())
PATH = str(Path(pth).parents[1])
csv = ".csv"

logfile = "logfile.txt"
sqlfile = "create_db_tables.sql"

# VARIABLES FOR OUTPUTS
if (platform.system() == "Darwin") | (platform.system() == "Linux"):
    path_data_normalisation = PATH + "/data/data_normalization/"
    path_sql_file = PATH + "/src/db_interface/" + sqlfile
    logfile = PATH + "/log/" + logfile
else:
    path_data_normalisation = PATH + "\\data\\data_normalization\\"
    path_sql_file = PATH + "\\src\\db_interface\\" + sqlfile
    logfile = PATH + "\\log\\" + logfile

tables = ["category", "geographic_zone", "category", "language", "persona"]
columns_sql = ["persona_id", "first_name", "middle_name", "last_name", "geographic_zone_id", "state", "country",
               "continent", "category_id", "category", "language_id", "language"]
columns_news = ["persona_id", "title", "media", "date", "desc", "link", "content_txt", "source_search"]
columns_news_extended = ["persona_id", "title", "media", "date", "desc", "link", "content_txt", "source_search"]

news_content = "newscontent"
