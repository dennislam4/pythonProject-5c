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
        """Saves information starting at DBN's as CSV file"""
        new_data = []

        for index in self._sat_data['data']:
            if index[8] in dbns:
                new_data.append(index)
            new_data.sort()

        with open("output.csv", "w") as outfile:
            headers = ['DBN', 'School Name', 'Number of Test Takers', 'Critical Reading Mean', 'Mathematics Mean', 'Writing Mean']

            for elements in headers:
                elements.strip()
                outfile.write(elements)
                outfile.write(',')
            outfile.write('\n')

            data_list = []

            for data in new_data:
                if data == data[-1]:
                    data_list.append(data)
                    outfile.write(str(data_list))
                outfile.write('\n')
