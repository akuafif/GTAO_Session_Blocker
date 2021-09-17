import socket
from GTAIP import GTAIP
from scapy.all import sniff,IP
from datetime import datetime
from threading import Thread

class SnifferThread(Thread):
    def __init__(self):
       # Call the Thread class's init function
        Thread.__init__(self)
        self.ipDictionary = {}

    def pc(self, packet):
        if packet.proto == 17:
            udp = packet.payload

    def stop(self):
        self.keeprunning = False

    def getlocalIPAddress(self) -> str:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip

    def clearIPDictionary(self):
        self.ipDictionary = {}
    
    def getIPDictionary(self):
        return self.ipDictionary
        
    def run(self) -> None:
        print('Sniffer thread spawned')

        self.keeprunning = True
        self.ipDictionary = {}
        localIP = self.getlocalIPAddress()
        while True:
            # Checks for 6672 
            packet = sniff(filter="udp and port 6672", prn=self.pc, store=1, count=1) 
            dest = packet[0][IP].dst
            if dest == localIP: 
                pass
            else:
                if not dest in self.ipDictionary.keys():
                        self.ipDictionary[dest] = GTAIP(dest)
                else:
                    self.ipDictionary[dest]._lastseen = datetime.now()