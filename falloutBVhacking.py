def FVin():
    print('what are the words? seperate with space')
    words = input().split(' ')
    return words

def pickword(words, pickedword, pickedfam):
    possiblewords = []
    for word in words:
        matching = [iletter
                    for j, iletter in enumerate(pickedword)
                    for i, oletter in enumerate(word)
                    if i == j and oletter == iletter]
        if len(matching) == pickedfam:
            possiblewords.append(word)
    return possiblewords

def mainthing():
    words = FVin()
    while len(words) > 1:
        print('pick a word:')
        pickedword = input()
        print('how many points did the word score? for 2/5, type 2')
        pickedfam = int(input())
        while pickedfam < 0 or pickedfam > 20:
            print('incorrect number')
            pickedfam = input()
        words = pickword(words, pickedword, pickedfam)
        print(" ".join(words))
    print("done")

mainthing()

