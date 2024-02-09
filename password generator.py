# python project - password program
# create a password creater with strong requirements

import random


caps = "QWERTYUIOPASDFGHJKLZXCVBNM"
small = "qwertyuiopasdfghjklzxcvbnm"
num = "1234567890"
spec = "!@#$%^&*=+"

upper,lower,digits,odd = True,True,True,True            #can set true or false depending on need
final_pass = ""

if upper:
    final_pass += caps
if lower:
    final_pass += small
if digits:
    final_pass += num
if odd:
    final_pass +=spec

length = 8
amount = 3

for a in range(amount):
    password = "".join(random.sample(final_pass,length))
    print(password)
