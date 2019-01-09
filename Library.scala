object MathAlgo {
  def makePrimes(size: Int) :  = {
    val primes = List(Int)
  }
}

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
    var primes: Array[Int]
    var flag = Array.fill[Boolean](size)(true)

    for (i <- 2 until size) {
      if (flag(i)) {
        primes :+ i
        for (j <- i until size by i) {

        }
      }
    }
  }
}