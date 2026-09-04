import datetime
alias=""
def mainMenu():#finished
  accCheck=input("Do you have an account? \n1)Yes \n2)No (I'd like to create one though!) \n " )
  if accCheck=="1" or accCheck.lower()=="yes":
    login()
  elif accCheck=="2" or accCheck.lower()=="no":
    createAccount()
  elif accCheck=="3":
    secretAdminLogin()
  else:
    print("You didn't enter 1 or 2!! Try again \n")
    mainMenu()

def secretAdminLogin():#finished
  print("Welcome to the secret admin page!")
  userinp=input("What is your username? ").lower()
  userpass=input("What is your password? ")
  global alias
  userList=[]
  passList=[]
  index=0
  f1=open("admins.txt","r")
  for line in f1:
    username,password=line.split(",")
    password=password.split()
    userList.append(username)
    passList.append(password[0])
  userFound=False
  for i in range(len(userList)):
    if userinp==userList[i].lower():
      if userpass==passList[i]:
        print("You entered the correct password. You will soon be logged in")
        alias=userinp
        adminLoggedIn()
        userFound=True
        break
      else:
        print("You entered the incorrect password. Redirecting you to the login page")
        login()
    index=index+1
    if index==len(userList) and userFound==False:
      print("Cannot find your username! You will be returned to the main menu")
      mainMenu()
  f1.close()
  
def adminLoggedIn():
  global alias
  dateList=[]
  adminList=[]
  userList=[]
  print("Welcome admin",alias)
  adchoi=input("What would you like to do? \n 1)View/Cancel appointments  2)Logout\n")#adminChoice
  if adchoi=="1":
    f5=open("appointments.txt","r")
    for line in f5:
      date,admin,user=line.split(",")
      dateList.append(date)
      adminList.append(admin)
      userList.append(user)
    for i in range(len(adminList)):
      if alias.lower()==adminList[i].lower():
        print("You have an appointment on ",dateList[i],"with",userList[i])
    print("Cancelling hasnt been added yet!")
    
  elif adchoi=="2":
    alias=""
    mainMenu()
  
  

  
def loggedIn():#finished
  global alias
  print("You're logged in",alias+"!")
  inp=input("Would you like to 1)Book an appointment? \n 2) logout\n")
  if inp=="yes" or inp=="1":
    appointmentBooking()
  if inp=="2":
    alias=""
    mainMenu()
    
def appointmentBooking():
  f3=open("appointments.txt","r")
  dateList=[]
  adminList=[]
  goodDate=False
  adminChosen=False
  inde=0
  for line in f3:
    date,admin,user=line.split(",")
    dateList.append(date)
    adminList.append(admin)
    inde=inde+1
  f3.close
  while goodDate==False:
    inpDate=input("What date would you like your appointment for? (in form dd/mm/yyyy)\n")
    if inpDate in dateList:
      print("This date is already busy! Please choose another\n")
    else:
      goodDate=True
  while adminChosen==False:
    admPick=input("Which admin would you like to meet with? 1)David 2)Jacquis 3)Nimai 4)Camilla\n")
    if admPick=="1":
      admPick="David"
      adminChosen=True
    elif admPick=="2":
      admPick="Jacquis"
      adminChosen=True
    elif admPick=="3":
      admPick="Nimai"
      adminChosen=True
    elif admPick=="4":
      admPick= "Camilla"
      adminChosen=True
    else:
      print("You didn't select a number! Try again.")
  print("You have an appointment on",inpDate, "with",admPick+". I will maybe add a feature to restart if it was inputted incorrectly later")
  adminList.append(admPick)
  dateList.append(inpDate)
  lorne=dateList[inde]+","+adminList[inde]+","+alias+"\n"
  f4=open("appointments.txt","a")
  f4.write(lorne)
  f4.close
      
    

    
  
  

  
  

  
def login():#finished
  global alias
  userinp=input("What is your username? ").lower()
  userpass=input("What is your password? ")
  userList=[]
  passList=[]
  index=0
  f1=open("users.txt","r")
  for line in f1:
    username,password=line.split(",")
    password=password.split()#when i split it, it makes it into a list so instead of working out why i will just append with the first element of said list
    userList.append(username)
    passList.append(password[0])
  #print("Userlist",userList)
  #print("PassList",passList)
  userFound=False
  for i in range(len(userList)):
    if userinp==userList[i].lower():
      if userpass==passList[i]:
        print("You entered the correct password. You will soon be logged in")
        alias=userinp
        loggedIn()
        userFound=True
        break
      else:
        print("You entered the incorrect password. Redirecting you to the login page")
        login()
    index=index+1
    if index==len(userList) and userFound==False:
      print("Cannot find your username! You will be returned to the main menu")
      mainMenu()
  f1.close()
      
    

def createAccount():#finished
  passSame=False
  user=input("What do you want your username to be? ")#add non repeatable functionality
  pasw=input("What do you want your password to be? ")
  chepasw=input("Repeat your password. ")
  if chepasw==pasw:
    passSame=True
  while passSame==False:
    print("The second password you gave was not the same. Please try again")
    chepasw=input("Repeat your password. ")
  f1=open("users.txt","a")
  bleep=user+","+pasw+"\n"#bleep was just a random word, line didnt seem suitable
  f1.write(bleep)
  f1.close()
  mainMenu()


mainMenu()