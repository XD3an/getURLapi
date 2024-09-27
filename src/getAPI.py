import sys
import requests
import argparse

from utils import getAPI

def argParse():
    parser = argparse.ArgumentParser(description="Get API response")
    parser.add_argument("--url", type=str, help="Target URL(API)")
    parser.add_argument("--method", type=str, help="HTTP Method(GET, POST, PUT, DELETE)")
    parser.add_argument("--params", type=str, nargs="?", default=None, help="Params (param1=value1,param2=value2,...)")
    parser.add_argument("--header", type=str, nargs="?", default=None, help="Header (header1=value1,header2=value2,...)")
    args = parser.parse_args()
    return args

### main
### 
### usage: getAPI.py [-h] [--url URL] [--method METHOD] [--params [PARAMS]] [--header [HEADER]]
### 
### Get API response
### 
### options:
###   -h, --help         show this help message and exit
###   --url URL          Target URL(API)
###   --method METHOD    HTTP Method(GET, POST, PUT, DELETE)
###   --params [PARAMS]  Params (param1=value1,param2=value2,...)
###   --header [HEADER]  Header (header1=value1,header2=value2,...)
### 
### Example:
###     python getAPI.py --url http://example.com/api --method GET
###
### 
def main() -> None:

    # get argv
    argc = len(sys.argv)
    if argc < 2:
        print("[!] Usage: python getAPI.py <url> <method> [params (params=value)]")
        return
    
    # parse argv 
    args = argParse()
    url = args.url
    method = args.method
    params = args.params
    params = dict([param.split("=") for param in params.split(",")]) if params else None
    headers = args.header
    headers = dict([param.split("=") for param in headers.split(",")]) if headers else None

    # getAPI
    if not getAPI(url, method, params, headers):
        print("[!] Failed to get API response")
        return

if __name__ == '__main__':
    main() 