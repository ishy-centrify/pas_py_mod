from util.funct_tools import query_request
from util.logger import logging as log
import argparse
import pprint

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Have a SQL query to tenant.")
    parser.add_argument('-q','--Query', type=str, required=True, help= 'Query to the tenant.')
    args = parser.parse_args()

log.info("Using SQL query: {0}".format(args.Query))
log.info("Executing query....")
try:
    query_request(sql=args.Query, Debug=True)
except:
    log.error("Issue running raw_query.")