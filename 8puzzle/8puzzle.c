#include <stdio.h>
#include <stdlib.h>

#define DATA(x) (x)->data
#define NEXT(x) (x)->next

#define MAP(a, x, y) ((a).map).map[(x-1)][(y-1)]
#define PARENT_X(a) (a).parent[0]
#define PARENT_Y(a) (a).parent[1]
#define H_COST(a) (a).heuristic_cost

typedef
struct node
{
    long long int data;
    struct node *next;
    
}node, *np;

typedef
struct pqNode
{
    char map[3][3];
    char parent[2];
    int heuristic_cost;
}pqNode, ;

np explored;

pqNode priorityQueue[10000];

void exploredInitializer()
{
    explored=malloc(sizeof(node));
    DATA(explored)=0;
    NEXT(explored)=NULL;
}

np createNewNode(long long int n)
{
    np ret=malloc(sizeof(node));
    DATA(ret)=n;
    NEXT(ret)=NULL;
    return ret;
}

void addToExplored(long long int n)
{
    np iter;
    if(DATA(explored)==0)
    {
        NEXT(explored)=createNewNode(n);
        DATA(explored)++;
        return;
    }
    
    iter=explored;
    while(NEXT(iter)!=NULL && DATA(NEXT(iter))<n)
        iter=NEXT(iter);
        
        

    
    
}

