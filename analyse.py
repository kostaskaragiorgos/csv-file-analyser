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

def count_empty(dataframe)-> int:
    """ returns the number of empty cells
    Args:
        a dataframe
    Returns:
        an int
    """
    return dataframe.isnull().sum().sum()


def getcolnames(dataframe):
    """ returns the names of the columns
    Args:
        a dataframe
    Returns:
        a list
    """
    return list(dataframe.columns)

def getcoltypes(dataframe):
    """ returns the types of the columns
    Args:
        a dataframe
    Returns:
        a list
    """
    return list(dataframe.dtypes)

def haveduplicates(dataframe):
    """ returns yes or no if the dataframe has duplicates
    Args:
        a dataframe
    Returns:
        YES OR NO
    """
    return "YES" if dataframe.duplicated().all() else "NO"

def count_duplicates(dataframe):
    """ returns the number of duplicates
    Args:
        a dataframe
    Returns:
        an int
    """
    return dataframe.duplicated().sum().sum()

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



def percent_missing(dataframe):
    percent_nan = 100* dataframe.isnull().sum()/ len(dataframe)
    percent_nan = percent_nan[percent_nan> 0].sort_values()
    return percent_nan
