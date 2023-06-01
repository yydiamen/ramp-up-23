def odd_even(int):
    if int > 2:
        odd_even(int/2)
    elif int == 2:
        print("even")
    else:
        print("odd")