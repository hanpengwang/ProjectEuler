def squareDiff(l):
  from functools import reduce
  sumSquare = sum([num**2 for num in l])
  squareSum = ((l[0] + l[-1]) * len(l) / 2 )**2
  return squareSum - sumSquare

print(squareDiff([i for i in range(101)][1:]))
