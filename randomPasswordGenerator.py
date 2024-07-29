import random
import string
from colorama import Fore
import hashlib
import time
from tqdm import tqdm
from plyer import notification


def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''
    for _ in range(length):
        password += random.choice(characters)
        time.sleep(0.1)  # Simulate some delay
    return password

def hash_pass(password):
    hashed_pass = hashlib.sha256(password.encode()).hexdigest()
    return hashed_pass

#choose the lenght
lenght = int(input(Fore.GREEN + """Enter the number of passwords to generate: """ + Fore.RESET))

for _ in tqdm(range(lenght), desc=""):
    word = generate_password(49)
    encoded = hash_pass(word)

    # save to file
    with open("passwords.txt","a") as f:
        f.write(word+ "\n")

    with open("encoded.txt","a") as b:
        b.write(encoded + "\n")

notification.notify(
    title= "Password Generated",
    message="All the password(s) have been generated"
)
