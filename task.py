## bucnh of task that echo bot can do ##

#running task function
def run(taskname):
    if taskname == 'wfnotes':
        return wfnotes()

    elif taskname == 'logout':
        return logout()

    elif taskname == 'lock_screen':
        return lock_screen()

    elif taskname == 'shutdown':
        return shutdown()

    elif taskname == 'alarm':
        alarm()

#wifinote task
def wfnotes():
    import subprocess
    data = subprocess.check_output(['netsh', 'wlan', 'show', 'profiles']).decode('utf-8', errors ="backslashreplace").split('\n')
    profiles = [i.split(":")[1][1:-1] for i in data if "All User Profile" in i]
    f = open("Your_WiFi_Note.txt", "w")

    for i in profiles:
        try:
            results = subprocess.check_output(['netsh', 'wlan', 'show', 'profile', i, 'key=clear']).decode('utf-8', errors="backslashreplace").split('\n')
            results = [b.split(":")[1][1:-1]for b in results if "Key Content" in b]
            try:
                hasil = "{:<30}| {:<}".format(i,results[0])
                f.write(hasil)
                f.write("\n")
                #print(hasil)
            except IndexError:
                hasil = "{:<30}| {:<}".format(i,"")
                f.write(hasil)
                f.write("\n")
                #print(hasil)
        except subprocess.CalledProcessError:
            hasil = "{:<30}| {:<}".format(i, "ENCODING ERROR")
            f.write(hasil)
            f.write("\n")
            #print(Hasil)
    f.close()

#log out
def logout():
    import os
    print("ECHO : Do you wanna logout ?(y/n)\n")
    ask = input("You : ")
    if ask.lower() == "y":
        os.system('shutdown -l')
    else : 
        pass

#lock screen
def lock_screen():
    import ctypes
    ctypes.windll.user32.LockWorkStation()

#log out
def shutdown():
    import os
    print("ECHO : Do you wanna shutdown your pc ?(y/n)\n")
    ask = input("You : ")
    if ask.lower() == "y":
        os.system("shutdown /s /t 1 -f")
    else : 
        pass

#alarm functioon
def alarm():
    from dictionary import taskdict
    import random

    print("ECHO : when ? \n")
    set_time = str(input("You : "))

    response = random.choice(taskdict.responses['alarm'])
    print("ECHO : ", response)
    
    #executing
    import myalarm 
    myalarm.set_alarm(set_time) 

