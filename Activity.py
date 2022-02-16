introduction=input("Tell about yourself:")
lettercount=0
wordcount=1
for i in introduction:
    lettercount=lettercount+1
    if (i==" "):
        wordcount=wordcount+1
print("Number of words:",wordcount) 
print ("Number of letters:",lettercount)       