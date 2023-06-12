from math import pow

number = 32
hosts = 1
cidr = "/"
defaultSubnet = "0.0.0.0"
indexOfOctets = 0

ip_address = input("IP: ")
subnetmask = input("Subnet: ")

first_octet_ip = int(ip_address.split(".")[0])

def setDefaultSubnetMask():
    global subnetMenu
    subnetMenu = defaultSubnet.replace("0", "x", indexOfOctets).replace("x", "255", indexOfOctets - 1).center(30, "-")
    return subnetMenu

def countBinary(counter):
        counter1 = counter.count("1")
        counter0 = counter.count("0")
        subnetCount = pow(2, counter1)
        hostCount = pow(2, counter0) - 2

        countAllOnes = '.'.join(binary_ip)
        cidrRange = countAllOnes.count("1")

        return f"Subnets: {int(subnetCount):,}\nHosts: {int(hostCount):,}\n{ip_address}{cidr}{cidrRange}"

while number != 0:
    if number == 32 or number == 24 or number == 16 or number == 8:
        indexOfOctets += 1
        print("\n")
        print(setDefaultSubnetMask())
    print(f"{cidr}{number} : {int(hosts):,}")
    number -= 1
    hosts = hosts * 2
print("\n")

octets = subnetmask.split('.')
binary_ip = []
for octet in octets:
    binary_octet = bin(int(octet))[2:].zfill(8)
    binary_ip.append(binary_octet)

print(f"{subnetmask} : {'.'.join(binary_ip)}")

if 1 <= first_octet_ip <= 126:
    print(f"{ip_address}'s class is A")
    print(countBinary(counter='.'.join(binary_ip[1:])))
elif 128 <= first_octet_ip <= 191:
    print(f"{ip_address}'s class is B")
    print(countBinary(counter='.'.join(binary_ip[2:])))
elif 192 <= first_octet_ip <= 223:
    print(f"{ip_address}'s class is C")
    print(countBinary(counter='.'.join(binary_ip[-1])))
elif 224 <= first_octet_ip <= 239:
    print(f"{ip_address}'s class is D")
    print("There is no Subnet Mask")
elif 240 <= first_octet_ip <= 255:
    print(f"{ip_address}'s class is E")
    print("There is no Subnet Mask")
else:
    print("Invalid IP address")
