import logging
from pathlib import Path
import os
import stat
import errno
####
#fixing due to remaking the handler
#make a log to the term so that it can at least be seen there as info level
class getLogPath:
    def __init__(self, fname='pyapi.log'):
        if os.name == "posix":        
            self.path = os.path.join('/tmp/pas_api/log/' + fname)
        elif os.name == "nt":
            self.path = os.path.join("C:/pas_api/log/" + fname)
        if not os.path.exists(self.path):
            with open(self.path, 'w'):
                pass 
        #if not os.path.exists(self.path):
        #    os.mkdir(self.path)
    @property
    def real_path(self):
        return self.path

def logs(name, fnname = 'pyapi.log'):
    logger = logging.getLogger(name)
    #change the level. Maybe in a ini file setting?
    logger.setLevel(logging.DEBUG)
    fhand = logging.FileHandler(fnname)#, encoding=None, delay=False)
    fhand.setLevel(logging.DEBUG)
    logger.addHandler(fhand)
    #logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    #formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fhand.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
    #fhand.setFormatter(formatter)
    #logger.disabled = True
    return logger

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s %(message)s',
    level=logging.DEBUG,
    datefmt='%Y-%m-%d %H:%M:%S'
    )
#log =  logging
#log = logs(__name__, 'py_api.log')