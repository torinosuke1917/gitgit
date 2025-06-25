import random

def number_guessing_game():
    """
    数字当てゲームを実行する関数
    """
    # 1. ランダムに正解の数字を決定 (100から999の3桁の数字)
    answer = random.randint(100, 999)
    
    # 5. 回答回数の制限
    max_attempts = 10
    attempts = 0
    
    # 履歴管理用のリスト
    guess_history = []
    
    print("=== 3桁の数字当てゲーム ===")
    print(f"{max_attempts}回以内に正解の数字を当ててください。")
    
    while attempts < max_attempts:
        # 2. キーボード入力で回答
        try:
            guess_str = input(f"\n[{attempts + 1}回目] 3桁の数字を入力してください: ")
            guess = int(guess_str)
            
            # 入力値が3桁かどうかのチェック
            if not 100 <= guess <= 999:
                print("エラー: 3桁の数字を入力してください。")
                continue

        except ValueError:
            print("エラー: 数字を入力してください。")
            continue
            
        # 回答履歴を追加
        guess_history.append(guess)
        attempts += 1
        
        # 3. 正解・不正解のフィードバック
        if guess == answer:
            print(f"おめでとうございます！正解です！")
            print(f"正解の数字は {answer} でした。")
            print(f"{attempts}回で正解しました。")
            break
        else:
            print("残念、不正解です。")
            # 4. 不正解時にヒントを出力
            if guess < answer:
                print("ヒント: 正解の数字はもっと大きいです。")
            else:
                print("ヒント: 正解の数字はもっと小さいです。")
            
            # 残りの試行回数を表示
            print(f"残りの挑戦回数: {max_attempts - attempts}回")

        # 現在の回答履歴を表示
        print(f"あなたの回答履歴: {guess_history}")

    # ループが終了（回数制限に達した場合）
    else:
        print("\nゲームオーバーです。")
        print(f"正解の数字は {answer} でした。")

# ゲームを開始
if __name__ == "__main__":
    number_guessing_game()