#subject to:
# a^2 + b^2 = c^2
# a + b + c = 1000
# a < b <c

collect = []
for a in range(303)[1:]:
  BplusC = 1000-a;
  if BplusC % 2 == 0:
    MaxB = int(BplusC/2 - 1)
  else: MaxB = BplusC//2
  for b in range(MaxB+1)[a:]:
    c = BplusC - b
    if a**2 + b**2 == c**2:
      collect.append([a,b,c])
    

print(collect)
