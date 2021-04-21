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
parser.add_argument('filename', help="The source csv file, which should have two columns for the space_desc and space_cvode")
args = parser.parse_args()

def do_things():
    process_area_types()

def process_area_types():

    mb = matrixb.Importer(args.filename).get_matrix()

    spacedata = []
    for row in mb.rowmap():
        spacedata.append({
            'label': row['space_desc'],
            'value': row['space_code'],
        })

    with open('js/operations-spacetypes-acdata.js', 'w') as fh:
        print("spacetypes = " + json.dumps(spacedata) + ";\n\n", file=fh)

def main():
    try:
        do_things()
    except Exception as e:
        print("\n\n**** ERRROR ******")
        type, value, tb = sys.exc_info()
        traceback.print_exc()
        pdb.post_mortem(tb)

main()



