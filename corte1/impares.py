#Este codigo vale 1 decima

times = input("Enter a number of times: ")
times = float(times)
times = int(times)
print(type(times))
print(times)

for i in range (1,times):
  residual = i%2
  if residual == 0:
         print(f'{i} is even')
  else:
         print(f'{i} is odd')
         print(str(i) + ' is odd')




