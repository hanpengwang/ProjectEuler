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

def nthPrime(n):
  count = 1
  mover = 3
  while count < n:
    if len(primeFactor(mover)) == 1:
      count +=1
    mover += 2
    
  
  return (2 if n == 1 else (mover -2) )




print(nthPrime(10001))
