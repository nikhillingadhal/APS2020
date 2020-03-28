#include<stdio.h>
int visited[20];
int s[20];
int top=-1;
void push(int n)
{
top++;
s[top]=n;
}
int pop()
{
int k;
k=s[top];
top--;
return(k);
}
void BFS(int a[20][20],int m,int source)
{
push(source);
int k;
while(top!=-1)
{
k=pop();
visited[k]=1;
//printf("\nvisited[%d]=%d\n",k,visited[k]);
for(int i=0;i<m;i++)
{
if(a[k][i]!=0 && visited[i]==0)
{
printf("%d\t",i);
visited[i]=1;
push(i);
}
}
}
}
int main()
{
int a[20][20];
int m,n,source;
printf("Enter the rows and columns:");
scanf("%d %d",&m,&n);
for(int i=0;i<m;i++)
visited[i]=0;
for(int i=0;i<m;i++)
{
for(int j=0;j<n;j++)
scanf("%d",&a[i][j]);
}
for(int i=0;i<m;i++)
{
for(int j=0;j<n;j++)
printf("%d\t",a[i][j]);
printf("\n");
}
printf("\nEnter the source:");
scanf("%d",&source);
BFS(a,m,source);
return(0);
}
