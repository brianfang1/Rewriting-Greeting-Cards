## Brian Fang, brian.fang@csu.fullerton.edu
## Edward Le, edwardl@csu.fullerton.edu
## Ashu Singh, ashusingh28@csu.fullerton.edu
## CPSC 535
## March 3, 2021



##S = "My dear Anna, let me congratulate you on the beautiful car that you purchased today. It looks very posh. I hope you got a good deal. Cars are expensive but much needed. Best regards, Naomi."
##LS = [ ["Anna", "Jovi and Victor"], ["car", "house"], ["today", "last week"], ["posh", "well built"] ]

##S = "Our newest students have been asked to stay today until the end of the classes. The old principal."
##LS = [ ["new", "old"] , [ "student", "teacher"], ["to", "yester"], ["old", "young"], ["end", "beginning"] ]

##S = "Our newest students have been asked to stay today until the end of the classes. The old principal."
##LS = [["old", "young"],  ["student", "teacher"],  ["to", "yester"],  ["end", "beginning"], ["new", "old"]]

##S = "Happy Birthday Tom! Today is a very special day. Remember to enjoy yourself. This only happens once a year. Bye!"
##LS = [["Tom", "Amy"], ["Today", "Yesterday"], ["day", "night"], ["once", "to"], ["to", "here"]]
##Expected outcome: "Happy Birthnight Amy! Yesterday is a very special night. Remember here enjoy yourself. This only happens to a year. Bye!"

##S = "new new old new old old new"
##LS = [["new", "old"], ["old", "young"]]
##"old old young old young young old"

S = "May the spirit of Christmas infuse your life and that of your family members with hope, positivity, and joy."
LS = [["spirit", "world"], ["life", "day"], ["family", "kids"], ["joy", "happiness"]]


N = len(S)
M = len(LS)
print("S: " + S)
print("N: " + str(N))
print("M: " + str(M))
print("LS: " + str(LS))


firstIndex = N
tempP = ""
finalString = ""
stringsToReplace = True

while(stringsToReplace == True):
  ## Iterate through List of String Pairs
  for P in LS:
    ## Find earliest occurence out of a string that needs to be replaced in String S
    index = S.find(P[0])
    if(index > -1 and index < firstIndex):
      ## Grab String Pair from LS of earliest occurence
      tempP = P
      firstIndex = index 

  ## If there are NO MORE strings to replace, concatenate rest of String S to the final String to be displayed
  if(firstIndex == N):
    finalString += S
    stringsToReplace = False
  else:
    ## Replace the earliest occurence of the String Pair
    S = S.replace(tempP[0], tempP[1], 1)
    ## Partition string; [0] = String BEFORE delimiter, [1] = Delimiter, [2] = String AFTER delimiter
    stringPartition = S.partition(tempP[1])
    ##  Take the String BEFORE the delimiter and including the delimiter and concatenate it to a String that will be outputted 
    finalString += stringPartition[0] + stringPartition[1]
    ## Take the rest of the String and look for more words to replace
    S = stringPartition[2]
    firstIndex = N

print("Final String: " + finalString)
