import re
filename = "logical_interconnect.rb"
def file_rewrite(filename):
    file_lines = open(filename).readlines()
    fw = open("test212.txt", 'w')
    for line in file_lines:
        if re.match("\s+class", line.strip("\n")):
            fw.write(line)
            break
        else:
            fw.write(line)
    fw.writelines(file_lines[-4:])
    fw.close()

file_rewrite(filename)