"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    list_neos = []
    with open(neo_csv_path, 'r') as f:
        reader = csv.DictReader(f)
        for elem in reader:
            hazardous = True if elem['pha'] == 'Y' else False
            diameter = float('nan') if elem['diameter'] == "" else float(elem['diameter'])
            name = None if elem['name'] == "" else elem['name']
            list_neos.append(NearEarthObject(designation= elem['pdes'],name=name,diameter=diameter, hazardous=hazardous))
    return list_neos


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    list_ca = []
    with open(cad_json_path, 'r') as f:
        data = json.load(f)
        for elem in data['data']:
            list_ca.append(CloseApproach(designation=elem[0],time=elem[3], distance=float(elem[4]), velocity=float(elem[7])))
    return list_ca
