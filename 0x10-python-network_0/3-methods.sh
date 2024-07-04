#!/bin/bash
# Bash script that takes in a URL, and display all htpp methods
#!/bin/bash

URL=$1
curl -sI -X OPTIONS "$URL" | grep -i '^allow:' | awk '{print $2}'
