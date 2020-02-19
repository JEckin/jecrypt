#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
from array import *

#Verwandelt String in hexa in array
#hexa("a") => ['6','1']
def hexa(x):
	temp = list(x.encode('hex'))
	return temp

#Verbindet input char mit key char
def one (x,y):
	#x = input y = key
	if x == "":
		print "Error: x is empty"
		exit()
	if y == "":
		print "Error: y is empty"
		exit()
	#print x
	x= list(x.encode('hex'))
	#print x
	y= list(y.encode('hex'))
	#print y
	x[0]=int(str(x[0]), 16)
	for z in range(int(y[0],16)):
		#print "x0",x[0]
		if x[0] < 7:
			x[0]=x[0]+1
		else:
			x[0]=2
	x[1]=int(str(x[1]), 16)
	for z in range(int(y[1],16)):
		#print "x1",x[1]
		if x[1] < 15:
			x[1]=int(x[1]+1)
		else:
			x[1]=0

	x=str(hex(x[0]).split('x')[-1]),str(hex(x[1]).split('x')[-1])
	#x=table[x[0]][x[1]]
	x=''.join(x)
	#print "Hex: ",x
	x=x.decode('hex')
	#print "x2: ",x
	return x

#String zu hex zu array tausch mit table zu String
#two("a") => 4
def two(x):
	temp = list(x.encode('hex'))
	temp=table[temp[0]][temp[1]]
	temp=''.join(temp)
	return temp

os.system("clear")

input = list(raw_input("Input: "))
key = list(raw_input("Key: "))

table = {"0":"","1":"","2":"","3":"","4":"","5":"","6":"","7":""}
#print table["0"]["a"]
table["0"] = {"0":"","1":"","2":"","3":"","4":"","5":"","6":"","7":"","8":"","9":"","a":"","b":"","c":"","d":"","e":"","f":""}
table["1"] = {"0":"","1":"","2":"","3":"","4":"","5":"","6":"","7":"","8":"*","9":"","a":"","b":"","c":"","d":"","e":"","f":""}
table["2"] = {"0":"C","1":"n","2":"%","3":"D","4":"E","5":"]","6":"\\","7":"[","8":"Z","9":"$","a":" ","b":"m","c":"e","d":"W","e":"X","f":"Y"}
table["3"] = {"0":"o","1":"?","2":"\/","3":"_","4":"v","5":"t","6":"d","7":"&","8":"’","9":"~","a":"-","b":"(","c":"l","d":"=","e":"j","f":"k"}
table["4"] = {"0":"B","1":"0","2":".","3":"r","4":"u","5":"!","6":"^","7":"K","8":")","9":"7","a":"8","b":"Q","c":"-","d":"f","e":"i","f":"V"}
table["5"] = {"0":"A","1":"1","2":">","3":"\"","4":"F","5":"s","6":"c","7":"w","8":"x","9":"6","a":"9","b":"\'","c":"P","d":"g","e":"h","f":"U"}
table["6"] = {"0":"+","1":"4","2":"p","3":"q","4":"`","5":"G","6":"I","7":"}","8":"y","9":"5","a":":","b":"N","c":"O","d":"<","e":"S","f":"T"}
table["7"] = {"0":"@","1":"3","2":"?","3":"z","4":"a","5":"H","6":"b","7":"J","8":"#","9":"L","a":"M","b":";","c":"\{","d":"R","e":">","f":"xx"}
####
output=input
#one(input[0],key[0])
for x in range(len(key)):
	for y in range(len(input)):
		temp = one(output[y],key[x])
		#print "Hex1: ",temp
		output[y] = two(temp)
#print one()
#output[y]=one(input[y])
####
output = ''.join(output)
print "Output:",output
