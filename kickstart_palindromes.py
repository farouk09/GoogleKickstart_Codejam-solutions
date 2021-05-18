# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 00:20:14 2019

@author: Snow
"""
f = open("demofile3.txt", "w")
chaine=""
list=[1,2,3]
for x in list:
    chaine=chaine+" "+str(x)
chaine=chaine+"\n"   
f.write(chaine[1:])
f.write("Woops! I have deleted the content!")

f = open("demofile3.txt", "r")
f1 = open("demofile.txt", "w")


f1.write('lalala'+"\n")
for x in f:
    f1.write(x)

#open and read the file after the appending:
f1 = open("demofile3.txt", "r")
print(f1.read())
