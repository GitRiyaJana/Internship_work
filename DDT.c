#include<stdio.h>
int main()
{
	int a[16][16]={0},s[]={6,4,12,5,0,7,2,14,1,15,3,13,8,10,9,11},i,j,x;
	for(i=0;i<16;i++){
		for(j=0;j<16;j++)
		{
			x=s[i]^s[i^j];
			a[j][x]+=1;
		}	
	}
	
	
	for(i=0;i<16;i++){
                for(j=0;j<16;j++)
                {
                        printf("%d ",a[i][j]);
                }
		printf("\n");
        }


}
