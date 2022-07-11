


#Modules:

from qrcode import make
from os import system
from time import sleep
import sys

#Colour_List

black="\033[1;30m"   
red="\033[1;91m"        
green="\033[1;92m"  
yellow="\033[1;93m"     
blue="\033[1;94m"      
purple="\033[1;95m"   
cyan="\033[1;96m"
end="\033[0m" 
#Login Access:

def login():
    access=True
    while access:
        logo()
        user=input(cyan+'username :'+green)
        if user == 'Yasin Arafat Ajad':
                print(end)
                system('clear')
                logo()
                pw=input(end+cyan+'password :'+green) 
                if pw == 'Tama Bangali':
                     system('clear')
                     logo()
                     print(end+purple+'Checking....'+end)  
                     sleep(3)
                     system('clear')
                     logo()
                     print(green+'Login Succesful..!!!',end)
                     sleep(2)
                     system('clear')
                     break
                
                if pw!='Tama Bangali':
                    system('clear')
                    logo()
                    print(end,purple,'Checking....',end)
                    sleep(2)
                    system('clear')
                    logo()
                    print(end,red,'Sorry!   Wrong Password..!!!',end) 
                    sleep(3)
                    system('clear')

        if user!='Yasin Arafat Ajad':
            print(end,red,'Sorry!   Wrong Username..!!!',end)
            sleep(3)
            system('clear')
            
                
#Logo :
def logo():
    Logo=f"""

{red}                  ██▀███   ██ ▄█▀▀
                 ▓██ ▒ ██▒ ██▄█▒ 
                 ▓██ ░▄█ ▒▓███▄░ 
              {end}{blue}   ▒██▀▀█▄  ▓██ █▄ 
                 ░██▓ ▒██▒▒██▒ █▄▄
              {end}{black}   ░ ▒▓ ░▒▓░▒ ▒▒ ▓▒
                   ░▒ ░ ▒░░ ░▒ ▒░
                   ░░   ░ ░ ░░ ░ 
                    ░     ░  ░   
                   {end}
{yellow}......................................................
.....................{end}{red}RAJ.KUMAR{end}{yellow}.......................
......................................................{end}
 {yellow}•••••••••{end}{cyan}[Created by:// RUPKOTHAR RAJKUMAR]{end}{yellow}•••••••••


{end}"""
    print(Logo)

#Information in QR Code
system('clear')
sleep(1)
login()
system('clear')
logo()
sleep(1)
information=input(yellow+'Give Informaion in QR Code : '+end+green) 
print(end)
system('clear') 
logo()
print(f'''{cyan}
    
              PROCESSING..{end}''') 
sleep(1)
system('clear')
logo()
print(f'''{blue}
    
              PROCESSING...{end}''')
sleep(1)
system('clear')
logo()
print(f'''{red}
    
              PROCESSING....{end}''')
sleep(3)
system('clear')

# QR Code Genarate:

def qr_genarate():
    
   qr= make(information)
   sleep(1)
   logo()
   sleep(1)
   qr_name=input(yellow+'Enter Your QR Name : '+end+green) 
   system('clear')
   print(end)
   logo()
   sleep(1)
   print(cyan+'              Please, Wait for some time......'+end)
   sleep(3)
   system('clear')
   logo()
   print(blue+'Loading .....'+end)
   sleep(1)
   system('clear')
   logo()
   print(yellow+'Loading .....'+end)
   sleep(1)
   system('clear')
   logo()
   print(purple+'Loading .....'+end)
   sleep(1)
   system('clear')
   logo()
   print(cyan+'Loading .....'+end)
   sleep(1)
   system('clear')
   logo()
   print(green+'Loading .....'+end)
   sleep(1)
   system('clear')
   qr.save(qr_name+'.png')
   


qr_genarate()
sleep(1)
logo()
sleep(1)
print(f'''       

        {purple}   ..........RESULT..........{end}''')
sleep(1)
print(f'''

{green}
              ...QR Code saved...{end}

      {blue}    YOUR QR CODE IS CREATED BY{end}
          {red}       "RAJKUMAR"{end}''')
 
sys.exit()
