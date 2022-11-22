from Crypto.PublicKey import RSA
from Crypto.PublicKey.RSA import RsaKey

import threading
import pickle

import os
import socket as sock

import json

def getKey() -> RsaKey:
    if not (os.path.exists("public.pem") and os.path.exists("private.pem")):
        print("No keys exist on this directory. Generating new one...")
        KEY = RSA.generate(1028)
        with open("private.pem", "w") as file:
            file.write(KEY.export_key().decode())
        with open("public.pem", "w") as file:
            file.write(KEY.public_key().export_key().decode())
        return KEY
    KEY = None
    with open('private.pem', "r") as file:
        KEY = RSA.importKey(file.read())
    return KEY

socks = sock.socket(sock.AF_INET, sock.SOCK_STREAM)

def connect(ip="127.0.0.1", port=2212):
    socks.connect((ip, port))
def packet():
    while True:
        packet = socks.recv(4096).decode('utf-8')
        try:
            packet: dict = json.JSONDecoder().decode(packet)
        except Exception as e:
            print(e)

        if packet != None:
            print(packet)
            print(type(packet))

        if packet.get('message') == "givepubkey":
            socks.send(json.JSONEncoder().encode({"message": "pubkey", 'key': getKey().public_key().export_key().decode()}).encode('utf-8'))


if __name__ == '__main__':
    connect(port=6969)
    socksthread = threading.Thread(target=packet)
    socksthread.start()
    pass