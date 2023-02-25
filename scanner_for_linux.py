import os
import json
import argparse
import requests
import socket
# Пример команды запуска:python3 scanner_for_linux.py -i 192.168.2.1 -n 3 scan

""" функция сканер ip """
def do_ping_sweep(ip, num_of_host):
    ip_parts = ip.split('.')
    network_ip = ip_parts[0] + '.' + ip_parts[1] + '.' + ip_parts[2] + '.'
    scanned_ip = str(network_ip + str(int(ip_parts[3]) + num_of_host))
    response = os.popen(f'ping -c 1 {scanned_ip}')
    res = response.readlines()
    #if "ttl" in res[2]:
    #    ip_ok.append(scanned_ip) # all ip good
    print(f"[#] Result of scanning: {scanned_ip} [#]\n{res[1]}", end='\n')# Для Линукса

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

""" ввод аргументов"""
parser = argparse.ArgumentParser(description='Network scanner')
parser.add_argument('task', choices=['scan', 'sendhttp'], type=str, default='scan', help='Network scan or send HTTP request')
parser.add_argument(
    '-i',  # краткая форма аргумента
    '--ip', # полное имя аргумента
    type=str,
    default='192.168.2.1', # значение по умолчанию, если не передан аргумент
    help='IP address'
 )
parser.add_argument('-n', '--num_of_hosts', type=int, help='кол-во хостов')
args = parser.parse_args()
# args.task = 'scan'
# args.num_of_hosts = 2
# args.ip = '192.168.2.1'
# num_of_hosts = 1
ip_ok = []
if args.task == 'scan':
    for host_num in range(args.num_of_hosts):
        do_ping_sweep(args.ip, host_num)
elif args.task == 'sendhttp':
#    target = str(input("Target:"))
#    method = str(input("Method (GET|POST):"))
#    headers = list(input("Headers (name1:value1 name2:value2 ...)").split())
    if method == "POST":
        payload = str(input("Payload:"))
    sent_http_request(target, method, headers, payload)
print("Список ответивших хостов:\n", ip_ok)

"""хост и диапазон портов"""
if input("Просканировать порты обнаруженных хостов - ""1"". Ввести новый хост вручную -""2"" : ") == "1":
    host = ip_ok
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