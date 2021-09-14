from dataclasses import dataclass
from datetime import datetime

@dataclass
class GTAIP:
    ipaddress : str
    firstseen : datetime
    lastseen : datetime
    country : str
    region : str
    city : str