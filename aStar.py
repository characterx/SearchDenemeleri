from environment import *
ev=Environment([4, 2], [4, 8])
ev.readEnvironment()


    
def h(c1, c2):
    return ((c1[0]-c2[0])**2 + (c1[1]-c2[1])**2)**0.5

def g(n1, n2):
    return 1

def f(n1, n2, target, distList):
    return distList[n1[0]][n1[1]]+h(n2, target)
    
def addToFrontier(frontier, child, distList):
    
    if frontier==[]:
        frontier+=[child]
        return frontier
    i=0
    while(i<len(frontier)):
        if frontier[i][2]>child[2]:
            return frontier[0:i]+[child]+frontier[i:]
        i+=1
            
    return frontier+[child]
    
def A_Star():
    global ev
    frontier=[ev.start+[h(ev.start, ev.target), [ev.start]]]
    ev.giveEnvironmentList()
    distList=[]
    for i in ev.cleanMap:
        temp=[]
        for j in i:
            temp+=[-1]
        distList+=[temp]
    distList[ev.start[0]][ev.start[1]]=0
    while(len(frontier)!=0):
        node=frontier[0]
        if(len(node[3])>1):
            distList[node[0]][node[1]]=distList[node[3][-2][0]][node[3][-2][1]]+1
        else:
            distList[node[0]][node[1]]=1
        #print frontier
        #print distList
        frontier=frontier[1:]
        temp_queue=ev.actions(node)
        
        while(temp_queue!=[]):
             
            child=temp_queue[0]
            if child==ev.target:
                print "Hell Yeah"
                answer=node[3]
                for i in range(0, len(answer)):
                    ev.setColor(answer[i], "new")
                ev.setColor(child[:2], "new")
                ev.printEnvironment()
                return
            ev.setColor(child[:2], "new")
            ev.printEnvironment()
            ev.setColor(child[:2], "explored")
            hmm=raw_input()
            child+=[f(node, child, ev.target, distList)]
            child+=[node[3][:]+[child[:2]]]
            temp_queue=temp_queue[1:]
            if(distList[child[0]][child[1]]==-1):
                flag=0
                for i in range(0, len(frontier)):
                    if frontier[i][:2]==child[:2]:
                        if child[2]<frontier[i][2]:
                            frontier.remove(frontier[i])
                            break
                        else:
                            flag=1
               
                if flag!=1:
                    frontier=addToFrontier(frontier, child, distList)
                    
                    
                    
                    
A_Star()
                    
                
    