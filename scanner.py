import socket
import threading
import concurrent.futures
import colorama 
from colorama import Fore
import time
import os
colorama.init()

print_lock = threading.Lock()

os.system('cls')

ip = input('Enter The Ip/Url To Scan: ')

def scan(ip, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)
    try:
        scanner.connect((ip, port))
        scanner.close()
        with print_lock:
            print(Fore.RED + f'[{port}]' + Fore.GREEN + ' Open')
    except:
        pass

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    for port in range(1000):
        executor.submit(scan, ip, port + 1)

print(Fore.BLUE + f'Please Press CTRL+C to exits! Done Scanning Script Make By Mr Noobking : {ip}')
time.sleep(5000)