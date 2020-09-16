import pandas as pd

def CreateDataFrame(filename):
    """ Creates a dataframe
    Args:
        a filename
    Return:
        a dataframe
    """
    f = pd.read_csv(filename)
    return pd.DataFrame(f)

def HaveEmptyCells(dataframe):
    """ returns yes or no if the dataframe has emptycells
    Args:
        a dataframe
    Returns:
        YES OR NO
    """
    return "YES" if dataframe.isnull().any else "NO"

def HaveDuplicates(dataframe):
    """ returns yes or no if the dataframe has duplicates
    Args:
        a dataframe
    Returns:
        YES OR NO
    """
    return "YES" if dataframe.duplicated().any else "NO"

def getShape(dataframe):
    """ Returns the shape of a dataframe
    Args:
        A dataframe
    Returns:
        the shape of the dataframe
    """
    return dataframe.shape

def getIndex(dataframe):
    """ Returns the index of a dataframe
    Args:
        A dataframe
    Returns:
        the index number of the dataframe
    """
    return dataframe.index