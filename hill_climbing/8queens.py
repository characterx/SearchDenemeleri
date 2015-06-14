from random import randint
from copy import deepcopy
def generateRandomState(n):
    state=[[0 for i in range(n)] for j in range(n)]
    for j in range(n):
        state[randint(0,n-1)][j]=1
    return state
    

#how many queens attack each other
def heuristicFunction(state):
    h=0
    n=len(state)
    for i in range(n):
        for j in range(n):
            if state[i][j]==1:
                for k in range(n):
                    if state[i][k]==1 and k!=j:
                        h+=1
                for k in range(n):
                    if state[k][j]==1 and k!=i:
                        h+=1
                x=i-1
                y=j-1
                while x>=0 and y>=0:
                    if state[x][y]==1:
                        h+=1
                    x-=1
                    y-=1
                
                x=i+1
                y=j+1
                while x<n and y<n:
                    if state[x][y]==1:
                        h+=1
                    x+=1
                    y+=1
                
                x=i+1
                y=j-1
                while x<n and y>=0:
                    if state[x][y]==1:
                        h+=1
                    x+=1
                    y-=1
                    
                x=i-1
                y=j+1
                while x>=0 and y<n:
                    if state[x][y]==1:
                        h+=1
                    x-=1
                    y+=1
    return h/2
    
def minimumNeighbour(state):
    n=len(state)
    minimum_cost=n*n
    minimum_neighbour=[]
    for i in range(n):
        for j in range(n):
            if state[i][j]==1:
                for k in range(n):
                    if k==i:
                        continue
                    neighbour_state=deepcopy(state)
                    neighbour_state[i][j]=0
                    neighbour_state[k][j]=1
                    neighbour_cost=heuristicFunction(neighbour_state)
                    if minimum_cost>neighbour_cost:
                        minimum_cost=neighbour_cost
                        minimum_neighbour=neighbour_state
    
    return (minimum_cost, minimum_neighbour)
    

def hillClimbing(state):
    while True:
        minimum_cost, minimum_neighbour = minimumNeighbour(state)
        state_cost=heuristicFunction(state)
        if minimum_cost<state_cost:
            state=minimum_neighbour
        else:
            return (state_cost, state)
        


def randomRestartHillClimbing(n, trial_number):
    success=0
    for i in range(trial_number):
        initial_state=generateRandomState(n)
        state_cost, state = hillClimbing(initial_state)
        if state_cost==0:
            success+=1
        print "state_cost =", state_cost
        for j in range(n):
            for k in range(n):
                print state[j][k],
            print ""
        print ""
        
    print "Success Rate :", success,"/", trial_number
    
randomRestartHillClimbing(20, 100)