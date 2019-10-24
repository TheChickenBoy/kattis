#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main(void){
    int n=0,s1=0,s2=0;
    cin>>n;
    vector<int> nr(n);
    for(int i=0;i<n;i++)
        cin>>nr[i];
    sort(nr.begin(),nr.end(), greater<int>());
    for(int i=0;i<n;i++){
        if(i%2==0)
            s1+=nr[i];
        else
            s2+=nr[i];
    }
    cout << s1 << " " << s2 << endl;
    return 0;
}
