"""
Name: lemonadeStand.py
Description: Game of Selling Lemonade
"""

__author__ = "Spencer Dockham"
__date__ = "12/14/2014"
__version__ = '1.0.5'

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

def clockData(pace,day,m,hour,minute):
    if minute > 5:
        minute = 0
        hour += 1
    if hour > 12:
        hour = 1
        if m == 'am':
            m = 'pm'
        else:
            day += 1
            m = 'am'
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
    with open('data\dataV'+__version__+'.txt','w') as file:
        file.write(tmpStr)
        print("Game Saved...")

# LOAD DATA
money = 250;price = 0.5;lemon = 100;sugar = 100;cups = 50;ice = 400;shopRep = 0.1
custRep = 0.0;custLimit = 10;shopIndex = 0;upgradeIndex = 0;openHour = 10;closeHour = 4
day = 1;m = 'am';hour = openHour;minute = 0;gameTime = '';clockList = [];pace = 1

if not os.path.exists('data\dataV'+__version__+'.txt'):
    print("No Save Data Found...")
    money = 250
    price = 0.5
    lemon = 100
    sugar = 100
    cups = 50
    ice = 400
    shopRep = 0.1
    custRep = 0.0
    custLimit = 10
    shopIndex = 0
    upgradeIndex = 0
    openHour = 10
    closeHour = 4
    day = 1
    m = 'am'
    hour = openHour
    minute = 0
    gameTime = ''
    clockList = []
    pace = 1
    recomSellPrice = 0.5
    curAds=[]
    saveGame()
    print("NEW GAME CREATED...")
else:
    print("Loading save data...")
    with open('data\dataV'+__version__+'.txt','r') as file:
        data = file.read()
        lineList=data.split(',')
        dataList=[]
        for line in lineList:
            dataList.append(line)
        money = float(dataList[0])
        price = float(dataList[1])
        lemon = int(dataList[2])
        sugar = int(dataList[3])
        cups = int(dataList[4])
        ice = int(dataList[5])
        shopRep = float(dataList[6])
        custRep = float(dataList[7])
        custLimit = int(dataList[8])
        shopIndex = int(dataList[9])
        upgradeIndex = int(dataList[10])
        openHour = int(dataList[11])
        closeHour = int(dataList[12])
        day = int(dataList[13])
        m = str(dataList[14])
        hour = int(dataList[15])
        minute = int(dataList[16])
        recomSellPrice = float(dataList[17])
        curAds=[]
        # loading ads
        tmpIndex = (len(dataList)-18)
        steps = (tmpIndex/4);tmpAd=[]
        for ct in range(0,int(steps)):
            tmpAd=[dataList[17+(ct*4)],dataList[17+(ct*4)+1],dataList[17+(ct*4)+2],dataList[17+(ct*4)+3]]
            curAds.append(tmpAd)
        clockList = []
        clockList = clockData(pace,day,m,hour,minute)
        gameTime = clockList[4]
        pace = 1
               
# vars
shopCost = [250,500,1000,1500,2500]
upgradeCost = [25,50,100,250,500]
lemonPrice = 0.5
sugarPrice=0.05
cupPrice=0.1
icePrice=0.2

recomSellPrice = 0.5

delay = 0.2

# Type, Cost, Dur(days), result(%)4
adList = [['Megazine','70','7','20'],['TV','150','4','60'],['Radio','95','5','35']]

# MAIN
run = True
while run:
    
    # get time
    clockList = clockData(pace,day,m,hour,minute)
    day = clockList[0]
    m = clockList[1]
    hour = clockList[2]
    minute = clockList[3]
    gameTime = clockList[4]
    print(gameTime)
    time.sleep(0.1)

    # request info
    print("Lets setup shop.")
    print("Money: $%.2f"%float(money))
    print("Weather: Clear");print('');print('-'*30);print('')
    menu = True
    while menu:
        print("1. Buy Inventory")
        print("2. Advertise")
        print("3. Upgrade Shop")
        print("4. Open Store")
        print("5. Close for the day")
        print("6. Shop Details")
        print("7. Settings")
        print("8. Save Game")
        print("9. Quit")
        menuList = ['1','2','3','4','5','6','7','8','9']
        option = input("Select Option: ")
        while option not in menuList:
            print("ERROR: option must be a number...")
            option = input("Select Option: ")
        if option == '1':
            print("Buying inventory...")
            print('-'*30);print('Inventory');print('-'*30);print('')
            print('Lemons: '+str(lemon))
            print('Sugar: '+str(sugar)+' oz')
            print('Ice: '+str(ice)+' cubes')
            print('Cups: '+str(cups));print('')
            subMenu = True
            while subMenu:
                print("Money: $%.2f"%float(money))
                print("1. Buy Lemons $%.2f"%float(lemonPrice))
                print("2. Buy Sugar $%.2f"%float(sugarPrice))
                print("3. Buy Ice $%.2f"%float(icePrice))
                print("4. Buy Cups $%.2f"%float(cupPrice))
                print("5. Back")
                menuList = ['1','2','3','4','5']
                option = input("Select Option: ")
                while option not in menuList:
                    print("ERROR: option must be a number...")
                    option = input("Select Option: ")
                if option == '1':
                    print('');print('-'*30);print('')
                    print("Buying Lemons...")
                    amount = input("Amount: ")
                    while is_number(amount) == False:
                        print("ERROR: option must be a number...")
                        amount = input("Amount: ")
                    else:
                        while priceCheck(amount,lemonPrice,money) == False:
                            print("You can't afford that...")
                            break
                        else:
                            cost = lemonPrice * int(amount)  
                            money = float(float(money) - float(cost))
                            lemon += int(amount);print('')
                            print("Cost: $%.2f"%float(cost))
                            print("Money: $%.2f"%float(money))
                            print("Lemons: "+str(lemon));print('')
                    break
                elif option == '2':
                    print('');print('-'*30);print('')
                    print("Buying Sugar...")
                    amount = input("Amount: ")
                    while is_number(amount) == False:
                        print("ERROR: option must be a number...")
                        amount = input("Amount: ")
                    else:
                        while priceCheck(amount,sugarPrice,money) == False:
                            print("You can't afford that...")
                            break
                        else:
                            cost = sugarPrice * int(amount)
                            money = float(float(money) - float(cost))
                            sugar += int(amount);print('')
                            print("Cost: $%.2f"%float(cost))
                            print("Money: $%.2f"%float(money))
                            print("Sugar: "+str(sugar));print('')
                    break
                elif option == '3':
                    print('');print('-'*30);print('')
                    print("Buying Ice...")
                    amount = input("Amount: ")
                    while is_number(amount) == False:
                        print("ERROR: option must be a number...")
                        amount = input("Amount: ")
                    else:
                        while priceCheck(amount,icePrice,money) == False:
                            print("You can't afford that...")
                            break
                        else:
                            cost = icePrice * int(amount)
                            money = float(float(money) - float(cost))
                            ice += int(amount);print('')
                            print("Cost: $%.2f"%float(cost))
                            print("Money: $%.2f"%float(money))
                            print("Ice: "+str(ice));print('')
                    break
                elif option == '4':
                    print('');print('-'*30);print('')
                    print("Buying Cups...")
                    amount = input("Amount: ")
                    while is_number(amount) == False:
                        print("ERROR: option must be a number...")
                        amount = input("Amount: ")
                    else:
                        while priceCheck(amount,cupPrice,money) == False:
                            print("You can't afford that...")
                            break
                        else:
                            cost = cupPrice * int(amount)
                            money = float(float(money) - float(cost))
                            cups += int(amount);print('')
                            print("Cost: $%.2f"%float(cost))
                            print("Money: $%.2f"%float(money))
                            print("Cups: "+str(cups));print('')
                    break
                elif option == '5':
                    print('')
                    break
        elif option == '2':
            print("\n\nLooking up advertising...")
            print('-'*30);print('Advertising');print('-'*30);print('')
            print("Current  Ads:")
            for ct in range(0,len(curAds)):
                tmpList = curAds[ct]
                print("  > "+str(tmpList[0])+"  - Days Left: "+str(tmpList[2]))
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
            print('');option = input("Select Option: ")
            while option not in choiceList:
                print("ERROR: option must be a number...")
                option = input("Select Option: ")
            if option == '1':
                tmpList = adList[0]; cost = tmpList[1]
                print('Price: $'+str(cost)+'\n')
                if (money - int(cost)) < 0:
                    print('You cannot afford this campaign...\n')
                    print('');print('');print('-'*30);print('')
                    break
                else:
                    money = float(float(money) - float(cost))
                    curAds.append(adList[0])
                    print('Megazine campaign started for 7 days')
                    print('Cost: $%.2f'%float(cost)+'\n')
            elif option == '2':
                tmpList = adList[1]; cost = tmpList[1]
                print('Price: $'+str(cost)+'\n')
                if (money - int(cost)) < 0:
                    print('You cannot afford this campaign...\n')
                    print('');print('');print('-'*30);print('')
                    break
                else:
                    money = float(float(money) - float(cost))
                    curAds.append(adList[1])
                    print('TV campaign started for 4 days\n')
            elif option == '3':
                tmpList = adList[2]; cost = tmpList[1]
                print('Price: $'+str(cost)+'\n')
                if (money - int(cost)) < 0:
                    print('You cannot afford this campaign...\n')
                    print('');print('');print('-'*30);print('')
                    break
                else:
                    money = float(float(money) - float(cost))
                    curAds.append(adList[2])
                    print('Radio campaign started for 7 days\n')
            elif option == '4':
                print('')
                break
        elif option == '3':
            print("Upgrading shop...\n")
            print("1. Upgrade Current Stand")
            print("2. Buy New Stand")
            print("3. Back")
            menuList = ['1','2','3']
            option = input("Select Option: ")
            while option not in menuList:
                print("ERROR: option must be a number...")
                option = input("Select Option: ")
            print('')
            if option == '1':
                if upgradeIndex == len(upgradeCost):
                    print("You have already upgraded this shop to it's limit.")
                    print("Consider upgrading to a new shop.")
                else:
                    cost = upgradeCost[upgradeIndex]
                    print("Money: $%.2f"%float(money))
                    print("Upgrad Current Stand: $%.2f"%float(cost))
                    choiceList=['y','n']
                    choice = input("Would you like to upgrade? [y/n]: ")
                    while choice not in choiceList:
                        print("ERROR: option must be 'y' or 'n'")
                        choice = input("Would you like to upgrade shop? [y/n]: ")
                    if choice == 'y':
                        if (money - cost) < 0:
                            print("You cannot afford this upgrade\n")
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
                            print('-'*30+'\n')
                    else:
                        continue
            elif option == '2':
                cost = shopCost[shopIndex]
                print("Money: $%.2f"%float(money))
                print("New Stand Upgrade: $%.2f"%float(cost))
                choiceList=['y','n']
                choice = input("Would you like to upgrade? [y/n]: ")
                while choice not in choiceList:
                    print("ERROR: option must be 'y' or 'n'")
                    choice = input("Would you like to upgrade? [y/n]: ")
                if choice == 'y':
                    if (money - cost) < 0:
                        print("You cannot afford this upgrade\n")
                        print('-'*30+'\n')
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
                        print('-'*30+'\n')
                else:
                    continue
            elif option == '3':
                print('\n')
            
        elif option == '4':
            print("Opening shop for the day...\n")
            if testInventory(lemon-0.2,sugar-1,cups-1,ice-1):
                # Starting Day Clock
                hour = openHour;minute=0;Open = True; m = 'am'
                if hour >= closeHour and m == 'pm':
                    Open == False
                else:
                    Open == True
                clockList = clockData(pace,day,m,hour,minute)
                day = clockList[0]
                m = clockList[1]
                hour = clockList[2]
                minute = clockList[3]
                gameTime = clockList[4]
                print(gameTime);print('-'*30+'\n')
                time.sleep(0.1);ask=True
                while Open:
                    # spawn customer
                    tmpList=[];tmpNum=10
                    for ct in range(0,len(curAds)):
                        tmpList = curAds[ct]
                        tmpNum += float(tmpList[3])
                    popMod = tmpNum/100
                    custs = (popMod+shopRep+custRep)*100
                    ran = random.randint(1,3)
                    if ran == 1:
                        custs *= .8
                    elif ran == 3:
                        custs *= 1.2
                    custs = round(custs)
                    if custs > custLimit:
                        custs = custLimit
                    print("Customers: "+str(custs))
                    choiceList = [0,1,2]
                    closed = False
                    for ct in range(0,custs):
                        if closed == False:
                            choice = random.choice(choiceList)
                            if choice == 0:
                                if testInventory(lemon-0.2,sugar-1,cups-1,ice-1):
                                    if checkPrice(price,recomSellPrice):
                                        money += price
                                        lemon -= 0.2
                                        sugar -= 1
                                        cups -= 1
                                        ice -= 4
                                        print("Lemonade sold for $"+str(price))
                                        num = random.randint(0,4)
                                        if num == 2:
                                            if custRep < 0.5: 
                                                print("Customer Satisfaction Increased.")
                                                custRep+=0.02
                                    else:
                                        print("Customer left due to prices being too high")
                                else:
                                    print("You are out of supplies...")
                                    print("CLOSING SHOP...");time.sleep(delay*3)
                                    if custRep > 0.1:
                                        custRep -= 0.1
                                        print("Customer Satisfaction Decreased.")
                                    closed = True
                                    time.sleep(delay)
                            elif choice == 1:
                                if testInventory(lemon-0.2,sugar-1,cups-1,ice-1):
                                    if checkPrice(price,recomSellPrice):
                                        money += (price*2)
                                        lemon -= 0.4
                                        sugar -= 2
                                        cups -= 2
                                        ice -= 8
                                        print("Lemonade sold for $"+str(price*2))
                                        num = random.randint(0,4)
                                        if num == 2:
                                            if custRep < 0.5:
                                                print("Customer Satisfaction Increased.")
                                                custRep+=0.02
                                    else:
                                        print("Customer left due to prices being too high")
                                else:
                                    print("You are out of supplies...")
                                    print("CLOSING SHOP...");time.sleep(delay*3)
                                    if custRep > 0.1:
                                        custRep -= 0.1
                                        print("Customer Satisfaction Decreased.")
                                    closed = True
                                    time.sleep(delay)
                            elif choice == 2:
                                ice -= 2
                                print("...")
                                time.sleep(delay)
                        else:
                            money = money
                    if closed == False:
                        lemon = math.floor(lemon)
                        # time
                        print('\n'*1)### NEW LINES ###
                        print('-'*30);print('Hourly Report');print('-'*30+'\n');hour+=1
                        time.sleep(delay*3)
                        clockList = clockData(pace,day,m,hour,minute)
                        day = clockList[0]
                        m = clockList[1]
                        hour = clockList[2]
                        minute = clockList[3]
                        gameTime = clockList[4]
                        print(gameTime);print('-'*30);print('')
                        time.sleep(0.1)
                        print("Money: $%.2f"%float(money))
                        print('Lemons: '+str(lemon))
                        print('Sugar: '+str(sugar)+' oz')
                        print('ice: '+str(ice)+' cubes')
                        print('cups: '+str(cups));print('')
                        while ask:
                            print('1. Continue');print('2. Close Early');print('3. Continue, Do not ask again \n')
                            choice = input("Select Option: ")
                            choiceList = ['1','2','3']
                            while choice not in choiceList:
                                print("ERROR: Must enter a number...")
                                choice = input("Select Option: ")
                            if choice == '1':
                                break
                            if choice == '2':
                                print("Closing Shop...")
                                Open = False
                                break
                            if choice == '3':
                                ask = False
                        if hour >= closeHour and m == 'pm':
                            Open = False
                    else:
                        print('-'*30);print('CLOSING...');print('-'*30+'\n\n')
                        lemon = round(lemon)
                        print("Money: $%.2f"%float(money))
                        print('Lemons: '+str(lemon))
                        print('Sugar: '+str(sugar)+' oz')
                        print('ice: '+str(ice)+' cubes')
                        print('cups: '+str(cups)+'\n')
                        break
                else: # Closed
                    print('-'*30);print('CLOSING...');print('-'*30+'\n\n')
                    lemon = round(lemon)
                    print("Money: $%.2f"%float(money))
                    print('Lemons: '+str(lemon))
                    print('Sugar: '+str(sugar)+' oz')
                    print('ice: '+str(ice)+' cubes')
                    print('cups: '+str(cups));print('')
            #calc ads
            days = 0
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
                    print("You are out of supplies...\n");time.sleep(delay*3)
            day+=1
            clockList = clockData(pace,day,m,hour,minute)
            day = clockList[0]
            m = clockList[1]
            hour = clockList[2]
            minute = clockList[3]
            gameTime = clockList[4]
            print(gameTime+'\n')
        elif option == '5':
            day+=1
            print("Closing shop for the day...\n");days = 0
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
                        print("You are out of supplies...\n");time.sleep(delay*3)
            clockList = clockData(pace,day,m,hour,minute)
            day = clockList[0]
            m = clockList[1]
            hour = clockList[2]
            minute = clockList[3]
            gameTime = clockList[4]
            print(gameTime+'\n')
        elif option == '6':
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
            print('Shop Reputation Bonus: '+str(shopRep*100)+'%')
            print('Customer Satisfaction Bonus: %.1f'%float(custRep*100)+'%');print('')
            print('Shop: '+str(shopIndex+1)+'/'+str(len(shopCost)+1))
            print('Shop Upgrade: '+str(upgradeIndex)+'/'+str(len(upgradeCost)));print('')
            print('Open Hour: '+str(openHour)+":00 am")
            print('Close Hour: '+str(closeHour)+":00 pm\n")
            print('-'*30)
            print("Current  Ads:")
            if len(curAds) == 0:
                print("  > NONE")
            else:
                for ct in range(0,len(curAds)):
                    tmpList = curAds[ct]
                    print("  > "+str(tmpList[0])+"  - Days Left: "+str(tmpList[2]))
            print('\n'+'='*30)
            choice = input("Continue: ")
        elif option == '7':
            print('\n'+'-'*30);print('Settings\n'+'-'*30)
            print('1. Lemonade Price')
            print('2. Game Speed')
            menuList = ['1','2']
            option = input("Select Option: ")
            while option not in menuList:
                print("ERROR: option must be a number...")
                option = input("Select Option: ")
            if option == '1':
                checking = True
                print('Current Lemonade Price: $%.2f'%float(price))
                tmp = input('New Lemonade Price: ')
                while testFloat(tmp)==False:
                    print("ERROR: option must be a number")
                    tmp = input('New Lemonade Price: ')
                price = float(tmp)
                print('Lemonade price set to: '+str(price))
        elif option == '8':
            saveGame()
        elif option == '9':
            choiceList=['y','n']
            choice = input("Would you like to save before quiting? [y/n]: ")
            while choice not in choiceList:
                print("ERROR: option must be 'y' or 'n'")
                choice = input("Would you like to save before quiting? [y/n]: ")
            if choice == 'y':
                saveGame()
            menu = False
            run = False
print('done')
    

    
