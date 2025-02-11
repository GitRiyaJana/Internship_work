#include<stdio.h>
int main()
{
	int k,p1,p2,c1,c2,ip_diff,u1,u2,v1,v2,i,match,a,b;
	int s[]={4,8,6,10,1,3,0,5,12,14,13,15,2,11,7,9};
	printf("Enter two plaintext pair:\n");
	scanf("%d %d",&p1,&p2);
	printf("Enter two ciphertext pair:\n");
	scanf("%d %d",&c1,&c2);
	
	ip_diff=p1^p2;
	for(i=0;i<16;i++)
	{
		v1=c1^i;
		v2=c2^i;
		u1=s[v1];
		u2=s[v2];
		match=u1^u2;
		if(ip_diff==match)
		{
			printf("K2 might be:%d\n",i);
			a=u1^p1;
			b=u2^p2;
			if(a==b)
				printf("k1 might be:%d\n",a);
		}
		printf("\n");
	}
	
		
}
