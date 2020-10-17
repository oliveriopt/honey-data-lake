import os
import platform
from pathlib import Path

pth = os.path.abspath(os.getcwd())
PATH = str(Path(pth).parents[1])
csv = ".csv"

# VARIABLES FOR OUTPUTS
if platform.system() == "Darwin":
    path_data_normalisation = PATH + "/data/data_normalization/"
else:
    path_data_normalisation = PATH + "\\data\\data_normalization\\"

