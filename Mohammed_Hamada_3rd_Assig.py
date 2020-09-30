
#Student Name: Mohammed Hamada
#Student No: 120201362
#Assignmet3

#get first string and second string
firstString = input("Plz Enter First string ")
secondString = input("Plz Enter second string ")

#get the length of both 2 strings
i = len(firstString)
j = len(secondString)


# define a function for the algorithm of min edit distance with getting arg of 1st string 2nd string and length of both
def minEditDist(firstString,secondString,i,j):
    #check if 1st string is empty then return other string length which mean you need to change all letters
    if i == 0:
        return j
    #check if 2st string is empty then return other string length which mean you need to change all letters
    if j == 0:
        return i
    #if the letters are the same then we have to pass and go back with reduce the length to pointing to next letter
    if firstString[i-1]== secondString[j-1]:
        return minEditDist(firstString,secondString,i-1,j-1)
    
    # we will calculate the minum of left cell and right cell as well doen cell and add 1 for initial letter
    return 1+min(minEditDist(firstString,secondString,i,j-1),minEditDist(firstString,secondString,i-1,j),minEditDist(firstString,secondString,i-1,j-1))


print(minEditDist(firstString,secondString,i,j))