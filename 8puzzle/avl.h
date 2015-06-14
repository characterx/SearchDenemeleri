#ifndef
#define AVL

np tree;

typedef
struct node
{
    long long int data;
    int height;
    struct node *parent;
    struct node *left_child;
    struct node *right_child;
}node, *np;

#endif