import tkinter as tk
import random

# タイピングゲームの基本フレーム
class TypingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("タイピングゲーム")

        self.words = ["apple", "banana", "cherry", "grape", "lemon", "mango", "orange", "peach", "pear", "plum"]
        self.current_word = ""
        self.score = 0
        self.time_left = 30

        # 背景設定
        self.root.geometry("600x500")
        self.root.config(bg="#f0f8ff")

        # ゲームのラベル
        self.word_label = tk.Label(root, text="Press Start!", font=("Arial", 32), bg="#f0f8ff", fg="#333333")
        self.word_label.pack(pady=30)

        self.entry = tk.Entry(root, font=("Arial", 24), justify="center", width=20)
        self.entry.pack(pady=20)
        self.entry.bind("<Return>", self.check_word)

        self.score_label = tk.Label(root, text=f"スコア: {self.score}", font=("Arial", 16), bg="#f0f8ff", fg="#333333")
        self.score_label.pack()

        self.timer_label = tk.Label(root, text=f"残り時間: {self.time_left} 秒", font=("Arial", 16), bg="#f0f8ff", fg="#333333")
        self.timer_label.pack()

        self.start_button = tk.Button(root, text="スタート", font=("Arial", 16), command=self.start_game, bg="#87cefa", fg="#ffffff", activebackground="#4682b4", activeforeground="#ffffff")
        self.start_button.pack(pady=20)

    def start_game(self):
        self.score = 0
        self.time_left = 30
        self.update_score()
        self.update_timer()
        self.next_word()
        self.countdown()

    def next_word(self):
        self.current_word = random.choice(self.words)
        self.word_label.config(text=self.current_word)
        self.entry.delete(0, tk.END)

    def check_word(self, event):
        typed_word = self.entry.get()
        if typed_word == self.current_word:
            self.score += 1
            self.update_score()
        self.next_word()

    def update_score(self):
        self.score_label.config(text=f"スコア: {self.score}")

    def update_timer(self):
        self.timer_label.config(text=f"残り時間: {self.time_left} 秒")

    def countdown(self):
        if self.time_left > 0:
            self.time_left -= 1
            self.update_timer()
            self.root.after(1000, self.countdown)
        else:
            self.word_label.config(text="ゲーム終了！")
            self.entry.delete(0, tk.END)
            self.entry.config(state="disabled")

# アプリケーションを実行
if __name__ == "__main__":
    root = tk.Tk()
    game = TypingGame(root)
    root.mainloop()
