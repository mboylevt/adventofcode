f = open('../data/p2.data', 'r')
data = f.readlines()
f.close()

twice = 0
thrice = 0

for word in data:
    letters = {}
    found_two = False
    found_three = False
    for letter in word:
        if letter not in letters.keys():
            apperance_count = word.count(letter)
            if apperance_count == 2 and found_two is False:
                twice += 1
                found_two = True
            elif apperance_count == 3 and found_three is False:
                thrice += 1
                found_three = True
            letters[letter] = apperance_count
    print("Found Two: {}\nFound Three: {}".format(found_two, found_three))
    print("Twice: {}\nThrice: {}".format(twice, thrice))
    print(letters)


print("Twice: {}\n, Thrice:{}".format(twice, thrice))
print("Checksum: {}".format(twice * thrice))