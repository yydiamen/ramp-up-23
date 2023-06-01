def statistic_info(numbers: list[int]):
    sum = 0
    for i in numbers:
        sum = sum + i
    print("the sum is")
    print(sum)
    min = numbers[0]
    for i in numbers:
        if i < min:
            min = i
    print("the smallest number is")
    print(min)
    max = numbers[0]
    for i in numbers:
        if i > max:
            max = i
    print("the largest number is")
    print(max)
    print("the avarage number is")
    print(sum / len(numbers))
