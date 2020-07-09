myList = ["apple", "orange", "banana", "mango"]

# e = enumerate(myList)

# print(list(e))

# for index, ele in e:
#     print(index, ele)

e = enumerate(myList, 100)

# print(list(e))
for count, ele in e:
    print(count, ele)
