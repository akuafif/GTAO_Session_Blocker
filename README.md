# GTAO Session Blocker
My first python project with multithreading and subprocess with GUI tkinter.
I had enough of grievers in game!

This program writes, edits and deletes its own Windows Firewall rule, which will prompt for admin rights upon running the program.
This program does not touch, hack, inject, edit nor modify any GTA 5 files. 

### Features
* Play Grand Theft Auto Online with friends only, in private or public lobby
* Detects IP addresses in current session, with more details (lastseen, location)
* Whitelist IP addresses and creates a new firewall rule
* Auto saves/load and leave notes for whitelist IP list

### Installation
1. Download and install [npcap driver](https://nmap.org/npcap/) for packet sniffing
2. Download [the latest .zip file](https://github.com/fscene8/GTAO_Session_Blocker/releases) from the release page
3. Extract the folder inside the zip file to any directory (such as Desktop or Documents)

### How to use?
1. Run GTA Online
2. Run `GTAO_Session_Blocker.exe` from the extracted zip file
3. Load into any session, then suspend GTA5 process to be alone and be the session host
4. Invite your friends over to your session (skip to step 6 if you're playing alone)
5. Whitelist their IP address (right click the table below to add)
6. Turn on the firewall (only whitelist will stay in your session)
7. When the firewall is on, you need to turn off the firewall if your friend disconnected and needs to rejoin your session

### Screenshot
![screenshot](https://cdn.discordapp.com/attachments/489078888648015892/889070243178229770/Capture.PNG)

![screenshot](https://cdn.discordapp.com/attachments/489078888648015892/889070517917737001/Capture.PNG)

### Issue and Workaround
| Issue | Workaround |
|-------------|------------------------------------------|
| The game kicked me or everyone left the lobby<br> when I turned this on!  | This program will not work unless you are the host<br>Check the `Help > How-To` to identify yourself as session host |
| The game kicked me into single player<br>after a mission/heist instance | Can be avoided if the firewall is disabled before the game loads<br>you into a public session |
| Keep getting game save error<br>`Saving failed - Unable to connect to the rockstar game services` | Turn off the firewall and find new session<br>Wait for a few minutes and your game will be saved |
| My friend can't join my session when my firewall is on | Turn off the firewall<br>Invite your friend over and whitelist his IP<br>Turn on the firewall |

# For Development 

### Python
- Version 3.8.6

### IDE
- MS Visual Studio Code

### Driver
| Driver | Description |
|----|---|
| [npcap](https://nmap.org/npcap/) | Packet sniffing |

### Module

| Module | Description |
|-------------|------------------------------------------|
| [tksheet](https://github.com/ragardner/tksheet) | Table widget for displaying tabular data |
| [scapy](https://github.com/secdev/scapy) | Packet manipulation |
| [ip2geotools](https://github.com/tomas-net/ip2geotools) | Geolocation information IP address |
| [psutil](https://github.com/giampaolo/psutil) | Process and system monitoring in Python |

### Thanks
* @abdulmudhir for sharing [firewall.py](https://github.com/AbdulMudhir/GTA_V_Firewall_Public_Online/blob/master/firewall.py), which made this project possible
