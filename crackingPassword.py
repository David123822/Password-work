import hashlib
from tqdm import tqdm
import time
import random

def password_cracking(hashed_pass, password_list):
    for password in tqdm(password_list, desc="Looping over the list of passwords"):
        if hashlib.sha256(password.encode()).hexdigest() == hashed_pass:
            return password
        time.sleep(0.1)
    return "Password not found"

# choosing a random hash from the file
hash = []
file = open("encoded.txt","r")
for line in file:
    hash.append(line.strip())

encode = random.choice(hash)

#converting the data from the password file in a list

commoc_pass= ["admin","pass","qwerty21!", "123456789", "z+t^JdHk?rpBj>QCv>y@{&wM1:#?EH"]
file = open("passwords.txt","r")
for line in file:
    commoc_pass.append(line.strip())

#cracking the password
result = password_cracking(encode, commoc_pass)
print(f"The random hash was {encode} and the password is {result}")