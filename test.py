import os
from pathlib import Path
zone_file=open('add.txt','r')
a=[]
for line in zone_file:
  print(line)
 #if line.startswith('#'):
 # a.append(line)
 # continue
 #elif not line.strip():
 # a.append(line)
 # continue
 #else:
  line=line.replace('0.0.0.0','127.0.0.1')
  #line=line.replace('\n','')
  #line=line+' A 0.0.0.0\n'
  a.append(line)
#print(a)
zone_file.close()
del zone_file
zone_file=open('add.txt','w')
for each in a:
 zone_file.write(each)
