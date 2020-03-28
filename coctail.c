#include<stdio.h>
void swap(int *a,int *b)
{
int temp;
temp=*a;
*a=*b;
*b=temp;
}
int main()
{
int a[20];
int n;
printf("\nEnter the number of elements:");
scanf("%d",&n);
printf("\nEnter the elements:");
for(int i=0;i<n;i++)
scanf("%d",&a[i]);
for(int j=n-2;j>0;j--)
{
for(int i=n-j-2;i<j+1;i++)
{
if(a[i]>a[i+1])
swap(&a[i],&a[i+1]);
}
for(int i=j;i>n-j-2;i--)
{
if(a[i]<a[i-1])
swap(&a[i],&a[i-1]);
}
}
printf("\n-----------------------\n");
for(int i=0;i<n;i++)
printf("%d\n",a[i]);
printf("\n-----------------------\n");
return(0);
}
