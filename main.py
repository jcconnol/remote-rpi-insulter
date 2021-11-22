# This script is based on the following script: https://github.com/akkana/scripts/blob/master/rpi/pyirw.py
# It opens a socket connection to the lirc daemon and parses the commands that the daemon receives
# It then checks whether a specific command was received and generates output accordingly

import socket
import json
from playsound import playsound

SOCKPATH = "/var/run/lirc/lircd"

sock = None

# Establish a socket connection to the lirc daemon
def init_irw():
    global sock
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    sock.connect(SOCKPATH)
    print ('Socket connection established!')
    print ('Ready...')

# parse the output from the daemon socket
def getKey():
    while True:
        data = sock.recv(128)
        data = data.strip()

        if (len(data) > 0):
            break

    words = data.split()
    return words[2], words[1]

if __name__ == '__main__':
    try:
        init_irw()
        with open('data.json', 'r') as dataJSON:
            data=dataJSON.read()
            
        dataJSON = json.loads(data)
        
        while True:
            key, dir = getKey()
            key = key.decode() # This variable contains the name of the key
            dir = dir.decode() # This variable contains the direction (pressed/released)
            # Only print the name when the key is pressed (and not released)
            if (dir == '01'):
                if(key in dataJSON and dataJSON[key] != ''):
                    print(dataJSON[key])
                    playsound('audio.mp3')

                else:
                    print('button not found')
    except KeyboardInterrupt:
        print ("\nShutting down...")
        # Close the socket (if it exists)
        if (sock != None):
            sock.close()
        print ("Done!")
