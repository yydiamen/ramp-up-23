def factorial_integer(number: int):
    number = abs(number)
    fact = 1
    for i in range(1, number+1):
        fact = fact*i
    print("loop method factorial:")
    print(fact)
    rec = recursive_factorial(number, 1)
    print("recursive method")
    print(rec)

def recursive_factorial(num: int, sum: int) -> int:
     if num == 1:
         return sum;
     else:
         sum = sum*num
         return recursive_factorial(num-1, sum)