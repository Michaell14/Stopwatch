#include <iostream>
#include <string>
#include <vector>
#include <ostream>
#include <cmath>
using namespace std;

int main(){
	int cas;
	cin>>cas;

	for (int i=1; i<cas; i+=2){
		string s;
		getline(cin, s);
		string n="";
		n+=s[0];

		for (int x=0; x<s.length();x++){
			n+=s[x];
		}
		cout <<n<<endl;
	}
}