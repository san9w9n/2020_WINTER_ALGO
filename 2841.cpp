#include <iostream>
#include <stack>
#include <array>
using namespace std;

stack<int> guitar[6];

int main() {
	int N, P, n, h;
	int cnt = 0;
	cin >> N >> P;
	
	for(int i=0; i<N; i++) {
		cin >> n >> h;
		while(!guitar[n-1].empty() && guitar[n-1].top() > h) {
			guitar[n-1].pop();
			cnt+=1;
        }
		if (!guitar[n-1].empty() && guitar[n-1].top() == h) continue;
		guitar[n-1].push(h);
		cnt+=1;
	}
	cout << cnt;
}