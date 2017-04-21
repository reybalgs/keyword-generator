"""
Module for reading CSVs from files or passed into the reader itself.
"""

import csv

class CSVReader(object):
    """
    The actual reader class.
    """

    def __init__(self):
        pass

    @classmethod
    def read_file(cls, filename):
        """
        Reads a file from a given filename and passes it back as a list.
        """
        keywords = []
        with open(filename, newline='') as csvfile:
            for row in csv.reader(csvfile, skipinitialspace=True):
                for string in row:
                    keywords.append(string)
            csvfile.close()

        return keywords
