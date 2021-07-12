import re
spp = "/home/venkatesh/Synergy_Custom_SPP_2021.02.01_Z7550-97110.iso"
spp_sub = re.sub(r'\.(\d)', r'_\1', spp)
print(spp_sub)