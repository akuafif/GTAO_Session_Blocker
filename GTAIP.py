
from datetime import datetime
from ip2geotools.databases.noncommercial import DbIpCity

class GTAIP:
    def __init__(self, ip) -> None:
        self.__ip = ip 
        self._firstseen = datetime.now()
        self._lastseen = datetime.now()
        self._timeago = str(datetime.now() - self._lastseen).split(".")[0]
        
        try:
            self._country = DbIpCity.get(self.__ip, api_key='free').country
            self._region = DbIpCity.get(self.__ip, api_key='free').region            
            self._city = DbIpCity.get(self.__ip, api_key='free').city
        except:
            self._country = "ZZ"
            self._region = "Unable to retrieve"
            self._city = "Unable to retrieve"
            pass
    
    @property
    def ip(self) -> str: return self.__ip
    @property 
    def firstseen(self) -> datetime: return self._firstseen
    @property 
    def lastseen(self) -> datetime: return self._lastseen
    @property 
    def timeago(self) -> str: return self._timeago
    @property 
    def country(self) -> str: return self._country
    @property 
    def region(self) -> str: return self._region
    @property
    def city(self) -> str: return self._city

    @lastseen.setter
    def updateLastseen(self, newtime):
        self._lastseen = newtime