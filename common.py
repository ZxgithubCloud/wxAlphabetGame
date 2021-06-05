

import os
import random

pwd = os.path.abspath('.')

print("pwd is : ",pwd)

balldir = pwd + '/pygame/resources'

print("balldir is : ",balldir);

#print("os.path : ",os.path)

adict = {'test': 1,'hello': 2}
bdict = adict
adict['test'] = 100
print(bdict['test'])
print(id(bdict))
print('address is : ',bdict)
print(id(adict))
print(adict)

print("random: test!!")
n = random.randint(0, 100)
print("random value is: ", n)

print("ascii 97 is: ", chr(97))
#print("ascii 97 is: ", ascii('a'))