import init
import lib
import protocol

Initizaling = init.Init()
Initizaling.Start()
Protocol = protocol.Protocol()
Peers = lib.Peers()
User = lib.Listen_Commands()
Work_Mode = 0
Protocol_Version = 1

ip = lib.getIp()
peer = Peers.getOnlinePeer()

if peer != 'offline':
    Work_Mode = 1
    print('Online peer is ' + peer)
else:
    while True:
        peer = input('Input online peer that you know or type \'offline\' to work offline: ')
        if peer == 'offline':
            Work_Mode = 2
            break
        elif peer == 'exit':
            lib.initExit()
        else:
            peer = Peers.getOnlinePeer(peer)
            if peer != '':
                break

if Work_Mode == 1:
    print('You are online\nInput any commands to interact with PurpleCoin network')

while True:
    command = input('')
    User.DoCommands(User.GetCommands(command))

lib.initExit()
