import numpy as np
import pandas as pd

def import_csv (string):
    dataframe = pd.read_csv(string,encoding = "ISO-8859-1")
    return dataframe


def import_xls_to_csv (string):
    string_csv = string.replace('.xls','.csv')
    read_file = pd.read_excel (string)
    read_file.to_csv (string_csv,
                  index = None,
                  header=True)
    dataframe = pd.DataFrame(pd.read_csv(string_csv))
    #print("dataset imported to .csv, assigned to variable: 'dataframe', please call function again by assigning it to 'dataframe'")
    return dataframe

def change__to_dtype_category(list):
    for df in list:
        if df.column.dtype == 'object':
            df[i] = df_2019.apply(lambda x: x.astype('category')).type
            pass