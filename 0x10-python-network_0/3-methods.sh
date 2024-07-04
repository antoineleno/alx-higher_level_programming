#!/bin/bash
# Bash script that takes in a URL, and display all htpp methods
curl -sI -X OPTIONS "$1" | grep -i '^allow:' | awk '{print $2}'
