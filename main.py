#!/usr/bin/env python3

"""
Main executable file to be used for demos/testing.
"""

from generator import KeywordGenerator
from csv_reader import CSVReader

def main(filename="./sample.csv"):
    """
    Main method for testing
    """
    reader = CSVReader()

    generator = KeywordGenerator(reader.read_file(filename))
    for word in generator.generate():
        print(word + ",", end="", flush=True)

if __name__ == '__main__':
    main()
