def fibonacci(n):
    if n == 0:
         return 0
    elif n == 1:
         return 1
    else:
         return fibonacci(n-1)+fibonacci(n-2)
         
         
n = 5 
# It prints first 5 fibonacci numbers
for i in range(n):
    print(fibonacci(i))
    print("\n")
