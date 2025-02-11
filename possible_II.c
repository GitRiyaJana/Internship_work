#include<stdio.h>
#include<math.h>
int main()
{
	int n,i,j,m=0,r,p,a[32][5]={0};
	printf("Enter number of bits:\n");
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		m=m+pow(2,i);
	}
	//int a[m][n]={0};
	
	printf("Total combination in decimal:0 to %d\n",m);
	printf("Combinations are:\n");
	for(i=1;i<=m;i++)
	{
			p=i,j=0;
			while(p!=0){
				a[i][n-1-j]=p-((p>>1)<<1);
				//printf("%d ",a[i][n-1-j]);
				p=p>>1;
				if(j<n-1)
					j++;
			}
	}	
	
	for(i=0;i<=m;i++)
	{
		for(j=0;j<n;j++)
		{
			printf("%d ",a[i][j]);
		}
		printf("\n");
	}
}
