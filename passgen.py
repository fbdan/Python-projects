#Generator de parole 18.03.20 B Florea
# zNx8W%Ij 
# exemplu mai sus

import random

toatechar = "abcdefghijklmnopqrstuvwxyz123456789ABCDEFGHIJKLMNPQRSTUVWXYZ!@#$%^&*"

passlen = int(input("Introdu dimenisiune parola: "))

p ="".join(random.sample(toatechar,passlen))

print(p)