
#Student Name : Mohammed Hamada
#student No: 120201362

def minEditDist(s, t, costs=(1, 1, 2)):

    

    #calculate the length
    rows = len(s)+1
    cols = len(t)+1

    #delete = 1 , insert = 1 , substitues = 2 , 
    deletes, inserts, substitutes = costs
    
    #2D arr
    dist = [[0 for x in range(cols)] for x in range(rows)]

    #for each row i from 1 to n do D[i,0] D[i-1,0] + del-cost(source[i])
    for row in range(1, rows):
        dist[row][0] = row * deletes

    #for each column j from 1 to m do D[0,j] D[0, j-1] + ins-cost(target[j])
    for col in range(1, cols):
        dist[0][col] = col * inserts
        

    #D[i, j] MIN( D[i􀀀1, j] + del-cost(source[i]), D[i􀀀1, j􀀀1] + sub-cost(source[i], target[j]), D[i, j􀀀1] + ins-cost(target[j]))
    for col in range(1, cols):
        for row in range(1, rows):
            if s[row-1] == t[col-1]:
                cost = 0
            else:
                cost = substitutes
            dist[row][col] = min(dist[row-1][col] + deletes,
                                 dist[row][col-1] + inserts,
                                 dist[row-1][col-1] + cost) # substitution

    for r in range(rows):
        print(dist[r])
    
 
    return dist[row][col]

firstString = input("Plz Enter First string ")
secondString = input("Plz Enter second string ")


print(minEditDist(firstString, secondString))
