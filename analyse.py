import pandas as pd

def CreateDataFrame(filename):
    return pd.read_csv(filename)

def HaveEmptyCells(dataframe):
    return "YES" if dataframe.isnull().any else "NO"

def HaveDuplicates(dataframe):
    return "YES" if dataframe.duplicated().any else "NO"

def getShape(dataframe):
    return dataframe.shape

def getIndex(dataframe):
    """ Returns the index of a dataframe
    Args:
        A dataframe
    Returns:
        the dataframe index
    """
    return dataframe.index