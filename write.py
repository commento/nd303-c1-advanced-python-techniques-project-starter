"""Write a stream of close approaches to CSV or to JSON.

This module exports two functions: `write_to_csv` and `write_to_json`, each of
which accept an `results` stream of close approaches and a path to which to
write the data.

These functions are invoked by the main module with the output of the `limit`
function and the filename supplied by the user at the command line. The file's
extension determines which of these functions is used.

You'll edit this file in Part 4.
"""
import csv
import json

from helpers import datetime_to_str


def write_to_csv(results, filename):
    """Write an iterable of `CloseApproach` objects to a CSV file.

    The precise output specification is in `README.md`. Roughly, each output row
    corresponds to the information in a single close approach from the `results`
    stream and its associated near-Earth object.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    fieldnames = ('datetime_utc', 'distance_au', 'velocity_km_s', 'designation', 'name', 'diameter_km', 'potentially_hazardous')
    with open(filename, 'w') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for elem in results:
            d = {}
            d["datetime_utc"] = datetime_to_str(elem.time)
            d["distance_au"] = elem.distance
            d["velocity_km_s"] = elem.velocity
            d["designation"] = elem.neo.designation
            d["name"] = elem.neo.name if elem.neo.name else 'None'
            d["diameter_km"] = elem.neo.diameter if elem.neo.diameter else 'nan'
            d["potentially_hazardous"] = 'True' if elem.neo.hazardous else 'False'
            writer.writerow(d)


def write_to_json(results, filename):
    """Write an iterable of `CloseApproach` objects to a JSON file.

    The precise output specification is in `README.md`. Roughly, the output is a
    list containing dictionaries, each mapping `CloseApproach` attributes to
    their values and the 'neo' key mapping to a dictionary of the associated
    NEO's attributes.

    :param results: An iterable of `CloseApproach` objects.
    :param filename: A Path-like object pointing to where the data should be saved.
    """
    with open(filename, 'w') as outfile:
        l = []
        for elem in results:
            d = {}
            d["datetime_utc"]            = datetime_to_str(elem.time)
            d["distance_au"]             = elem.distance
            d["velocity_km_s"]           = elem.velocity
            neo = {}
            neo["designation"]           = elem.neo.designation
            neo["name"]                  = elem.neo.name
            neo["diameter_km"]           = elem.neo.diameter
            neo["potentially_hazardous"] = elem.neo.hazardous
            d["neo"] = neo
            l.append(d)
        json.dump(l, outfile, indent=2)
