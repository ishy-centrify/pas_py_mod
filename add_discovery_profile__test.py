from util.funct_tools import query_request, other_requests, boolize, sanitizedict
from util.logger import logging as log
import argparse
import os
import ast
#https://developer.centrify.com/reference#post_servermanage-creatediscoveryprofile
def cl():
    parser = argparse.ArgumentParser(description="Add a discovery profile.")
    parser.add_argument('-co','--ComputerOUs', type=ast.literal_eval, required=False, help= 'List of computer Organization Unit names.')
    parser.add_argument('-d','--Domains', type=ast.literal_eval, required=False, help= 'List of domain objects. an array of DomainId[str], Enabled[bool], NamingContext[str], Name[str].')
    parser.add_argument('-ct','--ComputerType', type=str, required=False, help= 'Type of computer. eg Server, Workstation.')
    parser.add_argument('-ues','--UpdateExistingSystems', type=bool, required=False, help= 'Determines whether existing systems should be updated.')
    parser.add_argument('-dai','--DefaultAccountId', type=str, required=False, help= 'ID of the default Account')
    parser.add_argument('-j','--CurrentConnector', type=str, required=False, help= 'Determines whether to use the current connector.')
    parser.add_argument('-des','--Description', type=str, required=False, help= 'Description of the discovery profile..')
    parser.add_argument('-n','--Name', type=str, required=True, help= 'JSON file of accounts. Please input the full file path.')
    parser.add_argument('-dt','--DiscoveryType', type=str, required=True, help= 'User Name of the default Account.')
    parser.add_argument('-dun','--DefaultUserName', type=str, required=False, help= 'User Name of the default Account.')
    return parser.parse_args()
if __name__ == "__main__":
	args = vars(cl())
log.info('Using argument values: {0}'.format(args))
log.info('Using endpoint /ServerManage/CreateDiscoveryProfile')
new_args = dict((k, v) for k, v in args.items() if v != None)
other_requests(Call='/ServerManage/CreateDiscoveryProfile', **new_args, Debug=True)