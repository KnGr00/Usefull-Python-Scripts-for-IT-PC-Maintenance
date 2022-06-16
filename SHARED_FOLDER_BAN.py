import win32net
import win32netcon
import os
from sys import exit

names = []
COMPUTER_NAME = str(os.environ['COMPUTERNAME'])# look at this machine
INFO_LEVEL = 2

resume = 0


while 1:
  (shares, total, resume) = win32net.NetShareEnum (
      COMPUTER_NAME,
      INFO_LEVEL,
      resume,
      win32netcon.MAX_PREFERRED_LENGTH
    )
  for share in shares:
    print (share['netname'], "=>", share['path'])
    names.append(share['netname'])
  if not resume:
    break
for name in names:
  if name != "C$" and name != "IPC$" and name != "ADMIN$":
    break
  else:
    if name == names[-1]:
      print("There are only default shares on this machine")
      exit()


while True:
  os.system("runas /profile /user:Administrator net share "+ name +" /delete")
  for name in names:
    if name != "C$" and name != "IPC$" and name != "ADMIN$":
      print("Deleting " + name)
      os.system("net share "+ name +" /delete")
      if name == names[-1]:
        print("There are only default shares left on this machine")
        exit()