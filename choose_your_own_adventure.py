name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road its has come to an end and you can go left or right. Which way will you like to go? ").lower()

if answer == "left":
  answer = input("You come to a river, you can walk around it or swim across? Type walk to walk around it or swim to swim across: ")
  
  if answer == "swim":
    print("You swam across and were eaten by a crocodile.")
    print("You lose!!")
  elif answer == "walk":
    print("You walked for many miles and ran out of water.")
    print("You lose!!")
  else:
    print("Not a valid option. you lose!!")
    
elif answer =="right":
  answer =input("You came to a bridge it looks wobbly, do you want to cross it or head back?(cross/back) ")
  if answer == "cross":
    answer = input("You crossed the bridge and came across a stranger. Do you talk to them (yes/no)? ")
    if answer == "yes":
      print("Mama said don't talk to strangers.")
      print("You lose!!")
    elif answer == "no":
      print("You made it home.")
      print("You win!!!")
    else:
      print("Not a valid option. you lose!!")
      
  elif answer == "back":
    print("You turn back there was a lion stalking. You were attacked. You died.")
    print("You lose!!")
  else:
    print("Not a valid option. you lose!!")
    
else:
  print("Not a valid option. you lose!!")
  
print("Thank you for trying", name)