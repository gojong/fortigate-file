import re

# 메모장 파일의 경로를 가져옵니다.
input_file_path = "input.txt"
output_file_path = "output.txt"

# 메모장 파일을 읽습니다.
with open(input_file_path, "r") as f:
    lines = f.readlines()

# IP 주소와 서브넷 마스크를 찾습니다.
addresses = []
for line in lines:
    match = re.search(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2})|(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\s+\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", line)
    if match:
        addresses.append(match.group())

# Fortigate 주소를 만듭니다.
command = ""
for address in addresses:
    ip_subnet = address.split('/')
    if len(ip_subnet) == 2:
        ip = ip_subnet[0]
        subnet = ip_subnet[1]
    else:
        ip_subnet = address.split(' ')
        ip = ip_subnet[0]
        subnet = ip_subnet[1] if len(ip_subnet) > 1 else ""

    if subnet:
        command += """
config firewall address
    edit "{0}"
    set type ipmask
    set subnet {1}
    next
end
""".format(ip, address)

# 명령을 다른 메모장 파일에 씁니다.
with open(output_file_path, "w") as f:
    f.writelines(command)
