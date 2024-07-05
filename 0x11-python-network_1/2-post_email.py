#!/usr/bin/python3
"""hbtn_header module
"""

import urllib.request
import sys

url = sys.argv[1]
email = sys.argv[2]

data = f"email={email}".encode('utf-8')

with urllib.request.urlopen(url, data=data) as response:
    body = response.read()
    print(body.decode('utf-8'))
