import socket
import time
from GTAIP import GTAIP
from scapy.all import sniff,IP
from datetime import datetime
from threading import Thread

class SnifferThread(Thread):
    def __init__(self):
       # Call the Thread class's init function
        Thread.__init__(self)
        self._keepalive = True
        self._updatenew = True
        self.__ipDictionary = {}

    def pc(self, packet):
        if packet.proto == 17:
            udp = packet.payload

    def stop(self):
        self._keepalive = False

    def pause(self):
        self._updatenew = False
        print('Pause thread')

    def resume(self):
        self._updatenew = True
        print('Resume thread')

    def getlocalIPAddress(self) -> str:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip

    def clearIPDictionary(self):
        self.__ipDictionary = {}
    
    def getIPDictionary(self):
        return self.__ipDictionary
        
    def run(self) -> None:
        print('Sniffer thread spawned')

        self.__ipDictionary = {}
        localIP = self.getlocalIPAddress()
        while self._keepalive:
            time.sleep(1) 
            # Checks for 6672 
            packet = sniff(filter="udp and port 6672", prn=self.pc, store=1, count=1) 
            dest = packet[0][IP].dst
            if dest != localIP: 
                if self._updatenew:
                    if dest not in self.__ipDictionary.keys():
                            self.__ipDictionary[dest] = GTAIP(dest)
                    else:
                        (self.__ipDictionary[dest]).lastseen = datetime.now()
                else:
                    if dest in self.__ipDictionary.keys():
                        (self.__ipDictionary[dest]).lastseen = datetime.now()