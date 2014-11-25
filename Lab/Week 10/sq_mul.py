def square_multiply(m,k,n):
  res = 1
  for i in bin(k)[2:]:
    res = res * res %n
    if i == '1':
      res = res * m % n
  return res