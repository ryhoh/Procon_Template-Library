import unittest

import Library


class MathAlgorithmTest(unittest.TestCase):

    def test_gcd(self):
        test_sets = {
            (0, 10): 0,
            (10, 0): 0,
            (1, 1): 1,
            (1, 2): 1,
            (2, 1): 1,
            (12, 4): 4,
            (4, 12): 4,
            (9, 12): 3,
            (12, 9): 3,
        }
        for k, v in test_sets.items():
            try:
                self.assertEqual(Library.MathAlgorithm.gcd(*k), v)
            except AssertionError as e:
                print(k, v, ": ", e)

        test_sets = {
            (0, 0),
            (-1, 1),
            (1, -1),
            (-1, -1),
        }
        for s in test_sets:
            self.assertRaises(ValueError, Library.MathAlgorithm.gcd, *s)

        return self

    def test_lcm(self):
        test_sets = {
            (1, 1): 1,
            (1, 2): 2,
            (2, 1): 2,
            (12, 4): 12,
            (4, 12): 12,
            (9, 12): 36,
            (12, 9): 36,
        }
        for k, v in test_sets.items():
            try:
                self.assertEqual(Library.MathAlgorithm.lcm(*k), v)
            except AssertionError as e:
                print(k, v, ": ", e)

        test_sets = {
            (0, 10),
            (10, 0),
            (0, 0),
        }
        for s in test_sets:
            self.assertRaises(ValueError, Library.MathAlgorithm.lcm, *s)

        return self

    def test_factorial(self):
        test_sets = {
            0: [1],
            1: [1],
            2: [1, 2],
            3: [1, 2, 6],
            4: [1, 2, 6, 24],
            5: [1, 2, 6, 24, 120],
        }
        map(lambda k, v:
            self.assertEqual(Library.MathAlgorithm.factorial(k), v),
            test_sets)

        self.assertRaises(ValueError,
                          Library.MathAlgorithm.factorial, -1)

        return self


class EListTest(unittest.TestCase):
    def test_accumulation_sum(self):
        e_list = Library.EList(range(8))
        self.assertEqual(e_list, list(range(8)))

        e_list.accumulation_sum()
        self.assertEqual(e_list, [0, 1, 3, 6, 10, 15, 21, 28])

        e_list = Library.EList(range(8))
        e_list.back_accumulation_sum()
        self.assertEqual(e_list, [28, 28, 27, 25, 22, 18, 13, 7])

        self.assertEqual(str(type(e_list.copy())), "<class 'Library.EList'>")

        return self


class DP2DOptimizerTest(unittest.TestCase):
    def test_01knapsack_solve(self):
        dp = Library.DP2DOptimizer(4, 5, [4, 5, 2, 8], [2, 2, 1, 3])
        res = dp.solve(dp.expr_01knapsack)[5][4]
        self.assertEqual(res, 13)

        dp = Library.DP2DOptimizer(2, 20, [5, 4], [9, 10])
        res = dp.solve(dp.expr_01knapsack)[20][2]
        self.assertEqual(res, 9)

        return self

    def test_knapsack_solve(self):
        dp = Library.DP2DOptimizer(4, 8, [4, 5, 2, 8], [2, 2, 1, 3])
        res = dp.solve(dp.expr_knapsack)[8][4]
        self.assertEqual(res, 21)

        dp = Library.DP2DOptimizer(2, 20, [5, 4], [9, 10])
        res = dp.solve(dp.expr_knapsack)[20][2]
        self.assertEqual(res, 10)

        return self

    def test_coin_solve(self):
        def builder(n: int):
            return Library.DP2DOptimizer(
                values_len, n, [1 for _ in range(values_len)], values, initializer=int(10e5)).fill_0_idx_with(0)

        values = sorted(list(set([6 ** i for i in range(7)] + [9 ** i for i in range(6)])))
        values_len = len(values)
        dp = builder(127)
        self.assertEqual(dp.solve(dp.expr_coin)[127][values_len], 4)

        dp = builder(3)
        self.assertEqual(dp.solve(dp.expr_coin)[3][values_len], 3)

        dp = builder(44852)
        self.assertEqual(dp.solve(dp.expr_coin)[44852][values_len], 16)

        return self


if __name__ == '__main__':
    MathAlgorithmTest()\
        .test_gcd()\
        .test_lcm()\
        .test_factorial()
    EListTest().test_accumulation_sum()
    DP2DOptimizerTest()\
        .test_01knapsack_solve()\
        .test_knapsack_solve()\
        .test_coin_solve()
