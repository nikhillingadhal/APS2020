#include<stdio.h>
void merge(int *a,int first,int mid,int last)
{

	int i=first;
	int j=mid+1;
	int k=first;
	int temp[20];
	while(j<=last&&i<=mid)
	{
		if(a[i]<=a[j])
			temp[k++]=a[i++];
		else if(a[j]<=a[i])
			temp[k++]=a[j++];
	}
	while(i<=mid)
		temp[k++]=a[i++];
	while(j<=last)
		temp[k++]=a[j++];
	for(int w=first;w<=last;w++)
		a[w]=temp[w];
}
void mergesort(int *a,int first,int last)
{
	int mid;
	if(first<last)
		{
			mid=(last+first)/2;
			mergesort(a,first,mid);
			mergesort(a,mid+1,last);
			merge(a,first,mid,last);
		}
}
int main()
{
int n;
int a[20];
printf("Enter the number of elements in array:");
scanf("%d",&n);
printf("Enter the elements in array:");
for(int i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
mergesort(a,0,n-1);
for(int i=0;i<n;i++)
	{
		printf("%d\n",a[i]);
	}
return(0);
}
