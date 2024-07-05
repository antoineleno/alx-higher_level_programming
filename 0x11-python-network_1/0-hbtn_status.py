#!/usr/bin/python3
"""hbtn_status module
"""
import urllib.request


if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as body:
        html = body.read()
        print("Body response:")
        print("    - type: {}".format(type(html)))
        print("    - content: {}".format(html))
        print("    - utf8 content: {}".format(html.decode('utf-8')))
