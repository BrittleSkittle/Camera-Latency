import dpkt
import usbrply
import struct
from PIL import Image
import csv
from matplotlib import pyplot

f = open("/home/paw/424x240/susCarr15.txt")
pktnum = list()
pktTime = list()
data = list()
size = 100000
with open('/home/paw/424x240/suscsv15.csv', newline='') as csvfile:
    """spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in spamreader:
        for sus in row:"""
    read = csv.reader(csvfile)
    for thing in read:
        if(thing[2]=="2.5.4"):
            pktnum.append(int(thing[0]))
            pktTime.append(thing[1])
#print(pktnum)
for i in range(0,size): #2055
    line = f.readline().rstrip()
    try:
        pInd = line.index("pkt")+3
        ind = pInd
        endInd = pInd+1
        while(endInd<len(line)):
            if(line[endInd].isdigit()):
                endInd+=1
            else:
                break
        pktNum = int(line[int(pInd):int(endInd)])
        #print(pktNum)
        try:
            pktnum.index(pktNum)
        except Exception as e:
            #print(e)
            continue
    except Exception as e:
        #print(e) 
        continue
    dataTemp = list()
    for x in range(0, 2055):
        line = f.readline().rstrip()
        if line.endswith("*/"):
            line = line.split("/*")[1]
            line = line.split("*/")[0]
            dataTemp.append(line)
        #print(line)
    data.append(dataTemp)
    #print(dataTemp)
print(len(data))
dots = list()
for pkt in data:
    #print(len(pkt))
    dot = 0
    for line in pkt:
        #print(line)
        dot+=line.count('.')+line.count('~')
    dots.append(dot)
for x in range(0,len(dots)):
    if (dots[x]>15500):
        print(pktTime[x][6:len(pktTime[x])-1])
#print(dots)
for x in range(len(pktTime)-1):
    pktTime[x] = pktTime[x][6:len(pktTime[x])-3]
xRange = int(len(dots)/2)
#pyplot.plot(range(0,xRange,1), dots[0:xRange:1])
#pyplot.xticks(range(0,xRange,50), pktTime[0:xRange:50])
#pyplot.show()

