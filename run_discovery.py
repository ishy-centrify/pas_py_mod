from util.funct_tools import query_request, other_requests, boolize, sanitizedict
from util.logger import logging as log
import argparse
import ast

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run discovery job. Use name.")
    parser.add_argument('-p','--Path', type=ast.literal_eval, required=True, help= 'Name of the discovery agent.')
    