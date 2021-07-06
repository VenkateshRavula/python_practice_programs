import os, platform
host = "15.212.164.17"
out = os.system("ping " + ("-n 3 " if  platform.system().lower()=="windows" else "-c 3 ") + host)
print(out)