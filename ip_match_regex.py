import re
ip_pattern = '^(((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))$'
ip = "10.1.19.222"

out = re.search(ip_pattern, ip)
if out:
    print(out.groups())
    print(out.group(4))
    print(out.group(1))
    print(out.group(2))
    print(out.group(3))