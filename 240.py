def TopDice(sides, rep, num, total):
  import itertools as it
  dice = [i for i in range(sides+1)[1:]]
  c = it.product(dice, repeat = rep)
  count = 0
  for i in c:
    i = sorted(i, reverse = True)
    if sum(i[0:num]) == total:
      count += 1
  
  print(count)
    

TopDice(12, 20, 10, 70)
