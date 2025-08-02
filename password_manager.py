from cryptography.fernet import Fernet , MultiFernet
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
import base64

''''
def write_key():
  key = Fernet.generate_key()
  with open("key.key", "wb") as key_file:
    key_file.write(key)'''

def load_key():
  file =open("key.key", "rb")
  key = file.read()
  file.close()
  return key

def d_key(master:bytes, load:bytes):
  kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=load,
    iterations=390000,
    backend=default_backend
  )
  return base64.urlsafe_b64encode(kdf.derive(master))

master_pwd = input("What is the master password? ")
key = d_key(master_pwd.encode(), load_key())
fer = MultiFernet([Fernet(key)])
#fer = MultiFernet([Fernet(key), Fernet(master_pwd.encode())]) 


def view():
  with open("password.txt", "r") as f:
    for line in f.readlines():
      data = line.rstrip()
      user, passw = data.split("|")
      print("User:", user, "| Password:", fer.decrypt(passw.encode()).decode())

def add():
  name = input("Account Name: ")
  pwd = input("Password: ")
  
  with open("password.txt", "a") as f:
    f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
  mode = input("Would you like to add a new password or view existing ones (view/add)? Press q to quit. ").lower()

  if mode == "q":
    break
  
  if mode == "view":
    view()
  
  elif (mode == "add"):
    add()
  
  else:
    print("Invalid mode!!!")
    continue
