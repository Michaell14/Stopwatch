#include <iostream>
#include <vector>
#include <string>
#include <cmath>
using namespace std;

int main()
{
    int match;
    cin>>match;
    for (int i=0; i<match; ++i){
        int length;
        cin>>length;
        vector<int>odds;
        vector<int>evens;
        string num;
        vector<char> lst(num.begin(), num.end());

        for (int x=1; x<=length; x++){

            if (x%2==1){
                odds.push_back(lst[x-1]);
            }else{
                ev
                ens.push_back(lst[x-1]);
            }

            if (odds.size()>=evens.size()){
                for (int f=0; f<odds.size(); f++){
                    if (odds[f]%2==1){
                        cout<<1;
                        continue;
                    }
                }
                cout<<2;
            }else{
                for (int f=0; f<evens.size(); f++){
                    if (evens[f]%2==0){
                        cout<<2;
                        continue;
                    }
                }
                cout<<1;
            }
        }
    }
}
