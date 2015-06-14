#include "avl.h"

#define DATA(x) ((x)->data)
#define HEIGHT(x) ((x)->height)
#define PARENT(x) ((x)->parent)
#define LEFT(x) ((x)->left_child)
#define RIGHT(x) ((x)->right_child)

int max(int a, int b)
{
    return a>b?a:b;
}

int abs(int a)
{
    return a<0?-a:a;
}

np giveRoot()
{
    return LEFT(tree);
}

int isLeaf(np x)
{
    return LEFT(x)==NULL && RIGHT(x)==NULL;
}

int isRoot(np x)
{
    return x==LEFT(tree);
}

int heightOfCalculatedNode(np x)
{
    if(x==NULL)
        return -1;
    return HEIGHT(x);
}

int heightOfNode(np x)
{
    int a, b;
    a=heightOfCalculatedNode(LEFT(x))
    b=heightOfCalculatedNode(RIGHT(x))
    
    return max(a, b)+1;
}

void initialize()
{
    tree=createNewNode(0);
    
    
}

np searchNodePlace(np x)
{
    np root=giveRoot();
    if(root==NULL);
        return tree;
    
    while(root!=NULL)
    {
        if(DATA(root)==DATA(x))
            return NULL;/*meaning there is already x in tree*/
        if(DATA(root)<DATA(x))
        {
            if(RIGHT(root)==NULL)
                return root;
            else
                root=RIGHT(root);
        }
        else
        {
            if(LEFT(root)==NULL)
                return root;
            else
                root=LEFT(root);
        }
    }
    return NULL; /*something went wrong*/
}
int nodeBalance(np x)
{
    if(heightOfCalculatedNode(LEFT(x))>heightOfCalculatedNode(RIGHT(x)))
        return -1;
    if(heightOfCalculatedNode(LEFT(x))<heightOfCalculatedNode(RIGHT(x)))
        return 1;
    return 0;
}

int addNode(long long int n)
{
    np new_node;
    np news_parent;
    new_node=createNewNode(n);
    news_parent=searchNodePlace(new_node);
    if(news_parent==NULL)
    {
        return 0;/*meaning there is already a node exist which has the same value*/
    }
    
    if(news_parent==tree)/*it will be the first node in the tree*/
    {
        LEFT(news_parent)=new_node;
        PARENT(new_node)=news_parent;
        DATA(tree)++;
        return 1;
    }
    
    if(DATA(news_parent)<DATA(new_node))
    {
        RIGHT(news_parent)=new_node;
        PARENT(new_node)=news_parent;
    }
    else
    {
        LEFT(news_parent)=new_node;
        PARENT(new_node)=news_parent;
    }
    
    fixAVL(new_node);
    DATA(tree)++;
    return 1;
}

void addYtoParentOfX(np x, np y)
{
    PARENT(y)=PARENT(x);
    if(LEFT(PARENT(x))==x)
        LEFT(PARENT(x))=y;
    else
        RIGHT(PARENT(x))=y;
}


void fixAVL(np x)
{
    int left_height, right_height;
    np temp;
    np y, z, a, b, c, d;
    if(x==tree)
        return;
    
    left_height=heightOfCalculatedNode(LEFT(x));
    right_height=heightOfCalculatedNode(RIGHT(x));
    
    if(abs(left_height-right_height)<=1)
    {
        HEIGHT(x)=heightOfNode(x);
        fixAVL(PARENT(x));
        return;
    }

    
    if(right_height>left_height)
    {
        if(nodeBalance(RIGHT(x))>=0)
        {
            temp=RIGHT(x);
            addYtoParentOfX(x, RIGHT(x));
            RIGHT(x)=LEFT(RIGHT(x));
            PARENT(LEFT(temp))=x;
            PARENT(x)=temp;
            LEFT(temp)=x;
            HEIGHT(x)=heightOfNode(x);
            HEIGHT(temp)=heightOfNode(temp);
            fixAVL(PARENT(temp));
            return;
        }
        else
        {
            a=LEFT(x);
            z=RIGHT(x);
            y=LEFT(z);
            d=RIGHT(z);
            b=LEFT(y);
            c=RIGHT(y);
            addYtoParentOfX(x, y);
            LEFT(y)=x;
            PARENT(x)=y;
            RIGHT(y)=z;
            PARENT(z)=y;
            
            LEFT(x)=a;
            PARENT(a)=x;
            RIGHT(x)=b;
            PARENT(b)=x;
            
            LEFT(z)=c;
            PARENT(c)=z;
            RIGHT(z)=d;
            PARENT(d)=z;
            
            HEIGHT(x)=heightOfNode(x);
            HEIGHT(z)=heightOfNode(z);
            HEIGHT(y)=heightOfNode(y);
            fixAVL(PARENT(y));
            return;
        }
    }
    else
    {
        if(nodeBalance(x)<=0)
        {
            y=LEFT(x);
            a=RIGHT(x);
            
            b=LEFT(y);
            c=RIGHT(y);
            
            addYtoParentOfX(x, y);
            
            LEFT(y)=b;
            PARENT(b)=y;
            
            RIGHT(y)=x;
            PARENT(x)=y;
            
            LEFT(x)=c;
            PARENT(c)=x;
            
            RIGHT(x)=a;
            PARENT(a)=x;
            
            HEIGHT(x)=heightOfNode(x);
            HEIGHT(y)=heightOfNode(y);
            fixAVL(PARENT(y));
            return;
        }
        else
        {
            z=LEFT(x);
            d=RIGHT(x);
            a=LEFT(z);
            y=RIGHT(z);
            b=LEFT(y);
            c=RIGHT(y);
            
            addYtoParentOfX(x, y);
            
            LEFT(y)=z;
            PARENT(z)=y;
            
            RIGHT(y)=x;
            PARENT(x)=y;
            
            LEFT(z)=a;
            PARENT(a)=z;
            
            RIGHT(z)=b;
            PARENT(b)=z;
            
            LEFT(x)=c;
            PARENT(c)=x;
            
            RIGHT(x)=d;
            PARENT(d)=x;
            
            HEIGHT(z)=heightOfNode(z);
            HEIGHT(x)=heightOfNode(x);
            HEIGHT(y)=heightOfNode(y);
            
            fixAVL(PARENT(y));
            return;
        }
    }
}


np createNewNode(long long int n)
{
    np ret=malloc(sizeof(node));
    DATA(ret)=n;
    HEIGHT(ret)=0;
    PARENT(ret)=NULL;
    LEFT(ret)=NULL;
    RIGHT(ret)=NULL;
    return ret;
}


