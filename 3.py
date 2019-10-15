def primeFactor(n):
  mover = 2
  primes = []
  while mover<=n:
    if n%mover==0:
      primes.append(mover)
      n = n/mover
      mover = 2
    else:
      mover+=1
  return(primes)
    


print(primeFactor(600851475143)[-1])
