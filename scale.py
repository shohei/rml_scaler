import re
import math
fin = open('in.rml')
print """
###########################################
*** RML scaling script ***

2014, Shohei Aoki
for the sake of MDX-40A users and so on...

###########################################

"""
#scale = 2.3
scale = raw_input("Input the scale you want (ex.2.3): ")
try:
    scale = float(scale)
except:
    print "Input a valid number!! Aborting."	
    exit()
pu = re.compile("^PU")
z = re.compile("^Z") 
input = raw_input("RML file name to convert?: ")
output = raw_input("Output file name?: ") 
if input == "":
    print "No input file specified. Exit."	
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


