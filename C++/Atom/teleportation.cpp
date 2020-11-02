/*
ID: your_id_here
PROG: test
LANG: C++
*/
#include <bits/stdc++.h>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

int main() {
  //ifstream fin ("test.in");
  //ofstream fout ("test.out");
  //int a, b;
  //fin >> a >> b;
  //fout << a+b << endl;
  //return 0;
  int a,b;
  int x,y;
  cin>>a>>b>>x>>y;
  cout <<abs(max(a,b)-max(x,y))+abs(min(a,b)-min(x,y));
  return 1;
}
