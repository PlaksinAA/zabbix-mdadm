# ------------------------------------------------
# Program by Plaksin Andrei.
# Version      Date        Info
# 1.0          2019    Initial Version
# ------------------------------------------------

#!/usr/bin/python3
"""
\d   = Any Digit 0-9
\D   = Any non DIGIT
\w   = Any Alphabet symbol  [A-Z a-z]
\W   = Any non Alphabet symbol
\s   = breakspace
\S   = non breakspace
[0-9]{3}
[A-Z][a-z]+
"""
import re
import json
import sys
import subprocess

data = {
	'{#DISK}': '',
	'{#RAID}': ''
}

all_data = []
regex = r"(md\d+).+\n.+\[(.+)\]"
status = subprocess.run(["cat", "/proc/mdstat"], stdout=subprocess.PIPE).stdout.decode('utf-8')

matches = re.finditer(regex, str(status), re.MULTILINE)

for matchNum, match in enumerate(matches, start=1):
	all_data.append(data.copy())

	for groupNum in range(0, len(match.groups())):
		groupNum = groupNum + 1
		if groupNum % 2 != 0:
			all_data[matchNum-1]['{#DISK}'] = match.group(groupNum)
		else:
			all_data[matchNum-1]['{#RAID}'] = match.group(groupNum)

x = len(sys.argv)
if x > 1:

	for i in range(0, len(all_data)):

		if all_data[i]['{#DISK}'] == sys.argv[1]:
			print(all_data[i]['{#RAID}'])
	sys.exit()

all_data = json.dumps(all_data)
print("{\"data\":" + all_data +"}")
