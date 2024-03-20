import random
from ColoredText import *

def main():
    #outcome = "You win!"
    #shotgunner = 100
    #leaderboard(outcome, shotgunner)
    developerInfo()
    description()
    print()
    while True:
        start = startMenu()
        if start.title() == "Help":
            helpMenu()
            print()
        else:
            print()
            battleMenu()
            restart = restartMenu()
            if restart == "no" or restart == "No":
                break
            elif restart == "yes" or restart == "Yes":
                continue

def description():
    printc(purple("Shotguns versus Aliens is a game where you can either choose to heal yourself\nor shoot the alien. If you choose to shoot the alien then the game will ask you\n'How many times will you like to shoot?' You can only enter a value in the\nrange of 1 to 3. After this, a secret number is created between 1 and 10 and\nyou have to guess this number in order to hit the alien. The higher the shots,\nthe higher the chance you will hit the alien but you will deal less damage and\nvice versa. If you have more questions please visit the FAQ by typing 'Help'.\nGood luck!"))

def startMenu():
    start = input("Press enter to start the game... ")
    return start

def restartMenu():
    restart = input("\nWould you like to play again? ")
    while True:
        if restart == 'yes' or restart == "Yes":
            break
        elif restart == "no" or restart == "No":
            printc(purple("\nThank you for using this program"))
            break
        else:
            printc(black("\nPlease enter a valid answer. Type in yes or no.\n"))
            restart = input("Would you like to play again? ")
    return restart

def helpMenu():
    printc(purple("\nFAQ:\n"))
    printc(blue("How much do I heal for?"))
    printc(green("You heal for 15 HP everytime you type in heal."))
    printc(blue("What percentage is the chance of me hitting the alien every round?"))
    printc(green("There is a 33% chance of hitting the alien when you choose to shoot 3 times.\nA 20% chance when you choose to shoot two times and a 10% chance when you shoot 1 time."))
    printc(blue("What is a lucky number?"))
    printc(green("A lucky number is when multiple secret numbers choose 1 number to be the secret\nnumber and if you guess this number you will heal for 25 HP(If you choose to\nshoot 2 times) or 40 HP (If you choose to shoot 3 times). You will also deal\ncritical damage to the alien."))
    printc(blue("How do I shoot for critical damage?"))
    printc(green("You choose to shoot 1 time and guess the secret number correctly or you\npick the lucky number if 2 or 3 shots is chosen."))
    printc(blue("How much is my health?"))
    printc(green("The shotgunner and the alien start out with 100 HP. The shotgunner can go up to 120 HP though."))

def battleMenu():
    shotgunner = 100
    alien = 100
    healpot = 105
    while alien > 0 and shotgunner > 0:
        battleMenu = input("Would you like to heal or shoot? ")
        if battleMenu == "shoot" or battleMenu == "Shoot":
            shotgunner, alien, shotgunAmmo = shotgunnerTurn(shotgunner, alien)
            if alien <= 0:
                printc(green("Shotgunner's Health "),end='')
                printc(green(str(shotgunner)),end='')
                printc(green(" HP"))
                printc(green("Alien's Health "),end='')
                printc(green(str(alien)),end='')
                printc(green(" HP\n"))
                outcome = "You win!"
                printc(purple(outcome))
                break
            shotgunner = alienAttack(shotgunner, alien, shotgunAmmo)
            if shotgunner <= 0:
                outcome = "You lost!"
                printc(purple(outcome))
                break
        elif battleMenu == "heal" or battleMenu == "Heal":
            shotgunner, shotgunAmmo, healpot = healing(shotgunner,healpot)
            shotgunner = alienAttack(shotgunner, alien, shotgunAmmo)
            if shotgunner <= 0:
                outcome = "You lost!"
                printc(purple(outcome))
        else:
            printc(black("\nPlease enter a valid answer. Type in heal or shoot.\n"))

    return outcome
        

def shotgunnerTurn(shotgunner, alien):
    ahPlaceholder = alien
    shotgunAmmo = int(input("How many times would you like to shoot? "))
    while shotgunAmmo > 3 or shotgunAmmo < 0:
        printc(black("\nPlease pick a number between 1 and 3. Thank you.\n"))
        shotgunAmmo = int(input("How many times would you like to shoot? "))
    while shotgunAmmo <= 3 and shotgunAmmo >= 1:
        for s in range(shotgunAmmo):
            number = int(input("\nPick a number in the range of 1 to 10: "))
            print("\n",end='')
            shotgunCritical = random.randint(40,50)
            shotgunDamage = random.randint(15,25)
            magicNumber1 = random.randint(1,10)
            magicNumber2 = random.randint(1,10)
            magicNumber3 = random.randint(1,10)
            if shotgunAmmo == 1:
                if number == magicNumber1:
                    alien -= shotgunCritical
                    printc(red("You shot the alien for "),end='')
                    printc(red(str(ahPlaceholder - alien)),end='')
                    printc(red(" HP! Critical Damage!"))
                    ahPlaceholder = alien
                    if alien <= 0:
                        break
                else:
                    printc(red("The alien dodged!"))
            if shotgunAmmo == 2:
                if number == magicNumber1 and number == magicNumber2:
                    alien -= shotgunCritical
                    shotgunner += 25
                    printc(red("You shot the alien for "),end='')
                    printc(red(str(ahPlaceholder - alien)),end='')
                    printc(red(" HP! Nice shot!"))
                    printc(orange("You picked the lucky number! Shotgunner is healed for 25 HP!"))
                    ahPlaceholder = alien
                    if alien <= 0:
                        break
                elif number == magicNumber1 or number == magicNumber2:
                    alien -= shotgunDamage
                    printc(red("You shot the alien for "),end='')
                    printc(red(str(ahPlaceholder - alien)),end='')
                    printc(red(" HP! Nice shot!"))
                    ahPlaceholder = alien
                    if alien <= 0:
                        break
                else:
                    printc(red('The alien dodged!'))
            if shotgunAmmo == 3:
                if number == magicNumber1 and number == magicNumber2 and number == magicNumber3:
                    alien -= shotgunCritical
                    shotgunner += 40
                    printc(red("You shot the alien for "), end='')
                    printc(red(str(ahPlaceholder - alien)),end='')
                    printc(red(" HP! Nice shot!"))
                    printc(orange("You picked the lucky number! Shotgunner is healed for 40 HP!")) 
                    ahPlaceholder = alien
                    if alien <= 0:
                        break
                if number == magicNumber1 and number == magicNumber2 or number == magicNumber1 and number == magicNumber3 or number == magicNumber2 and number == magicNumber3:
                    alien -= shotgunCritical
                    shotgunner += 25
                    printc(red("You shot the alien for "), end='')
                    printc(red(str(ahPlaceholder - alien)),end='')
                    printc(red(" HP! Nice shot!"))
                    printc(orange("You picked the lucky number! Shotgunner is healed for 25 HP!")) 
                    ahPlaceholder = alien
                    if alien <= 0:
                        break
                elif number == magicNumber1 or number == magicNumber2 or number == magicNumber3:
                    alien -= shotgunDamage
                    printc(red("You shot the alien for "), end='')
                    printc(red(str(ahPlaceholder - alien)),end='')
                    printc(red(" HP! Nice shot!"))
                    ahPlaceholder = alien
                    if alien <= 0:
                        break
                else:
                    printc(red("The alien dodged!"))
        break
    printc(black("End of Your Turn\n"))
        
    if alien < 0:
        alien = 0
        ahPlaceholder = alien
    return shotgunner, alien, shotgunAmmo

def healing(shotgunner,healpot):
    healpot -= 15
    if healpot < 0:
        printc(black("Heal Pot is empty. Turn is lost."))
    else:
        shotgunner += 15
        printc(orange("\nYou healed for 15 HP!"))
        printc(orange("Healpot "),end='')
        printc(orange(str(healpot)))
    if shotgunner > 120:
        shotgunner = 120
    shotgunAmmo = random.randint(1,3)
    printc(black("End of Your Turn\n"))
    return shotgunner, shotgunAmmo, healpot

def alienAttack(shotgunner, alien, shotgunAmmo):
    alienDamage = random.randint(15,33)
    alienCritical = random.randint(33,49)
    shPlaceholder = shotgunner
    while shotgunAmmo >= 1 and shotgunAmmo <= 3:
        if shotgunAmmo == 1:
            count = 0
            for a in range(shotgunAmmo):
                alienProb = random.randint(1,5)
                magicNumber = random.randint(1,5)
                if alienProb == magicNumber:
                    count += 1
            if count == 0:
                shotgunner -= 10
                printc(red("The alien hit you for 10 HP!"))
                if shotgunner <= 0:
                    break
            if count == 1:
                shotgunner -= alienDamage
                shotgunner -= 10
                printc(red("The alien hit you for "),end='')
                printc(red(str(shPlaceholder - shotgunner)),end='')
                printc(red(" HP!"))
                if shotgunner <= 0:
                    break
                
        if shotgunAmmo == 2:
            count = 0
            for a in range(shotgunAmmo):
                alienProb = random.randint(1,5)
                magicNumber = random.randint(1,5)
                if alienProb == magicNumber:
                    count += 1
            if count == 0:
                shotgunner -= 5
                printc(red("The alien slightly grazed you for 5 HP!"))
                if shotgunner <= 0:
                    break
            if count == 1:
                shotgunner -= alienDamage
                shotgunner -= 5
                printc(red("The alien hit you for "),end='')
                printc(red(str(shPlaceholder - shotgunner)),end='')
                printc(red(" HP!"))
                if shotgunner <= 0:
                    break
            if count == 2:
                shotgunner -= alienDamage
                shotgunner -= alienCritical
                shotgunner -= 5
                printc(red("The alien hit you for "),end='')
                printc(red(str(shPlaceholder - shotgunner)),end='')
                printc(red(" HP! Critical Damage!"))
                shPlaceholder = shotgunner
                if shotgunner <= 0:
                    break
                
        if shotgunAmmo == 3:
            count = 0
            for a in range(shotgunAmmo):
                alienProb = random.randint(1,5)
                magicNumber = random.randint(1,5)
                if alienProb == magicNumber:
                    count += 1
            if count == 0:
                printc(red("You dodged all the aliens attacks!"))
                if shotgunner <= 0:
                    break
            if count == 1:
                shotgunner -= alienDamage
                printc(red("The alien hit you for "),end='')
                printc(red(str(shPlaceholder - shotgunner)),end='')
                printc(red(" HP!"))
                if shotgunner <= 0:
                    break
            if count == 2:
                shotgunner -= alienDamage
                shotgunner -= alienCritical
                printc(red("The alien hit you for "),end='')
                printc(red(str(shPlaceholder - shotgunner)),end='')
                printc(red(" HP! Critical Damage!"))
                shPlaceholder = shotgunner
                if shotgunner <= 0:
                    break
            if count == 3:
                shotgunner -= alienDamage
                shotgunner -= alienCritical
                shotgunner -= alienCritical
                printc(red("The alien hit you for "),end='')
                printc(red(str(shPlaceholder - shotgunner)),end='')
                printc(red(" HP! Critical Damage!"))
                shPlaceholder = shotgunner
                if shotgunner <= 0:
                    break     

        break
    printc(black("End of Alien's Turn\n"))
            
            
    if shotgunner < 0:
        shotgunner = 0
    shPlaceholder = shotgunner
    printc(green("Shotgunner's Health "),end='')
    printc(green(str(shotgunner)),end='')
    printc(green(" HP"))
    printc(green("Alien's Health "),end='')
    printc(green(str(alien)),end='')
    printc(green(" HP\n"))
        
    return shotgunner

def leaderboard(outcome, shotgunner):
    if outcome == "You win!":
        inFile = open('Leaderboard.txt', 'r')
        outFile = open('Leaderboard.txt', 'a')
        name = input("\nType a three character name to put into the leaderboard... ")
        outFile.write(name + " " + str(shotgunner) + '\n')
        count = 1
        printc(purple("%8s  %25s\n" % ("Name", "Shotgunner's Health")))
        lineRead = inFile.readline()
        while lineRead != '':
            ranking = lineRead.split()
            previous = ranking[1]
            if shotgunner < previous:
                printc(black(count),end='')
                printc(purple("%8s" % (ranking[0])),end='')
                printc(green("%25s" % (ranking[1])),end='')
            count += 1

            lineRead = inFile.readline()

def developerInfo():
    print("Name:         Donavan Drouin")
    print("Date:         12/20/2020")
    print("Program:      Program Practice #2")
    print()
            

main() 


    

#leaderboard (impossible)

