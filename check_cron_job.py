#!/usr/bin/env python3

import re
import sys

print("--- Program starting up ---\n")

try:
    logfile = sys.argv[1]
except:
    print("Invalid expression. Please key in file name after calling program. Example: ./check_cron_job.py syslog")

pattern = r"USER \((\w+)\)$"

with open(logfile) as f:
    for line in f:

        if "CRON" not in line:
            continue
        
        result = re.search(pattern, line)
        print(result[1])

print("\n--- Program exiting ---")