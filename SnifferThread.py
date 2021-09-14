import socket
from GTAIP import GTAIP
from scapy.all import *
from ip2geotools.databases.noncommercial import DbIpCity
from datetime import datetime

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
            packet = sniff(filter="udp and port 6672", prn=self.pc, store=1, count=1) # GTA V Online UDP default Port is 6672
            #y = x[0][IP].src
            dest = packet[0][IP].dst
            if dest == localIP: 
                pass
            else:
                if not dest in self.ipDictionary.keys():
                    try:
                        self.ipDictionary[dest] = GTAIP(dest,datetime.now(), datetime.now(), DbIpCity.get(dest, api_key='free').country, DbIpCity.get(dest, api_key='free').region, DbIpCity.get(dest, api_key='free').city)
                    except:
                        self.ipDictionary[dest] = GTAIP(dest,datetime.now(), datetime.now(), DbIpCity.get(dest, api_key='free').country, "Spoof", "IP")
                else:
                    self.ipDictionary[dest].lastseen = datetime.now()