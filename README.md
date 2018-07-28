Merge sort

#include<stdio.h>
void merge(int a[],int ,int ,int ,int );
void mergesort(int a[] , int , int);
int main()
{
	int a[100],i,n;
	printf("Enter array size : \n");
	scanf("%d",&n);
	printf("Enter array elements : \n");
	for(i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}
	mergesort(a,0,n-1);
		for(i=0;i<n;i++)
	{
		printf("%d ",a[i]);
	}
	return 0;
}
void mergesort(int a[],int first,int last)
{
	int mid;
	if(first<last)
	{
		mid=(last+first)/2;
		mergesort(a,first,mid);
		mergesort(a,mid+1,last);
		merge(a,first,mid,mid+1,last);
	}
}
void merge(int a[],int first,int mid,int mid1,int last)
{
	int i,j,temp[100],k=0;
	i=first;
	j=mid1;
	while(i<=mid && j<=last)
	{
		if(a[i]<a[j])
		temp[k++]=a[i++];
		else 
		temp[k++]=a[j++];
	}
	while(i<=mid)
	temp[k++]=a[i++];
	while(j<=last)
	temp[k++]=a[j++];
	for(i=first,j=0;i<=last;i++,j++)
	a[i]=temp[j];
}
