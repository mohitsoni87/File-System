import os, click
home = 'C:\\Users\\mohit\\Desktop\\OS'
while(1):
      path = os.getcwd()
      print(path + '>', end = '')
      command = input()
      check = command.split()
      if(command == 'e'):
            break
      elif(command == 'cl'):
            os.system('cls')
            continue
      elif(check[0] == 'nd'):
            os.chdir(check[1])
            last = os.getcwd()
            continue
      else:
            temp = os.getcwd()
            os.chdir(home)
            os.system("python Shell.py " + command)
            os.chdir(temp)

