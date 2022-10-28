import string
import random

from numpy import outer

character = list(string.ascii_letters + string.digits + "!@#$%^&*()")



length = int(input("Enter your password length: "))

random.shuffle(character)

password = []

for i in range(length):
    password.append(random.choice(character))

random.shuffle(password)

output = "".join(password)

print("= ", output)

print(string.ascii_letters)