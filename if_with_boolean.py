auto_sh = True
sh_uri = True
sh_uri_exist = False

enc_name = False
enc_bay = False

if auto_sh and not sh_uri and not sh_uri_exist or auto_sh and not enc_name and not enc_bay:
    print("Will assign auto hardware")
else:
    print("Will not assign hardware")

