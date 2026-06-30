import random

# じゃんけんの手を定義する
hands = ["グー", "チョキ", "パー"]

# プレイヤーに説明を表示する
print("じゃんけんゲーム")
print("グー（石）")
print("チョキ（はさみ）")
print("パー（紙）")

# プレイヤーの入力を受け取る
player = input("あなたの手を入力してください: ")

# 入力が正しいか確認する
if player not in hands:
    print("正しい手を入力してください。")
    exit()

# コンピューターの手をランダムに選ぶ
computer = random.choice(hands)

# 結果を表示する
print("あなた:", player)
print("コンピューター:", computer)

# 勝敗を判定する
if player == computer:
    print("あいこです！")
elif (
    (player == "グー" and computer == "チョキ") or
    (player == "チョキ" and computer == "パー") or
    (player == "パー" and computer == "グー")
     ):
          print("あなたの勝ちです！")
else:
    print("あなたの負けです。")
