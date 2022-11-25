import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from SRK64_NUM import main
 
        main()
 
 
 
elif bit == "32bit":
 
        from SRK32_NUM import main
 
 
        main()
 

