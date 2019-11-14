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
    

def smallestMultiple(l):
  collect = {}
  from collections import Counter
  from functools import reduce
  for num in l:
    primes = Counter(primeFactor(num))
    for prime in primes.keys():
      if prime not in collect:
        collect[prime] = primes[prime]
      else:
        if primes[prime] > collect[prime]:
          collect[prime] = primes[prime]
  
  return reduce(lambda a,b :a *b ,[prime ** collect[prime] for prime in collect.keys()])


print(smallestMultiple([i for i in range(11)[1:]]))
