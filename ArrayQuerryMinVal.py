#include <stdio.h> 
#include <math.h> 
#include <limits.h> 
long long minVal(long long x, long long y) { return (x < y)? x: y; } 
long long getMid(long long s, long long e) { return s + (e -s)/2; } 
long long RMQUtil(long long *st, long long ss, long long se, long long qs, long long qe, long long index) 
{ 
    if (qs <= ss && qe >= se) 
        return st[index]; 
    if (se < qs || ss > qe) 
        return INT_MAX; 
    long long mid = getMid(ss, se); 
    return minVal(RMQUtil(st, ss, mid, qs, qe, 2*index+1), 
                RMQUtil(st, mid+1, se, qs, qe, 2*index+2)); 
} 
long long RMQ(long long *st, long long n, long long qs, long long qe) 
{ 
    if (qs < 0 || qe > n-1 || qs > qe) 
    { 
        printf("Invalid Input"); 
        return -1; 
    } 

    return RMQUtil(st, 0, n-1, qs, qe, 0); 
} 
long long constructSTUtil(long long arr[], long long ss, long long se, long long *st, long long si) 
{ 
    if (ss == se) 
    { 
        st[si] = arr[ss]; 
        return arr[ss]; 
    } 
    long long mid = getMid(ss, se); 
    st[si] = minVal(constructSTUtil(arr, ss, mid, st, si*2+1), 
                    constructSTUtil(arr, mid+1, se, st, si*2+2)); 
    return st[si]; 
} 

long long *constructST(long long arr[], long long n) 
{ 
    long long x = (long long)(ceil(log2(n))); 
    long long max_size = 2*(long long)pow(2, x) - 1; 
    long long *st=(long long*)malloc(max_size * sizeof(long long));
    constructSTUtil(arr, 0, n-1, st, 0); 
    return st; 
} 
int main() 
{ 
long long n;
long long m;
scanf("%lld",&n);
scanf("%lld",&m);
long long a[n];
for(long long i=0;i<n;i++)
{
    scanf("%lld",&a[i]);
}
long long *st = constructST(a, n); 
for(long long i=0;i<m;i++)
{
    long long l;
    long long r;
    scanf("%lld",&l);
    scanf("%lld",&r);
    // Prlong long minimum value in arr[qs..qe] 
    printf("%lld\n",RMQ(st, n, l, r));
} 
    return 0; 
} 
