test_in=input()
#take input from user

for i in test_in:
    if(i.isalpha()):
        print(chr(ord(i)+2),end="")
        
#the odr functions returns the ascii value of character i 
#after adding 2, by using the chr funstion we obtain the character from the ascii value 

    else:
        print(i,end="")

#if a character is not an alphabet there is no need to convert it.

    

