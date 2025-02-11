#include<stdio.h>
int main()
{
	int k1=3,k2=8,k3=13,p1,v1,x1,c1; 
	int s[]={6,4,12,5,0,7,2,14,1,15,3,13,8,10,9,11};
	printf("Enter paintext :\n");
	scanf("%d",&p1);
	v1=s[p1^k1];
	x1=s[v1^k2];
	c1=x1^k3;
	printf("Cipher text is:%d\n",c1);
	
}
