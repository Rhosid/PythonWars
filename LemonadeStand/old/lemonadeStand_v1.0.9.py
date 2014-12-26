"""
Name: lemonadeStand.py
Description: Game of Selling Lemonade
"""

__author__ = "Spencer Dockham"
__date__ = "12/19/2014"
__version__ = '1.0.9'

import time
import random
import math
import os
import numbers

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def clockData(day,m,hour,minute):
    if minute > 5:
        minute = 0
        hour += 1
    if hour == 12:
        if m == 'am':
            m = 'pm'
        else:
            day += 1
            m = 'am'
    if hour > 12:
        hour = 1
    tmpTime = str("Day: "+str(day)+"   "+str(hour)+":"+str(minute)+"0 "+str(m))
    returnList = [day,m,hour,minute,tmpTime]
    return returnList

def priceCheck(amount,price,money):
    cost = int(price * int(amount))
    if money - cost < 0:
        return False
    else:
        return True

def testInventory(lemon,sugar,cups,ice):
    if lemon < 0:
        return False
    if sugar < 0:
        return False
    if cups < 0:
        return False
    if ice < 0:
        return False
    return True

def testFloat(num):
    numbet=['1','2','2','3','4','5','6','7','8','9','0','.']
    cnt=0
    for ct in num:
        if ct not in numbet:
            return False
        if '.' == ct:
            cnt+=1
        if cnt > 1:
            return False
    foo = num.split('.')
    if cnt == 1:
        if len(foo[1]) > 2:
            print("Invalid input: can't enter number less than one cent.")
            return False
    return True

def testHour(hour,m):
    if m == 'am':
        if hour < 8:
            num = random.randint(0,20)
            if num < 12:
                return True
        elif hour < 10:
            num = random.randint(0,20)
            if num < 16:
                return True
        elif hour < 12:
            num = random.randint(0,20)
            if num < 19:
                return True
    elif m == 'pm':
        if hour == 12:
            return True
        if hour < 2:
            num = random.randint(0,20)
            if num < 18:
                return True
        elif hour < 5:
            num = random.randint(0,20)
            if num < 17:
                return True
        elif hour < 8:
            num = random.randint(0,20)
            if num < 16:
                return True
        elif hour < 10:
            num = random.randint(0,20)
            if num < 14:
                return True
        elif hour < 12:
            num = random.randint(0,20)
            if num < 4:
                return True
    return False

def testInt(num):
    numbet = ['1','2','2','3','4','5','6','7','8','9','0']
    number = num.split()
    for ct in number:
        if ct not in numbet:
            return False
    return True

def checkPrice(num,recom):
    if num <= recom:
        return True
    foo = random.randint(0,9)
    if num <= recom*2:
        if foo < 4:
            return True
    if num <= recom*3:
        if foo < 2:
            return True
    if num <= recom*4:
        if foo < 1:
            return True
    return False

def getWeather():
    weather = ''
    wList = ['clear','clear','clear','clear','clear','clear','clear','clear','clear',
             'partly cloudy','partly cloudy','partly cloudy',
             'rainy','rainy','rainy',
             'foggy','foggy',
             'thunderstorms',
             'windy',
             'hailing','hailing']
    num = random.randint(0,len(wList)-1)
    string = str(wList[num])
    return string

def testWeather(weather):
    if weather == 'clear':
        return True
    elif weather == 'partly cloudy':
        num=random.randint(0,10)
        if num >= 2:
            return True
    elif weather == 'rainy':
        num=random.randint(0,9)
        if num >= 5:
            return True
    elif weather == 'foggy':
        num=random.randint(0,5)
        if num >= 4:
            return True
    elif weather == 'thunderstorms':
        num=random.randint(0,15)
        if num == 0:
            return True
    elif weather == 'windy':
        num=random.randint(0,7)
        if num >= 5:
            return True
    elif weather == 'hailing':
        num=random.randint(0,50)
        if num == 0:
            return True
    return False

def hexi(tmp):
    strNum=''
    for ch in str(tmp):
        if ch in dicNum:
            strNum+=(str(dicNum[ch])+'.')
        else:
            strNum+=(str(ch)+'.')
    strNum=strNum[:-1]
    return strNum

def decode(tmp):
    tmp = str(tmp);lst=[];string=''
    lst = tmp.split('.')
    for ct in range(0,len(lst)):
        if lst[ct] in dicTrans:
            string+=(str(dicTrans[lst[ct]]))
        else:
            string+=str(lst[ct])
    return string
        

def saveGame():
    dataList = []
    dataList.append(money)
    dataList.append(price)
    dataList.append(lemon)
    dataList.append(sugar)
    dataList.append(cups)
    dataList.append(ice)
    dataList.append(shopRep)
    dataList.append(custRep)
    dataList.append(custLimit)
    dataList.append(shopIndex)
    dataList.append(upgradeIndex)
    dataList.append(openHour)
    dataList.append(closeHour)
    dataList.append(day)
    dataList.append(m)
    dataList.append(hour)
    dataList.append(minute)
    dataList.append(recomSellPrice)
    dataList.append(gameSpeed)
    dataList.append(weather)
    dataList.append(__version__)
    dataList.append(reportDelay)
    tmpStr = ''
    for ct in range(0,len(dataList)):
        tmpStr+=str(dataList[ct])+','
    tmpAds = ''; tmpList = []
    for ct in range(0,len(curAds)):
        tmpList = curAds[ct]
        for cnt in range(0,len(tmpList)):
            tmpAds+=str(tmpList[cnt])+','
    tmpStr+=tmpAds
    tmpStr = tmpStr[:-1]
    tmpStr = hexi(tmpStr)
    with open('data/'+user+__version__+'.txt','w') as file:
        file.write(tmpStr)
        print("Game Saved...")

# dics used for encoding save file
dicNum = {'0':'a','1':'b','2':'c','3':'d','4':'e','5':'f','6':'g','7':'h','8':'i','9':'j',
       'a':'10','b':'11','c':'12','d':'13','e':'14','f':'15','g':'16','h':'17','i':'18','j':'19',
       'k':'20','l':'21','m':'22','n':'23','o':'24','p':'25','q':'26','r':'27','s':'28','t':'29',
       'u':'30','v':'31','w':'32','x':'33','y':'34','z':'35','A':'36','B':'37','C':'38','D':'39',
       'E':'40','F':'41','G':'42','H':'43','I':'44','J':'45','K':'46','L':'47','M':'48','N':'49',
       'O':'50','P':'51','Q':'52','R':'53','S':'54','T':'55','U':'46','V':'57','W':'58','X':'59',
       'Y':'60','Z':'61','.':'*'
       }
dicTrans = {'a':'0','b':'1','c':'2','d':'3','e':'4','f':'5','g':'6','h':'7','i':'8','j':'9',
       '10':'a','11':'b','12':'c','13':'d','14':'e','15':'f','16':'g','17':'h','18':'i','19':'j',
       '20':'k','21':'l','22':'m','23':'n','24':'o','25':'p','26':'q','27':'r','28':'s','29':'t',
       '30':'u','31':'v','32':'w','33':'x','34':'y','35':'z','36':'A','37':'B','38':'C','39':'D',
       '40':'E','41':'F','42':'G','43':'H','44':'I','45':'J','46':'K','47':'L','48':'M','49':'N',
       '50':'0','51':'P','52':'Q','53':'R','54':'S','55':'T','56':'U','57':'V','58':'W','59':'X',
       '60':'Y','61':'Z','*':'.'
       }

print("LEMONADE STAND GAME");time.sleep(1)
# LOGIN
login = True
print('Attempting to login')
while login:
    user = input("Please enter your username: ")
    while not os.path.exists('data/'+user+__version__+'.txt'):
        print("No Info Found...")
        print('1. New Game')
        print('2. Try Again')
        tmpList = ['1','2']
        choice = input("Please choose and option: ")
        while choice not in tmpList:
            print("ERROR: Couldn't read choice...")
            choice = input("Please choose and option: ")
        if choice == '1':
            money = 250;price = 0.5;lemon = 100;sugar = 100
            cups = 50;ice = 400;shopRep = 0.1;custRep = 0.0
            custLimit = 10;shopIndex = 0;upgradeIndex = 0
            openHour = 10;closeHour = 4;day = 1;m = 'am'
            hour = openHour;minute = 0;gameTime = '';clockList = []
            recomSellPrice = 0.5;gameSpeed = float(1);weather = 'clear'
            reportDelay = 1
            curAds=[];saveGame()
            print("NEW GAME CREATED...");time.sleep(gameSpeed)
            login = False
            break
        elif choice == '2':
            user = input("Please enter your username: ")
    else:
        print("Loading save data...");time.sleep(1)
        with open('data/'+user+__version__+'.txt','r') as file:
            data = file.read();data=decode(data);lineList=data.split(',');dataList=[]
            for line in lineList:
                dataList.append(line)
            for ct in range(0,len(dataList)):
                tmp = dataList[ct]
            money = float(dataList[0]);price = float(dataList[1]);lemon = int(dataList[2])
            sugar = int(dataList[3]);cups = int(dataList[4]);ice = int(dataList[5])
            shopRep = float(dataList[6]);custRep = float(dataList[7]);custLimit = int(dataList[8])
            shopIndex = int(dataList[9]);upgradeIndex = int(dataList[10]);openHour = int(dataList[11])
            closeHour = int(dataList[12]);day = int(dataList[13]);m = str(dataList[14])
            hour = int(dataList[15]);minute = int(dataList[16]);recomSellPrice = float(dataList[17])
            gameSpeed = float(dataList[18]);weather = str(dataList[19]);v=dataList[20];reportDelay=dataList[21];curAds=[]
            # loading ads
            tmpIndex = (len(dataList)-22)
            steps = (tmpIndex/4);tmpAd=[]
            for ct in range(0,int(steps)):
                tmpAd=[dataList[22+(ct*4)],dataList[22+(ct*4)+1],dataList[22+(ct*4)+2],dataList[22+(ct*4)+3]]
                curAds.append(tmpAd)
            clockList = [];clockList = clockData(day,m,hour,minute)
            gameTime = clockList[4]
        if v != __version__:
            print("VERSION OUT OF DATE\n"*10)
        print('logged in')
        login = False
               
# vars
shopCost = [250,500,1000,1500,2500,5000,10000,50000,100000,500000,1000000]
upgradeCost = [25,50,100,250,500]
lemonPrice = 0.5
sugarPrice=0.05
cupPrice=0.1
icePrice=0.02

delay = 0.2

# Type, Cost, Dur(days), result(%)4
adList = [['Megazine','70','7','20'],['TV','150','4','60'],['Radio','95','5','35']]

# MAIN
run = True
while run:
    
    # get time
    hour=openHour
    clockList = clockData(day,m,hour,minute)
    day = clockList[0]
    m = clockList[1]
    hour = clockList[2]
    minute = clockList[3]
    gameTime = clockList[4]
    print()
    print(gameTime);time.sleep(gameSpeed)
    time.sleep(0.1)

    # request info
    print("Lets setup shop.");time.sleep(gameSpeed)
    menu = True
    while menu:
        print('='*30)
        print("\nMoney: $%.2f"%float(money))
        print("Weather: "+weather);print('');print('-'*30);print('');time.sleep(gameSpeed)
        print("1. Open Store")
        print("2. Buy Inventory")
        print("3. Upgrade Shop")
        print("4. Advertise")
        print("5. Shop Details")
        print("6. Close for the day")
        print("7. Settings")
        print("8. Save Game")
        print("9. Quit")
        menuList = ['1','2','3','4','5','6','7','8','9']
        option = input("Select Option: ");time.sleep(gameSpeed)
        while option not in menuList:
            print("ERROR: option must be a number...")
            option = input("Select Option: ");time.sleep(gameSpeed)
        if option == '1':
            print("Opening shop for the day...\n");time.sleep(gameSpeed)
            if testInventory(lemon-0.2,sugar-1,cups-1,ice-1):
                # Starting Day Clock
                hour = openHour;minute=0;Open = True; m = 'am'
                if hour >= closeHour and m == 'pm':
                    Open == False
                else:
                    Open == True
                clockList = clockData(day,m,hour,minute)
                day = clockList[0]
                m = clockList[1]
                hour = clockList[2]
                minute = clockList[3]
                gameTime = clockList[4]
                print(gameTime);print('-'*30+'\n')
                time.sleep(0.1);ask=True
                while Open:
                    # spawn customer
                    tmpAdList=[];tmpNum=10;adMod=float(0)
                    for ct in range(0,len(curAds)):
                        tmpAdList = curAds[ct]
                        adMod += float(tmpAdList[3])
                    mod = (adMod+(shopRep*100)+(custRep*100))
                    custs = (mod*10)*custLimit
                    ran = random.randint(1,3)
                    if ran == 1:
                        custs *= .8
                    elif ran == 3:
                        custs *= 1.2
                    custs = round(custs)
                    if custs > custLimit:
                        custs = custLimit
                    print("Customers: "+str(custs*int(reportDelay)));time.sleep(gameSpeed)
                    choiceList = [0,1,2]
                    closed = False
                    custDetur=0
                    for ct in range(0,int(reportDelay)):
                        if m == 'pm':
                            if (hour+int(reportDelay))>(int(closeHour)+int(reportDelay)):
                                closed = True
                        for ct in range(0,custs):
                            if m == 'pm':
                                if hour+1>(int(closeHour)):
                                    closed = False
                            if closed == False:
                                choice = random.choice(choiceList)
                                if choice == 0:
                                    if testHour(hour,m):
                                        if testWeather(weather):
                                            if testInventory(lemon-0.2,sugar-1,cups-1,ice-2):
                                                if checkPrice(price,recomSellPrice):
                                                    money += price
                                                    lemon -= 0.2
                                                    sugar -= 1
                                                    cups -= 1
                                                    ice -= 2
                                                    print("Lemonade sold for $"+str(price));time.sleep(gameSpeed/4)
                                                    num = random.randint(0,4)
                                                    if num == 2:
                                                        if custRep < 0.5: 
                                                            print("Customer Satisfaction Increased.");time.sleep(gameSpeed/8)
                                                            custRep+=0.02
                                                else:
                                                    print("Customer left due to prices being too high");time.sleep(gameSpeed/4)
                                                    if (custRep-0.05) >= 0:
                                                        custRep-=0.05
                                                        print("Customer Satisfaction Decreased.");time.sleep(gameSpeed/8)
                                            else:
                                                print("You are out of supplies...")
                                                print("CLOSING SHOP...");time.sleep(gameSpeed)
                                                if custRep > 0.1:
                                                    custRep -= 0.1
                                                    print("Customer Satisfaction Decreased.");time.sleep(gameSpeed/2)
                                                closed = True
                                                time.sleep(delay)
                                        else:
                                            custDetur+=1
                                elif choice == 1:
                                    if testHour(hour,m):
                                        if testWeather(weather):
                                            if testInventory(lemon-0.4,sugar-2,cups-2,ice-4):
                                                if checkPrice(price,recomSellPrice):
                                                    money += (price*2)
                                                    lemon -= 0.4
                                                    sugar -= 2
                                                    cups -= 2
                                                    ice -= 4
                                                    print("Lemonade sold for $"+str(price*2));time.sleep(gameSpeed/4)
                                                    num = random.randint(0,4)
                                                    if num == 2:
                                                        if custRep < 0.5:
                                                            print("Customer Satisfaction Increased.");time.sleep(gameSpeed/8)
                                                            custRep+=0.02
                                                else:
                                                    print("Customer left due to prices being too high");time.sleep(gameSpeed/4)
                                                    if (custRep-0.05) >= 0:
                                                        custRep-=0.05
                                                        print("Customer Satisfaction Decreased.");time.sleep(gameSpeed/8)
                                            else:
                                                print("You are out of supplies...")
                                                print("CLOSING SHOP...");time.sleep(gameSpeed)
                                                if custRep > 0.1:
                                                    custRep -= 0.1
                                                    print("Customer Satisfaction Decreased.");time.sleep(gameSpeed/2)
                                                closed = True;time.sleep(gameSpeed)
                                        else:
                                            custDetur+=2
                                elif choice == 2:
                                    ice -= 2
                                    print("...");time.sleep(gameSpeed)
                        hour+=1
                        clockList = clockData(day,m,hour,minute)
                        day = clockList[0]
                        m = clockList[1]
                        hour = clockList[2]
                        minute = clockList[3]
                        gameTime = clockList[4]
                        print('Time: '+str(hour)+':'+str(minute)+'0 '+str(m))
                        if m == 'pm':
                            if hour != 12:
                                if hour>=(int(closeHour)):
                                    closed = True
                                    break
                    if closed == False:
                        lemon = math.floor(lemon)
                        # time
                        print('\n'*1)
                        print('-'*30);print('Hourly Report');print('-'*30+'\n');time.sleep(gameSpeed)
                        clockList = clockData(day,m,hour,minute)
                        day = clockList[0]
                        m = clockList[1]
                        hour = clockList[2]
                        minute = clockList[3]
                        gameTime = clockList[4]
                        print(gameTime);print('-'*30);print('')
                        time.sleep(gameSpeed)
                        print("Money: $%.2f"%float(money))
                        print('Lemons: '+str(lemon))
                        print('Sugar: '+str(sugar)+' oz')
                        print('ice: '+str(ice)+' cubes')
                        print('cups: '+str(cups))
                        print("\nWeather: "+weather)
                        print('Customers Deturred By Weather: '+str(custDetur));print('');time.sleep(gameSpeed)
                        while ask:
                            print('1. Continue');print('2. Continue, Do not ask again');print('3. Close Early\n')
                            choice = input("Select Option: ");time.sleep(gameSpeed)
                            choiceList = ['1','2','3']
                            while choice not in choiceList:
                                print("ERROR: Must enter a number...")
                                choice = input("Select Option: ");time.sleep(gameSpeed)
                            if choice == '1':
                                break
                            if choice == '2':
                                ask = False
                            if choice == '3':
                                print("Closing Shop...");time.sleep(gameSpeed)
                                Open = False
                                break
                        if hour >= closeHour and m == 'pm':
                            Open = False
                    else:
                        print('-'*30);print('CLOSING...');print('-'*30+'\n\n');time.sleep(gameSpeed)
                        lemon = round(lemon)
                        print("Money: $%.2f"%float(money))
                        print('Lemons: '+str(lemon))
                        print('Sugar: '+str(sugar)+' oz')
                        print('ice: '+str(ice)+' cubes')
                        print('cups: '+str(cups)+'\n');time.sleep(gameSpeed)
                        break
                else: # Closed
                    print('-'*30);print('CLOSING...');print('-'*30+'\n\n');time.sleep(gameSpeed)
                    lemon = round(lemon)
                    print("Money: $%.2f"%float(money))
                    print('Lemons: '+str(lemon))
                    print('Sugar: '+str(sugar)+' oz')
                    print('ice: '+str(ice)+' cubes')
                    print('cups: '+str(cups));print('');time.sleep(gameSpeed)
            #calc ads
            days = 0
            for ct in range(0,len(curAds)):
                tmpList = curAds[ct]
                days = tmpList[2]
                days = int(days)-1
                if days < 0:
                    curAds.pop(ct)
                    print("Campaign Ended...");time.sleep(gameSpeed/2)
                else:
                    tmpList[2] = days; curAds[ct] = tmpList
                    print(str(tmpList[0])+": "+str(tmpList[2])+" days left");time.sleep(gameSpeed/2)
            else:
                if testInventory(lemon-0.2,sugar-1,cups-1,ice-1) == False:
                    print("You are out of supplies...\n");time.sleep(gameSpeed)
            day+=1
            clockList = clockData(day,m,hour,minute)
            day = clockList[0]
            m = clockList[1]
            hour = clockList[2]
            minute = clockList[3]
            gameTime = clockList[4]
            print(gameTime+'\n');time.sleep(gameSpeed/2)
            weather = getWeather()
        elif option == '2':
            print("Buying inventory...");time.sleep(gameSpeed)
            print('-'*30);print('Inventory');print('-'*30);print('')
            print('Lemons: '+str(lemon))
            print('Sugar: '+str(sugar)+' oz')
            print('Ice: '+str(ice)+' cubes')
            print('Cups: '+str(cups));print('');time.sleep(gameSpeed)
            subMenu = True
            while subMenu:
                print("Money: $%.2f"%float(money))
                print("1. Buy Lemons $%.2f"%float(lemonPrice))
                print("2. Buy Sugar $%.2f"%float(sugarPrice))
                print("3. Buy Ice $%.2f"%float(icePrice))
                print("4. Buy Cups $%.2f"%float(cupPrice))
                print("5. Back")
                menuList = ['1','2','3','4','5']
                option = input("Select Option: ");time.sleep(gameSpeed)
                while option not in menuList:
                    print("ERROR: option must be a number...")
                    option = input("Select Option: ");time.sleep(gameSpeed)
                if option == '1':
                    print('');print('-'*30);print('')
                    print("Buying Lemons...");time.sleep(gameSpeed)
                    amount = input("Amount: ");time.sleep(gameSpeed)
                    while is_number(amount) == False:
                        print("ERROR: option must be a number...")
                        amount = input("Amount: ");time.sleep(gameSpeed)
                    else:
                        while priceCheck(amount,lemonPrice,money) == False:
                            print("You can't afford that...");time.sleep(gameSpeed)
                            break
                        else:
                            cost = lemonPrice * int(amount)  
                            money = float(float(money) - float(cost))
                            lemon += int(amount);print('')
                            print("Cost: $%.2f"%float(cost))
                            print("Money: $%.2f"%float(money))
                            print("Lemons: "+str(lemon));print('');time.sleep(gameSpeed)
                    break
                elif option == '2':
                    print('');print('-'*30);print('')
                    print("Buying Sugar...");time.sleep(gameSpeed)
                    amount = input("Amount: ");time.sleep(gameSpeed)
                    while is_number(amount) == False:
                        print("ERROR: option must be a number...")
                        amount = input("Amount: ");time.sleep(gameSpeed)
                    else:
                        while priceCheck(amount,sugarPrice,money) == False:
                            print("You can't afford that...");time.sleep(gameSpeed)
                            break
                        else:
                            cost = sugarPrice * int(amount)
                            money = float(float(money) - float(cost))
                            sugar += int(amount);print('')
                            print("Cost: $%.2f"%float(cost))
                            print("Money: $%.2f"%float(money))
                            print("Sugar: "+str(sugar));print('');time.sleep(gameSpeed)
                    break
                elif option == '3':
                    print('');print('-'*30);print('')
                    print("Buying Ice...");time.sleep(gameSpeed)
                    amount = input("Amount: ");time.sleep(gameSpeed)
                    while is_number(amount) == False:
                        print("ERROR: option must be a number...")
                        amount = input("Amount: ");time.sleep(gameSpeed)
                    else:
                        while priceCheck(amount,icePrice,money) == False:
                            print("You can't afford that...");time.sleep(gameSpeed)
                            break
                        else:
                            cost = icePrice * int(amount)
                            money = float(float(money) - float(cost))
                            ice += int(amount);print('')
                            print("Cost: $%.2f"%float(cost))
                            print("Money: $%.2f"%float(money))
                            print("Ice: "+str(ice));print('');time.sleep(gameSpeed)
                    break
                elif option == '4':
                    print('');print('-'*30);print('')
                    print("Buying Cups...");time.sleep(gameSpeed)
                    amount = input("Amount: ");time.sleep(gameSpeed)
                    while is_number(amount) == False:
                        print("ERROR: option must be a number...")
                        amount = input("Amount: ");time.sleep(gameSpeed)
                    else:
                        while priceCheck(amount,cupPrice,money) == False:
                            print("You can't afford that...");time.sleep(gameSpeed)
                            break
                        else:
                            cost = cupPrice * int(amount)
                            money = float(float(money) - float(cost))
                            cups += int(amount);print('')
                            print("Cost: $%.2f"%float(cost))
                            print("Money: $%.2f"%float(money))
                            print("Cups: "+str(cups));print('');time.sleep(gameSpeed)
                    break
                elif option == '5':
                    print('')
                    break
        elif option == '3':
            print("Upgrading shop...\n")
            cost = upgradeCost[upgradeIndex];cost = cost*(shopIndex+1) 
            print("1. Upgrade Current Stand: $%.2f"%float(cost))
            cost = shopCost[shopIndex]
            print("2. Buy New Stand: $%.2f"%float(cost))
            print("3. Back")
            menuList = ['1','2','3']
            option = input("Select Option: ");time.sleep(gameSpeed)
            while option not in menuList:
                print("ERROR: option must be a number...")
                option = input("Select Option: ");time.sleep(gameSpeed)
            print('')
            if option == '1':
                if upgradeIndex == len(upgradeCost):
                    print("You have already upgraded this shop to it's limit.")
                    print("Consider upgrading to a new shop.");time.sleep(gameSpeed)
                else:
                    cost = upgradeCost[upgradeIndex]
                    cost = cost*(shopIndex+1)
                    print("Money: $%.2f"%float(money))
                    print("Upgrad Current Stand: $%.2f"%float(cost))
                    choiceList=['y','n']
                    choice = input("Would you like to upgrade? [y/n]: ");time.sleep(gameSpeed)
                    while choice not in choiceList:
                        print("ERROR: option must be 'y' or 'n'")
                        choice = input("Would you like to upgrade shop? [y/n]: ");time.sleep(gameSpeed)
                    if choice == 'y':
                        if (money - cost) < 0:
                            print("You cannot afford this upgrade\n");time.sleep(gameSpeed)
                            print('-'*30+'\n')
                        else:
                            money -= cost
                            upgradeIndex += 1
                            shopRep += (upgradeIndex*.1)
                            custRep += 0.1
                            recomSellPrice += 0.1
                            print("Customer Satisfaction Increased.")
                            print("\nCost: $%.2f"%float(cost))
                            print("Money: $%.2f"%float(money))
                            print("Increased shop popularity\n")
                            print('-'*30+'\n');time.sleep(gameSpeed)
                    else:
                        continue
            elif option == '2':
                cost = shopCost[shopIndex]
                print("Money: $%.2f"%float(money))
                print("New Stand Upgrade: $%.2f"%float(cost))
                choiceList=['y','n']
                choice = input("Would you like to upgrade? [y/n]: ");time.sleep(gameSpeed)
                while choice not in choiceList:
                    print("ERROR: option must be 'y' or 'n'")
                    choice = input("Would you like to upgrade? [y/n]: ");time.sleep(gameSpeed)
                if choice == 'y':
                    if (money - cost) < 0:
                        print("You cannot afford this upgrade\n")
                        print('-'*30+'\n');time.sleep(gameSpeed)
                    else:
                        money -= cost
                        upgradeIndex = 0
                        shopIndex += 1
                        custLimit += (shopIndex*10)
                        custRep += 0.1
                        recomSellPrice += 0.5
                        print("Customer Satisfaction Increased.")
                        print("\nCost: $%.2f"%float(cost))
                        print("Money: $%.2f"%float(money))
                        print("New Customer Limit: "+str(custLimit)+'\n')
                        print('-'*30+'\n');time.sleep(gameSpeed)
                else:
                    continue
            elif option == '3':
                print('\n');time.sleep(gameSpeed)
        elif option == '4':
            print("\n\nLooking up advertising...");time.sleep(gameSpeed)
            print('-'*30);print('Advertising');print('-'*30);print('')
            print("Current  Ads:")
            for ct in range(0,len(curAds)):
                tmpList = curAds[ct]
                print("  > "+str(tmpList[0])+"  - Days Left: "+str(tmpList[2]))
            time.sleep(gameSpeed)
            print("\nMoney: $%.2f"%float(money))
            print("Ad Campaign's Available:");adTmpList = []
            for ct in range(0,len(adList)):
                tmpList = adList[ct]
                adTmpList.append(tmpList[0])
            choiceList = [];moneyList = ['70','150','95']
            for ct in range(0,len(adTmpList)):
                print('  '+str(ct+1)+'. '+str(adTmpList[ct])+"  $"+str(moneyList[ct]))
                choiceList.append(str(ct+1))
            choiceList.append(str(len(adTmpList)+1))
            print("  4. Back")
            print('');option = input("Select Option: ");time.sleep(gameSpeed)
            while option not in choiceList:
                print("ERROR: option must be a number...")
                option = input("Select Option: ");time.sleep(gameSpeed)
            if option == '1':
                tmpList = adList[0]; cost = tmpList[1]
                print('Price: $'+str(cost)+'\n');time.sleep(gameSpeed)
                if (money - int(cost)) < 0:
                    print('You cannot afford this campaign...\n')
                    print('');print('');print('-'*30);print('');time.sleep(gameSpeed)
                    break
                else:
                    money = float(float(money) - float(cost))
                    curAds.append(adList[0])
                    print('Megazine campaign started for 7 days')
                    print('Cost: $%.2f'%float(cost)+'\n');time.sleep(gameSpeed)
            elif option == '2':
                tmpList = adList[1]; cost = tmpList[1]
                print('Price: $'+str(cost)+'\n');time.sleep(gameSpeed)
                if (money - int(cost)) < 0:
                    print('You cannot afford this campaign...\n')
                    print('');print('');print('-'*30);print('');time.sleep(gameSpeed)
                    break
                else:
                    money = float(float(money) - float(cost))
                    curAds.append(adList[1])
                    print('TV campaign started for 4 days\n');time.sleep(gameSpeed)
            elif option == '3':
                tmpList = adList[2]; cost = tmpList[1]
                print('Price: $'+str(cost)+'\n');time.sleep(gameSpeed)
                if (money - int(cost)) < 0:
                    print('You cannot afford this campaign...\n')
                    print('');print('');print('-'*30);print('');time.sleep(gameSpeed)
                    break
                else:
                    money = float(float(money) - float(cost));time.sleep(gameSpeed)
                    curAds.append(adList[2])
                    print('Radio campaign started for 7 days\n');time.sleep(gameSpeed)
            elif option == '4':
                print('')
                break
        elif option == '5':
            print('\n'*30)
            print('\n'+'='*30+'\n')
            print("Money: $%.2f"%float(money)+'\n')
            print("Lemonade sell price: $%.2f"%float(price))
            if int(shopIndex) > 1:
                print("Recommended selling price: $%.2f"%float(recomSellPrice))
            print("\nINVENTORY");print('-'*30)
            print('Lemons: '+str(lemon))
            print('Sugar: '+str(sugar)+' oz')
            print('Ice: '+str(ice)+' cubes')
            print('Cups: '+str(cups)+'\n')
            print('-'*30)
            print('Customer Limit: '+str(custLimit))
            print('Shop Reputation Bonus: %.0f'%float(shopRep*100)+'%')
            print('Customer Satisfaction Bonus: %.0f'%float(custRep*100)+'%');print('')
            print('Shop: '+str(shopIndex+1)+'/'+str(len(shopCost)+1))
            print('Shop Upgrade: '+str(upgradeIndex)+'/'+str(len(upgradeCost)));print('')
            print('Open Hour: '+str(openHour)+":00 am")
            print('Close Hour: '+str(closeHour)+":00 pm\n")
            if int(reportDelay)==1:
                print('Report Delay: '+str(reportDelay)+' hour\n')
            else:
                print('Report Delay: '+str(reportDelay)+' hours\n')
            print('-'*30)
            print("Current  Ads:")
            if len(curAds) == 0:
                print("  > NONE")
            else:
                for ct in range(0,len(curAds)):
                    tmpList = curAds[ct]
                    print("  > "+str(tmpList[0])+"  - Days Left: "+str(tmpList[2]))
            print('\n'+'='*30)
            choice = input("Continue: ");time.sleep(gameSpeed)
        elif option == '6':
            day+=1
            print("Closing shop for the day...\n");days=0
            if len(curAds) > 0:
                for ct in range(0,len(curAds)):
                    tmpList = curAds[ct]
                    days = tmpList[2]
                    days = int(days)-1
                    if days < 0:
                        curAds.pop(ct)
                        print("Campaign Ended...")
                    else:
                        tmpList[2] = days; curAds[ct] = tmpList
                        print(str(tmpList[0])+": "+str(tmpList[2])+" days left")
                else:
                    if testInventory(lemon-0.2,sugar-1,cups-1,ice-1) == False:
                        print("You are out of supplies...\n");time.sleep(gameSpeed)
            clockList = clockData(day,m,hour,minute)
            day = clockList[0]
            m = clockList[1]
            hour = clockList[2]
            minute = clockList[3]
            gameTime = clockList[4]
            print(gameTime+'\n');time.sleep(gameSpeed/2)
            weather = getWeather()
        elif option == '7':
            print('\n'+'-'*30);print('Settings\n'+'-'*30)
            print('1. Lemonade Price')
            print('2. Game Speed')
            print('3. Report Delay')
            print('4. Store Open Hour')
            print('5. Store Closing Hour')
            print('6. Back')
            menuList = ['1','2','3','4','5','6']
            option = input("Select Option: ");time.sleep(gameSpeed)
            while option not in menuList:
                print("ERROR: option must be a number...")
                option = input("Select Option: ");time.sleep(gameSpeed)
            if option == '1':
                print('Current Lemonade Price: $%.2f'%float(price))
                tmp = input('New Lemonade Price: ');time.sleep(gameSpeed)
                while testFloat(tmp)==False:
                    print("ERROR: option must be a number")
                    tmp = input('New Lemonade Price: ');time.sleep(gameSpeed)
                price = float(tmp)
                print('Lemonade price set to: '+str(price));time.sleep(gameSpeed)
            elif option == '2':
                print('Current Game Speed: '+str(gameSpeed))
                tmp = input('New Game Speed: ');time.sleep(gameSpeed)
                while testFloat(tmp)==False:
                    print("ERROR: option must be a number")
                    tmp = input('New Game Speed: ');time.sleep(gameSpeed)
                gameSpeed = float(tmp)
                print('Game Speed set to: '+str(gameSpeed));time.sleep(gameSpeed)
            elif option == '3':
                print('Current Report Delay: '+str(reportDelay))
                tmp = input('New Report Delay: ');time.sleep(gameSpeed)
                while testInt(tmp) == False:
                    print("ERROR: option must be a number")
                    tmp = input('New Report Delay: ');time.sleep(gameSpeed)
                reportDelay = int(tmp)
                print('Report Delay set to: '+str(reportDelay));time.sleep(gameSpeed)
            elif option == '4':
                print('Current Open Hour: '+str(openHour))
                tmp = input("New Open Hour Time: ");time.sleep(gameSpeed)
                tmpList = ['6','7','8','9','10','11']
                while tmp not in tmpList:
                    print("Must be an hour between 6-11")
                    tmp = input("New Open Hour Time: ");time.sleep(gameSpeed)
                openHour = int(tmp)
                print('Open Hour set to: '+str(openHour));time.sleep(gameSpeed)
            elif option == '5':
                print('Current Closing Hour: '+str(closeHour))
                tmp = input("New Closing Hour Time: ");time.sleep(gameSpeed)
                tmpList = ['12','1','2','3','4','5','6','7','8','9','10','11']
                while tmp not in tmpList:
                    print("Must be an hour between 12-11")
                    tmp = input("New Closing Hour Time: ");time.sleep(gameSpeed)
                closeHour = int(tmp)
                print('Closing Hour set to: '+str(closeHour));time.sleep(gameSpeed)
            elif option == '6':
                continue
        elif option == '8':
            saveGame();time.sleep(gameSpeed)
        elif option == '9':
            choiceList=['y','n']
            choice = input("Would you like to save before quiting? [y/n]: ");time.sleep(gameSpeed)
            while choice not in choiceList:
                print("ERROR: option must be 'y' or 'n'")
                choice = input("Would you like to save before quiting? [y/n]: ");time.sleep(gameSpeed)
            if choice == 'y':
                saveGame();time.sleep(gameSpeed)
            menu = False
            run = False
print('done')
    

    
