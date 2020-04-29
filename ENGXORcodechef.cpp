#include <iostream>
#include <bitset>
using namespace std;
#define first(n) n,n+1,n+1,n+2
#define second(n) first(n),first(n+1),first(n+1),first(n+2)
#define third(n) second(n),second(n+1),second(n+1),second(n+2)
#define bits_val third(0),third(1),third(1),third(2)
unsigned int tab[256] = { bits_val };
int BitsSet(int n)
{
    int count=tab[n&0xff]+tab[(n>>8)&0xff]+tab[(n>>16)&0xff]+tab[(n>>24)&0xff];
    return count;
}
int main()
{
	ios_base::sync_with_stdio(false); 
    cin.tie(NULL);
	long long T;
    cin>>T;
    for(long long w=0;w<T;w++)
    {
    long long N,Q;
    long long P;
    cin>>N;
    cin>>Q;
    long long A[N];
    long long even=0;
    long long odd=0;
    for(long long i=0;i<N;i++)
    {
        cin>>A[i];
    }
    for(long long j=0;j<N;j++)
    {
    	long long val;
    		val=BitsSet(A[j]);
    		if (val%2==0 && val!=0)
    			even+=1;
    		else if(val%2==1)
    			odd+=1;
    }
    for(long long i=0;i<Q;i++)
    {
    	cin>>P;
    	long long evenCount=0;
    	long long oddCount=0;
    	long long val;
    	val=BitsSet(P);
    	if(val%2==0)
    	{
    		evenCount=even;
    		oddCount=odd;
    	}
    	else if(val%2==1)
    	{
    		oddCount=even;
    		evenCount=odd;
    	}
    	/*
    	for(long long i=0;i<N;i++)
    	{
        	if(P==A[i] && val%2==0)
        	{
        		evenCount-=1;
        	}
        	else if(P==A[i] && val%2==1)
        	{
        		oddCount-=1;
        	}
    	}
    	*/
    	cout<<evenCount<<" "<<oddCount<<"\n";
    }
	}
	return 0;
}
