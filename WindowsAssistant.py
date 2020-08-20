#This software almost Support 38 software and websites
#This is user friendly
#If not found your Command in software it redirects to google with your permission
#It saves the command by which user is not satisfied at last in the file "rawdata.txt" so that developer will read those command and will try to update the software next time.
#It has 
#   Default Browers as chrome
#   Default MP3 Music Player as Spotify    
#   Default Video Song and Movies Player as VLC
#It also support google photos,google drive,gmail,youtube in it

import pyttsx3
import os

print("Hey, Welcome To My Tool")
pyttsx3.speak("Hey, Welcome To My Tool")
print("I am Tom. Your virtual Assistant")
pyttsx3.speak("I am Tom. Your virtual Assistant")

while True:
    
    print("What can i do for you? ",end = " ")
    pyttsx3.speak("How may i help you ?")
    p =input().lower()
        
#Launch Microsoft Edge
    if(((('microsoft' in p) or ('edge' in p) or ('windows' in p)) and (('browser' in p) or ('edge' in p) or ('search' in p) or ('browse' in p) or ('find' in p) or ('www' in p) or ('http' in p) or ('.co' in p) or ('.in' in p) or ('.org' in p) or ('.edu' in p))) and (('run' in p) or ('show' in p) or ('execute' in p) or ('open' in p) or ('launch' in p) or ('view' in p) or ('browse' in p) or ('search' in p) or ('find' in p)) and not (("don't" in p) or ("not"  in p) or ("no"  in p) or ("never" in p))): 
        print("Launching Microsoft Edge")
        pyttsx3.speak("Launching Microsoft Edge")
        os.system("start microsoft-edge:")
   
#Launch Chrome Browers
    elif((('chrome' in p) or ('browser' in p) or ('search' in p) or ('browse' in p) or ('find' in p) or ('www' in p) or ('http' in p) or ('.co' in p) or ('.in' in p) or ('.org' in p) or ('.edu' in p)) and (('run' in p) or ('show' in p) or ('execute' in p) or ('open' in p) or ('launch' in p) or ('view' in p) or ('browse' in p) or ('search' in p) or ('find' in p)) and not (("don't" in p) or ("not"  in p) or ("no"  in p) or ("never" in p))): 
        #Ask for Searching
        print("May I search for You  ",end = " ")
        pyttsx3.speak("May I search for You")
        ans = input().lower()
        if((('search' in ans) or ('ok' in ans) or ('can'in ans) or ('yes' in ans) or ('yeah' in ans) or ('y' in ans) or ('okay' in ans) or ('ohk' in ans)) and not (("don't" in ans) or ("not" in ans) or ("no" in ans) or ("never" in ans))):
            print("What will you like to search ? ",end = " ")
            pyttsx3.speak("What will you like to search ?")
            search = input().lower() 
            #Searching Website
            if(('www' in search) or ('http' in search) or ('.co' in search) or ('.in' in search) or ('.org' in search) or ('.edu' in search)):
                search = "Chrome "+search
                print("Launching Chrome")
                pyttsx3.speak("Launching Chrome")
                os.system(search)
            #Searching for Content typed by user incase it is not website
            else :
                search = "Chrome https://www.google.com/search?q=\""+search+"\""
                print(search)
                print("Launching Chrome") 
                pyttsx3.speak("Launching Chrome") 
                os.system(search)
         #Just Launch Chrome without any activity         
        else : 
            print("Launching Chrome")
            pyttsx3.speak("Launching Chrome")
            os.system("Chrome")
            
#Launch VLC Media Player        
    elif((('vlc' in p) or ('media' in p) or ('player' in p) or ('movie' in p) or ('video' in p)) and (('run' in p) or ('launch' in p) or ('show' in p) or ('watch' in p) or ('execute' in p) or ('open' in p) or ('view' in p) or ('play' in p) or ('entertain' in p)) and not (("don't" in p) or ("not"  in p) or ("no"  in p) or ("never" in p))):
        #Play's Mp3 Songs
        if((('mp3' in p) or ('song' in p) or ('music' in p) or ('audio' in p)) and not (('video' in p) or ('movie' in p))):
            print("Launching MP3 Songs in VlC Media Player")
            os.system("vlc \"D:\MyPlaylist\mymp3playlist.xspf\" -f")
        #Go for Video's
        elif(('movie' in p) or ('video' in p) or ('mp4' in p) or ('view' in p)):
            #Play Video Songs
            if(('song' in p) or ('music' in p)):
                print("Launching Video Songs in VLC Media Player")
                pyttsx3.speak("Launching Video Songs in VLC Media Player")
                os.system("vlc \"D:\MyPlaylist\\videosongs.xspf\" -f")
            #Play Movies
            else:
                print("Playing Movies in VLC Media Player")
                pyttsx3.speak("Playing Movies in VLC Media Player")
                os.system("vlc \"D:\MyPlaylist\moviesplaylist.xspf\" -f")
        else :
        #Ask for Playing
            print("May I Play something for You  ",end = " ")
            pyttsx3.speak("May I Play something for You  ")
            ans = input().lower()
            if((('search' in ans) or ('ok' in ans) or ('can'in ans) or ('yes' in ans) or ('yeah' in ans) or ('y' in ans) or ('okay' in ans) or ('ohk' in ans)) and not (('dont' in ans) or ('not' in ans) or ('no' in ans) or ('never' in ans))):
                #Asks for Choices
                print("Press  1.For Movies     2.For Video Songs    3.For MP3 Songs ",end = " ")
                pyttsx3.speak("Press  1.For Movies     2.For Video Songs    3.For MP3 Songs ")
                play = input().lower()
                if(play == '1'):
                    print("Playing Movies in VLC Media Player")
                    pyttsx3.speak("Playing Movies in VLC Media Player")
                    os.system("vlc \"D:\MyPlaylist\moviesplaylist.xspf\" -f")
                elif(play == '2'):
                    print("Launching Video Songs in VLC Media Player")
                    pyttsx3.speak("Launching Video Songs in VLC Media Player")
                    os.system("vlc \"D:\MyPlaylist\\videosongs.xspf\" -f")
                else:
                    print("Launching MP3 Songs in VlC Media Player")
                    pyttsx3.speak("Launching MP3 Songs in VlC Media Player")
                    os.system("vlc \"D:\MyPlaylist\mymp3playlist.xspf\" -f")
            else :
                print("Launching VlC Media Player")
                pyttsx3.speak("Launching VlC Media Player")
                os.system("vlc -f")
    
#Launch Youtube
    elif((('youtube' in p) or ('browser' in p) or ('stream' in p) or ('search' in p) or ('browse' in p) or ('find' in p) or ('video' in p)) and (('run' in p) or ('show' in p) or ('launch' in p) or ('execute' in p) or ('open' in p) or ('view' in p) or ('play' in p) or ('entertain' in p) or ('video' in p)) and not (("don't" in p) or ("not"  in p) or ("no"  in p) or ("never" in p))):
        print("May I search for You ",end = " ")
        pyttsx3.speak("May I search for You ")
        ans = input().lower()
        #Ask for Searching
        if((('search' in ans) or ('ok' in ans) or ('can'in ans) or ('yes' in ans) or ('yeah' in ans) or ('y' in ans) or ('okay' in ans) or ('ohk' in ans)) and not (("don't" in ans) or ("not" in ans) or ("no" in ans) or ("never" in ans))):
            print("What will you like to search ? ",end = " ")
            pyttsx3.speak("What will you like to search ?")
            search = input().lower()
            search = "Chrome https://www.youtube.com/results?search_query=\""+search+"\""
            os.system(search)
            print("Launching Youtube in Chrome")   
            pyttsx3.speak("Launching Youtube in Chrome")
        else :
            os.system("Chrome www.youtube.com")
            print("Launching Youtube in Chrome")
            pyttsx3.speak("Launching Youtube in Chrome")
            
#Launch Mailbox
    elif((('mail' in p) or ('gmail' in p) or ('contact' in p)) and (('run' in p) or ('launch' in p) or ('execute' in p) or ('open' in p) or ('show' in p) or ('view' in p) or ('send' in p) or ('receive' in p)) and not (("don't" in p) or ("not"  in p) or ("no"  in p) or ("never" in p))):
          print("Launching Mailbox")
          pyttsx3.speak("Launching Mailbox")
          os.system("explorer.exe shell:appsFolder\microsoft.windowscommunicationsapps_8wekyb3d8bbwe!microsoft.windowslive.mail")        
          
#Launch Google Photos in Chrome
    elif(((('photos' in p) or ('pic' in p) or ('Images' in p) or ('memories' in p)) and ('google' in p)) and  (('run' in p) or ('show' in p) or ('launch' in p) or ('execute' in p) or ('open' in p) or ('view' in p) or ('play' in p) or ('entertain' in p)) and not (("don't" in p) or ("not"  in p) or ("no"  in p) or ("never" in p))):
        print("Launching Google Photos")
        pyttsx3.speak("Launching Google Photos")
        os.system("Chrome https://photos.google.com/?tab=rq&authuser=0&pageId=none")

#Launch Microsoft OneDrive
    elif(('onedrive' in p) and (('write' in p) or ('format' in p) or ('edit' in p) or ('launch' in p) or ('run' in p) or ('show' in p) or ('execute' in p) or ('open' in p) or ('view' in p)) and not (("don't" in p) or ("not"  in p) or ("no"  in p) or ("never" in p))):
        print("Launching MS OneDrive")
        pyttsx3.speak("Launching MS OneDrive")
        os.system("OneDrive") 
        
#Launch Google Drive
    elif((('drive' in p) or (('folder' in p) or ('files' in p) or ('doc' in p)  and ('google' in p))) and (('edit' in p) or ('launch' in p) or ('run' in p)or ('execute' in p) or ('open' in p) or ('view' in p) or ('show' in p)) and not (("don't" in p) or ("not"  in p) or ("no"  in p) or ("never" in p))):
        print("Launching Google Drive")
        pyttsx3.speak("Launching Google Drive")
        os.system("Chrome https://drive.google.com/?tab=ro&authuser=0")
             
#Launch File Explorer            
    elif((('file' in p) or('explorer' in p) or ('folder' in p) or (('manage' in p) and (('file' in p) or ('folder' in p)))) and ((('manage' in p) and (('file' in p) or ('folder' in p))) or ('database' in p) or ('data' in p) or ('edit' in p) or ('launch' in p) or ('run' in p)or ('execute' in p) or ('open' in p) or ('show' in p) or ('view' in p)) and not (("don't" in p) or ("not"  in p) or ("no"  in p) or ("never" in p))):
        print("Launching File Explorer")
        pyttsx3.speak("Launching File Explorer")
        os.system("explorer")
        
#Launch Spoify  -as default music player  
    elif((('spotify' in p) or ('songs' in p) or ('music' in p)) and (('run' in p)or ('execute' in p) or ('open' in p) or ('view' in p) or ('play' in p) or ('launch' in p) or ('entertain' in p)) and not (("don't" in p) or ('video' in p) or ("not"  in p) or ("no"  in p) or ("never" in p))):
        print("Launching Spotify")
        pyttsx3.speak("Launching Spotify")
        os.system("spotify")
    
#Launch Groove  
    elif((('groove' in p) or ((('local' in p) or ('offline' in p) or ('Microsoft' in p) or ('windows' in p)) and (('player' in p) or ('music' in p) or ('song' in p))) or ('song' in p) or ('music' in p)) and (('run' in p)or ('execute' in p) or ('open' in p) or ('view' in p) or ('play' in p) or ('show' in p) or ('launch' in p) or ('entertain' in p)) and not (("don't" in p) or ('video' in p) or ("not"  in p) or ("no"  in p) or ("never" in p))):
        print("Launching Groove Music")
        pyttsx3.speak("Launching Groove Music")
        os.system("start mswindowsmusic:")
    
#Launch Microsoft Word
    elif((('word' in p) or ('doc' in p) or ('paper' in p) or ('A4' in p) or ('A5' in p) or ('letter' in p) or ('synopsis' in p) or (('format' in p) and ('text' in p))) and ((('format' in p) or ('show' in p) and ('text' in p)) or ('write' in p) or ('edit' in p) or ('launch' in p) or ('run' in p)or ('execute' in p) or ('open' in p) or ('view' in p)) and not (("don't" in p) or ("not"  in p) or ("no"  in p) or ("never" in p))):
        print("Launching MS Word")
        pyttsx3.speak("Launching MS Word")
        os.system("winword")
    
 #Launch Microsoft Excel
    elif((('excel' in p) or ('sheet' in p) or ('table' in p) or ('xls' in p) or ('column' in p) or ('records' in p)) and (('write' in p) or ('edit' in p) or ('show' in p) or ('launch' in p) or ('run' in p)or ('execute' in p) or ('open' in p) or ('view' in p)) and not (("don't" in p) or ("not"  in p) or ("no"  in p) or ("never" in p))):
        print("Launching MS Excel")
        pyttsx3.speak("Launching MS Excel")
        os.system("excel")
        
#Launch Microsoft Powerpoint    
    elif((('ppt' in p) or ('presentation' in p) or ('powerpoint' in p) or ('impres' in p) or ('slide' in p) or ((('animation' in p) or ('transition' in p) or ('presentation' in p) or ('slideshow' in p)) and (('paper' in p) or ('document' in p)))) and (('animation' in p) or ('transition' in p) or ('presentation' in p) or ('slideshow' in p) or ('write' in p) or ('format' in p) or ('edit' in p) or ('launch' in p) or ('show' in p) or ('run' in p)or ('execute' in p) or ('open' in p) or ('view' in p) or ((('animation' in p) or ('transition' in p) or ('slideshow' in p)) and (('paper' in p) or (document in p)))) and not (("don't" in p) or ("not"  in p) or ("no"  in p) or ("never" in p))):
        print("Launching MS Powerpoint Presentation")
        pyttsx3.speak("Launching MS Powerpoint Presentation")
        os.system("POWERPNT")
    
#Launch Microsoft Access
    elif(('access' in p) and (('database' in p) or ('data' in p) or ('edit' in p) or ('show' in p) or ('launch' in p) or ('run' in p)or ('execute' in p) or ('open' in p) or ('view' in p)) and not (("don't" in p) or ("not"  in p) or ("no"  in p) or ("never" in p))):
        print("Launching MS Access")
        pyttsx3.speak("Launching MS Access")
        os.system("MSACCESS") 
    
#Launch Skype
    elif((('call' in p) or ('contact' in p) or ('sky' in p)) and (('video' in p) or ('show' in p) or ('edit' in p) or ('launch' in p) or ('run' in p)or ('execute' in p) or ('open' in p) or ('view' in p)) and not (("don't" in p) or ("not"  in p) or ("no"  in p) or ("never" in p))):
        print("Launching Skype")
        pyttsx3.speak("Launching Skype")
        os.system("skype") 
    
#Launch Calculator
    elif((('calc' in p) or ('calculator' in p) or ('add' in p) or ('sub' in p) or ('div' in p) or ('mul' in p) or ('expression' in p)) and (('solve' in p) or ('show' in p) or ('launch' in p) or ('run' in p) or ('execute' in p) or ('open' in p) or ('view' in p)) and not (("don't" in p) or ("not"  in p) or ("no"  in p) or ("never" in p))):
        print("Launching Calculator")
        pyttsx3.speak("Launching Calculator")
        os.system("calc"); 
        
#Launch Alarms and Clock
    elif((("alarm" in p) or ("clock" in p) or ("time" in p) or ("watch" in p) or ("minute" in p) or ("hours" in p)) and (('run' in p) or ('launch' in p) or ('show' in p) or ('execute' in p) or ('open' in p) or ('view' in p) or ('play' in p)) and not (("don't" in p) or ("not"  in p) or ("no"  in p) or ("never" in p))):
        print("Launching Alarms and Clock")
        pyttsx3.speak("Launching Alarms and Clock")
        os.system("start ms-clock:") 
    
#Launch Available Networks
    elif((("wifi" in p) or ("network" in p) or ("internet" in p) or ("wireless" in p) or ("connect" in p) or ("airplane" in p) or ("hotspot" in p) or ("flight" in p)) and (('run' in p) or ('launch' in p) or ('execute' in p) or ('open' in p) or ('view' in p) or ('show' in p) or ('device' in p)) and not (("don't" in p) or ("not"  in p) or ("no"  in p) or ("never" in p))):
        print("Launching Available Networks")
        pyttsx3.speak("Launching Available Networks")
        os.system("start ms-availablenetworks:")
    
#Launch Calendar
    elif((("date" in p) or ("month" in p) or ("year" in p) or ("festival" in p) or ("calender" in p) or ("event" in p)) and (('run' in p) or ('launch' in p) or ('today' in p) or ('execute' in p) or ('show' in p) or ('open' in p) or ('view' in p) or ('play' in p)) and not (("don't" in p) or ("not"  in p) or ("no"  in p) or ("never" in p))):
        print("Launching Calender")
        pyttsx3.speak("Launching Calender")
        os.system("start outlookcal:")
        
#Launch Camera
    elif((("camera" in p) or ("capture" in p) or ("click" in p) or ("record" in p)) and (('run' in p) or ('launch' in p) or ('execute' in p) or ('open' in p) or ('view' in p) or ('play' in p)) and not (("don't" in p) or ("not"  in p) or ("no"  in p) or ("never" in p))):
        print("Launching Camera")
        pyttsx3.speak("Launching Camera")
        os.system("start microsoft.windows.camera:")
        
#Launch Maps
    elif((("map" in p) or ("location" in p) or ("direction" in p) or ("compass" in p) or ("Naviga" in p) or ("locat" in p) or ("place" in p) or ("road" in p) or ("highway" in p) or ("route" in p) or ("street" in p)) and (('run' in p) or ('get' in p) or ('launch' in p) or ('execute' in p) or ('open' in p) or ('view' in p) or ('play' in p) or ('show' in p)) and not (("don't" in p) or ("not"  in p) or ("no"  in p) or ("never" in p))):
        print("Launching Maps")
        pyttsx3.speak("Launching Maps")
        os.system("start bingmaps:")
        
#Launch Photos
    elif((('photos' in p) or ('pic' in p) or ('Images' in p) or ('memories' in p)) and  (('run' in p) or ('launch' in p) or ('execute' in p) or ('open' in p) or ('view' in p) or ('play' in p) or ('show' in p) or ('entertain' in p)) and not (("don't" in p) or ("not"  in p) or ("no"  in p) or ("never" in p))):
        print("Launching Photos")
        pyttsx3.speak("Launching Photos")
        os.system("start ms-photos:")
        
#Launch Projection
    elif((("project" in p) or ("screen" in p) or ("display" in p) or ("extend" in p) or ("cast" in p) or ("connect" in p)) and (('run' in p) or ('launch' in p) or ('execute' in p) or ('connect' in p) or ('join' in p) or ('open' in p) or ('show' in p) or ('view' in p) or ('play' in p)) and not (("don't" in p) or ("not"  in p) or ("no"  in p) or ("never" in p))):
        print("Launching Projection")
        pyttsx3.speak("Launching Projection")
        os.system("start ms-settings-displays-topology:projection")
    
#Launch Windows Defender
    elif((("privacy" in p) or ("security" in p) or ("antivirus" in p) or ("protection" in p) or ("defender" in p) or ("firewall" in p) or ("threat" in p)) and (('run' in p) or ("setting" in p) or ('show' in p) or ('launch' in p) or ('execute' in p) or ('open' in p) or ('view' in p) or ('play' in p)) and not (("don't" in p) or ("not"  in p) or ("no"  in p) or ("never" in p))):
        print("Launching Windows Defender")
        pyttsx3.speak("Launching Windows Defender")
        os.system("start windowsdefender:")
        
#Launch Weather
    elif((("weather" in p) or ("climate" in p) or ("season" in p) or ("temper" in p) or ("celsius" in p) or ("fahrenheit" in p) or ("rain" in p) or ("language" in p) or ("winter" in p) or ("summer" in p) or ("cloud" in p) or ("cold" in p) or ("sun" in p) or ("shin" in p)) and (('run' in p) or ("setting" in p) or ('launch' in p) or ('execute' in p) or ('open' in p) or ('view' in p) or ('show' in p) or ('play' in p) or ('today' in p)) and not (("don't" in p) or ("not"  in p) or ("no"  in p) or ("never" in p))):
        print("Launching MSN Weather")
        pyttsx3.speak("Launching MSN Weather")
        os.system("start bingweather:")    
    
#Launch Contol Panel Manage program
    elif((("install" in p) or ("uninstall" in p) or ("remove" in p) or ("manage program" in p) or ("software" in p) or ("repair" in p) or ("feature" in p) or ("organize" in p)) and (('run' in p) or ("manage program" in p) or ('program' in p) or ('launch' in p) or ('execute' in p) or ('open' in p) or ('view' in p) or ('play' in p)) and not (("don't" in p) or ("not"  in p) or ("no"  in p) or ("never" in p))):
        print("Launching Contol Panel Manage program ")
        pyttsx3.speak("Launching Contol Panel Manage program ")
        os.system("control appwiz.cpl")
        
#Launch Device Manager
    elif((("device" in p) and ("manage" in p)) and (('run' in p) or ("manage" in p) or ('launch' in p) or ('execute' in p) or ('open' in p) or ('show' in p) or ('view' in p) or ('play' in p)) and not (("don't" in p) or ("not"  in p) or ("no"  in p) or ("never" in p))):
        print("Launching Device Manager")
        pyttsx3.speak("Launching Device Manager")
        os.system("devmgmt.msc")
    
#Launch Printer Setting
    elif((("printer" in p) or ("scanner" in p)) and (('run' in p) or ('launch' in p) or ('setting' in p) or ('execute' in p) or ('show' in p) or ('open' in p) or ('view' in p) or ('play' in p)) and not (("don't" in p) or ("not"  in p) or ("no"  in p) or ("never" in p))):
        print("Launching Printer Setting")
        pyttsx3.speak("Launching Printer Setting")
        os.system("control printers")
        
#Launch Power Setting
    elif((("power" in p) or ("battery" in p)) and (('run' in p) or ('launch' in p) or ('setting' in p) or ('execute' in p) or ('show' in p) or ('open' in p) or ('view' in p) or ('play' in p)) and not (("don't" in p) or ("not"  in p) or ("no"  in p) or ("never" in p))):
        print("Launching Power Setting")
        pyttsx3.speak("Launching Power Setting")
        os.system("control powercfg.cpl")
    
#Launch Sound Setting
    elif((("sound" in p) or ("audio" in p) or ("speaker" in p) or ("microphone" in p)) and (('run' in p) or ('launch' in p) or ('show' in p) or ('setting' in p) or ('execute' in p) or ('open' in p) or ('view' in p) or ('play' in p)) and not (("don't" in p) or ("not"  in p) or ("no"  in p) or ("never" in p))):
        print("Launching Sound Setting")
        pyttsx3.speak("Launching Sound Setting")
        os.system("control mmsys.cpl")
        
#Launch Taskbar Setting
    elif((("task" in p) or ("notification" in p)) and (('run' in p) or ('launch' in p) or ('setting' in p) or ('execute' in p) or ('show' in p) or ('open' in p) or ('view' in p) or ('play' in p)) and not (("don't" in p) or ("not"  in p) or ("no"  in p) or ("never" in p))):
        print("Launching Taskbar Setting")
        pyttsx3.speak("Launching Taskbar Setting")
        os.system("control /name Microsoft.Taskbar")
        
#Launch Android Studio
    elif((("firebase" in p) or ("android" in p) or ("studio" in p)) and (('run' in p) or ("code" in p) or ("project" in p) or ('launch' in p) or ('setting' in p) or ('execute' in p) or ('open' in p) or ('view' in p) or ('play' in p)) and not (("don't" in p) or ("not"  in p) or ("no"  in p) or ("never" in p))):
        print("Launching Android Studio")
        pyttsx3.speak("Launching Android Studio")
        os.system("studio64")
        
#Launch Turbo C
    elif((("program c" in p) or ("turbo c" in p) or ("c++" in p)) and (('run' in p) or ("code" in p) or ("project" in p) or ('show' in p) or ('launch' in p) or ('setting' in p) or ('execute' in p) or ('open' in p) or ('view' in p) or ('play' in p)) and not (("don't" in p) or ("not"  in p) or ("no"  in p) or ("never" in p))):
        print("Launching Turbo C")
        pyttsx3.speak("Launching Turbo C")
        os.system("\"Turbo C++\"")
    
#Launching MySQL
    elif((("mysql" in p) or ("sql" in p) or ("query" in p) or ("dbms" in p) or ("database" in p)  or ("benchmark" in p)) and (('run' in p) or ('show' in p) or ("code" in p) or ("project" in p) or ('launch' in p) or ('setting' in p) or ('execute' in p) or ('open' in p) or ('view' in p) or ('play' in p)) and not (("don't" in p) or ("not"  in p) or ("no"  in p) or ("never" in p))):
        print("Launching MySQL")
        pyttsx3.speak("Launching MySQL")
        os.system("MySQLWorkbench")
        
#Launching Anaconda
    elif((("anaconda" in p) or ("conda" in p) or ("python" in p) or ("pycharm" in p) or (".py" in p)  or ("navigator" in p)) and (('run' in p) or ("code" in p) or ("project" in p) or ('launch' in p) or ('setting' in p) or ('execute' in p) or ('open' in p) or ('view' in p) or ('play' in p) or ('show' in p)) and not (("don't" in p) or ("not"  in p) or ("no"  in p) or ("never" in p))):
        print("Launching Anaconda")
        pyttsx3.speak("Launching Anaconda")
        os.system("anaconda-navigator")
    
#Launch Oracle Virtual Studio
    elif((("oracle" in p) or ("virtual" in p) or ("redhat" in p) or ("linux" in p)) and (('run' in p) or ("code" in p) or ("project" in p) or ('launch' in p) or ('setting' in p) or ('execute' in p) or ('open' in p) or ('view' in p) or ('show' in p) or ('play' in p)) and not (("don't" in p) or ("not"  in p) or ("no"  in p) or ("never" in p))):
        print("Launching Oracle Virtual Studio")
        pyttsx3.speak("Launching Oracle Virtual Studio")
        os.system("VirtualBox")
        
#Launch Setting
    elif((("setting" in p) or ("manage" in p) or ("display" in p) or ("preference" in p) or ("resolution" in p) or ("device" in p) or ("system" in p) or ("language" in p) or ("privacy" in p) or ("personalization" in p) or ("security" in p) or ("update" in p) or ("reset" in p) or ("restore" in p)) and (('run' in p) or ("setting" in p) or ('launch' in p) or ('execute' in p) or ('show' in p) or ('open' in p) or ('view' in p) or ('play' in p)) and not (("don't" in p) or ("not"  in p) or ("no"  in p) or ("never" in p))):
        print("Launching setting")
        pyttsx3.speak("Launching setting")
        os.system("start ms-settings:")
        
#Launch Control Panel
    elif((("setting" in p) or ("manage" in p) or ("control" in p) or ("panel" in p) or ("display" in p) or ("preference" in p) or ("resolution" in p) or ("device" in p) or ("system" in p) or ("language" in p) or ("privacy" in p) or ("personalization" in p) or ("security" in p) or ("update" in p) or ("reset" in p) or ("restore" in p)) and (('run' in p) or ("setting" in p) or ('show' in p) or ('launch' in p) or ('execute' in p) or ('open' in p) or ("panel" in p) or ("control" in p) or ('view' in p) or ('play' in p)) and not (("don't" in p) or ("not"  in p) or ("no"  in p) or ("never" in p))):
        print("Launching Control Panel")
        pyttsx3.speak("Launching Control Panel")
        os.system("control")
    
#Launch Notepad
    elif((('text' in p) or ('editor' in p) or ('note' in p) or ('pad' in p) or ('write' in p) or ('file' in p)) and (('show' in p) or ('it' in p) or ('write' in p) or ('edit' in p) or ('launch' in p) or ('run' in p)or ('execute' in p) or ('open' in p) or ('view' in p)) and not (("don't" in p) or ("not"  in p) or ("no"  in p) or ("never" in p))):
        print("Do You want to open any specific file ",end = " ")
        pyttsx3.speak("Do You want to open any specific file")
        ans = input().lower()
        #Search for file
        if((('search' in ans) or ('ok' in ans) or ('can'in ans) or ('yes' in ans) or ('yeah' in ans) or ('y' in ans) or ('okay' in ans) or ('ohk' in ans)) and not (("don't" in ans) or ("not" in ans) or ("no" in ans) or ("never" in ans))):
            print("Please the path or name of file ",end = " ")
            pyttsx3.speak("Please the path or name of file")
            search = input().lower()
            search = "notepad \""+search+"\""
            print("Launching Notepad")
            pyttsx3.speak("Launching Notepad")
            os.system(search) 
        else :
            print("Launching Notepad")
            pyttsx3.speak("Launching Notepad")
            os.system("notepad")
    elif(('how' in p) and ('you' in p)):
        print("I am Good");
        pyttsx3.speak("I am Good");
    
#Exit the Program
    elif(('exit' in p) or ('break' in p) or ('leave' in p) or ('nothing' in p) or ('nope' in p)):
        print("Are You Sure You want to exit ",end = " ")
        pyttsx3.speak("Are You Sure You want to exit")
        ans = input().lower()
        #Ask Permission if No 
        if((('ok' in ans) or ('can'in ans) or ('yes' in ans) or ('yeah' in ans) or ('okay' in ans) or ('ohk' in ans)) and not (("don't" in ans) or ("not" in ans) or ("no" in ans) or ("never" in ans))):
            break
        else :
            print("Not Found on this PC")
            pyttsx3.speak("Not Found on this PC")
            #Ask for Searching
            print("May I search on Web  ",end = " ")
            pyttsx3.speak("May I search on Web  ")
            ans = input().lower()
            #Search on Web
            if((('search' in ans) or ('ok' in ans) or ('can'in ans) or ('yes' in ans) or ('yeah' in ans) or ('y' in ans) or ('okay' in ans) or ('ohk' in ans)) and not (("don't" in ans) or ("not" in ans) or ("no" in ans) or ("never" in ans))):
                search = "Chrome https://www.google.com/search?q=\""+p+"\""
                os.system(search)
                print("Launching Chrome")
                pyttsx3.speak("Launching Chrome")
            else :
                f=open("rawdata.txt", "a+")
                p =" \n"+p
                f.write(p) 
                f.close() 
                print('Ok')
                pyttsx3.speak('Ok')               
    elif((('will' in p) or ('do' in p) or ('have' in p) or ('has' in p) or ('would' in p) or ('how' in p) or ('what' in p) or ('which' in p) or ('when' in p))  and ('you' in p)):
        print("Not now, I will Update Myself and will late you know soon")
        pyttsx3.speak("Not now, I will Update Myself and will late you know soon")
        f=open("rawdata.txt", "a+")
        p =" \n"+p
        f.write(p) 
        f.close()
        
#If Command Not Executed            
    else :
        print("Not Found on this PC")
        pyttsx3.speak("Not Found on this PC")
        #Ask for Searching
        print("May I search on Web  ",end = " ")
        pyttsx3.speak("May I search on Web  ")
        ans = input().lower()
        #Search on Web
        if((('search' in ans) or ('ok' in ans) or ('can'in ans) or ('yes' in ans) or ('yeah' in ans) or ('yup' in ans) or ('okay' in ans) or ('ohk' in ans)) and not (("don't" in ans) or ("not" in ans) or ("no" in ans) or ("never" in ans))):
            search = "Chrome https://www.google.com/search?q=\""+p+"\""
            os.system(search)
            print("Launching Chrome")
            pyttsx3.speak("Launching Chrome")
        #Save the Query in Text file named "rawdata.txt"    
        else :
            f=open("rawdata.txt", "a+")
            p =" \n"+p
            f.write(p) 
            f.close() 
            print('Ok')
            pyttsx3.speak('Ok')
        