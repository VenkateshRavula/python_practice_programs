import os
'''
filename = str(input("Enter file name: "))

if os.path.exists(os.path.join("..",filename)):
  print("file {} exists".format(filename))
else:
  print("file {} doesnot exists.. creating that file".format(filename))
  f = open(os.path.join("..",filename), 'w')
  f.close()
'''

print(os.path.join(os.path.dirname(__file__), '../test.txt'))