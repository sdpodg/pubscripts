import sys,os,re,shutil
from pprint import pprint
import warnings, pdb, traceback
import datetime
import pickle
import googleapps
import matrixb
import json
from pprint import pprint

import argparse
parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('--space-filename', '-s', default='input/spacetypes.csv', help="The source csv file, which should have two columns for the space_desc and space_code")
parser.add_argument('--building-filename', '-b', default='input/school drill down.xlsx', help="The source file to generate the building list")
args = parser.parse_args()

def do_things():
    create_building_map(args.building_filename)
    process_area_types(args.space_filename)



def create_building_map(filename):
    mb = matrixb.Importer(filename).get_matrix()
    js = {}
    for row in mb.rowmap():
        js[row['building_id']] = [row['ulcs'], row['school_name'], row['building_name']]
    with open('js/operations-building-map.js', 'w') as fh:
        print("building_map = " + json.dumps(js) + ";\n", file=fh)


def process_area_types(filename):

    mb = matrixb.Importer(filename).get_matrix()

    spacedata = []
    for row in mb.rowmap():
        spacedata.append({
            'label': row['space_desc'],
            'value': row['space_code'],
        })

    with open('js/operations-spacetypes-acdata.js', 'w') as fh:
        print("spacetypes = " + json.dumps(spacedata) + ";\n", file=fh)

def main():
    try:
        do_things()
    except Exception as e:
        print("\n\n**** ERRROR ******")
        type, value, tb = sys.exc_info()
        traceback.print_exc()
        pdb.post_mortem(tb)

main()



