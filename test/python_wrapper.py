from subprocess import call

for i in range(20):
  call("python table_cmd_args.py " + str(i))
