import datetime
import asyncio
import requests
import socket

def getAPIreq(url, port):
    # connSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # connSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    # connSocket.bind('localhost',port)
    # req = socket.sendTo(socket.gethostbyname())
    req = requests.get(url)
    return req
                        
