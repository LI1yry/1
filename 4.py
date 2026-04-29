year = int(input("Какого года? "))
pay = int(input("Сколько стоит игра? "))
if year >= 2018 or pay <= 1500:
    print("Нам подходит игра")
elif 2018 > year > 2010:
    print("На счет этой игры надо подумать")
else:
    print("Ищи другую")