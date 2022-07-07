
#imports
import random
import socket
import time

#stage
print("\033c", end='')
list_of_ips = []
legit_list_of_ips = []
failed = 0
ips_to_generate = int(input("Enter number or ip`s to be generated: "))

#generate ip adress
for i in range(0, 5):
    a = str(random.randint(100, 255))
    b = str(random.randint(100, 255))
    c = str(random.randint(100, 255))
    d = str(random.randint(100, 255))
    
    ip = a + "." + b + "." + c + "." + d
    #add ips to list of ips
    list_of_ips.append(ip)
    #check te lenght of list
    len_list_of_ips = len(list_of_ips)

#loop trough generated ip`s
for e in range(0,len_list_of_ips):
  len_list_of_ips -= len_list_of_ips

  #check if ip`s are responsive
  try:
    socket.gethostbyaddr(str(list_of_ips[len_list_of_ips]))
    legit_list_of_ips.append(list_of_ips[len_list_of_ips])
  except socket.herror:
    failed += failed
    

#inform the user
if failed == len_list_of_ips:
  print("All generated ip`s were unresponsive!")
else:
  print("We have managed to generate a few active ip`s! Here is the list:")
  time.sleep(2.6969696969696969)
  print(legit_list_of_ips)
