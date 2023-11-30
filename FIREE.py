import os, platform
 
try:
 
        import requests
 
except:
 
        os.system('pip2 install requests')
 
 
 
import requests
 
bit = platform.architecture()[0]
 
if bit == "64bit":
 
        from X64_NUM import _xnxx_
 
        _xnxx_()
 
 
 
elif bit == "32bit":
 
        from X32_NUM import _xnxx_
 
 
        _xnxx_()
 

