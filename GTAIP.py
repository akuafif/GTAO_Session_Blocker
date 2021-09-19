
from datetime import datetime
from ip2geotools.databases.noncommercial import DbIpCity

class GTAIP:
    def __init__(self, ip) -> None:
        self.__ip = ip 
        self.__firstseen = datetime.now()
        self.__lastseen = datetime.now()
        self.__timeago = str(datetime.now() - self.__lastseen).split(".")[0]
        self.__packetsin = 1
        
        try:
            self.__country = DbIpCity.get(self.__ip, api_key='free').country
            self.__region = DbIpCity.get(self.__ip, api_key='free').region            
            self.__city = DbIpCity.get(self.__ip, api_key='free').city
        except:
            self.__country = "ZZ"
            self.__region = "Unable to retrieve"
            self.__city = "Unable to retrieve"
            pass
    
    @property
    def ip(self) -> str: return self.__ip
    @property 
    def firstseen(self) -> datetime: return self.__firstseen
    @property 
    def lastseen(self) -> datetime: return self.__lastseen
    @property 
    def timeago(self) -> str: return self.__timeago
    @property
    def packetsin(self) -> int: return self.__packetsin
    @property 
    def country(self) -> str: return self.__country
    @property 
    def region(self) -> str: return self.__region
    @property
    def city(self) -> str: return self.__city

    @lastseen.setter
    def lastseen(self, newtime):
        self.__lastseen = newtime
        self.__packetsin += 1