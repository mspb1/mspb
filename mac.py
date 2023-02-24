import subprocess
import argparse
import tqdm
import time
import scapy.all as scapy
scapy.arping("192.168.2.0/24")
print("Смена мак адреса", "---"*20, sep='\n')
parser = argparse.ArgumentParser()
parser.add_argument('-i', '--interfece', dest='inter_arg', help='выбор сетевого интерфейса(eth0):')
parser.add_argument('-m', '--macaddr', dest='mac_arg', help='Выбор мас адреса(08:00:27:22:46:4f):')
args = parser.parse_args()
# interface = args.inter_arg
# mac = args.mac_arg
#interface = 'eth0'
mac = '08:00:27:22:46:44'
interface = input ("введите сетевой интерфейс eth0 -->")
if not (mac and interface):
    print("Вы неввели адрес карты")
    pass
print("интерфейс сетевой карты -", interface, "Новый мак адрес -", mac)
print("---"*20)
subprocess.call("ifconfig " +interface+ " down", shell=True)
if interface and mac:
    print("Не ввели параметр ")

print("Stop interface -", interface)
subprocess.call("ifconfig " +interface+ " hw ether " +mac, shell=True)
print("Setup мак адрес -", mac)
subprocess.call("ifconfig " + interface + " up", shell=True)
subprocess.call("ifconfig " +interface, shell=True)


# parser = argparse.ArgumentParser()
# parser.add_argument('-i', '--ip', dest='ip_arg', help='выбор ip:')
# # parser.add_argument('-m', '--macaddr', dest='mac_arg', help='Выбор мас адреса(08:00:27:22:46:4f):')
# args = parser.parse_args()
# ip = args.ip_arg
# ip = "192.168.2.172"
# arp_reg = scapy.ARP(pdst=ip)
# broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
# packet = broadcast/arp_reg
# print(packet.show())