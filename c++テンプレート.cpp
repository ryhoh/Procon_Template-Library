* コンパイル
gpp-7の方がインクルード可能なヘッダの種類の点で都合が良い
g++ -std=c++14
g++-7 -std=c++14

#include <iostream>
#include <vector>
#include <array>
#include <algorithm>
#include <string>
#include <numeric>

#define rep(s, i, n) for(int i = s; i < n; i++)
#define rrep(s, i, n) for(int i = s; i != n; i--)
#define sum(start, end) accumulate(start, end, 0)
#define mmax(start, end) *max_element(start, end)
#define mmin(start, end) *min_element(start, end)

using namespace std;

int main() {
    return 0;
}

* yupro 4/21配布分 + 自己追加分
#include <iostream>
#include <vector>
#include <algorithm>
#include <array>
#include <string>
#include <numeric>
#include <climits>
#include <utility>

using namespace std;

#define rep(i, n) for(int i = 0; i < (int)(n); i++)
#define REP(i,k,n) for(int i=k;i<n;i++)
#define sum(start, end) accumulate(start, end, 0)
#define mmax(start, end) *max_element(start, end)
#define mmin(start, end) *min_element(start, end)
#define pb push_back
#define ALL(x) (x).begin(), (x).end()

typedef long long ll;
typedef string str;

using namespace std;
template <class T = ll> T in() { T _in; cin >> _in; return (_in); }


int main(){
    cin.tie(0);
    ios::sync_with_stdio(false);



    return 0;
}

* 2018101014版
#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) REP(i, 0, n)
#define REP(i, k, n) for(auto i = k; i != n; i++)
#define rrep(i, n) RREP(i, n, 0)
#define RREP(i, n, k) for(auto i = n; i != k; i--)
#define ALL(x) (x).begin(), (x).end()
#define debug(x) cerr << #x << " " << x << endl
#define in(x, data) (data).find(x) != (data).end()

typedef long long ll;

int main(){
    cin.tie(0);
    ios::sync_with_stdio(false);



    return 0;
}

* 20181017版
#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) REP(i, 0, n)
#define REP(i, k, n) for(auto i = k; i != n; i++)
#define rrep(i, n) RREP(i, n, 0)
#define RREP(i, n, k) for(auto i = n; i != k; i--)
#define all(x, r) (x), (x)+(r)
#define ALL(x) (x).begin(), (x).end()
#define debug(x) cerr << #x << " " << x << endl
#define exst(x, data) (data).find(x) != (data).end()
#define mp make_pair
#define mt make_tuple
#define pb push_back
#define eb emplace_back
#define np next_permutation
#define b32 bitset<32>

using ll = long long;
using Pii = pair<int,int>;
using Tiii = tuple<int, int, int>;
template<class T>using V = vector<T>;

int main(){
    cin.tie(0);
    ios::sync_with_stdio(false);

    return 0;
}

* 20181125版（現行）
#include <bits/stdc++.h>
using namespace std;

#define rep(i, n) REP(i, 0, n)
#define REP(i, k, n) for(auto i = k; i != n; i++)
#define rrep(i, n) RREP(i, n, 0)
#define RREP(i, n, k) for(auto i = n; i != k; i--)
#define all(x, r) (x), (x)+(r)
#define ALL(x) (x).begin(), (x).end()
#define debug(x) cerr << #x << " " << x << endl
#define in(c,x) find(c.begin(),c.end(),x) != c.end()
#define mp make_pair
#define mt make_tuple
#define pf push_front
#define pb push_back
#define ppf pop_front
#define ppb pop_back
#define eb emplace_back
#define np next_permutation
#define b32 bitset<32>
#define spc << " " <<
#define ANS cout << ans << endl

using ll = long long;
using Pii = pair<int,int>;
using Tiii = tuple<int, int, int>;
template<class T>using V = vector<T>;
template<class T>using VV = vector<vector<T>>;
using Vi = vector<int>;
using VVi = vector<vector<int>>;

int main(){
    cin.tie(0);
    ios::sync_with_stdio(false);

    ANS;
    return 0;
}
