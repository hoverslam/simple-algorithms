# ----------
# The Fibonacci numbers, form a sequence in which each number is the sum of the two preceding ones.
# https://en.wikipedia.org/wiki/Fibonacci_number
# ----------

def fibonacci_itertative(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        n0 = 0
        n1 = 1
        i = 3        
        while i <= n+1:
            n3 = n0 + n1
            n0 = n1
            n1 = n3
            i += 1
            
        return n3         

def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci_recursive(n-2) + fibonacci_recursive(n-1)
    
def fibonacci_sequence(n):
    fib = []
    for i in range(n+1):
        fib.append(fibonacci_recursive(i))
        
    return fib
    
    
if __name__ == "__main__":
    print(fibonacci_sequence(10))