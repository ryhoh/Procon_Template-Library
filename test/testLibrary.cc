#include <gtest/gtest.h>

#include "Library.cc"

TEST(test_gcd, zero) {
   ASSERT_EQ(0, gcd(0, 10));
   ASSERT_EQ(0, gcd(10, 0));
}

TEST(test_gcd, one) {
   ASSERT_EQ(1, gcd(1, 1));
   ASSERT_EQ(1, gcd(1, 2));
   ASSERT_EQ(1, gcd(2, 1));
}

TEST(test_gcd, simple) {
   ASSERT_EQ(4, gcd(12, 4));
   ASSERT_EQ(4, gcd(4, 12));
}

TEST(test_gcd, complex) {
   ASSERT_EQ(3, gcd(9, 12));
   ASSERT_EQ(3, gcd(12, 9));
}

TEST(test_gcd, big) {
   ASSERT_EQ(10, gcd(10000000000, 10));
}

TEST(test_gcd, except) {
   ASSERT_THROW(gcd(0, 0), invalid_argument);
   ASSERT_THROW(gcd(1, -1), invalid_argument);
   ASSERT_THROW(gcd(-1, 1), invalid_argument);
}

TEST(test_lcm, one) {
   ASSERT_EQ(1, lcm(1, 1));
   ASSERT_EQ(2, lcm(1, 2));
   ASSERT_EQ(2, lcm(2, 1));
}

TEST(test_lcm, simple) {
   ASSERT_EQ(12, lcm(12, 4));
   ASSERT_EQ(12, lcm(4, 12));
}

TEST(test_lcm, complex) {
   ASSERT_EQ(36, lcm(9, 12));
   ASSERT_EQ(36, lcm(12, 9));
}

TEST(test_lcm, except) {
   ASSERT_THROW(lcm(0, 0), invalid_argument);
   ASSERT_THROW(lcm(0, 1), invalid_argument);
   ASSERT_THROW(lcm(1, 0), invalid_argument);
   ASSERT_THROW(lcm(0, -1), invalid_argument);
   ASSERT_THROW(lcm(-1, 0), invalid_argument);
}

TEST(test_primes, normal) {
   vector<int> expected = vector<int>(7);
   expected[0] = 2;
   expected[1] = 3;
   expected[2] = 5;
   expected[3] = 7;
   expected[4] = 11;
   expected[5] = 13;
   expected[6] = 17;

   ASSERT_EQ(expected, primes(18));
}

TEST(test_primes, none) {
   vector<int> expected = vector<int>(0);

   ASSERT_EQ(expected, primes(0));
   ASSERT_EQ(expected, primes(1));
   ASSERT_EQ(expected, primes(2));
}

TEST(test_primes, border) {
   vector<int> expected = vector<int>(1, 2);
   ASSERT_EQ(expected, primes(3));

   expected.push_back(3);
   ASSERT_EQ(expected, primes(4));

   expected.push_back(5);
   ASSERT_EQ(expected, primes(6));

   expected.push_back(7);
   ASSERT_EQ(expected, primes(8));
}

TEST(test_primes, except) {
   ASSERT_THROW(primes(-1), invalid_argument);
}

TEST(test_primeFactors, simple) {
   map<int, int> expected;
   expected.insert(make_pair(2, 2));
   expected.insert(make_pair(3, 1));
   vector<int> p = primes(13);
   ASSERT_EQ(expected, primeFactors(12, p));
}

TEST(test_primeFactors, complex) {
   map<int, int> expected;
   expected.insert(make_pair(2, 11));
   expected.insert(make_pair(13, 2));
   expected.insert(make_pair(17, 3));
   vector<int> p = primes(100000);
   ASSERT_EQ(expected, primeFactors(1700448256, p));
}

TEST(test_primeFactors, one) {
   // 1の素因数分解は 1の1乗 と定義
   // それ以外のテストケースには 1の1乗 を含まないこと
   map<int, int> expected;
   expected.insert(make_pair(1, 1));
   vector<int> p = primes(13);
   ASSERT_EQ(expected, primeFactors(1, p));
}

TEST(test_primeFactors, except_invalid_primes) {
   // 不十分なprimes
   vector<int> p = primes(3);
   ASSERT_THROW(primeFactors(12, p), invalid_argument);
}

TEST(test_primeFactors, except_zero) {
   // 0の素因数分解
   vector<int> p = primes(13);
   ASSERT_THROW(primeFactors(0, p), invalid_argument);
}

TEST(test_primeFactors, except_minus) {
   vector<int> p = primes(13);
   ASSERT_THROW(primeFactors(-1, p), invalid_argument);
}

TEST(test_pow_mod, simple) {
   ASSERT_EQ(512, pow_mod(2, 9, 10000000000));
}

TEST(test_pow_mod, zero) {
   ASSERT_EQ(1, pow_mod(3, 0, 10000000000));
   ASSERT_EQ(0, pow_mod(0, 1, 10000000000));
   // 0の0乗は1とする
   ASSERT_EQ(1, pow_mod(0, 0, 10000000000));
}

TEST(test_pow_mod, big) {
   ASSERT_EQ(120678297, pow_mod(123456789, 6574837563712, 234567894));
}

TEST(test_pow_mod, except_minus) {
   // 負数は扱わない
   ASSERT_THROW(pow_mod(2, -3, 10000000000), invalid_argument);
   ASSERT_THROW(pow_mod(-3, 2, 10000000000), invalid_argument);
   ASSERT_THROW(pow_mod(-5, -5, 10000000000), invalid_argument);
}