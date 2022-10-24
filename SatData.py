# Author: Dennis Lam
# GitHub username: dennislam4
# Date: 10-18-2022
# Description: Reads JSON file contatting SAT results and writes data into a CSV file.

import json


class SatData:
    """Class that represents 2010 SAT results for NYC."""

    def __init__(self):
        with open("sat.json", "r") as infile:
            self._sat_data = json.load(infile)

    def save_as_csv(self, dbns):
        """Saves list of dbns as CSV file"""
        new_data = []

        for index in self._sat_data['data']:
            if index[8] in dbns:
                new_data.append(index)
            new_data.sort()

        with open("output.csv", "w") as outfile:
            dbn_header = "DBN"
            school_header = "School Name"
            tt_header = "Number of Test Takers"
            crit_header = "Critical Reading Mean"
            math_header = "Mathematics Mean"
            writing_header = "Writing Mean"
            outfile.write(dbn_header + school_header + tt_header + crit_header + math_header + writing_header + '\n')
            outfile.write(str(new_data))
