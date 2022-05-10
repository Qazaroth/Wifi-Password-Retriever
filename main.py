import subprocess
import re

cmd = "netsh wlan show profile"

networks = subprocess.check_output(cmd, shell=True, universal_newlines="\n")
networkNamesList = re.findall("(?:Profile\s*:\s)(.*)", networks)

result = ""
for n in networkNamesList:
    cmd = "netsh wlan show profile " + n + " key=clear"
    curRes = subprocess.check_output(cmd, shell=True, universal_newlines="\n")
    password = re.findall("(?:Key Content\s*:\s)(.*)", curRes)
    if len(password) > 0:
        password = password[0]
    else:
        password = "N/A"

    curRes = "{} - {}\n".format(n, password)
    result = result + curRes

print(result)
