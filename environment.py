from colorama import *

class Environment:
    
    def __init__(self, A, B):
        self.start=A
        self.target=B
        init(autoreset=True)
        self.Map=[]
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
                if(self.Map[i][j][1]=='cyan'):
                    raw+=[Back.CYAN + '  ']
                if(self.Map[i][j][1]=='yellow'):
                    raw+=[Back.YELLOW + '  ']
            print "".join(raw)
    def giveEnvironmentList(self):
        L=[]
        for i in range(0, len(self.Map)):
            temp=[]
            for j in range(0, len(self.Map[i])):
                temp+=[s[i]]
            L+=[temp]
            
        return L
                
    def setColor(self,coordinates, obj):
        if(obj=="barrier"):
            self.Map[coordinates[0]][coordinates[1]][1]="green"
        elif(obj=="unexplored"):
            self.Map[coordinates[0]][coordinates[1]][1]="white"
        elif(obj=="start"):
            self.Map[coordinates[0]][coordinates[1]][1]="cyan"
        elif(obj=="target"):
            self.Map[coordinates[0]][coordinates[1]][1]="yellow"
        elif(obj=="explored"):
            self.Map[coordinates[0]][coordinates[1]][1]="blue"
        elif(obj=="new"):
            self.Map[coordinates[0]][coordinates[1]][1]="red"
            
        
    
        
    
    

