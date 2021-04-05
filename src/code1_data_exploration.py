import numpy as np
import pandas as pd

def test_import_link(dataset):
    return list(dataset.columns)

def import_csv (string):
    dataframe_orig = pd.read_csv(string,encoding = "ISO-8859-1")
    #print("dataset imported to .csv, assigned to variable: 'dataframe_orig', please call function by reassigning it to 'dataframe_orig'")
    return dataframe_orig

def import_xls_to_csv (string):
    string_csv = string.replace('.xls','.csv')
    read_file = pd.read_excel (string)
    read_file.to_csv (string_csv,
                  index = None,
                  header=True)
    dataframe_updated = pd.DataFrame(pd.read_csv(string_csv))
    #print("dataset imported to .csv, assigned to variable: 'dataframe', please call function again by assigning it to 'dataframe'")
    return dataframe_updated

def remove_empty_and_duplicate_rows(dataframe):
    print('dataframe original shape is: ',dataframe.shape)
    dataframe.dropna(how="all",inplace = True)
    print('dataframe shape after removing empty rows is: ',dataframe.shape)
    dataframe.drop_duplicates(keep=False, inplace = True, ignore_index = True)
    print('dataframe shape after removing duplicate rows is: ',dataframe.shape)
    return dataframe

'''
def remove_unnecessary_columns(droppable_columns,data):
    print(data.columns)
    data = data.drop(columns = droppable_columns,inplace=True)
    #data = data.drop(columns = droppable_columns)
    print("dataframe now assigned to variable: 'data', refer to it as 'data' from this point forward")
    return data
'''

def remove_unnecessary_columns(droppable_columns,data1):
    #print(dataframe.columns)
    data1 = data1.drop(columns = droppable_columns,inplace=True)
    #data = data.drop(columns = droppable_columns)
    #print("dataframe now assigned to variable: 'dataframe', refer to it as 'dataframe' from this point forward")
    return data1

def rename_columns(data1):
    renamable_columns = list(data1.columns)
    renamed_columns = ['fatal' if each == 'Fatal (Y/N)' else str(each).lower().strip().replace(" ","_") for each in renamable_columns]
    data1.columns = renamed_columns
    return data1

def export_df_to_csv_and_check (data2):
    data2.to_csv('data-processed/attacks_updated_v1.csv',index = False)
    if True:
        print('Attention: export succesfull, importing new file to check format')
        check_exported_file = pd.read_csv('data-processed/attacks_updated_v1.csv',nrows=3)
        if True:
            print('Attention: showing first 3 rows of .csv to check format')
            print(check_exported_file)
            print("Attention: Check succesfull and file exported correctly to 'data-processed/attacks_updated_v1.csv'")
        else:
            print('cannot show first 3 rows of .csv, check format')