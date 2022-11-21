import socket
import threading

from Crypto.PublicKey import RSA
from Crypto.PublicKey.RSA import RsaKey

# Node

class Node(threading.Thread):
    def __init__ (self, socket : socket.socket, address : tuple):
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
            self.__socks.recv(3072).decode('utf-8')