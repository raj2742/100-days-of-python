print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************''')
print("Welcome to Treasure Island.")
print("Your mission to find the treasure.")
try_1=input('you\'re at a cross road. Where do you want to go? Type "left" or "right" ').lower()
if try_1 == "left":
    try_2 = input('You come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across? ').lower()
    if try_2 =="wait":
        try_3 = input("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and blue. Which colour do you choose? ").lower()
        if try_3 == "red":
            print("You burned by fire. Game Over.")
        elif try_3=="blue":
            print("you eaten by beasts. Game Over.")
        elif try_3=="yellow":
            print("You win and treasure is yours!!!")
        else:
            print("Game Over")
    else:
        print("Attacked by Trout. Game Over.")
else:
    print("Fall into the hole. Game Over.")