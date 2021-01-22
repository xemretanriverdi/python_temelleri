
matchResults=[1,1,1,0,2,1,1,2,2,1,1,0,1,2,2,1,1,2,2,2,0,1,0,1,1,2,1,1,2,1,1,2,2,2]

def score(list):
    firstSeason=list[0:17]
    secondSeason=list[17:34]

    week=1
    score=0
    for i in firstSeason:
        
        if i == 0 :
            score+=1
        
        if i == 1 :
            score+=3
    
    for i in secondSeason:
        
        if i == 0 :
            score+=1
        
        if i == 2 :
            score+=3

    return score



print("Besiktas sezon sonu puanı :",score(matchResults))

    


    
