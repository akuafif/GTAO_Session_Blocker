import psutil, ctypes, sys, os, atexit
from MainWindow import *

def kill_proc_tree():
    try: 
        pid = os.getpid() 

        firewall.delete_firewall_rule()
        parent = psutil.Process(pid)
        
        print('cleanup done')
        parent.kill()
    
    except:
        print("Something really went wrong")

def is_admin():
    try: return ctypes.windll.shell32.IsUserAnAdmin()
    except: return False

def main():
    if is_admin():
        os.chdir(os.path.dirname(sys.argv[0]))
        app = MainWindow()
        app.mainloop()
        atexit.register(kill_proc_tree())
    else:
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)

if __name__ == "__main__":
    main()  