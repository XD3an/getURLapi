import requests
import json

# get API response and print the result
def getAPI(url: str, method: str, params: dict, headers: dict) -> bool:
    # check method
    method = method.upper()

    # check params
    if params is None:
        params = {}

    # check headers
    if headers != None:
        headers.update({"accept": "application/json"})

    # =================== get API response ===================
    print("[*] URL:", url)
    print("[*] Method:", method)
    print("[*] Params:", params)
    print("[*] Headers:", headers)
    # request 
    response = requests.request(method, url, params=params, headers=headers)

    # print response
    if response.status_code != 200:
        print("[!] Failed to get API response")
        print("[!] Status Code:", response.status_code)
        print("[!] Response:", response.text)
        return False
    
    print("[*] API Response:")
    print(json.dumps(response.json(), indent=4, ensure_ascii=False))  # utf-8 encoding
    return True