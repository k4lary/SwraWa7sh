import requests
import random 
import os 
import sys 
import time



def instalost():
              os.system("clear")
namee=open("user.txt","r").readlines()
for x in namee:

  time.sleep(1)

  u=x.strip()

  re =requests.get('https://www.instagram.com/{}/'.format(u)).status_code

  if re==200:

   print("")

   print(u+ " >= \033[1;31mHAYA\033[1;37m")

  else:

   print("")

   print(u+ " >= \033[1;32mNYA\033[1;37m")
   
def tiktokswra():
              os.system("clear")
namee=open("user.txt","r").readlines()
for x in namee:

  time.sleep(1)

  u=x.strip()

  re =requests.get('https://www.tiktok.com/{}/'.format(u)).status_code

  if re==200:

   print("")

   print(u+ " >= \033[1;31mHAYA\033[1;37m")

  else:

   print("")

   print(u+ " >= \033[1;32mNYA\033[1;37m")
   
def facebookswra):
               os.system("clear")
namee=open("user.txt","r").readlines()
for x in namee:

  time.sleep(1)

  u=x.strip()

  re =requests.get('https://www.facebook.com/{}/'.format(u)).status_code

  if re==200:

   print("")

   print(u+ " >= \033[1;31mHAYA\033[1;37m")

  else:

   print("")

   print(u+ " >= \033[1;32mNYA\033[1;37m")
   
def snapchatswra():
                os.system("clear")
namee=open("user.txt","r").readlines()
for x in namee:

  time.sleep(1)

  u=x.strip()

  re =requests.get('https://www.snapchat.com/{}/'.format(u)).status_code

  if re==200:

   print("")

   print(u+ " >= \033[1;31mHAYA\033[1;37m")

  else:

   print("")

   print(u+ " >= \033[1;32mNYA\033[1;37m")

def telegramswra():
                os.system("clear")
namee=open("user.txt","r").readlines()
for x in namee:

  time.sleep(1)

  u=x.strip()

  re =requests.get('https://t.me/{}/'.format(u)).status_code

  if re==200:

   print("")

   print(u+ " >= \033[1;31mHAYA\033[1;37m")

  else:

   print("")

   print(u+ " >= \033[1;32mNYA\033[1;37m")
   
def userswra():
              os.system("clear")
filer=open("user.txt","w")

print("==================")

print("")

user=int(input("Chand Pet be :"))

for x in range(300):

            text="qwertyuioplkjhgfdsazxcvbnm1234567i90-_."

            word=''.join(random.choice(text) for x in range(user))

            filer.write(word+"\n")

  

print(word)

time.sleep(3)

print("")

print("----------")

print("")

print("ALL USER SAVED IN FILE USER.TXT")

time.sleep(3)
 
def menu():
                  os.system("clear")
                  print ("by - SwraWa7shsoftware")
                  print (" 《1》henane username")
                  print ("---------------------------------------")
                  print (" 《2》fa7s krdni user insta")
                  print ("---------------------------------------")
                  print (" 《3》fa7s krdni user tik tok")
                  print ("---------------------------------------")
                  print (" 《4》fa7s krdni user snap chat")
                  print ("---------------------------------------")
                  print (" 《5》fa7s krdni user facebook")
                  print ("---------------------------------------")
                  print (" 《6》fa7s krdni user telegram")
                  print ("---------------------------------------")
                  swra=int(input(" Choice : "))
                  if lost==1:
                                 os.system("clear")
                                 userswra()
                                 
                  if swra==2:
                                 os.system("clear")
                                 instaswra()
                                 
                  if swra==3:
                                 os.system("clear")
                                 tiktokswra()
                             
                  if swra==4:
                                 os.system("clear")
                                 snapchatswra()
                            
                  if swra==5:
                                 os.system("clear")
                                 facebookswra()
                            
                  if swra==6:
                                 os.system("clear")
                                 telegramswra()
                                 
                                 
                                 
menu()