import pandas as pd

def CreateDataFrame(filename):
    return pd.read_csv(filename)

def HaveEmptyCells(dataframe):
    return "YES" if dataframe.isnull().any else "NO"

def HaveDuplicates(dataframe):
    retrun "YES" if dataframe.duplicated().any else "NO"

