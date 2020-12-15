import core as ec #mengimport module Echo
import time

"""
ini adalah suatu program chat bot sederhana
ECHO BOT akan merespon inputan yang anda masukkan

#just for fun :D
"""
print("welcome to Simple ECHO_BOT")
print("Type \"help\" or \"info\" for more information.\n")
#temp = ""
def read_file(filename):
  file = open(filename  , "r")
  content = file.read()
  print(content)
  file.close

#ini untuk perulanganya 
#this is looping
#def main(): 
while True:
  pesan = str(input('You : '))

    #temp = pesan
    #ec.temp_msg(temp)
    #print(temp)
  ec.send_message(pesan)
  if 'bye' in pesan:
    time.sleep(0.5)
    exit()
    break
  elif 'info' in pesan:
    read_file("INFO.txt")
    print("\n")
    #if 'info' in pesan:
    # read_file("README.txt")
    
#print(temp)
#main()