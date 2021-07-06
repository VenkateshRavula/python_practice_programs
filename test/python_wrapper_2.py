# from subprocess import call
from subprocess import PIPE, run

failed_files = []

f = open("log.txt", "a+")

for file in range(1,11):
  try:
    command = ["python", "table_cmd_args.py", str(file)]
    result = run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True)
  finally:
    f.write(result.stdout)