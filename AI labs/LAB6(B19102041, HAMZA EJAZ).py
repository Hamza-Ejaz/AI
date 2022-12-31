def printTT(transition_Table):    
    print("\n--Transition_Table--")
    # printing values from list (i.e. language) 
    print("    "+'  '.join(map(str, language))) 
# lab6 (B19102041 Hamza Ejaz)
    for key,value in transition_Table.items():
        print(key,end=": ")
        for j in value.values():
            print(j,end=" ")
        print("\n")

def createTT(statesCount,language):
    tt={}
    for i in range(statesCount):
        dict={}
        print(f"\n\tCURRENT STATE: S{i}")
        for j in language:
            dict[j]=[]
            print("\nNote: Enter 'BREAK' when finish specifing transitions")
            while True:
                next_state=input(f"{j} : ").upper()
                if(next_state=="BREAK"):
                    break
                dict[j].append(next_state)
        tt["S"+str(i)] = dict
    return tt

def checkRe(root,str_val,f_state,index): 
    if(root==f_state and index==len(str_val)):        
        return True
    elif(index>len(str_val)-1):
        return False
    else:
        for i in tt[root][str_val[index]]:
            a=checkRe(i,str_val,f_state,index+1)
            if(a):
                return True
            else:
                pass
    return False
    
""" 
    DRIVER CODE
"""
language=[]
lCount=int(input("\nSpecify count for language characters: "))
for i in range(lCount):
    print(f"Enter Character: ",end="")
    a=input()
    language.append(a)

print("\nSpecify States Count: ", end="")
states_Count=int(input())
print("\nSpecify Final State: ", end=" ")
final_State= input().upper()

tt=createTT(states_Count,language)

while True:
    #This function prints dict in the format of TT
    printTT(tt) #You can also use 'print(tt)' here 

    print("\nSpecify String: ", end="" )
    str_val=input()
    if(str_val.lower()=='bye'):
        break
    else:
        print("\nstatus: ", checkRe("S0",str_val,final_State,0))
        print("\nNOTE:To exit enter: bye")