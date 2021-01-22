
def activeChecker():

    """


"""
 
    q = input("Are you watching Netflix right now? (Type YES): ")

    if(q=="YES"):


             return True
             
    else:
            return False




def activeCalc():
    """
 
 """
    isActive = True
    start = timeNow()
    hourWait(2)


    activeChecker()


    end = timeNow()


    return end - start - 0.5



def profitCalc():
    """
 
 """
    activeTime = 150 
    rate = 14 #bu gelecek seneye olan zam oranı olarak anladım
    profit = 0
    cost = 240
    raiseRate=0.1
    i=1;

    while(activeTime>100):
        # // ile kalansiz
        profit += (0.05 *((activeTime-100)//10)+0.20)*cost
        activeTime -= 14
        cost += cost*raiseRate 
        i+=1

    return profit


