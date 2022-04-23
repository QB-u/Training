#include <bits/stdc++.h>
#include <pwd.h>
#include <grp.h>
#include <unistd.h>
using namespace std;

int main() {
    char user[6]="userB";    
    struct passwd *entry;
    entry = getpwnam(user);
    int changeid = (int) entry->pw_uid;
    setuid(changeid);
    cout << "User name: " << entry->pw_name << endl;
    int a;
    cin >> a;
}