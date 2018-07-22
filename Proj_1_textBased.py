#Program Name: Prog Whambulance 
#Developer: Anthony Calandra
#Date: 10/06/2014
#Description:Project 1
import random
import time
location = 11 # starting location on map
prevLocation = None
inventory = []
winItems = ("satillite phone", "phone battery")
XP = 0 # increases on every enemy killed
bosses = (25,32) #tuple for the 2 locations where bosses are
def UI ():
    print("please enter what you would like to do")
    print("0 = Resume previous game")
    print("1 = Start Game")
    print("2 = Quit")

def story():
    Story_doc = open("story.txt", "r")
    for line in Story_doc:
       print(line)
    

def save ():
    global inventory
    global location
    global XP
    Game_Save = open("GameSaveInfo.txt", "w")
    for item in inventory:
        print(item)
        Game_Save.write(item)
        Game_Save.write("\n")   
    Game_Save.write(str(location))
    Game_Save.write("\n")    
    Game_Save.write(str(XP))
    Game_Save.close()
    print("GAME SAVED")

    
def load():
    global inventory
    global location
    global XP
    global prevLocation
    Game_Save = open("GameSaveInfo.txt", "r")
    j = -1
    for line in Game_Save:
        inventory.append(line.replace("\n", ""))
        j = j+1
    XP = inventory[j]
    location = inventory[j-1]
    inventory.remove(XP)
    inventory.remove(location)
    XP = int(XP)
    location = int(location)
    prevLocation = int(location)

    
def characters ():
    #attributes: 
    char1 = [7,4,5]
    char2 = [3,8,4]
    char3 = [4,3,8]
    
    x = None
    while x == None:
        print()
        print("oddly enough i cant remember who i am")
        print()
        print("what is your name")
        name = input()
        print ("oh ya my name is ", name,"... I wonder how long ive been knocked out")
        print()
        print("select your characters attibutes")
        print()
        print ("character 1 has 7 stregth, 4 dexterity, and 5 health, type '1' to select")
        print ("character 2 has 3 stregth, 8 dexterity, and 5 health, type '2' to select")
        print ("character 3 has 5 stregth, 3 dexterity, and 8 health, type '3' to select")
        print()
        print ("strength effects your damage output, dexerity helps you dodge enemy attacks,\nand health effects how much damage you can absorb")
        pick = input()
     
        if pick == "1":
            return char1
        if pick == "2":
            return char2
        if pick == "3":
            return char3
        else:
            print("Invalid number please re-select")
        print("I had a satillite phone on me when we crashed... im sure its somewhere on the island... i should look around and see if any critters ran off with it")

def yourChar (yourAtts): 
    Strength = yourAtts[0]#effects Damage
    Dexterity = yourAtts[1] #effects Dodge
    health = yourAtts[2] #effects health
   

def gameMap():
    global location
    spot = ""
    beach = [1,8,9,10,11,20,21,30,31,41]
    lightJungle = [6,7,12,17,18,19,28,29,38,39]
    thickJungle = [14,15,16,25,26,27,35,36,37]
    mangrove = [13,22,23,24,32,33,34]
    cliff = [2,3,4,5,40,42,43,44,45,46,47,48,49,50]
    if location in beach:
            print("your on the beach")
            spot = "beach"
            return spot
    elif location in lightJungle:
            print("your in the light jungle")
            spot = "light jungle"
            return spot
    elif location in thickJungle:
            print("your in the thick jungle")
            k = 0
            if k == 0:
                print("i think I just seen my phone but there was a large enemy by it so i better be carful")#tells you once that your phone is in here 
                k = 1
            spot = "thick jungle"
            return spot
    elif location in cliff:
            print("your on the cliffs")
            spot = "cliffs"
            return spot
    elif location in mangrove:
            print("your in the mangrove")
            g = 0
            if g == 0:
                print("i think I just seen my phone battery but there was a large enemy by it so i better be carful")
                g = 1
            spot = "mangrove"
            return spot
            
            
def movement ():
    global location
    global prevLocation
    print("what direction do you want to move, 'up', 'down', 'left', 'right', or 'stay'")
    print("or type 'm' to read your map type 's' To save your game or type 'q' to quit  ")


    playerMove = input()
    if playerMove.lower() == "s":
        save()
    elif playerMove.lower() == "q":
        done = "gameDone"
        return done
    elif playerMove.lower() == 'm':
        print()
        print("The island appears to have beaches on the east and west coast and cliffs on the north and south coasts")
        print("The interior of the island looks like it transistions from mangrove to thick jungle to thinner jungle as you move from west to east")
        print()
    elif playerMove.lower() == "up":
        if location in range(1,10):
            print("there is only water... no point in geetting wet")
        else: 
            location = location - 10
    elif playerMove.lower() == "down":
        if location in range(41,50):
            print("there is only water... no point in geetting wet")
        else:
            location = location + 10
    elif playerMove.lower() == "left":
        if location in (1,11,21,31,41):
            print("there is only water... no point in geetting wet")
        else:
            location = location - 1
    elif playerMove.lower() == "right":
        if location in (10,20,30,40,50):
            print("there is only water... no point in geetting wet")
        else:
            location = location + 1
    elif playerMove.lower() == "stay":
        location = location
    else:
        print("Invlid answer")
        movement()
   
    

def items (yourspot,dontPlayOn):
    global inventory
    if location != prevLocation:
        if location == 25:
            if dontPlayOn == "no":
                inventory.append("satillite phone")
                print("you found a satellite phone")
                winItemResponse()
        if location == 32:
            if dontPlayOn == "no":
                inventory.append("phone battery")
                print("you found a phone battery")
                winItemResponse()
    if location not in bosses:
        if yourspot == "mangrove":
            mangroveItems = ("boots", "40-40 Rifle", "pork 'n' beans")
            give = random.randint(0,3)
            if give <= 2:
                giveitem = mangroveItems[give]
                if giveitem in inventory:
                    print("you found a", giveitem)
                    print()
                    print("i already have one of these...")
                    print()
                else:
                    print("you found a", giveitem)
                    print()
                    inventory.append(giveitem)
                    if giveitem == "40-40 Rifle":
                        print("this should making fight a little easier")
                    if giveitem == "pork 'n' beans":
                        print("i should be a little harder to kill now")
                    if giveitem == "boots":
                        print("its now easier to flee from enemies")
                    print("your inventory", inventory)
                    print()
            else:
                print("you found nothing")
                print()
                
        if yourspot == "thick jungle":
            
            TjungItems = ("coffeh beans", "machete", "anti bacterial cream")
            give = random.randint(0,3)
            if give <=2:
                giveitem = TjungItems[give]
                if giveitem in inventory:
                    print("you found a", giveitem)
                    print()
                    print("i already have one of these...")
                    print()
                else:
                    print("you found a", giveitem)
                    print()
                    inventory.append(giveitem)

                    if giveitem == "machete":
                        print("this should making fight a little easier")
                    if giveitem == "anti bacterial cream":
                        print("i should be a little harder to kill now")
                    if giveitem == "coffeh beans":
                        print("its now easier to dodge enemy attack")
                    
                    print("your inventory", inventory)
                    print()
            else:
                print("you found nothing")
                print()
                
        if yourspot == "light jungle":
            LjungItems = ("assorted bandages", "snigle-shot rifle", "binoculers")
            give = random.randint(0,5)
            if give <= 2:
                giveitem = LjungItems[give]
                if giveitem in inventory:
                    print("you found a", giveitem)
                    print()
                    print("i already have one of these...")
                    print()
                else:
                    print("you found a", giveitem)
                    print()
                    inventory.append(giveitem)
                    if giveitem == "snigle-shot rifle":
                        print("this should making fight a little easier")
                    if giveitem == "assorted bandages":
                        print("i should be a little harder to kill now")
                    print("your inventory", inventory)
                    print()
            else:
                print("you found nothing")
                print()
                
        if yourspot == "cliffs":
            cliffsItems = ("ropes", "flare", "pointy stick")
            give = random.randint(0,4)
            if give <=2:
                giveitem = cliffsItems[give]
                if giveitem in inventory:
                    print("you found a", giveitem)
                    print()
                    print("i already have one of these...")
                    print()
                else:
                    print("you found a", giveitem)
                    print()
                    inventory.append(giveitem)
                    if giveitem == "pointy stick":
                        print("this should making fight a little easier")
                    print("your inventory", inventory)
                    print()
            else :
                print ("you found nothing") 
        if yourspot == "beach":
            beachItems = ("knife", "mug", "dead bird" )
            give = random.randint(0,5)
            if give <= 2:
                giveitem = beachItems[give]
                if giveitem in inventory:
                    print("you found a", giveitem)
                    print()
                    print("i already have one of these...")
                    print()
                else:
                    print("you found a", giveitem)
                    print()
                    inventory.append(giveitem)
                    if giveitem == "knife":
                        print("this should making fight a little easier")
                    if giveitem == "mug":
                        print("its now easier to dodge enemy attacks")
                    print("your inventory", inventory) 
                    print()
            else:
                print("you found nothing")
                print()

def enemies ():
    #tuple index 0-57 /// first number = health second number = damage
    enemy = (("Angry Turtle", 10 , 5), ("Pigeon",15,10), ("Boar",20,15), ("Jaguar",25,20)
             ,("Bear",30,25), ("Gorilla",35,30),("enormous Rabbit",40,35),("Pigeon Army",45,40))
    #if location == prevLocation:
    
    if location not in bosses:
        if XP <= 10:
            enemyselect = random.randint(0,2)
        if XP >= 11:
            enemyselect = random.randint(0,5)
    if location == 25:
        enemyselect = 6
    if location == 32:
        enemyselect = 7
    return enemy[enemyselect]

def itemModifiers():
    #add later---specific items have specific effects
    weapons = ["40-40 Rifle","machete","snigle-shot rifle","pointy stick","knife"]
    heals = ["pork 'n' beans","anti bacterial cream","assorted bandages"]
    dam = 0
    for item in weapons: 
        for item2 in inventory:
            if item == item2:
                dam = dam + 2
    
    health = 0
    for item in heals: 
        for item2 in inventory:
            if item == item2:
                health = health + 5
   
    
    mods= [dam, health]
    return mods

def fight (enemystats, yourAtts, playerMods):
    global location
    global XP
    global inventory
    
    if location != prevLocation:
   
        if location in bosses: #forces there to be a fight n these tiles becasue they're boss fights
            isThereAFight = 1

        if location  not in bosses: #gives a random oppertunity for fights 66% chance of a fight
            isThereAFight = random.randint(1,3)
        if isThereAFight == 1 or 2:
            escape = ["boots"]
            
            userDamage = (yourAtts[0] * 5) + XP + playerMods[0] # playerMods comes form modifiers from items
            userHealth =  (yourAtts[2] * 10) + XP + playerMods[1]
            enemyHealth = enemystats[1]
           
            dexBonus = ["coffeh beans","Mug"]
            if dexBonus[0 and 1] in inventory:
                yourDodge = yourAtts[1] + 1
               
            else:
                yourDodge = yourAtts[1]
            print ("your encountered a", enemystats[0])
            time.sleep(1)
            battle = 1
            while battle == 1:
                enemyDamage = enemystats[2]
                
                if userHealth >0 and enemyHealth > 0:
                    Dodge = random.randint(1,10)
                    MissedHit = random.randint(1,10)
                    print("It ATTACKS!!!")
                    print()
                    time.sleep(1)
                    if MissedHit in range(1,3):
                        print("it missed you")
                        print()
                    elif Dodge > yourDodge:
                        print("you dodged the attack")
                        print()
                    else:
                        print("it attacked you")
                        print()
                        userHealth = userHealth-enemyDamage
                        print()
                        print("Your Health",userHealth)
                        print("Enemy Health",enemyHealth)
                        print()
                userInput = "0"
                if userHealth > 0 and enemyHealth > 0:          
                    MissedHit = random.randint(1,10)
                    print("do you want to attack or try to flee")
                    print()
                    x = None
                    while x == None:
                        print("type '1' to attack or '2' to flee")
                        print()
                        userInput = input()
                        if userInput == "1":
                            if MissedHit in range(1,3):
                                print("you missed it")
                                print()
                                break
                            else:
                                print("you attacked the", enemystats[0])
                                print()
                                enemyHealth = enemyHealth-userDamage
                                print("Your Health",userHealth)
                                print("Enemy Health",enemyHealth)
                                print()
                                break
                             
                        elif userInput == "2":
                            if escape[0] in inventory:
                                flee = random.randint(1,4) #if you have boots item its easier to flee
                            else:
                                flee = random.randint(1,5)
                            print("you try to flee")
                            print()
                            if flee  in range(1,3):
                                print("you got away")
                                print()
                                break
                            else:
                                print("The", enemystats[0], "caught you")
                                print()
                                print ("the enemy critically hit you")
                                print()
                                userHealth = userHealth-(enemyDamage*2)
                                break
                        else:
                            print(userInput, "is not a valid answer")
                if userInput == "2":
                    if flee in range (1,3):
                        break
                if userHealth <= 0:
                    print("you died")
                    print()
                    youDied = "yes"
                    inventory = []#resets inventory and location after you die
                    location = 11
                    return youDied
                    break
                if enemyHealth <= 0:
                    print("you killed the",enemystats[0])
                    global XP
                    print("you gained XP... your health  and damage has increased")
                    if location not in bosses:
                        XP = XP +1
                    if location in bosses:
                        XP = XP + 5
                    print("XP =",XP)
                    
                    youDied = "no"
                    return youDied
                    break
        else:
            print("nothing attacked you")

    
def winCheck (): #function used to check the winning tuple agianst the users inventory to see of the user won 
    global winItems
    global inventory
    inventory.sort()
    j = 0
    doYouWin = 0
    for item in winItems: 
        for item2 in inventory:
            if item == item2:
                doYouWin = doYouWin +1 #for every matched item do you win increments 
        j = j + 1
    
    
    if doYouWin >= 2: # if doYouWin is >= 4 you win becasue there are 4 items in the tuple so if this = 4 or more you matched all the tuple items(is increased or deacresed based on win set)
        
       
        youwin = "yes"
        return youwin

def winItemResponse():
    global inventory
    x = None
    if "satillite phone" in inventory:
        while x == None:
            if "phone battery" in inventory:
                print("that battery should fit in this phone")
                x = 1
            else:
                print("the battery is missing... i bet it's somewhere around here")
                x = 1
    j = None
    if "phone battery" in inventory:
        
        while j == None:
            if "satillite phone" in inventory:
                print("this must go to the satellite phone")
                j = 1
            else:
                print("this must go to a phone... i bet it's somewhere around here")
                j = 1
                
def main ():
    global prevLocation
    endGame = "no" 
    x = None
    resume = "off"
    while x == None:
        if resume == "off":
            UI()
            run = input()
        if resume == "on":
            run = "1"
        
        if run == "0":
            load()
            print("your XP is",XP)
            print("you have have these in yor inventory",inventory)
            resume = "on"
            print("YOUR GAME HAS BEEN RESUMED")
        elif run == "1":
            if resume == "off":
                story()
            yourAtts = characters()
            yourChar(yourAtts)
            print()
            print("I had a satellite phone on me when we crashed... im sure its somewhere on the island... i should look around and see if any critters ran off with it")
            print()
            play = None
            while play == None:
                endGame = movement()
                yourspot = gameMap()#return from gameMap assigned to yourspot
                
                enemystats = enemies()
                playerMods = itemModifiers()
                dontPlayOn = fight(enemystats,yourAtts,playerMods)
                items(yourspot,dontPlayOn) #puts yourspot in items function
                
                if dontPlayOn == "yes":
                    break

                winCheck()
               
                youwon = winCheck()
                if youwon == "yes":
                    print()
                    
                    print ("You put your phone together and place a call for rescue... its only a matter of time before your taken off this island")
                    print()
                    break
                if endGame == "gameDone":
                    print("you ended the game")
                    endGame = "yes"
                    break
                
                prevLocation = location
    
      
        elif run == "2":
            print("Goodbye")
            break
        else:
            print(run, "is not a valid answer")

             
        if endGame == "yes":
            break
            
        
main()
