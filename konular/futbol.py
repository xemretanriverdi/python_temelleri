
matchResults=[1,1,1,0,2,1,1,2,2,1,1,0,1,2,2,1,1,2,2,2,0,1,0,1,1,2,1,1,2,1,1,2,2,2]

def score(list):
    """
 
 """
    score=0
    matchCount=0 

    for i in list:
        if(matchCount<=17):

                if i == 0 :
                    score=score+1
        
                if i == 1 :
                    score=score+3
        
        if(matchCount>=17):
                if i == 0 :
                    score=score+1
        
                if i == 2 :
                    score=score+3

        matchCount=matchCount+1
    return score

print("The total point of Besiktas JK",score(matchResults))

    


    
