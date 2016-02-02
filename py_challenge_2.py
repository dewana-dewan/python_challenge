import pprint

strr=input()
lis=[]

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
