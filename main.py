def fib(index):
  if index <= 0:
    print(0)
    return
  elif index  == 1:
    print(1)
    return
  f0 = 0
  f1 = 1
  fib_actual = 0
  i = 2
  while i <= index:
    fib_actual = f1 + f0
    f0 = f1
    f1 = fib_actual
    i += 1
  print(fib_actual)


fib(4)