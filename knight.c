#include<stdio.h>
#include<stdlib.h>
int main()
{
long long t;
long long i,j;
long long n;
scanf("%lld",&t);
for(long long y=0;y<t;y++)
{
scanf("%lld",&n);
long long a[n][n];
int rr=0;
for(long long k=0;k<n;k++)
{
for(long long w=0;w<n;w++)
{
a[k][w]=0;
}
}
for(long long w=0;w<n;w++)
{
scanf("%lld",&i);
scanf("%lld",&j);
a[i][j]=1;
}
scanf("%lld",&i);
scanf("%lld",&j);
a[i][j]=2;
for(long long k=0;k<n;k++)
{
for(long long w=0;w<n;w++)
{
if (a[k][w]==1)
{
if(a[k+1][w+2]==2 || a[k+2][w+1]==2 || a[k-1][w+2]==2 || a[k-2][w+1]==2 || a[k-2][w-1]==2 || a[k-1][w-2]==2 || a[k+2][w-1]==2 ||a[k+1][w-2]==2)
{
printf("YES\n");
rr=1;
break;
}
}
}
if(rr==1)
break;
}
if(rr!=1)
printf("NO\n");
}
return(0);
}
