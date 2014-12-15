"""
Name: lemonadeStand.py
Description: Game of Selling Lemonade
Version: 0.0.1
"""

__author__ = "Spencer Dockham"
__date__ = "12/12/2014"

import time
import random
import math

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
               
# vars
day = 1
m = 'am'
hour = 10
minute = 0
gameTime = ''
clockList = []
pace = 1

shopRep = 0.1
custRep = 0.0
custLimit = 10
shopIndex = 0

openHour = 10
closeHour = 4

money = 250.0
price = 0.5
lemon = 100; lemonPrice = 0.3
sugar = 100; sugarPrice = 0.05 #1 oz || get 10
cups = 50; cupPrice = 0.2
ice = 400; icePrice = 0.02 #cubes

delay = 0.2

        # Type, Cost, Dur(days), result(%)4
adList = [['Megazine','70','7','20'],['TV','150','4','60'],['Radio','95','7','35']]
curAds = []

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
        menuList = ['1','2','3','4','5']
        option = input("Select Option: ")
        while option not in menuList:
            print("ERROR: option must be a number...")
            option = input("Select Option: ")
        if option == '1':
            print("Buying inventory...")
            print('-'*30);print('Inventory');print('-'*30);print('')
            print('Lemons: '+str(lemon))
            print('Sugar: '+str(sugar)+' oz')
            print('ice: '+str(ice)+' cubes')
            print('cups: '+str(cups));print('')
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
            #custRep = 0.0
            #custLimit = 10
            print("1. Upgrade Current Stand")
            print("2. Buy New Stand")
            print("3. Back")
            menuList = ['1','2','3']
            option = input("Select Option: ")
            while option not in menuList:
                print("ERROR: option must be a number...")
                option = input("Select Option: ")
            if option == '1':
                continue################ upgrade current stand popularity
            elif option == '2':
                shopCost = [250,500,1000,1500,2500]
                cost = shopCost[shopIndex]
                print("New Stand Upgrad: $%.2f"%float(cost)) #print('Cost: $%.2f'%float(cost)+'\n')
                choiceList=['y','n']
                choice = input("Would you like to upgrad? [y/n]: ")
                while choice not in choiceList:
                    print("ERROR: option must be 'y' or 'n'")
                    choice = input("Would you like to upgrad? [y/n]: ")
                if choice == 'y':
                    if (money - cost) < 0:
                        money -= cost
                        custLimit += (shopIndex*10)
                        print("New Customer Limit: "+str(custLimit))
                    else:
                        print("You cannot afford this upgrade\n")
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
                    print("custs: "+str(custs))
                    choiceList = [0,1,2]
                    closed = False
                    for ct in range(0,custs):
                        if closed == False:
                            choice = random.choice(choiceList)
                            if choice == 0:
                                if testInventory(lemon-0.2,sugar-1,cups-1,ice-1):
                                    money += price
                                    lemon -= 0.2
                                    sugar -= 1
                                    cups -= 1
                                    ice -= 4
                                    print("Lemonade sold for $"+str(price))
                                else:
                                    print("You are out of supplies...")
                                    print("CLOSING SHOP...");time.sleep(delay*3)
                                    closed = True
                                    time.sleep(delay)
                            elif choice == 1:
                                if testInventory(lemon-0.2,sugar-1,cups-1,ice-1):
                                    money += (price*2)
                                    lemon -= 0.4
                                    sugar -= 2
                                    cups -= 2
                                    ice -= 8
                                    print("Lemonade sold for $"+str(price*2))
                                else:
                                    print("You are out of supplies...")
                                    print("CLOSING SHOP...");time.sleep(delay*3)
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
                        print("Money: $"+str(money))
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
                        print("Money: $"+str(money))
                        print('Lemons: '+str(lemon))
                        print('Sugar: '+str(sugar)+' oz')
                        print('ice: '+str(ice)+' cubes')
                        print('cups: '+str(cups)+'\n')
                        break
                else: # Closed
                    print('-'*30);print('CLOSING...');print('-'*30+'\n\n')
                    lemon = round(lemon)
                    print("Money: $"+str(money))
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
    
    

    
