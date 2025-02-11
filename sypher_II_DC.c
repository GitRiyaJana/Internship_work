#include<stdio.h>
int main()
{
	int p1,p2,c1,c2,ip,i,j,s1[]={6,4,12,5,0,7,2,14,1,15,3,13,8,10,9,11};
	int s2[]={4,8,6,10,1,3,0,5,12,14,13,15,2,11,7,9};
	int x[15],max,m,y[15]={0};
	printf("Enter two plaintext pair:\n");
	scanf("%d%d",&p1,&p2);
	printf("Enter two ciphertext pair:\n");
	scanf("%d%d",&c1,&c2);
	ip=p1^p2;
	for(i=0;i<16;i++)
	{
		x[i]=s1[i]^s1[i^ip];
		printf("%d ",x[i]);
		j=x[i];
		y[j]++;
	}	
	
	max=y[0];
	for(i=1;i<16;i++)
	{
		if(y[i]>max)
		{
			max=y[i];
			j=i;
		}	
	}
	
	printf("\n%d",j);

	
	for(i=0;i<16;i++)
	{
		m=s2[c1^i]^s2[c2^i];
		if(m==j)
		{
			printf("Key might be:%d\n",i);
		}
	}	

}	
