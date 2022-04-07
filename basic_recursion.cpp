#include<bits/stdc++.h>
using namespace std;
void sai(int x)
{
	if(x==0)
		return;
	cout<<x;
	sai(x-1);
}
int main()
{
	int n;
	cin>>n;
	sai(n);
	return 0;
}
