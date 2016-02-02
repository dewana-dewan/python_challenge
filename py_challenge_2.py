import pprint

strr=input()
lis=[]

#while executing the program in the ide, add a full stop at the end.
while(not(strr=='.')):
        if(not (strr == '\n')):
                lis=lis+[strr]
        strr=input()
        
dicta={}
strr1=''.join(lis)

for char in strr1:
	dicta.setdefault(char,0)
	dicta[char]=dicta[char]+1

pprint.pprint(dicta)

#after execution you will have the word->equality
#link for next problem -> http://www.pythonchallenge.com/pc/def/equality.html
