import platform
from main import PATH

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



ago = "ago"
