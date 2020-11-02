#include <iostream>

using namespace std;

int main()
{
    int first=1;
    int second=2;
    int s=0;
    int nextTerm=second+first;
    while (second<4000000){
        if (second%2==0){
            s+=second;
        }
        first=second;
        second=nextTerm;
        nextTerm=first+second;
    }
    cout<<s;
}
