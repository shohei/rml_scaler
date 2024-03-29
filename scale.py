#!/usr/bin/env python
#-*- coding: utf-8 -*-

import re
import math
print """
###########################################
*** RML scaling script ***

2014 May, Shohei Aoki
For the sake of MDX-40A users and so on...

If you have any problem, please contact: 
Shohei Aoki / shoaok [at] GMAIL.COM

###########################################

"""
#scale = 2.3
scale = raw_input("Input the scale you want (default 2.48): ")
if scale == "":
    scale = 2.48 
else:
    try:
        scale = float(scale)
    except:
        print "Input a valid number!! Aborting."	
        exit()
pu = re.compile("^PU")
z = re.compile("^Z") 
input = raw_input("RML file name to convert?: ")
if input == "":
    print "No input file specified. Exit."	
    exit()
fin = open(input)
output = raw_input("Output file name?: ") 
if output == "":
    fout = open('out.rml','w') 
else:
    fout = open(output,'w') 
for line in fin:
    newline = -1
    if not pu.match(line) == None:
        lat = line.split('PU')[1]
        x = lat.split(',')[0]
        y = lat.split(',')[1].split(';')[0]
        sx = int(int(x) * scale)
        sy = int(int(y) * scale)
        print 'Convert x:'+str(x)+"->"+str(sx)+", Convert y:"+str(y)+"->"+str(sy)
        newline = "PU"+str(sx)+","+str(sy)+";\n"
    elif not z.match(line) == None:
        lat = line.split('Z')[1]
        x = lat.split(',')[0]
        y = lat.split(',')[1].split(';')[0]
        depth = lat.split(',')[2].split(';')[0] 
        sx = int(int(x) * scale)
        sy = int(int(y) * scale)
        print 'Convert x:'+str(x)+"->"+str(sx)+", Convert y:"+str(y)+"->"+str(sy)
        newline = "Z"+str(sx)+","+str(sy)+","+depth+";\n"
     
    if newline == -1:
        fout.write(line)
    else:
        fout.write(newline)

print
print 
print "Successfully processed. Exit."

fout.close()


