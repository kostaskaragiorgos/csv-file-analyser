import analyse
import pandas as pd
TEST_FILE = 'testfiles/testf.csv'


def test_analyse():
    data = analyse.createdataframe(TEST_FILE)
    assert len(data) == 8
    assert analyse.haveemptycells(data) == "YES"
    assert analyse.haveduplicates(data) == "NO"
    assert analyse.count_empty(data) == 1


