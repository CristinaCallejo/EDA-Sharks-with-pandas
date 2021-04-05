import numpy as np
import pandas as pd

def import_csv (string):
    dataframe = pd.read_csv(string,encoding = "ISO-8859-1")
    return dataframe