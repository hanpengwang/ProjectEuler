def primeFactor(n):
  mover = 2
  primes = []
  while mover<=n**0.5:
    if n%mover==0:
      primes.append(mover)
      n = n/mover
      mover = 2
    else:
      mover+=1
  return(primes)

def sumPrimes(maxN):
  add = 2 
  mover = 3
  while mover < maxN:
    if len(primeFactor(mover)) == 0:
      add += mover

    mover += 2
    
    
  return add


print(sumPrimes(2*10**6))
