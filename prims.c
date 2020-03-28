#include<stdio.h>
int main()
{
int a[10][10];
int u,v;
int n;
printf("Enter the number of vertices:");
scanf("%d",&n);
int visited[n];
printf("Enter the matrix:\n");
for(int i=0;i<n;i++)
{
	visited[i]=0;
	for(int j=0;j<n;j++)
	{
		scanf("%d",&a[i][j]);
		if(a[i][j]==0)
			a[i][j]=999;
	}
}
for(int i=0;i<n;i++)
{
for(int j=0;j<n;j++)
{
printf("%d ",a[i][j]);
}
printf("\n");
}
int min;
visited[0]=1;
int total=0;
for(int count=0;count<n-1;count++)
{
	min=999;
	for(int i=0;i<n;i++)
	{
		if(visited[i]==1)
			{
				for(int j=0;j<n;j++)
					{
						if(visited[j]!=1)
							{
							if(min>a[i][j])
								{
									min=a[i][j];
									u=i;
									v=j;
								}
							}
					}
			}
	}
	visited[v]=1;
	printf("\nEdge selected is %d->%d",u,v);
	printf("\nThe minimum edge is %d",min);
	total+=min;
}
printf("\nThe total is %d",total);
return(0);
}
