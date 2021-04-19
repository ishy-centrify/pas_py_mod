import json
from util.funct_tools import query_request, other_requests, boolize, sanitizedict
from util.logger import logging as log
import argparse
import os
from pathlib import Path
import csv
import ast
#https://developer.centrify.com/reference#post_servermanage-adddatabases
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add a list of databases from a CSV file, JSON file, or list. All headers in file match the values of the API page. Check example_files to compare.")
    parser.add_argument('-p','--Path', type=str, required=False, default=None, help= 'Path to the csv file. Point to csv in arg path and use forward slashes in the path if using windows.')
    parser.add_argument('-l','--List', type=ast.literal_eval, required=False, default=None, help= 'Array of databases. Please input as a list such as .')
    parser.add_argument('-j','--JSON', type=str, required=False, default=None, help= 'JSON file of databases. Please input the full file path.')
    args = parser.parse_args()

log.info("Using endpoint /ServerManage/AddDatabases...")

if args.Path != None:
    path = os.path.abspath(args.Path)
    log.info("Path to the csv file to add databses is: {0}".format(path))
    with open(path, 'r') as f:
        d_reader = csv.DictReader(f)
        data = [sanitizedict(dict(line)) for line in d_reader]
        log.info("Sanitizing and cleaning up dictionary. Data is: {0}".format(data))
        other_requests(Call='/ServerManage/AddDatabases', Accounts=data, Debug=True)

elif args.List != None:
    log.info("List of accounts is: {0}".format(args.List))
    other_requests(Call='/ServerManage/AddDatabases', Accounts=args.List, Debug=True)

elif args.JSON != None:
    log.info("JSON file being used.")
    path = os.path.abspath(args.JSON)
    log.info("Path to the JSON file to add resources is: {0}".format(path))
    with open(path, 'r') as f:
        other_requests(Call='/ServerManage/AddDatabases', Accounts=json.load(f), Debug=True)

else:
    log.error("Need to input an argument.")