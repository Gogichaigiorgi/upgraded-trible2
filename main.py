import random
import time

roll_again = "yes"
while roll_again == "yes" or roll_again == 'y' or roll_again == "yes" or roll_again == "y":
        print("\nRolling the dice...")
        time.sleep(1)
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
    
        print("The values are:")
        print("Dice 1 =", dice1, "\nDice 2 =", dice2)
 
        if dice1 == dice2:
            print("tqven moiget!")
        if dice1 and dice2 <1 or dice1 and dice2 > 6:
            print("araswori ricxvia!")
        else:
                print("kidev scadet")
        roll_again = input("\Roll the dice again ? (Y/N) ")


            
