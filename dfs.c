#include<stdio.h>
int visited[20];
void DFS(int a[20][20],int m,int source)
{
	visited[source]=1;
for(int i=0;i<m;i++)
{
	if(a[source][i]!=0 && visited[i]==0)
		{
			printf("%d",i);
			DFS(a,m,i);
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
DFS(a,m,source);
return(0);
}
