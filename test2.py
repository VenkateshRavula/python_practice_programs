import re
ip = "This line contains ips192.168.10.12"

regex = "((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])$"

ip_pattern = "((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9]))$"
result = re.search(ip_pattern, ip)
if result:
    print(result.group(1))
else:
    print("invalid ip")

# a = 15
# b = 35
#
# a -= a-b
#
# b += a-b
# print(a,b)
