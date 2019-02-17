// 競プロで役立ちそうな関数s
// インクルードできないからコピペすること

// 動作確認用
#include "template.cc"

/* -- 関数s -- */
// 素数作成
set<int> Primes(int size) {
    set<int> primes;
    bool *opened = new bool[size];

    rep(i, size) {
        opened[i] = true;
    }

    long long limit = sqrt(size);
    REP(i, 2, limit) {
        if(opened[i]) {
            primes.insert(i);
            for(long long j=i; j<size; j+=i) {
                opened[j] = false;
            }
        }
    }
    REP(i, limit, size) {
        if(opened[i]) {
            primes.insert(i);
        }
    }

    delete[] opened;
    return primes;
}

// 素因数分解
map<int, int> PrimeFactors(long long N, set<int> primes) {
    map<int, int> m;
    m.insert(make_pair(1,1));
    while(true) {
        bool ok = false;
        for(long long i=0; i<primes.size(); i++) {
            if(N%primes[i] == 0) {
                if(m.find(primes[i]) != m.end()) m[primes[i]] += 1;
                else m.insert(make_pair(primes[i], 1));
                N /= primes[i];
                break;
            }
            if(primes[i] > N) {
                ok = true;
                break;
            }
        }
        if(ok) break;
    }
    return m;
}

// iが素数かどうかを表す2値配列を作る
//bool *binPrimesOf(bool *start, bool *end) {
//    long long size = end - start;
//
//    *(start) = *(start+1) = false;
//    bool *cur = start+2;
//    while(cur != end)
//        *cur = true;
//
//    int limit = sqrt(size);
//    REP(i, 2, limit) {
//        if(*(start+i)) {
//            for(int j=i; j<size; j+=i) {
//                *(start+j) = false;
//            }
//        }
//    }
//
//    return start;
//}

// 最大公約数（ユークリッドの互除法）
long long gcd(long long a, long long b) {
    if (b < 0 || (a == 0 && b == 0)) return -1;
    if (b > a) return gcd(b, a);

    if (b == 0) return 0;
    if (a % b == 0) return b;
    return gcd(b, a % b);
}

// 最小公倍数 ab = gcd(a,b)lcm(a,b) からの式変形で求める
long long lcm(long long a, long long b) {
    return a / gcd(a,b) * b;
}

// フェルマーの小定理, mod関連
// (aとpが互いに素で，pが素数の時，aで割ってmodを取るのは a^(p-2)を掛けてmodを取るのと同じ)
// 繰り返し2乗法
const long long MOD = 10000000 +7;
long long pow_mod(long long a, long long b) {
    if(b == 0) return 1;

    long long p = pow_mod(a, b/2);
    if(b%2 == 0) {
        return p * p % MOD;
    } else {
        return (p * p) % MOD * a % MOD;
    }
}

// Union Find
// uとrのデータ型，データ数nはご自由に
class UnionFind {
private:
    vector<int> pare, rk;

    void init(int n){
        rep(i, n){
            pare[i] = i;
            rk[i] = i;
        }
    }

public:
    UnionFind(int n) {
        pare = vector<int>(n);
        rk = vector<int>(n);
        init(n);
    }

    int find(int x){
        if (x == pare[x])
            return x;
        return pare[x] = find(pare[x]); // 経路圧縮
    }

    void unite(int x,int y){
        x = find(x);
        y = find(y);
        if(x == y) // すでに結合済
            return;

        // rkの低い方をrkの高い方に併合
        if(rk[x] < rk[y])
            pare[x] = y;
        else
            pare[y] = x;
        if(rk[x] == rk[y])
            rk[x]++;
    }

    bool same(int x,int y){
        return find(x) == find(y);
    }
};

// しゃくとり
void shakutori() {
    int right = 1;
    for(int left = 0; left < N; left++) {
        while (right < N && (right <= left || (rightを進める条件))) {
           // (rightを進めたり部分列の和積を変えたりする)
           right++;
        }

        // rightが伸びきった部分列でansに答えを追記

        if (right == left) {
            right++; // 追いついたらrightを進める
        } else {
            // (leftを進めることによる部分列の変更など)
        }
    }
}
//
//// yuproから
//void erast(int n){
//  memset(SO,1,sizeof(SO));
//  SO[1] = false;
//  SO[0] = false;
//  REP(i,2,sqrt(n)){
//    if(SO[i]){
//      REP(j,2,n){
//        if(i*j>=1000000) break;
//        SO[i*j] = false;
//      }
//    }
//  }
//}
//
//// DP
//int n,W;
//  cin >> n >> W;
//  vector<lint> dp(W,0);
//  int w[210];
//  int v[210];
//  rep(i,n) {
//    cin >> v[i] >> w[i];
//  }
//  rep(i,n){
//    rrep(k,W){
//      if(k-w[i]<0 || k > W) continue;
//      dp[k] = max<lint>(dp[k],dp[k-w[i]]+v[i]);
//    }
//  }
//  lint ma=0;
//  rep(k,200001) ma = max<lint>(ma,dp[k]);
//  cout << ma << endl;
//
//// 桁DP
//int dp[10001][2][101];
//int D;
//int rec(int k = 0,bool tight = true,int sum = 0){
//
//  if(k==n.size()) return sum%D == 0;
//  int x = n[k] - '0';
//  int r = (tight ? x : 9);
//  int &res = dp[k][tight][sum];
//  if(res!=-1) return res;
//  res = 0;
//  rep(i,r+1){
//    res += rec(k+1,tight && i == r, (sum + i)%D);
//    res %= mod;
//  }
//  return res;
//}

//// 順列全列挙
//// 重複あり
//void permutation_d(int n, int m) {
//    int t = pow(n,m)
//    rep(i,m){
//        a[i] = t%n
//        t/=m
//    }
//}
//// 重複なし
//void permutation(int n, int m) {
//    int t=n!/m!
//    rep(i,m){
//        a[i] = t%(m-i)
//        t/=(m-i)
//    }
//    rep(i,m){
//        rep(j,i){
//            if(!b[a[i]+j]){
//                b[a[i]+j]=true
//                a[i]+=j
//                break
//            }
//        }
//    }
//}

//// 組み合わせ数全列挙
//// vector< vector<long long> > C で nCr を C[n][r]に入れる
//vector< vector<long long> > makeC(long long limit) {
//    vector< vector<long long> > C;
//
//    // 0C0 = 1としておく
//    C.push_back(vector<long long>(1, 1));
//
//    for(long long i=1; i<limit; i++) {
//        vector<long long> c;
//        for(long long j=0; j<=i; j++) {
//            if(j == 0)
//                c.push_back(C[i-1][0]);
//            else if(j == i)
//                c.push_back(C[i-1][i-1]);
//            else
//                c.push_back(C[i-1][j-1] + C[i-1][j]);
//        }
//        C.push_back(c);
//    }
//
//    return C;
//}

// 階乗列挙
vector<long long> makeFactorial(long long limit) {
    vector<long long> F = vector<long long>(1, 1);

    for(long long i=1; i<limit; i++) {
        F.push_back(i * F[i-1]);
    }

    return F;
}

// 重複組合せ
long long H(int n, int k, vector<long long> factorials) {
    return factorials[n+k-1] / factorials[k] / factorials[n-1];
}


// ダイクストラ
class Node {
public:
    int dist, number;
    Node(int d, int n) {
        dist = d;
        number = n;
    }
};
bool operator < (const Node &l, const Node &r) {
    return l.dist < r.dist
    || r.dist >= l.dist && l.number < r.number;
};
bool operator > (const Node &l, const Node &r) {
    return r < l;
};

class Dijkstra {
private:
    class Edge {
    public:
        int to, cost;
        Edge(int t, int c) {
            to = t;
            cost = c;
        }
    };

    vector<vector<Edge>> edges;
    int start = 0;
    int node_n;

    void edge_initializer(int n) {
        edges = vector<vector<Edge>>(n);
    }

public:
    vector<int> d;
    vector<int> prev;

    Dijkstra(int n, int s) {
        start = s;
        node_n = n;
        edge_initializer(n);
    }

    void add_edge(int from, int to, int cost, bool rev=true) {
        edges[from].pb(Edge(to,cost));
        if(rev) edges[to].pb(Edge(from,cost));
    }

    vector<int> solve() {
        d = vector<int>(node_n, INT_MAX); d[start] = 0;
        prev = vector<int>(node_n);

        priority_queue<Node,vector<Node>,greater<Node>> Q;
        Q.push(Node(d[start],start));

        while(!Q.empty()) {
            Node u = Q.top(); Q.pop();
            if(u.dist > d[u.number]) continue;
            for(Edge &edge:edges[u.number]) {
                int alt = d[u.number] + edge.cost;
                int v = edge.to;
                if(d[v] > alt) {
                    d[v] = alt;
                    prev[v] = u.number;
                    Q.push(Node(d[v],v));
                }
            }
        }
        return d;
    }
};

// --

// ベルマンフォード
void BF(int start_p) {
    rep(i,node_n) d[i] = INT_MAX; d[start_p] = 0;
    bool renewed = true;
    while (renewed) {
        renewed = false;
        for(int i=0; i<node_n; i++) {
            if(d[i] == INT_MAX) continue;
            for(pair<int,int> c:cost[i]) {
                int alt = d[i] + c.second;
                int v = c.first;
                if(alt < d[v]) {
                    d[v] = alt;
                    renewed = true;
                }
            }
        }
    }
}
// --

// ワーシャルフロイド
const int NODE_N = 301;
int c[NODE_N][NODE_N];
void WF() {
    for(int i=0; i<NODE_N; i++) {
        for(int j=0; j<NODE_N; j++) {
            for(int k=0; k<NODE_N; k++) {
                if(c[j][i]!=INT_MAX && c[i][k]!=INT_MAX
                && c[j][k] > c[j][i]+c[i][k]) {
                    c[j][k] = c[j][i]+c[i][k];
                }
            }
        }
    }
}
// --

// ネットワークフロー（最大流）
// フォード・ファルカーソン
class Ford_Fulkerson {
private:
    static const int NODE_MAX = 300;

    class Edge {
    public:
        int to, cap, rev;
        Edge(int t, int c, int r) {
            to = t;
            cap = c;
            rev = r;
        }
    };

    bool used[NODE_MAX];
    vector<vector<Edge>> edges;

    void edge_initializer(int n) {
        edges = vector<vector<Edge>>(n);
    }

    int dfs(int v, int t, int f){
        if (v == t) return f;
        used[v] = true;
        for(int i=0; i < edges[v].size(); i++) {
            Edge &e = edges[v][i];
            if(!used[e.to] && e.cap > 0) {
                int d = dfs(e.to, t, min(f, e.cap));
                if (d > 0) {
                    e.cap -= d;
                    edges[e.to][e.rev].cap += d;
                    return d;
                }
            }
        }
        return 0;
    }

public:
    Ford_Fulkerson(int n) {
        edge_initializer(n);
    }

    void add_edge(int from, int to, int cap) {
        edges[from].push_back(Edge(to,cap,edges[to].size()));
        edges[to].push_back(Edge(from,0,edges[from].size()-1));
    }

    int max_flow(int s, int t){
        int flow = 0;
        while(true) {
            memset(used, 0, sizeof(used));
            int f = dfs(s,t,INT_MAX);
            if (f == 0) return flow;
            flow += f;
        }
    }
};

// スパニングツリー関連
// プリム法
class Node {
public:
    int number, mincost;
    Node(int n, int m) {
        number = n;
        mincost = m;
    }
};
bool operator < (const Node &l, const Node &r) {
    return l.mincost < r.mincost
    || (!(r.mincost < l.mincost) && l.number < r.number);
};
bool operator > (const Node &l, const Node &r) {
    return r < l;
};

class Prim {
private:
    class Edge {
    public:
        int to, cost;
        Edge(int t, int c) {
            to = t;
            cost = c;
        }
    };

    int node_n;
    vector<vector<int>> cost;
    vector<vector<Edge>> edges;

    void edge_initializer(int n) {
        edges = vector<vector<Edge>>(n);
    }

public:
    Prim(int n) {
        node_n = n;
        edge_initializer(node_n);
        edges = vector<vector<Edge>>(node_n);
    }

    void add_edge(int f, int t, int c) {
        edges[f].push_back(Edge(t,c));
    }

    int solve() {
        vector<int> mincost = vector<int>(node_n, INT_MAX); mincost[0] = 0;
        vector<bool> used = vector<bool>(node_n,false);

        priority_queue<Node,vector<Node>,greater<Node>> Q;
        for(int i=0; i<node_n; i++) {
            Q.push(Node(i,mincost[i]));
        }

        int res = 0;
        while(!Q.empty()) {
            Node node = Q.top(); Q.pop();
            if(used[node.number] || node.mincost > mincost[node.number])
                continue;
            used[node.number] = true;
            res += node.mincost;

            for(Edge &edge:edges[node.number]) {
                Q.push(Node(edge.to, edge.cost));
            }
        }
        return res;
    }
};

// クラスカル法
class Edge {
public:
    int from, to, cost;
    Edge(int f, int t, int c) {
        from = f;
        to = t;
        cost = c;
    }
};
bool operator < (const Edge &l, const Edge &r) {
    return l.cost < r.cost
    || (!(r.cost < l.cost) && l.to < r.to);
};
bool operator > (const Edge &l, const Edge &r) {
    return r < l;
};

class Kruskal {
private:
    vector<Edge> edges;
    int node_n;

public:
    Kruskal(int n) {
        node_n = n;
    }

    void add_edge(int f, int t, int c) {
        edges.pb(Edge(f,t,c));
    }

    int solve() {
        sort(edges.begin(),edges.end());
        UnionFind uf = UnionFind(node_n);

        int res = 0;
        for(Edge &edge:edges) {
            if(!uf.same(edge.from, edge.to)) {
                uf.unite(edge.from, edge.to);
                res += edge.cost;
            }
        }
        return res;
    }
};


// 平面探索用
const int dx[4] = {1, -1, 0, 0}, dy[4] = {0, 0, 1, -1};
const int dx8[8] = {-1, -1, -1, 0, 0, 1, 1, 1};
const int dy8[8] = {-1, 0, 1, -1, 1, -1, 0, 1};

// 動作確認用
int main() {
    cout << "hello" << endl;

    return 0;
}
