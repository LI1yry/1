spisok = [3, 10.5, True, "Привет", 3]
print(spisok)

spisok.append("Anton Chigyr")
print(spisok)

test = spisok.pop()
print(spisok)
print(test)

spisok.remove(3)
print(spisok)

spisok2 = [5,2,4,6,7,9,1,3]
spisok2.sort()
print(spisok2)
spisok.reverse()
print(spisok)


res = spisok[1]
print(res)

spisok.insert(2, "roblox")
print(spisok)

slices = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(slices[5:8])

phrase = list("Я не умею программировать")
print(phrase)
phrase.remove("н")
print(phrase)
...
print("".join(phrase))