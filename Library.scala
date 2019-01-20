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
}