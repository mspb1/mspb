import os
import json
import argparse
import requests

# """ функция сканер ip """
# def do_ping_sweep(ip, num_of_host):
#     ip_parts = ip.split('.')
#     network_ip = ip_parts[0] + '.' + ip_parts[1] + '.' + ip_parts[2] + '.'
#     scanned_ip = network_ip + str(int(ip_parts[3]) + num_of_host)
#     response = os.popen(f'ping -n 1 {scanned_ip}')
#     res = response.readlines()
#     print(f"[#] Result of scanning: {scanned_ip} [#]\n{res[2]}", end='\n\n')

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

# response = requests.get("https://vkkuhni.ru")
# headers = response.headers
# print("headers", "---"*50)
# print(headers["content-type"])
# print("status_code", "---"*50)
# print(response.status_code)
# print("response.text", "---"*50)
# print(response.text)
# """ ввод аргументов из cmd"""
# parser = argparse.ArgumentParser(description='Network scanner')
# parser.add_argument('task', choices=['scan', 'sendhttp'], default='scan', help='Network scan or send HTTP request')
# parser.add_argument(
#     '-i',  # краткая форма аргумента
#     '--ip', # полное имя аргумента
#     type=str,
#     default='192.168.2.1', # значение по умолчанию, если не передан аргумент
#     help='IP address'
# )
# parser.add_argument('-n', '--num_of_hosts', type=int, help='Number of hosts')
# args = parser.parse_args()
task = 'sendhttp'
if task == 'scan':
    for host_num in range(args.num_of_hosts):
        do_ping_sweep(args.ip, host_num)

elif task == 'sendhttp':
    target = str(input("Target:"))
    method = str(input("Method (GET|POST):"))
    headers = list(input("Headers (name1:value1 name2:value2 ...)").split())
    if method == "POST":
        payload = str(input("Payload:"))
        sent_http_request(target, method, headers, payload)



