import sqlite3
import os
import config
import lib
import socket
import queue

class Init:
    # Creating clear tables
    def db_create_tables(self):
        # Data base connect
        blockchain_connect = sqlite3.connect(config.BLOCKCHAIN_FILE)
        peers_list_connect = sqlite3.connect(config.PEERS_LIST_FILE)

        blockchain_cursor = blockchain_connect.cursor()
        peers_list_cursor = peers_list_connect.cursor()

        # Creating tables
        peers_list_cursor.execute('''
            CREATE TABLE `peers` (
            	`id`	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            	`ip`	TEXT NOT NULL
            );
        ''')

        peers_list_cursor.execute('''
            CREATE TABLE `info` (
                `id` INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                `value` TEXT,
                `int` INTEGER
            );
        ''')

        peers_list_cursor.execute('''
            INSERT INTO `peers` VALUES(NULL, :ip);
        ''', {'ip': lib.getIp()})

        blockchain_cursor.execute('''
            CREATE TABLE `blockchain` (
            	`id`	INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
            	`version`	INTEGER NOT NULL,
            	`prev_block`	TEXT NOT NULL,
            	`merkle_root`	TEXT NOT NULL,
            	`timestamp`	INTEGER NOT NULL,
            	`bits`	INTEGER NOT NULL,
            	`nonce`	INTEGER NOT NULL,
            	`txn_count`	INTEGER NOT NULL,
            	`txns`	TEXT NOT NULL
            );
        ''')

        peers_list_connect.commit()
        blockchain_connect.commit()

        blockchain_connect.close()
        peers_list_connect.close()

    # Check data base exist
    def db_check_exist(self):
        if not os.path.isfile(config.BLOCKCHAIN_FILE):
            open(config.BLOCKCHAIN_FILE, 'w+')
        if not os.path.isfile(config.PEERS_LIST_FILE):
            open(config.PEERS_LIST_FILE, 'w+')

    def check_for_first_launch(self):
        self.db_check_exist()
        self.db_create_tables()

    def Start(self):
        if not os.path.isfile(config.BLOCKCHAIN_FILE):
            self.check_for_first_launch()
        self.db_check_exist()

    def __init__(self):
        pass

class p2p:
    p2p_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    p2p_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    connections = []

    def __init__(self):
        pass

    def Server_Start(self):
        self.p2p_server.bind(('0.0.0.0', config.SERVER_PORT))
        self.p2p_server.listen(1)

    def Start_Client(self):
        self.p2p_client.recv(8192)
