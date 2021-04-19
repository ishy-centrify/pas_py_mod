from util.funct_tools import query_request, other_requests
from util.logger import logging as log
import pprint
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Get metadata of the .")
    parser.add_argument('-n','--Name', type=str, required=False, help= 'ID of Secret')
    args = parser.parse_args()
    
log.info("Querying ID for secret: {0}....".format(args.Name))
id = query_request(sql="SELECT DataVault.ID FROM DataVault WHERE UPPER(DataVault.SecretName) = '{0}'".format(args.Name)).parsed_json
if id['Result']['Count'] == 0:
    log.error("Secret not found")
log.info("Using endpoint /ServerManage/GetSecret....")
log.info("Using Secret ID: {0}".format(args.ID))
other_requests(Call="/ServerManage/GetSecret", ID=args.ID, Debug=True)
