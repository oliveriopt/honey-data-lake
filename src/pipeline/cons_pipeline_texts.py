from pathlib import Path

import platform

logfile = "logfile.txt"
csv = ".csv"
logfile = "logfile.txt"
sqlfile = "create_db_tables.sql"

PATH = str(Path(__file__).parent.parent.parent.absolute())
print(PATH)

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
news_content = "newscontent"
columns_sql = ["persona_id", "first_name", "middle_name", "last_name", "geographic_zone_id", "state", "country",
               "continent", "category_id", "category", "language_id", "language"]
colummn_news_change = {"persona_id": "persona_id", "position": "position_search", "title": "title", "source": "media",
                       "date": "date",
                       "snippet": "desc", \
                       "link": "link", "content_txt": "content_txt", "source_search": "source_search"}
columns_news_reshape = ["persona_id", "position_search", "title", "media", "date", "desc", "link", "content_txt",
                        "source_search"]