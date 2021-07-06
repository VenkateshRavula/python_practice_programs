import re
textfile = open("input_file.txt", 'r')
for line in textfile.readlines():
    capture = re.search(r'^a\w{3}s$', line)
    if capture:
        print(capture.group(0))
textfile.close()