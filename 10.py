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

def sumPrimes(maxN):
  add = 2 
  mover = 3
  while mover < maxN:
    if len(primeFactor(mover)) == 1:
      add += mover
    mover += 2
    
  
  return add


print(sumPrimes(2*10**6))
