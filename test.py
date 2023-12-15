"""
Pytest
"""
import text
import csv_read

def test_text():
    """
    Test text
    """
    test = text.open_text()
    assert test != {}

def test_csv_read():
    """
    Test csv_read
    """
    test = csv_read.open_csv()
    assert test
    