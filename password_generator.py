import random 
import string

def generate_password(min_length, numbers=True, special_characters=True):
  letters = string.ascii_letters
  digits = string.digits
  special = string.punctuation
  
  characters = letters
  if numbers:
    characters += digits
  if special_characters:
    characters += special
    
  pwd = ""
  meets_criteria = False
  has_number = False
  has_special = False
  
  while not meets_criteria or len(pwd) < min_length:
    new_char = random.choice(characters)
    pwd += new_char
    
    if new_char in digits:
      has_number = True
    elif new_char in special:
      has_special = True
      
    meets_criteria = True
    if numbers:
      meets_criteria = has_number
    if special_characters:
      meets_criteria = meets_criteria + has_special
      
  return pwd
  
while True:
  min_length = input("Enter the minimum length for the password or type q to quit: ")
  
  if min_length.lower() == "q":
    break
  
  if min_length.isdigit():
    min_length = int(min_length)
    has_number = input("Do you want to add numbers (y/n)? ").lower() == "y"
    has_special = input("Do you want to add special characters (y/n)? ").lower() =="y"
    pwd = generate_password(min_length, has_number, has_special)
    print(pwd)
    break
  else:
    print("Please type a number!! ")
    continue
  
  
