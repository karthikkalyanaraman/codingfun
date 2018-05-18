#!/usr/bin/env python3

"""This script is used for getting stats
from stream rate.

"""
import argparse

OLD = "Old="
NEW = "New="
TIME_START = 11
TIME_END = 23

class ParseFile(object):
    """Parser class

    """

    def __init__(self):
        """Constructor for the parser class

        Initializes the parser and grabs the
        file path from the command line argument.

        """
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument("file_path")
        self.args = self.parser.parse_args()
        self.file_path = self.args.file_path
        self.metrics = {}

    def parse_file(self):
        """Walks through each line of the
        file and parses the line for time,
        old value, new value and adds it to
        the metrics dict and prints the stats.

        """
        with open(self.file_path) as fp:
            line = fp.readline()
            while line:
                self.__parse_line(line)
                line = fp.readline()
        if self.metrics:
            self.print_stats()
        else:
            raise Exception("No stats found in the file")

    def __parse_line(self, line):
        """Parses a line and adds the old value,
        new value and time into the dict in the form,
        {time_old_new: [old, new]}

        """
        line.strip()
        if OLD in line and NEW in line:
            old = line[line.index(OLD) + len(OLD):line.index(OLD) + len(OLD) + 5]
            new = line[line.index(NEW) + len(NEW):line.index(NEW) + len(NEW) + 5]
            time = line[TIME_START:TIME_END]
            key = "_".join([time, old, new])
            self.metrics[key] = [float(old), float(new)]

    def get_min_old(self):
        """Gets the lowest old value and returns
        (time, lowest old value)

        """
        result = min(self.metrics.items(), key=lambda x: x[1][0])
        return (result[0].split("_")[0], result[1][0])

    def get_mid_old(self):
        """Gets the mid old value and returns
        (time, mid old value)

        """
        mid_index = len(self.metrics)/2 if len(self.metrics)%2 == 0 else len(self.metrics)/2 + 1
        result = sorted(self.metrics.items(), key=lambda x: x[1][0])[int(mid_index-1)]
        return (result[0].split("_")[0], result[1][0])

    def get_max_old(self):
        """Gets the max old value and returns
        (time, max old value)

        """
        result = max(self.metrics.items(), key=lambda x: x[1][0])
        return (result[0].split("_")[0], result[1][0])

    def get_avg_old(self):
        """Gets the average of all old values

        """
        return sum(old for old, new in self.metrics.values())/len(self.metrics)

    def get_min_new(self):
        """Gets the lowest new value and returns
        (time, lowest new value)

        """
        result = min(self.metrics.items(), key=lambda x: x[1][1])
        return (result[0].split("_")[0], result[1][1])

    def get_mid_new(self):
        """Gets the mid new value and returns
        (time, mid new value)

        """
        mid_index = len(self.metrics)/2 if len(self.metrics)%2 == 0 else len(self.metrics)/2 + 1
        result = sorted(self.metrics.items(), key=lambda x: x[1][1])[int(mid_index-1)]
        return (result[0].split("_")[0], result[1][1])

    def get_max_new(self):
        """Gets the max new value and returns
        (time, max new value)

        """
        result = max(self.metrics.items(), key=lambda x: x[1][1])
        return (result[0].split("_")[0], result[1][1])

    def get_avg_new(self):
        """Gets the average of all new values

        """
        return sum(new for old, new in self.metrics.values())/len(self.metrics)

    def print_stats(self):
        """Prints all the stats

        """
        print("\nOld: (Time, Min): %s, (Time, Mid): %s, (Time, Max): %s, Average: %s\n"
              % (self.get_min_old(), self.get_mid_old(), self.get_max_old(), self.get_avg_old()))
        print("New: (Time, Min): %s, (Time, Mid): %s, (Time, Max): %s, Average: %s\n"
              % (self.get_min_new(), self.get_mid_new(), self.get_max_new(), self.get_avg_new()))

if __name__ == "__main__":
    parsefile = ParseFile()
    parsefile.parse_file()
