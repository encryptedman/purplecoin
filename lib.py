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

# Classes

class Peers:
    def getOnlinePeer(self, peer=''):
        Initizaling = init.Init()
        Initizaling.Start()

        peers_list_connect = sqlite3.connect(config.PEERS_LIST_FILE)
        if peer == '':
            peers_list_connect.row_factory = lambda cursor, row: row[0]
            peers_list_cursor = peers_list_connect.cursor()

            for ip in peers_list_cursor.execute('SELECT `ip` FROM `peers` ORDER BY `id` DESC'):
                if not checkIp(ip):
                    continue
                print('Start - ' + ip)
                peer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                peer.settimeout(1)
                try:
                    peer.connect((ip, config.SERVER_PORT))
                    peers_list_connect.close()
                    print('Success - ' + ip)
                    return ip
                except socket.error:
                    print('Error - ' + ip)
                    continue

            return 'offline'
        else:
            peers_list_cursor = peers_list_connect.cursor()

            if not checkIp(peer):
                return 'Wrong peer\'s ip'
            print('Start - ' + peer)
            connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            connection.settimeout(1)
            try:
                connection.connect((peer, config.SERVER_PORT))
                peers_list_cursor.execute('''
                    INSERT INTO `peers` VALUES(NULL, :ip);
                ''', {'ip': peer})
                peers_list_connect.commit()
                peers_list_connect.close()
                print('Success - ' + peer)
                return peer
            except socket.error:
                print('Error - ' + peer)
                return 'offline'

class Listen_Commands:
    def GetCommands(self, command):
        commands = command.split(' ')
        for i in range(5):
            commands.append('')
        return commands

    def DoCommands(self, commands):
        if commands[0] == 'help' or commands[0] == 'Help' or commands[0] == 'HELP':
            print('\'Exit\' - Close the app')
        elif commands[0] == 'exit' or commands[0] == 'Exit' or commands[0] == 'EXIT' or commands[0] == 'quit' or commands[0] == 'Quit' or commands[0] == 'QUIT':
            initExit()
        elif commands[0] == '':
            print('Please input some command')
        else:
            print('Unknow command\nInput \'help\' to see all commands')
