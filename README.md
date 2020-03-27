
# 1. Raspberry pi OS update & upgrade 
   
  
        pi@raspberrypi:~ $ sudo apt-get update	
        pi@raspberrypi:~ $ sudo apt-get upgrade
        Do you want to continue? [Y/n]  y
        
        
 # 2. apt  install
 
 
        pi@raspberrypi:~ $ sudo apt-get install libxml2-dev libxmlsec1-dev libffi-dev
        Do you want to continue? [Y/n]  y 
        
        
#  3. pip install 


        pi@raspberrypi: ~ $ sudo pip3 install cryptography
        Looking in indexes: https://pypi.org/simple, https://www.piwheels.org/simple
        Requirement already satisfied: cryptography in /usr/lib/python3/dist-packages (2.6.1) 

        pi@raspberrypi: ~ $ sudo pip3 install freeopcua 
        Installing collected packages: pytz, opcua, freeopcua
        Successfully installed freeopcua-0.90.6 opcua-0.98.9 pytz-2019.3
        
