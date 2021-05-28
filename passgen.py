TYELLOW = '\033[33m'
TRED = '\033[31m'
TWHITEB='\033[41m'
print(TYELLOW+"PASSWORD GENERATOR"+" password generator "+" PASSWORD GENERATOR")
print(TRED+"MADE BY 'VIVEKPAL25' SEARCH ON GITHUB \n SUBSCIBE OUR CHANNEL  'HASH CRYPTING' ON YOUTUBE")
import random
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number="0123456789"
all=lower+upper+number
length=10
password="".join(random.sample(all,length))
TGREEN =  '\033[32m' # Green Text
TWHITE = '\033[37m'
print(TGREEN+"Your Password is: "+password)
print("\n")
ask=raw_input(TGREEN+"Do you want to save your password For backup:\n")

if ((ask=="yes" or ask == "Yes") or (ask == "YES" or ask == "y") or (ask == "Y")):
  print("\n")
  sino=raw_input(TGREEN+"Enter Name For Text File\n")
  rino=sino+".txt"
  f=open(rino,"w+")
  print("\n") 
  dino=raw_input(TWHITE+"This Password is For ????\n")
  f.write(dino+":"+password)
  f.close()
  print(TGREEN+"Your Password is Saved Check it out")
else:
  print(TGREEN+"OKAY YOUR Password is: "+password)
