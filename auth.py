import json
import os
import argparse
import requests
from util.logger import logging as log
from util.utility import getConfigPath
from cryptography.fernet import Fernet
import getpass

def cl():
    parser = argparse.ArgumentParser(description="API Auth config maker. Makes JSON file in current workers dir")
    parser.add_argument('-a','--auth', type=str, required=True, help= 'dmc OR oauth')
    parser.add_argument('-s','--scope', type=str, required=True, help= 'scope of token')
    parser.add_argument('-t','--tenant', type=str, required=True, help= 'abc0123.my.centrify.net') 
    parser.add_argument('-aid','--appid', type=str, required=False, help= 'app id of the oauth token')
    parser.add_argument('-sa','--service_account', type=str, required=False, help= 'service account of the token')
    parser.add_argument('-p','--password', type=str, required=False, default=None, help= 'pw of service account')
    parser.add_argument('-wp','--write_pw_to_file', type=bool, required=False, default=False, help= 'will save pw to file')
    return parser.parse_args()
if __name__ == "__main__":
    args = vars(cl())
#underconstruction#
#make Class and a cipher key file will be leveraging a hidden key file to reference in the local users hidden dir to encrypt to password
class cipher:
    def __init__(self):
        self.key = Fernet.generate_key() 
        self.cipher_suite = Fernet(self.key)
        self.encode = args['password'].encode('utf_8')
        self.encoded_pw = self.cipher_suite.encrypt(self.encode)
        #generate a hidden key file to read the key to unencrypt data at rest
        #https://stackoverflow.com/questions/549109/hide-folders-file-with-python
        #ctypes.windll.kernel32.SetFileAttributesW(path, 2)
def saveConfig(path = getConfigPath().real_path):
    if args['auth'].upper() == 'OAUTH':
        dictionary =  {'auth' : 'OAUTH','urls' : {'tenant': args['tenant'],'app_url': '{tenant}/Oauth2/Token/{appid}'.format(**args)},'body': {'scope': args['scope'],\
            'client_id': args['service_account'], 'grant_type': 'client_credentials'}}
        if args['write_pw_to_file'] == True:
            try:
                dictionary['body']['client_secret'] = args['password']
            except KeyError:
                log.error("Need to input PW value")
                raise Exception
            pass
        try:
            with open(path, "w", encoding='utf-8') as conf:
                conf.write(json.dumps(dictionary, sort_keys=True, indent = 4))
                #maybe permissions
                pass
            pass
        except:
            log.error("Error making oauth JSON config File")
            raise Exception
    if args['auth'].upper() == 'DMC':
        with open(path, "w+") as conf:
            try:
                conf.write(json.dumps({'auth':'DMC', 'scope':args['scope'], 'urls' : {'tenant': args['tenant']}}, sort_keys=True, indent=4))
                log.info('Made the DMC config file.')
                #maybe permissions
            except:
                log.error("Cannot Make file for DMC auth.")
                raise Exception
            pass
        pass
    else:
        log.warning('Not a valid auth type. Please use DMC or OAUTH')
        return {}
saveConfig()

