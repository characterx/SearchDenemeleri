def isPossible(state):
    coastA=state[0]
    coastB=state[1]
    flag=True
    if(coastA[0]!=0 and coastA[0]<coastA[1]):
        flag=False
    
    if(coastB[0]!=0 and coastB[0]<coastB[1]):
        flag=False
        
    return flag
    

def actions(state):
    coastA=state[0]
    coastB=state[1]
    boat_position=state[2]
    temp=[]
    if(boat_position==0):
        for i in range(0, min(coastA[0]+1, 3)):
            for j in range(0, min(coastA[1]+1, 3)):
                if(i+j<=2 and [i, j]!=[0, 0]):
                    temp+=[[i,j]]
    else:
        for i in range(0, min(coastB[0]+1, 3)):
            for j in range(0, min(coastB[1]+1, 3)):
                if(i+j<=2 and [i, j]!=[0, 0]):
                    temp+=[[i,j]]
    #print temp
    R=[]        
    for i in range(0, len(temp)):
        new_state=[0, 0, 0, 0, 0]
        new_state[0]=state[0][:]
        new_state[1]=state[1][:]
        new_state[2]=state[2]
        new_state[3]=state[3]
        new_state[4]=state[4][:]
        if boat_position==0:
            new_state[0][0]-=temp[i][0]
            new_state[0][1]-=temp[i][1]
            new_state[1][0]+=temp[i][0]
            new_state[1][1]+=temp[i][1]
            new_state[2]=1
            new_state[3]+=1
        
        if boat_position==1:
            new_state[0][0]+=temp[i][0]
            new_state[0][1]+=temp[i][1]
            new_state[1][0]-=temp[i][0]
            new_state[1][1]-=temp[i][1]
            new_state[2]=0
            new_state[3]+=1
        #print "a new_state before :",
        #print new_state
        #print "state after new_state :",
        #print state
        new_state[4]+=[[new_state[0][:], new_state[1][:]]]
        if isPossible(new_state):
            R+=[new_state]
    
    #print "R is:"
    #for i in R:
    #    print i
    return R
   
def addToQueue(queue, node):
    for i in range(0, len(queue)):
        if queue[i][:3]==node[:3]:
            if queue[i][3]>node[3]:
                queue=queue[:i]+queue[i+1:]
                return addToQueue(queue, node)
            else:
                return queue
    
    i=0
    while(i<len(queue) and queue[i][3]<node[3]):
        i+=1
    if i==len(queue):
        #print "queue in fn1: ",
        #print queue+[node]
        return queue + [node]
    #print "queue in fn2: ",
    #print queue[:i]+[node]+queue[i:]
    #print queue[:i]
    #print [node]
    #print queue[i:]
    return queue[:i]+[node]+queue[i:]

def isGoalState(state):
    return state[1]==[3, 3]

def mc():
    initial_state=[[3, 3], [0, 0], 0, 0, []]
    queue=[]
    explored=[]
    queue+=[initial_state]
    while queue!=[]:
        node=queue[0]
        queue=queue[1:]
        #print "node :",
        #print node
        explored+=[node[:3]]
        if isGoalState(node):
            return node
        temp=actions(node)
        #print "temp :",
        #print temp
        while temp!=[]:
            new_node=temp[0]
            temp=temp[1:]
            if new_node[:3] in explored:
                continue
            
            queue=addToQueue(queue, new_node)
        #print "queue after adding node's actions :",
        #print queue

a=mc()
print a
for i in a[4]:
    print i