import re
file_name = 'endpoints-support.md'

f = open(file_name, 'r')
for line in f.readlines():
    if re.search('^\|\s+Endpoints', line):

