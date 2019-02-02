import math
import heapq


class MathAlgorithm(object):

    MOD = 10000000 + 7

    @classmethod
    def gcd(cls, a: int, b: int) -> int:
        if b < 0 or (a == 0 and b == 0):
            raise ValueError

        if b > a:
            return cls.gcd(b, a)

        if b == 0:
            return 0

        if a % b == 0:
            return b

        return cls.gcd(b, a % b)

    @classmethod
    def lcm(cls, a: int, b: int) -> int:
        if a <= 0 or b <= 0:
            raise ValueError

        return a // cls.gcd(a, b) * b

    # @classmethod
    # def make_comb(cls, limit):  # nCr テーブル
    #     C = [[1, 1]]
    #     for i in range(1, limit):
    #         c = []
    #         for j in range(j, i + 1):
    #             if j == 0:
    #                 c.append(C[i - 1][0])
    #             elif j == i:
    #                 c.append(C[i - 1][i - 1])
    #             else:
    #                 c.append(C[i - 1][j - 1] + C[i - 1][j])
    #         C.append(c)
    #         cls.C = C
    #     return cls.C

    @classmethod
    def factorial(cls, limit: int) -> list:
        if limit < 0:
            raise ValueError

        f = [1]
        for i in range(1, limit):
            f.append(i * f[i - 1])
        cls.F = f
        return cls.F

    @classmethod
    def primes(cls, size: int) -> list:
        res = []
        flag = [True for _ in range(size)]
        limit = int(math.sqrt(size))

        for i in range(2, limit):
            if flag[i]:
                res.append(i)
                for j in range(i, size, i):
                    flag[j] = False

        for i in range(limit, size):
            if flag[i]:
                res.append(i)

        cls.primes = res
        cls.prime_flag = flag
        return cls.primes

    @classmethod
    def prime_factor(cls, n: int, primes: list) -> dict:
        res = {1: 1}
        while True:
            ok = False
            for i in range(len(primes)):
                if n % primes[i] == 0:
                    if primes[i] in res:
                        res[primes[i]] += 1
                    else:
                        res[primes[i]] = 1
                    n = n // primes[i]
                    break
                if primes[i] > n:
                    ok = True
                    break
            if ok:
                break
        return res

    @classmethod
    def pow_mod(cls, a: int, n: int) -> int:
        if n == 0:
            return 1

        half = cls.pow_mod(a, n//2)
        if n % 2 == 0:
            return half * half % cls.MOD
        else:
            return half * half % cls.MOD * a % cls.MOD


class DisjointSet(object):
    def __init__(self, size: int):
        self.size = size
        self.pare = [i for i in range(size)]
        self.rk = [i for i in range(size)]

    def find(self, x: int) -> int:
        if x == self.pare[x]:
            return x
        self.pare[x] = self.find(self.pare[x])
        return self.pare[x]

    def unite(self, x: int, y: int) -> "DisjointSet":
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return self

        if self.rk[x] < self.rk[y]:
            self.pare[x] = y
        else:
            self.pare[y] = x

        if self.rk[x] == self.rk[y]:
            self.rk[x] += 1
        return self

    def same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)


class Graph(object):

    class Edge:
        def __init__(self, to: int, cost: int):
            self.to = to
            self.cost = cost

        def __str__(self):
            return "Edge: (to " + str(self.to) + ", cost " + str(self.cost) + ")"

        def __repr__(self):
            return self.__str__()

    INF = 10e10

    def __init__(self, node_n: int):
        self.node_n = node_n
        self.edges = [{} for _ in range(self.node_n)]
        self.dist = [self.INF for _ in range(self.node_n)]

    def set_edge(self, from_pos: int, to_pos: int, cost: int, reversible: bool) -> None:
        self.edges[from_pos][to_pos] = self.Edge(to_pos, cost)
        if reversible:
            self.edges[to_pos][from_pos] = self.Edge(from_pos, cost)

    def solve(self) -> object:
        raise NotImplementedError


class Dijkstra(Graph):

    class Node:
        def __init__(self, dist: int, number: int):
            self.dist = dist
            self.number = number

        def __lt__(self, other):
            return self.dist < other.dist \
                   or (self.dist == other.dist
                       and self.number < other.number)

        def __le__(self, other):
            return self.dist <= other.dist

        def __gt__(self, other):
            return other <= self

        def __ge__(self, other):
            return other < self

        def __str__(self):
            return "Node: (dist " + str(self.number) + ", number " \
                   + str(self.dist) + ")"

        def __repr__(self):
            return self.__str__()

    hq = []
    prev: list

    def __init__(self, node_n: int, start: int):
        super(Dijkstra, self).__init__(node_n)
        self.start = start
        self.dist[self.start] = 0
        self.prev = [None for _ in range(node_n)]

    def solve(self) -> list:
        heapq.heappush(self.hq, self.Node(0, self.start))

        while len(self.hq) != 0:
            node = heapq.heappop(self.hq)
            if node.dist > self.dist[node.number]:
                continue

            for edge in self.edges[node.number].values():
                alt = self.dist[node.number] + edge.cost
                if self.dist[edge.to] > alt:
                    self.dist[edge.to] = alt
                    self.prev[edge.to] = node.number
                    heapq.heappush(self.hq, self.Node(alt, edge.to))
        return self.dist


class BellmanFord(Graph):
    def __init__(self, node_n: int, start: int):
        super(BellmanFord, self).__init__(node_n)
        self.start = start
        self.dist[self.start] = 0

    def solve(self) -> list:
        renewed = True

        while renewed:
            renewed = False
            for from_pos in range(self.node_n):
                if self.dist[from_pos] == self.INF:
                    continue

                for edge in self.edges[from_pos]:
                    alt = self.dist[from_pos] + edge.cost
                    if alt < self.dist[edge.to]:
                        self.dist[edge.to] = alt
                        renewed = True
        return self.dist


class WarshallFloyd(Graph):
    def solve(self) -> "WarshallFloyd":
        for via_p in range(self.node_n):
            for from_p in range(self.node_n):
                for to_p in range(self.node_n):
                    if via_p in self.edges[from_p].keys() and to_p in self.edges[via_p].keys():
                        alt = self.edges[from_p][via_p].cost + self.edges[via_p][to_p].cost
                        if to_p not in self.edges[from_p]:
                            self.edges[from_p][to_p].cost = alt
                        else:
                            self.edges[from_p][to_p].cost = min(self.edges[from_p][to_p].cost, alt)
        return self


class EList(list):
    def accumulation_sum(self) -> None:
        if self.__len__() > 1:
            for i in range(self.__len__() - 1):
                self[i + 1] += self[i]

    def back_accumulation_sum(self) -> None:
        if self.__len__() > 1:
            for i in range(self.__len__() - 1, 0, -1):
                self[i - 1] += self[i]

    def copy(self) -> "EList":
        return EList(list.copy(self))


class DP2D(object):

    def __init__(self, item_n: int, border: int, initializer: int = 0):
        self.item_n = item_n
        self.border = border
        self.table = [[initializer for _ in range(self.item_n + 1)] for _ in range(self.border + 1)]

    def __str__(self):
        return "\n".join(list(map(lambda l:
                                  " ".join(list(map(str, l)))
                                  , self.table)))

    def __repr__(self):
        return "DynamicProgramming object:\n" + \
               "item_n: " + str(self.item_n) + ", border: " + str(self.border) + "\n" + \
               "table:\n" + self.__str__()

    def solve(self, expr: callable) -> list:
        raise NotImplementedError

    def fill_0_idx_with(self, value: int) -> "DP2D":
        self.table[0] = [value for _ in range(self.item_n + 1)]
        for i in range(1, self.border + 1):
            self.table[i][0] = value
        return self


class DP2DOptimizer(DP2D):

    def __init__(self, item_n: int, border: int, obj_coef: list, sbj_coef: list, initializer: int = 0):
        super(DP2DOptimizer, self).__init__(item_n, border, initializer=initializer)

        if len(obj_coef) == self.item_n:  # to 1-base
            obj_coef = [0] + obj_coef
        self.obj_coef = obj_coef

        if len(sbj_coef) == self.item_n:
            sbj_coef = [0] + sbj_coef
        self.sbj_coef = sbj_coef

    def solve(self, expr: callable) -> list:
        for weight_lim in range(1, self.border + 1):
            for item_idx in range(1, self.item_n + 1):
                self.table[weight_lim][item_idx] = expr(weight_lim, item_idx)

        return self.table

    def expr_01knapsack(self, weight_lim: int, item_idx: int) -> int:
        res = self.table[weight_lim][item_idx - 1]
        if weight_lim - self.sbj_coef[item_idx] >= 0:
            res = max(res, self.table[weight_lim - self.sbj_coef[item_idx]][item_idx - 1] + self.obj_coef[item_idx])
        return res

    def expr_knapsack(self, weight_lim: int, item_idx: int) -> int:
        res = self.table[weight_lim][item_idx - 1]
        if weight_lim - self.sbj_coef[item_idx] >= 0:
            res = max(res, self.table[weight_lim - self.sbj_coef[item_idx]][item_idx] + self.obj_coef[item_idx])
        return res

    def expr_coin(self, target, coin_idx) -> int:
        if self.sbj_coef[coin_idx] == 1:
            res = target
        else:
            res = self.table[target][coin_idx - 1]
            if target - self.sbj_coef[coin_idx] >= 0:
                res = min(res, self.table[target - self.sbj_coef[coin_idx]][coin_idx] + self.obj_coef[coin_idx])
        return res
