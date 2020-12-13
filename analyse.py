""" functions to analyse a csv file """
import pandas as pd

def createdataframe(filename):
    """ Creates a dataframe
    Args:
        a filename
    Return:
        a dataframe
    """
    file = pd.read_csv(filename)
    return pd.DataFrame(file)

def haveemptycells(dataframe):
    """ returns yes or no if the dataframe has emptycells
    Args:
        a dataframe
    Returns:
        YES OR NO
    """
    return "YES" if dataframe.isnull().any else "NO"

def haveduplicates(dataframe):
    """ returns yes or no if the dataframe has duplicates
    Args:
        a dataframe
    Returns:
        YES OR NO
    """
    return "YES" if dataframe.duplicated().any else "NO"

def getshape(dataframe):
    """ Returns the shape of a dataframe
    Args:
        A dataframe
    Returns:
        the shape of the dataframe
    """
    return dataframe.shape

def getindex(dataframe):
    """ Returns the index of a dataframe
    Args:
        A dataframe
    Returns:
        the index number of the dataframe
    """
    return dataframe.index
