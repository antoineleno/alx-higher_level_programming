#!/usr/bin/python3
"""hbtn_header module
"""

import sys
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as body:
        x_reques_id = body.headers.get("X-Request-Id")
        print(x_reques_id)
