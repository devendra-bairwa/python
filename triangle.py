n=int(input("enter number "))
#
#for i in range(n):
 #   for j in range(n-i-1):
  #      print(' ', end='')
   # for k in range(i+1):
    #    print('* ', end='')
    #5print()
#
for i in range(n, 0, -1):
    print(' ' * (n - i) + '*' * (2 * i - 1))
