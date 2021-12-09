def count_str():
    try:
        string = input("Enter your string:")
        word1 = int(input("Enter your word:"))
        for ele in string.split():
            if ele == word1:
                pass
        print(string.count(word1))
    except Exception as e:
        print('the error is ',e)

count_str()
