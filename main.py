import subprocess
import argparse
import tqdm
import time
mac = input ("введите мак адрес:08:00:27:22:46:4f -->")
print("Смена мак адреса", "---"*20, sep='\n')

parser = argparse.ArgumentParser()
parser.add_argument('-i', '--interfece', dest='inter_arg', help='выбор сетевого интерфейса(eth0):')
parser.add_argument('-m', '--macaddr', dest='mac_arg', default='08:00:27:22:46:4f', help='Выбор мас адреса(08:00:27:22:46:4f):')
args = parser.parse_args()

interface = args.inter_arg
mac = args.mac_arg
interface = 'eth0'
print("интерфейс сетевой карты -", interface, "Новый мак адрес -", mac)
print("---"*20)
# subprocess.call("ifconfig " +interface+ " down", shell=True)
# print("Stop interface -", interface)
# subprocess.call("ifconfig " +interface+ " hw ether " +mac, shell=True)
# print("Setup мак адрес -", mac)
#subprocess.call("ifconfig " + interface + " up", shell=True)
subprocess.call("ipconfig ", shell=True)
print("тест сайта -")
print("---" * 20)
args = ["ping", "www.ya.ru"]
process = subprocess.Popen(args, stdout=subprocess.PIPE)
data = process.communicate()
for line in data:
    print(line)

# ifconfig eth0 down
# ifconfig eth0 hw ether 08:00:27:22:46:4f
# ifconfig eth0 up