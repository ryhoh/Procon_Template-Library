import scala.collection.mutable
import scala.util.control.Breaks

object MathAlgo {
  val MOD = 1000000007

  def pow_mod(a: Long, n: Long): Long = {
    if (n == 0) return 1

    val half = pow_mod(a, n / 2)

    if (n % 2 == 0) half * half % MOD
    else (half * half) % MOD * a % MOD
  }

  def gcd(a: Long, b: Long): Long = {
    if (b == 0) a
    else gcd(b, a%b)
  }

  def lcm(a: Long, b: Long): Long = {
    a / gcd(a, b) * b
  }

  def Primes(size: Int): Array[Int] = {
    var primes = new Array[Int](0)
    val flag = Array.fill[Boolean](size)(true)
    val limit = Math.sqrt(size).toInt

    (2 until limit).foreach(i => {
      if (flag(i)) {
        primes = primes :+ i
        (i until size by i).foreach(j => {
          flag(j) = false
        })
      }
    })

    (limit until size).foreach(i => {
      if (flag(i)) {
        primes = primes :+ i
      }
    })

    primes
  }

//  def PrimeFactor(N: Int, primes: Array[Int]): mutable.HashMap[Int, Int] = {
//    val primeFactor = mutable.HashMap[Int, Int]((1, 1))
//    var Num = N
//
//    val b1 = new Breaks
//    b1.breakable {
//      while (true) {
//        val b2 = new Breaks
//        b2.breakable {
//          for (prime <- primes) {
//            if (Num % prime == 0) {
//              if (primeFactor.contains(prime))
//                primeFactor(prime) += 1
//              else
//                primeFactor(prime) = 1
//              Num /= prime
//              b2.break
//            }
//            if (prime > N) {
//              b1.break
//            }
//          }
//        }
//      }
//    }
//
//    primeFactor
//  }

  def pow_mod(x: Int, n: Long): Long = {
    if (n == 0) return 1

    val half = pow_mod(x, n / 2)
    if (b % 2 == 0) half * half * MOD
    else (half * half) % MOD * x % MOD
  }
}

object Search {
  def lower_bound(array: Array[Int])(target: Int)(from: Int)(to: Int): Int = {
    if (to - from == 1) return -1

    val mid_idx: Int = (to - from) / 2
    val mid = array(mid_idx)
    val f = lower_bound(array)(target)

    if (mid > target) f(from)(mid_idx)

    else if (mid == target) {
      val res = f(from)(mid_idx)
      if (res != -1) res
      else mid_idx

    } else {
      f(mid_idx+1)(to)
    }
  }

  //  def upper_bound(array: Array[Int])(target: Int): Int = {
  //
  //  }
}

class UnionFind(n: Int) {
  private val pare = Array.ofDim[Int](n)
  private val rk = Array.ofDim[Int](n)

  (0 until n).foreach(i => {
    pare(i) = i
    rk(i) = i
  })

  def find(x: Int): Int = {
    if (x == pare(x)) x
    else {
      pare(x) = find(pare(x))
      pare(x)
    }
  }

  def unite(x: Int, y: Int): Unit = {
    val xx: Int = find(x)
    val yy: Int = find(y)
    if (xx != yy) {
      if (rk(xx) < rk(yy)) pare(xx) = yy
      else pare(yy) = xx
      if (rk(xx) == rk(yy)) rk(xx) += 1
    }
  }

  def same(x: Int, y: Int): Boolean = {
    find(x) == find(y)
  }
}

class Graph(n: Int, reversible: Boolean) {
  private val cost = Array.fill[Int](n, n)(Int.MaxValue)
  private val connected = Array.fill[Boolean](n, n)(false)
  private val N = n
  private val Reversible = reversible

  def connect(from: Int, to: Int, cost: Int): Unit = {
    connected(from)(to) = true
    this.cost(from)(to) = cost

    if (Reversible) {
      connected(to)(from) = true
      this.cost(to)(from) = cost
    }
  }

  def warshall_floyd(): Unit = {
    (0 until N).foreach(k => {
      (0 until N).foreach(i => {
        (0 until N).foreach(j => {
          if (connected(i)(k) && connected(k)(j))
            cost(i)(j) = math.min(cost(i)(j), cost(i)(k) + cost(k)(j))
        })
      })
    })
  }

  def getCost(from: Int)(to: Int): Int = {
    cost(from)(to)
  }
}

class TestMathAlgo {
  def testGcd = {
    val testSets = {
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
    testSets.foreach((k, v) => {
      print(k, v)
    })
  }
}

object Main {
  def main(args: Array[String]): Unit = {
    TestMathAlgo().testSets
  }
}