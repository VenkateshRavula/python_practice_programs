import os

def find(file_name):
  print(">>> Searching for the file {}".format(file_name))
  count = 0
  for (r,d,f) in os.walk('c:\\'):
    if file_name in f:
	  print("file {} found in {}".format(file_name, r))
	  count += 1
  print("we found total {} matches for {}".format(count, file_name))
  print("Finish")
  return 1

try:
  file_name = input("Enter file name : ")
  k=find(file_name)
except Exception as e:
  print("error")