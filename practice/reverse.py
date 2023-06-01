def string_reverse(word: str):
    charList = [*word]
    newStr = ""
    for i in charList:
        newStr = i+newStr
    print("reversed string:")
    print(newStr)
    vowelcount = 0
    for x in charList:
        if (x == 'a' or x == 'e' or x == 'i' or
                x == 'o' or x == 'u' or x == 'A' or
                x == 'E' or x == 'I' or x == 'O' or
                x == 'U'):
            vowelcount = vowelcount+1
    print("vowel count:")
    print(vowelcount)