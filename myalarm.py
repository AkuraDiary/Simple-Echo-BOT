def set_alarm(timing):
    import datetime
    import winsound
    from win10toast import ToastNotifier
    import ctypes 
    
    message = "ALARM !!!"

    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    while True : 
        #getting current time
        current_time = datetime.datetime.now()
        alarm_time = str(current_time.hour)+":"+str(current_time.minute)

        if alarm_time == timing :
            notification = ToastNotifier()
            winsound.Beep(frequency=2500,duration=2000)
            notification.show_toast("Alarm", message, duration =50)
            #exit()
            import Echo_BOT as EC
            EC.main()
            break
