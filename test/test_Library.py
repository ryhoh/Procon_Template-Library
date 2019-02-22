import unittest
import sys
sys.path.append('../src/Python')

import Library


class MathAlgorithmTest(unittest.TestCase):

    def setUp(self):
        self.primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
                       53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107,
                       109, 113, 127, 131, 137, 139, 149, 151, 157]

    def tearDown(self):
        pass

    def test_gcd(self):
        test_inputs = [
            (0, 10),
            (10, 0),
            (1, 1),
            (1, 2),
            (2, 1),
            (12, 4),
            (4, 12),
            (9, 12),
            (12, 9),
        ]
        test_outputs = [0, 0, 1, 1, 1, 4, 4, 3, 3]
        for test_i, test_o in zip(test_inputs, test_outputs):
            self.assertEqual(test_o, Library.MathAlgorithm.gcd(*test_i))

        test_error_sets = {
            (0, 0),
            (-1, 1),
            (1, -1),
            (-1, -1),
        }
        for test_i in test_error_sets:
            self.assertRaises(ValueError, Library.MathAlgorithm.gcd, *test_i)

    def test_lcm(self):
        test_inputs = [
            (1, 1),
            (1, 2),
            (2, 1),
            (12, 4),
            (4, 12),
            (9, 12),
            (12, 9),
        ]
        test_outputs = [1, 2, 2, 12, 12, 36, 36]
        for test_i, test_o in zip(test_inputs, test_outputs):
            self.assertEqual(test_o, Library.MathAlgorithm.lcm(*test_i))

        test_error_inputs = {
            (0, 10),
            (10, 0),
            (0, 0),
        }
        for test_i in test_error_inputs:
            self.assertRaises(ValueError, Library.MathAlgorithm.lcm, *test_i)

    def test_factorial_array(self):
        test_inputs = [0, 1, 2, 3, 4, 5]
        test_outputs = [
            [1],
            [1, 1],
            [1, 1, 2],
            [1, 1, 2, 6],
            [1, 1, 2, 6, 24],
            [1, 1, 2, 6, 24, 120],
        ]
        for test_i, test_o in zip(test_inputs, test_outputs):
            self.assertEqual(test_o, Library.MathAlgorithm.factorial_array(test_i))

        self.assertRaises(ValueError, Library.MathAlgorithm.factorial_array, -1)

    def test_factorial(self):
        test_inputs = [0, 1, 2, 3, 4, 5]
        test_outputs = [1, 1, 2, 6, 24, 120]
        for test_i, test_o in zip(test_inputs, test_outputs):
            self.assertEqual(test_o, Library.MathAlgorithm.factorial(test_i))

        self.assertRaises(ValueError, Library.MathAlgorithm.factorial, -1)

    def test_make_primes(self):
        test_inputs = [0, 1, 2, 3, 4, 5, 14]
        test_outputs = [
            [],
            [],
            [2],
            [2, 3],
            [2, 3],
            [2, 3, 5],
            [2, 3, 5, 7, 11, 13],
        ]
        for test_i, test_o in zip(test_inputs, test_outputs):
            self.assertEqual(test_o, Library.MathAlgorithm.make_primes(test_i))

        self.assertRaises(ValueError, Library.MathAlgorithm.make_primes, -1)

    def test_prime_factor(self):
        test_inputs = [1, 2, 3, 4, 12, 156]
        test_outputs = [
            {1: 1},
            {1: 1, 2: 1},
            {1: 1, 3: 1},
            {1: 1, 2: 2},
            {1: 1, 2: 2, 3: 1},
            {1: 1, 2: 2, 3: 1, 13: 1},
        ]
        for test_i, test_o in zip(test_inputs, test_outputs):
            self.assertEqual(test_o, Library.MathAlgorithm.prime_factor(test_i, self.primes))

        test_error_inputs = [-1, 0]
        for test_i in test_error_inputs:
            self.assertRaises(ValueError, Library.MathAlgorithm.prime_factor, test_i, self.primes)

    def test_pow_mod_positive(self):
        test_inputs = [
            (3, 0),
            (0, 3),
            (1, 1),
            (2, 2),
            (5, 31),
            (5, 30),
        ]
        test_outputs = [1, 0, 1, 4, 3162663, 2632534]
        for test_i, test_o in zip(test_inputs, test_outputs):
            self.assertEqual(test_o, Library.MathAlgorithm.pow_mod_positive(*test_i))

        test_error_inputs = [(3, -3), (-2, 3)]
        for test_i in test_error_inputs:
            self.assertRaises(ValueError, Library.MathAlgorithm.pow_mod_positive, *test_i)


class DisjointSetTest(unittest.TestCase):
    def setUp(self):
        self.dj_set = Library.DisjointSet(7)
        self.dj_set.parent[1] = 0
        self.dj_set.parent[2] = 1
        self.dj_set.parent[3] = 2
        self.dj_set.parent[4] = 0

    def tearDown(self):
        pass

    def test_find_parent(self):
        test_inputs = [0, 1]
        test_outputs = [0, 0]
        for test_i, test_o in zip(test_inputs, test_outputs):
            self.assertEqual(test_o, self.dj_set.find_parent(test_i))

        test_error_inputs = [-1]
        for test_i in test_error_inputs:
            self.assertRaises(ValueError, self.dj_set.find_parent, test_i)

    def test_unite(self):
        self.dj_set.unite(5, 6)
        self.assertEqual(self.dj_set.parent[5], self.dj_set.parent[6])

        test_error_inputs = [(-1, -2), (0, -3), (-5, 1)]
        for test_i in test_error_inputs:
            self.assertRaises(ValueError, self.dj_set.unite, *test_i)

    def test_have_same_parents(self):
        test_inputs_true = [(0, 1), (1, 2), (4, 2), (3, 4)]
        test_inputs_false = [(0, 5), (5, 6)]
        for test_i in test_inputs_true:
            self.assertTrue(self.dj_set.have_same_parents(*test_i))
        for test_i in test_inputs_false:
            self.assertFalse(self.dj_set.have_same_parents(*test_i))

        test_error_inputs = [(-1, -2), (0, -3), (-5, 1)]
        for test_i in test_error_inputs:
            self.assertRaises(ValueError, self.dj_set.unite, *test_i)


class GraphTest(unittest.TestCase):
    def setUp(self):
        self.graph = Library.Graph(3)

    def tearDown(self):
        pass

    def test_set_edge(self):
        self.graph\
            .set_edge(0, 1, 10, False)\
            .set_edge(1, 2, 20, True)
        self.assertEqual(Library.Graph.Edge(1, 10), self.graph.edges[0][1])  # 0 -> 1: cost 10
        self.assertNotIn(Library.Graph.Edge(0, 10), self.graph.edges[1])  # 1 -> 0: unavailable
        self.assertEqual(Library.Graph.Edge(2, 20), self.graph.edges[1][2])
        self.assertEqual(Library.Graph.Edge(1, 20), self.graph.edges[2][1])


class DijkstraTest(unittest.TestCase):
    def setUp(self):
        self.graph = Library.Dijkstra(5, 0)
        for connection in [
            (0, 1, 2, False),
            (0, 2, 3, False),
            (0, 3, 1, False),
            (1, 0, 2, False),
            (1, 3, 4, False),
            (2, 0, 3, False),
            (2, 3, 1, False),
            (2, 4, 1, False),
            (3, 0, 1, False),
            (3, 1, 4, False),
            (3, 2, 1, False),
            (3, 4, 3, False),
            (4, 2, 1, False),
            (4, 3, 3, False),
        ]:
            self.graph.set_edge(*connection)

    def tearDown(self):
        pass

    def test_solve(self):
        self.assertEqual([0, 2, 2, 1, 3], self.graph.solve())


class BellmanFordTest(unittest.TestCase):
    def setUp(self):
        self.graph = Library.BellmanFord(5, 0)
        for connection in [
            (0, 1, 2, False),
            (0, 2, 3, False),
            (0, 3, 1, False),
            (1, 0, 2, False),
            (1, 3, 4, False),
            (2, 0, 3, False),
            (2, 3, 1, False),
            (2, 4, 1, False),
            (3, 0, 1, False),
            (3, 1, 4, False),
            (3, 2, 1, False),
            (3, 4, 3, False),
            (4, 2, 1, False),
            (4, 3, 3, False),
        ]:
            self.graph.set_edge(*connection)

    def tearDown(self):
        pass

    def test_solve(self):
        self.assertEqual([0, 2, 2, 1, 3], self.graph.solve())


# class WarshallFloydTest(unittest.TestCase):
#     def setUp(self):
#         self.graph = Library.WarshallFloyd(5)
#         for connection in [
#             (0, 1, 2, False),
#             (0, 2, 3, False),
#             (0, 3, 1, False),
#             (1, 0, 2, False),
#             (1, 3, 4, False),
#             (2, 0, 3, False),
#             (2, 3, 1, False),
#             (2, 4, 1, False),
#             (3, 0, 1, False),
#             (3, 1, 4, False),
#             (3, 2, 1, False),
#             (3, 4, 3, False),
#             (4, 2, 1, False),
#             (4, 3, 3, False),
#         ]:
#             self.graph.set_edge(*connection)
#         self.graph.solve()
#
#     def tearDown(self):
#         pass
#
#     def test_solve(self):
#         test_inputs = [0, 1, 2, 3, 4]
#         test_outputs = [0, 2, 2, 1, 3]
#         for test_i, test_o in zip(test_inputs, test_outputs):
#             self.assertEqual(test_o, self.graph.edges[0][test_i].cost)


class EListTest1(unittest.TestCase):
    def setUp(self):
        self.e_list = Library.EList(range(8))
        self.e_list_single = Library.EList([1])
        self.e_list_none = Library.EList([])

    def tearDown(self):
        pass

    def test_class(self):
        self.assertEqual(str(type(self.e_list)), "<class 'Library.EList'>")

    def test_accumulation_sum(self):
        self.assertEqual([0, 1, 3, 6, 10, 15, 21, 28], self.e_list.accumulation_sum())
        self.assertEqual([1], self.e_list_single.accumulation_sum())
        self.assertEqual([], self.e_list_none.accumulation_sum())

    def test_back_accumulation_sum(self):
        self.assertEqual([28, 28, 27, 25, 22, 18, 13, 7], self.e_list.back_accumulation_sum())
        self.assertEqual([1], self.e_list_single.back_accumulation_sum())
        self.assertEqual([], self.e_list_none.back_accumulation_sum())


class DP2DOptimizerTest(unittest.TestCase):
    def test_01knapsack_solve(self):
        dp = Library.DP2DOptimizer(4, 5, [4, 5, 2, 8], [2, 2, 1, 3])
        res = dp.solve(dp.expr_01knapsack)[5][4]
        self.assertEqual(res, 13)

        dp = Library.DP2DOptimizer(2, 20, [5, 4], [9, 10])
        res = dp.solve(dp.expr_01knapsack)[20][2]
        self.assertEqual(res, 9)

    def test_knapsack_solve(self):
        dp = Library.DP2DOptimizer(4, 8, [4, 5, 2, 8], [2, 2, 1, 3])
        res = dp.solve(dp.expr_knapsack)[8][4]
        self.assertEqual(res, 21)

        dp = Library.DP2DOptimizer(2, 20, [5, 4], [9, 10])
        res = dp.solve(dp.expr_knapsack)[20][2]
        self.assertEqual(res, 10)

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


if __name__ == '__main__':
    unittest.main()
