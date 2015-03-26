from environment import *
ev=Environment([4, 3], [4, 11])
ev.readEnvironment()

def actions(coord, L):
    R=[]
    x=coord[0]
    y=coord[1]
    n=len(L)
    m=len(L[0])
    if(y+1<m and L[x][y+1]!='#'):
        R+=[[x, y+1]]
    
    if(x+1<n and L[x+1][y]!='#'):
        R+=[[x+1, y]]
    
    if(y-1>=0 and L[x][y-1]!='#'):
        R+=[[x, y-1]]
    
    if(x-1>=0 and L[x-1][y]!='#'):
        R+=[[x-1, y]]
        
    return R
    
def h(c1, c2):
    print c1, c2, ((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2)**0.5
    return ((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2)**0.5

def f(n1, n2, target, distList):
    return distList[n1[0]][n1[1]]+h(n2, target)+1
    
def addToFrontier(frontier, child, distList, childCost):
    
    if frontier==[]:
        frontier+=[child]
        return frontier
    i=0
    while(i<len(frontier)):
        if distList[frontier[i][0]][frontier[i][1]]>childCost:
            return frontier[0:i]+[child]+frontier[i:]
        i+=1
            
    return frontier+[child]
    
def A_Star():
    global ev
    frontier=[ev.start]
    explored=[]
    cleanMap=ev.giveEnvironmentList()
    distList=[]
    for i in cleanMap:
        temp=[]
        for j in i:
            temp+=[-1]
        distList+=[temp]
    distList[ev.start[0]][ev.start[1]]=0
    while(len(frontier)!=0):
        node=frontier[0]
        ev.setColor(node, 'new')
        ev.printEnvironment()
        ev.setColor(node, 'explored')
        print frontier
        print distList
        hmm=raw_input()
        frontier=frontier[1:]
        temp_queue=actions(node, cleanMap)
        
        while(temp_queue!=[]):
             
            child=temp_queue[0]
            if child==ev.target:
                print "Hell Yeah"
                return
            temp_queue=temp_queue[1:]
            childCost=f(node, child, ev.target, distList)
            if(distList[child[0]][child[1]]==-1):
                flag=0
                for i in range(0, len(frontier)):
                    if frontier[i]==child:
                        if childCost<distList[child[0]][child[1]]:
                            frontier.remove(child)
                        else:
                            flag=1
               
                if flag!=1:
                    frontier=addToFrontier(frontier, child, distList, childCost)
                    distList[child[0]][child[1]]=childCost
                    print ""
                    
                    
                    
                    
A_Star()
                    
                
    