"""
Python用ライブラリ
"""

import math


class MathAlgo(object):

    @classmethod
    def gcd(cls, a, b):
        if b == 0:
            return a
        else:
            return cls.gcd(b, a%b)

    @classmethod
    def lcm(cls, a, b):
        return a // cls.gcd(a, b) * b

    # def permutation_d(self, n, m): # mPn 重複あり
    #     t = n ** m
    #     a = [None for i in range(m)]
    #     for i in range(m):
    #         a[i] = t % (m-i)
    #         t = t // (m-i)
    #
    #
    # def permutation(self, n, m): # mPn
    #     t = n ** m
    #     a = [None for i in range(m)]
    #     b = [False for i in range(m)]
    #     for i in range(m):
    #         a[i] = t % (m-i)
    #         t = t // (m-i)
    #     for i in range(m):
    #         for j in range(i):
    #             if not b[a[i] +j]:
    #                 b[a[i] +j] = True
    #                 a[i] += j
    #                 break

    @classmethod
    def make_comb(cls, limit): # nCr テーブル
        C = [[1, 1]]
        for i in range(1, limit):
            c = []
            for j in range(j, i+1):
                if j == 0:
                    c.append(C[i-1][0])
                elif j == i:
                    c.append(C[i-1][i-1])
                else:
                    c.append(C[i-1][j-1] + C[i-1][j])
            C.append(c)
            cls.C = C
        return cls.C

    @classmethod
    def make_factorial(cls, limit):
        F = [1]
        for i in range(1, limit):
            F.append(i * F[i-1])
        cls.F = F
        return cls.F

    @classmethod
    def make_primes(cls, size):
        primes = []
        flag = [True for i in range(size)]
        limit = int(math.sqrt(size))

        for i in range(2, limit):
            if flag[i]:
                primes.append(i)
                for j in range(i, size, i):
                    flag[j] = False

        for i in range(limit, size):
            if flag[i]:
                primes.append(i)

        cls.primes = primes
        cls.prime_flag = flag
        return cls.primes

    @classmethod
    def prime_div(cls, N, primes):
        m = {1:1}
        while True:
            ok = False
            for i in range(len(primes)):
                if N%primes[i] == 0:
                    if primes[i] in m:
                        m[primes[i]] += 1
                    else:
                        m[primes[i]] = 1
                    N = N // primes[i]
                    break
                if primes[i] > N:
                    ok = True
                    break
            if ok:
                break
        cls.pd = m
        return cls.pd


class DisjointSet(object):
    def __init__(self, size):
        self.size = size
        self.pare = [None for i in range(size)]
        self.rk = [None for i in range(size)]
        for i in range(size):
            self.pare[i] = i
            self.rk[i] = i

    def find(self, x):
        if x == self.pare[x]:
            return x
        return self.pare[x] == self.find(self.pare[x])

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return None

        if self.rk[x] < self.rk[y]:
            self.pare[x] = y
        else:
            self.pare[y] = x

        if self.rk[x] == self.rk[y]:
            self.rk[x] += 1

    def same(self, x, y):
        return self.find(x) == self.find(y)
