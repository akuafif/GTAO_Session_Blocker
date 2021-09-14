# GTAO Session Blocker
My first python project with multithreading and subprocess with GUI tkinter.
I had enough of grievers in game!

### Features
* Play Grand Theft Auto Online with friends only.
* Detect other players IP in session, with more details (lastseen, location)
* Whitelist IP addresses and play with your friends without modder/hackers
* Auto saves and leave notes your whitelist IP list

### Installation
1. Install [npcap](https://nmap.org/npcap/) for packet sniffing
2. Run `GTAO_Session_Blocker.exe`

### How to use
1. Run GTA Online
2. Run `GTAO_Session_Blocker.exe`
3. Load to a session, suspend GTA5 process and be the session host
4. Invite your friend over to your session
5. Whitelist their IP (right click the table below)
6. Turn on firewall

# Requirements

### Drivers
| Driver | Description |
|----|---|
| [npcap](https://nmap.org/npcap/) | Packet sniffing |

### Modules

| Module | Description |
|-------------|------------------------------------------|
| [tksheet](https://github.com/ragardner/tksheet) | Table widget for displaying tabular data |
| [scapy](https://github.com/secdev/scapy) | Packet manipulation |
| [ip2geotools](https://github.com/tomas-net/ip2geotools) | Geolocation information IP address |
| [psutil](https://github.com/giampaolo/psutil) | Process and system monitoring in Python |

### Special Thanks
* @abdulmudhir for sharing [firewall.py](https://github.com/AbdulMudhir/GTA_V_Firewall_Public_Online/blob/master/firewall.py), which made this project possible