import json
import socket
import threading

from Crypto.PublicKey import RSA
from Crypto.PublicKey.RSA import RsaKey

# Node

class Node(threading.Thread):
    def __init__ (self, socket : socket.socket, address):
        threading.Thread.__init__(self)
        self.__socks = socket
        self.__address = address
        self.__publickey : RsaKey = None
    def getConnection(self):
        return self.__socks
    def getAddress(self):
        return self.__address
    def setPublickey(self, key : RsaKey):
        self.__publickey = key
    def run(self):
        while True:
            packet = self.__socks.recv(3072).decode()
            packet : dict = json.JSONDecoder().decode(packet)
            if packet.get('message') == 'pubkey':
                self.__publickey = RSA.importKey(packet.get('key'))
            print(packet)