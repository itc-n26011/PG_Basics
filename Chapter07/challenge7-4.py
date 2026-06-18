import random

while True:
    inp = input("1-5までの数字を入力してください: ").lower()
    if inp == "q":
        break
    if int(inp) == random.randint(1, 5):
        print("正解！！！")
        break
    else:
        print("不正解")
