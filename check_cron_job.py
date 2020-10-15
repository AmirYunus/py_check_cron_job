#!/usr/bin/env python3

import re
import sys

print("--- Program starting up ---\n")

try:
    logfile = sys.argv[1]
except:
    print("Invalid expression. Please key in file name after calling program. Example: ./check_cron_job.py syslog")

pattern = r"USER \((\w+)\)$"
username_dict = {}

with open(logfile) as f:
    for line in f:

        if "CRON" not in line:
            continue
        
        result = re.search(pattern, line)

        if result is None:
            continue

        name = result[1]
        username_dict[name] = username_dict.get(name, 0) + 1

print(username_dict)

print("\n--- Program exiting ---")