import pandas as pd

def CreateDataFrame(filename):
    return pd.read_csv(filename)

def FindEmptyCells(dataframe):
    return "YES" if dataframe.isnull().any else "NO"
