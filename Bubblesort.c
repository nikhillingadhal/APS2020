#include<stdio.h>
int main()
{
int a[10];
int temp;
int n;
printf("\n Enter the number of elements:");
scanf("%d",&n);
printf("\n Enter the array:");
for(int i=0;i<n;i++)
{
scanf("%d",&a[i]);
}
for(int i=0;i<n;i++)
{
for(int j=i+1;j<n-i;j++)
{
if(a[i]>a[j])
{
temp=a[i];
a[i]=a[j];
a[j]=temp;
}
}
}
for(int i=0;i<n;i++)
{
printf("\n------\n");
printf("%d\n",a[i]);
}

return(0);
}

