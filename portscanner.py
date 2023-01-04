import os
from colorama import Fore
import time

green = Fore.LIGHTGREEN_EX
red = Fore.RED

print(Fore.MAGENTA + "'  ..____............_.....____..................................")
print(Fore.MAGENTA + "'  .|.._.\.___.._.__|.|_../.___|..___.__._._.__.._.__...___._.__.")
print(Fore.MAGENTA + "'  .|.|_)./._.\|.'__|.__|.\___.\./.__/._`.|.'_.\|.'_.\./._.\.'__|")
print(Fore.MAGENTA + "'  .|..__/.(_).|.|..|.|_...___).|.(_|.(_|.|.|.|.|.|.|.|..__/.|...")
print(Fore.MAGENTA + "'  .|_|...\___/|_|...\__|.|____/.\___\__,_|_|.|_|_|.|_|\___|_|...")
print(Fore.MAGENTA + "'  ..............................................................")                                       							
print(" ")
print("[1] Scan de Ping")
print("[2] Scan Básico")
print("[3] Scan de todos los TCP y 100 UDP")
print("[4] Detección de Os y Servicios")
print("[5] Detección de CVE")
print("[6] Script HTTP NMAP") 
print("[7| Salir")
print(" ")

option = int(input(f"{green}[+]Choose an option (1-7): "))
objetivo= str(input(f"{green} [+]Objetivo: "))
archivo= str(input(f"{green} [+]Donde se va a guardar el archivo ejemplo: /home/ "))

if option == 1:
    print(f"{red}")
    os.system(f"sudo nmap -sp -v {objetivo} -oA {archivo}")

elif option==2:
    ports = input(f"{green}[+]Puertos a utilizar ejemplo: 0-80:  ")
    print(f"{red}")
    os.system(f"sudo nmap -p {ports} -T5 -v -Pn {objetivo} -oA {archivo}")
    
elif option==3:
    print(f"{red}")
    os.system(f"sudo nmap  -v -Pn -sS -sU -sV -sC -p T:1-65535,U:7,9,17,19,49,53,67-69,80,88,111,120,123,135-139,158,161-162,177,427,443,445,497,500,514-515,518,520,593,623,626,631,996-999,1022-1023,1025-1030,1433-1434,1645-1646,1701,1718-1719,1812-1813,1900,2000,2048-2049,2222-2223,3283,3456,3703,4444,4500,5000,5060,5353,5632,9200,10000,17185,20031,30718,31337,32768-32769,32771,32815,33281,49152-49154,49156,49181-49182,49185-49186,49188,49190-49194,49200-49201,65024 {objetivo} -oA {archivo}")

elif option==4:
    ports = input(f"{green}[+]Puertos a utilizar ejemplo: 0-80: ")
    print(f"{red}")
    os.system(f"nmap -A -T4 -p {ports} -v -Pn {objetivo} -oA {archivo}")

elif option==5:
    ports = input(f"{green}[+]Puertos a utilizar ejemplo: 0-80: ")
    print(f"{red}")
    os.system(f"sudo nmap -v -Pn --script vuln -p {ports} {objetivo} -oA {archivo}")
    
elif option==6:
    ports = input(f"{green}[+]Puertos a utilizar ejemplo: 0-80: ")
    print(f"{red}")
    os.system(f"sudo nmap -v -Pn --script http-enum -p {ports} {objetivo} -oA {archivo}")
     
else:
    print("Adios...")
    time.sleep(2)
