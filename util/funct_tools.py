import requests
import json
import traceback
from .logger import logging as log
from .utility import Cache as c
from .utility import f_check as f

if f().loaded['urls']['tenant'] or c().cached['header'] == None:
    log.error("Cache issue or Tenant is not set in config.json.")

def boolize(v):
    return {
        "TRUE": True,
        "FALSE": False,
    }.get(v.upper() if hasattr(v,"upper") else "", v)

def sanitizedict(d):
    return {k:boolize(v) for k,v in d.items() if v!= ""}

#RedRock Query
class query_request:
    def __init__(self, sql, Debug=False):
        url = "{0}/Redrock/Query".format(f().loaded['urls']['tenant'])
        self._q_headers = c().cached['header']
        log.info("Starting Query Request....")
        try:
            self.query_request = requests.post(url=url, headers=self._q_headers, json={"Script": sql}).json()
        except Exception as e:
            log.error("Internal error occurred. Please note it failed on a Query request.")
            log.error(traceback.print_exc(e))
        self.jsonlist = json.dumps(self.query_request)
        self.parsed_json = (json.loads(self.jsonlist))
        if self.parsed_json['success'] == False:
            log.error("Issue with Query. Dump is: {0}".format(self.jsonlist))
            return None
        log.info("JSON dump of Query is : {0}".format(self.jsonlist))
        log.info("Finished Query")
        ###!REMOVE AFTER TESTING!###
        if Debug == True:
            print(json.dumps(self.parsed_json, indent=4, sort_keys=True))
#for other requests
class other_requests:
    def __init__(self, Call, Debug=False, **kwargs):
        Call = '{0}{1}'.format(f().loaded['urls']['tenant'], Call)
        self._r_headers = c().cached['header']
        self.kwargs = kwargs
        self.__dict__.update(**self.kwargs) 
        try:       
            self.other_requests = requests.post(url=Call, headers=self._r_headers, json=self.kwargs).json()
        except Exception as e:
            log.error("Internal error occurred. Please note it failed on an other request")
            log.error(traceback.print_exc(e))
        self.jsonlist = json.dumps(self.other_requests)
        self.parsed_json = (json.loads(self.jsonlist))
        if self.parsed_json['success'] == False:
            log.error("Issue with other request. Dump is: {0}".format(self.jsonlist))
            return None
        log.info("JSON dump of request is : {0}".format(self.jsonlist))
        log.info("Finished request")
        ###!REMOVE AFTER TESTING!###
        if Debug == True:
            print(json.dumps(self.parsed_json, indent=4, sort_keys=True))
#make complicated request so that it trasfers complicated objects. This will allow to arrayed dicts and whatnot

