from colorama import *

class Environment:
    cleanMap=[]
    
    def __init__(self, A, B):
        self.start=A
        self.target=B
        init(autoreset=True)
        self.Map=[]
        cleanMap=self.giveEnvironmentList()
    def readEnvironment(self):
        outfile = open("map.txt", "r")
        s=outfile.read()
        L=[]
        i=0
        while(i<len(s)):
        	temp=[]
        	while(s[i]!='\n'):
        		temp+=[[s[i], "white"]]
        		i+=1
        		
        	L+=[temp]
        	i+=1
        self.Map=L
        
        self.setColor(self.start, "start")
        self.setColor(self.target, "target")
        
        for i in range(0,len(self.Map)):
            for j in range(0, len(self.Map[i])):
                if(self.Map[i][j][0]=='#'):
                    self.setColor([i,j], "barrier")
                    
        
    def printEnvironment(self):
        for i in range(0, len(self.Map)):
            raw=[]
            for j in range(0, len(self.Map[i])):
                if(self.Map[i][j][1]=='white'):
                    raw+=[Back.WHITE + '  ']
                if(self.Map[i][j][1]=='green'):
                    raw+=[Back.GREEN + '  ']
                if(self.Map[i][j][1]=='red'):
                    raw+=[Back.RED + '  ']
                if(self.Map[i][j][1]=='blue'):
                    raw+=[Back.BLUE + '  ']
                if(self.Map[i][j][1]=='black'):
                    raw+=[Back.BLACK + '  ']
                if(self.Map[i][j][1]=='yellow'):
                    raw+=[Back.YELLOW + '  ']
            print "".join(raw)
    def giveEnvironmentList(self):
        L=[]
        for i in range(0, len(self.Map)):
            temp=[]
            for j in range(0, len(self.Map[i])):
                temp+=[self.Map[i][j][0]]
            L+=[temp]
            
        self.cleanMap=L
        return L
                
    def setColor(self,coordinates, obj):
        if(obj=="barrier"):
            self.Map[coordinates[0]][coordinates[1]][1]="green"
        elif(obj=="unexplored"):
            self.Map[coordinates[0]][coordinates[1]][1]="white"
        elif(obj=="start"):
            self.Map[coordinates[0]][coordinates[1]][1]="black"
        elif(obj=="target"):
            self.Map[coordinates[0]][coordinates[1]][1]="yellow"
        elif(obj=="explored"):
            self.Map[coordinates[0]][coordinates[1]][1]="blue"
        elif(obj=="new"):
            self.Map[coordinates[0]][coordinates[1]][1]="red"
            
        
    def actions(self, coord):
        R=[]
        x=coord[0]
        y=coord[1]
        n=len(self.cleanMap)
        m=len(self.cleanMap[0])
        if(y+1<m and self.cleanMap[x][y+1]!='#'):
            R+=[[x, y+1]]
        
        if(x+1<n and self.cleanMap[x+1][y]!='#'):
            R+=[[x+1, y]]
        
        if(y-1>=0 and self.cleanMap[x][y-1]!='#'):
            R+=[[x, y-1]]
        
        if(x-1>=0 and self.cleanMap[x-1][y]!='#'):
            R+=[[x-1, y]]
            
        return R
    
        
    
    

