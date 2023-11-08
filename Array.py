from array import *

#vals = array('i', [1,2,3,34,4,5,6,7])

#vals.append(5)
#vals.append(4)
#vals.append(3)
#vals.append(2)
#for i in range(len(vals)):
   
  #  print(vals[i])





vals = array('i', [1,2,3,5,6,7])

newarr = array(vals.typecode,(a*a for a in vals))
for i in newarr:
    
    print(i)
print()
