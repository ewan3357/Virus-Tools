import Virus
import time
i = 1
while i >= 10:
  Virus.beep(800)#800 millisces
  Virus.msgbox('You are Infected','Virus','320x200')
  Virus.Kill('Chrome.exe')#To keep People From googling how to get rid of it
  time.sleep(1)
  i+=1
Virus.Syskill('s')#Shutdown PC
