import paramiko
import subprocess
import os, platform
host = input("Enter the host ip : ")
out = ''
try:
  out = os.system("ping " + ("-n 1 " if  platform.system().lower()=="windows" else "-c 1 ") + host)
except:
  raise Exception("An exception occured")
finally:
  if out != 0:
    raise Exception("host is not reachable")
  else:
    print("Host is Reachable")
	

ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=host, username='root', password='123iso*help')

sftp = ssh.open_sftp()
sftp.chdir('/root/')
sftp.mkdir('IO_scripts')
sftp.chdir('/root/IO_scripts/')

sftp.put('C:\\Users\\ravulav\\Documents\\Python_programs\\IO_scripts\\cycleload.sh', 'cycleload.sh')
sftp.put('C:\\Users\\ravulav\\Documents\\Python_programs\\IO_scripts\\krs.py', 'krs.py')

ssh.exec_command('chmod +x /root/IO_scripts/krs.py /root/IO_scripts/cycleload.sh')
ssh.exec_command('nohup ./IO_scripts/cycleload.sh &')

stdin, stdout, stderr = ssh.exec_command('tail -10 /tmp/cycleload.log')
print(stdout.readlines())

sftp.close()
ssh.close()