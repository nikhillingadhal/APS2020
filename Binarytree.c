#include<stdio.h>
#include<stdlib.h>
typedef struct node
{
	int a;
	struct node *left,*right;
}NODE;
int cnt=0;
NODE * getnode(NODE *p,int k)
{
if(p==NULL)
{
p=malloc(sizeof(NODE));
p->left=NULL;
p->right=NULL;
p->a=k;
return(p);
}
else
{
	if(k<=p->a)
	{
		p->left=getnode(p->left,k);
	}
	else if(k>p->a)
	{
		p->right=getnode(p->right,k);
	}
}
return(p);
}
NODE * findmin(NODE *p)
{
NODE *temp;
temp=p;
while(temp->left!=NULL)
{
temp=temp->left;
}
return(temp);
}
NODE * delete(NODE *p,int k)
{
if(p==NULL)
	return(p);
else if(k<p->a)
	p->left=delete(p->left,k);
else if(k>p->a)
	p->right=delete(p->right,k);
else
{
	if(p->right==NULL && p->left==NULL)
	{
		free(p);
		p=NULL;
		return(p);
	}
	else if(p->right!=NULL && p->left==NULL)
	{
		NODE *temp;
		temp=p->right;
		p=p->right;
		//temp->right=NULL;
	
		free(temp);
		return(p);
	}
	else if(p->left!=NULL && p->right==NULL)
	{
		NODE *temp;
		temp=p->left;
		p=p->left;
	//	p->a=temp->a;
	//	p->left=NULL;
		free(temp);
		return(p);
	}
	else
	{
		NODE *temp;
		temp=findmin(p->right);
		p->a=temp->a;
		p->left=delete(p->left,temp->a);
		return(p);
	}
}
}
int w=0;
int maxheight(int a,int b)
{
	if(a>b)
	return(a);
	else
	return(b);
}
int height(NODE *root )
{
if(root==NULL)
return(0);
if( root->right==NULL && root->left==NULL)
return(1);
return(1+maxheight(height(root->left),height(root->right)));
}
int k=0;
void search(NODE *p,int k)
{
	if(p==NULL)
	printf("\n not found");
	if(p!=NULL)
{
	if(p->a<k)
	search(p->right,k);
	else if(p->a>k)
	search(p->left,k);
	else if(p->a==k)
	{	
	printf("\n The key is found");
	}
	cnt++;
}
}
int level(NODE *p,int k)
{
	search(p,k);
	return(cnt);
}
void disp(NODE *p)
{
if(p!=NULL)
{
disp(p->left);
//if(p->left!=NULL || p->right!=NULL)
printf("\n%d",p->a);
disp(p->right);
}
}
int min(NODE *p)
{
NODE *temp;
temp=p;
while(temp!=NULL)
{
	temp=temp->left;
}
return(temp->a);
}
int main()
{
NODE *root;
root=NULL;
int ch;
printf("\n MENU\n----\n1.Add\n2.disp\n3.Search\n4.delete");
//printf("\n Enter the choice:");
//scanf("%d",&ch);
int rr;
int item,key;
do
{
printf("\n Enter the choice:");
scanf("%d",&ch);
switch(ch)
{

case 1:
	printf("\n Enter the data for the node");
	scanf("%d",&item);
	root=getnode(root,item);
	break;
case 2:
	disp(root);
	break;
case 3:
	printf("\n Enter the key:");
	scanf("%d",&key);
	search(root,key);
	break;
case 4:
	printf("\n Enter the key:");
	scanf("%d",&key);
	delete(root,key);
	break;
case 5:
	rr=height(root);
	printf("\nHeight=%d",rr);
	break;
case 6:
	printf("\n Enter the key:");
	scanf("%d",&key);	
	rr=level(root,key);
	printf("\n Level=%d",rr);
	break;
}
}while(ch<6);
return(0);
}
