def palindromeProduct(num_digits):
  num1 = 0
  num2 = 0
  m = 0
  for i1 in range(10**num_digits)[(10**(num_digits-1)):][::-1]:
    for i2 in range(i1+1)[(10**(num_digits-1)):][::-1]:
      prod = i1 * i2
      l = [d for d in str(prod)]
      if l == l[::-1]:
        if prod > m:
          m = prod
          num1 = i1
          num2 = i2

  return(m, num1, num2)
    
     

      


print(palindromeProduct(3))

  
