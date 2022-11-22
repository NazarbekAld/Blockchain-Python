import socket
import threading
import os
import pickle

from Crypto.PublicKey import RSA
from blockchain.node import Node
from blockchain.utils.HashMaps import HashMap

import json

"""
    Shhh! Keep it secret.
"""
if not (os.path.exists("public.pem") and os.path.exists("private.pem")):
    print("No keys exist on this directory. Generating new one...")
    KEY = RSA.generate(1028)
    with open("private.pem", "w") as file:
        file.write(KEY.export_key().decode())
    with open("public.pem", "w") as file:
        file.write(KEY.public_key().export_key().decode())
    

"""
    CREATING SERVER.
"""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

"""
    Amount of users connected on this server:
"""
Users : list[Node] = []
"""
    Tools for sending packets.
"""

# Safe connection:
RequirePubKey = { 'message': 'givepubkey' }



def Connect(ip="127.0.0.1", port=2212):
    print(("IP: " + ip), ("Port: " + str(port)), "Binding your sock...", sep="\n")
    """
        Binding
    """
    s.bind((ip, port))
    s.listen()
def gettingSocks():
    """
        Connection trigger.
    """
    print("Getting users...")
    while True:
        for i in Users:
            i.start()
        c, addr = s.accept()
        print ('Got connection from', addr)
        c.send(json.JSONEncoder().encode(RequirePubKey).encode('utf-8'))
        Users.append(Node(c, addr))

if __name__ == '__main__':
    Threads = HashMap()
    Connect(port=6969)
    Threads.put("gettingSocks", threading.Thread(target=gettingSocks))
    Threads.get("gettingSocks").start()