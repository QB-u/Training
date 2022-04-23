#include <bits/stdc++.h>
#include <pwd.h>
#include <grp.h>
#include <string>
#include <unistd.h>
using namespace std;

int main(){
    char user[100]={0};
    struct passwd *entry;
    cin >> user;
    entry = getpwnam(user);
    int changeid = (int) entry->pw_uid;
    setuid(changeid);
    cout << "User id: " << changeid << endl;
    system("myid");
}