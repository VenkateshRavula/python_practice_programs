import os
import shutil

for i in os.listdir(".."):
  if os.path.isdir(os.path.join("..",i)):
    print("{}".format(os.path.join("..",i)))
#    print("{} is a directory".format(i))
#  elif os.path.isfile(os.path.join("..",i)):
#    print("{} is a file".format(i))
#  else:
#    print(">>>>>>>>>>>>>>>>>>>>>>")

'''

  if os.path.isdir(i):
    print("{} is directory".format(i))
  else:
	print("{} is file".format(i))




if __name__ == "__main__":
  print("Present directory -> \"{}\"".format(os.getcwd()))
  out = []
  for (root, dirs, files) in os.walk("../GameOfThrones"):
    out.extend(files)
  print(out)

'''