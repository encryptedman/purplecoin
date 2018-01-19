import socket
import requests
import init
import sqlite3
import config
import sys
# import json
import os
import ipaddress

def checkIp(ip):
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        return False
    else:
        return True

def getIp():
    try:
        api = requests.get('https://api.ipify.org').text
        ip = format(api)
    except ConnectionError:
        print("Unavailable to get your ip by api")
        ip = socket.gethostbyname(socket.getfqdn())
    return ip

def checkExist(file):
    if not os.path.isfile(file):
        open(file, 'w+')

def initExit():
    quit = input("Press Enter to exit...")
    sys.exit(0)

def getOnlinePeer():
    Initizaling = init.Init()
    Initizaling.Start()

    peers_list_connect = sqlite3.connect(config.PEERS_LIST_FILE)
    peers_list_connect.row_factory = lambda cursor, row: row[0]
    peers_list_cursor = peers_list_connect.cursor()

    for ip in peers_list_cursor.execute('SELECT `ip` FROM `peers` ORDER BY `id` DESC'):
        if not checkIp(ip):
            continue
        print('Start - ' + ip)
        peer = socket.socket()
        peer.settimeout(2)
        try:
            peer.connect((ip, config.SERVER_PORT))
            print('Success - ' + ip)
            peers_list_connect.close()
            return ip
        except socket.error:
            print('Error - ' + ip)
            continue

    return 'offline'
