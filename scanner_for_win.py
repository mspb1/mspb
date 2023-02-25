import os
import json
import argparse
import requests
import socket
""" ввод аргументов"""
# Пример команды запуска под windows:py scanner_for_win.py -i 77.222.40.29 -n 3 scan
parser = argparse.ArgumentParser(description='Network scanner')
parser.add_argument('task', choices=['scan', 'sendhttp'], default='scan', help='Network scan or send HTTP request')
parser.add_argument(
    '-i',  # краткая форма аргумента
     '--ip', # полное имя аргумента
     type=str,
     default='192.168.2.1', # значение по умолчанию, если не передан аргумент
     help='IP address'
 )
parser.add_argument('-n', '--num_of_hosts', type=int, help='кол-во хостов')
parser.add_argument('-t', '--target', type=str, help='Выбрать домен.Target')
parser.add_argument('-m', '--method', choices=['GET', 'POST'], type=str, help='Method (GET|POST)')
parser.add_argument('-hd', '--headers', type=str, help='Headers (name1:value1 name2:value2 ...)')
args = parser.parse_args()
# Для тестирования без ввода аргументов
# task = 'scan'
# ip = '77.222.40.29'
# num_of_hosts = 3
""" функция сканер ip """
def do_ping_sweep(ip, num_of_host):
    ip_parts = ip.split('.')
    network_ip = ip_parts[0] + '.' + ip_parts[1] + '.' + ip_parts[2] + '.'
    scanned_ip = network_ip + str(int(ip_parts[3]) + num_of_host)
    response = os.popen(f'ping -n 1 {scanned_ip}')
    #response = os.popen(f'ping -n -c 1 {scanned_ip}') # Под линукс
    res = response.readlines()
    if "TTL" in res[2]:
        ip_ok.append(scanned_ip)
       #print(f"[#] Result of scanning: {scanned_ip} [#]\n{res[2]}", end='\n')" # Под Линукс
        print(f"[#] Result of scanning: {scanned_ip} [#]\n{res[2].encode('cp1251').decode('cp866')}", end='\n') #Под Windows

""" функция запроса к домену"""
def sent_http_request(target, method, headers=None, payload=None):
    headers_dict = dict()
    if headers:
        for header in headers:
            header_name = header.split(":")[0]
            header_value = header.split(":")[1:]
            headers_dict[header_name] = ":".join(header_value)

    if method == "GET":
        response = requests.get(target, headers=headers_dict)
    elif method == "POST":
        response = requests.post(target, headers=headers_dict, data=payload)
    print(
        f"[#] Response status code: {response.status_code}\n"
        f"[#] Response headers: {json.dumps(dict(response.headers), indent=4, sort_keys=True)}\n"
        f"[#] Response content:\n {response.text}"
    )

"""Сканер портов"""
def port_scanner(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        return True
    except:
        return False

"""выбор режима работ сканера """
ip_ok = []
payload = ""
if args.task == 'scan':
    for host_num in range(args.num_of_hosts):
        do_ping_sweep(args.ip, host_num)
else:args.task == 'sendhttp'
#    target = str(input("Выбрать домен.Target:"))
#    method = str(input("Method (GET|POST):"))
#    headers = list(input("Headers (name1:value1 name2:value2 ...)").split())
headers = args.headers
payload = ""
#if args.method == "POST":
        #payload = str(input("Payload:"))
sent_http_request(args.target, args.method, headers, payload)
#elif  sent_http_request(args.target, args.method, args.headers):

print("Список ответивших хостов:\n", ip_ok) # Список ответивших ip

""" выбор портов  и хостов для сканирования"""
if input("Просканировать порты обнаруженных хостов - ""1"". Ввести новый хост вручную -""2"" : ") == "1":
    host = ip_ok
else:
    host = input("Enter the host to be scanned: ").split()
    ip_ok = host
port_start = int(input("Enter start of the port range: "))
port_end = int(input("Enter end of the port range: "))
open_ports = []
for host in ip_ok:
    print(host)
    for port in range(port_start, port_end+1):
        if port_scanner(host, port):
            open_ports.append(port)
    if open_ports:
        print("Open ports:", open_ports)
        open_ports = []
    else:
        print("No open ports found.")

