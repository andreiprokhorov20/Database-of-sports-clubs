import tkinter as tk
import tkinter.messagebox as ms
from database import add_club  # Импортируем функцию добавления клуба

USER = "user1"
PASSWORD = "1234"

class LoginPage(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        login_lb = tk.Label(self, text="Ваш логин")
        password_lb = tk.Label(self, text="Ваш пароль")
        self.login_entry = tk.Entry(self)
        self.password_entry = tk.Entry(self, show='*')
        self.submit_button = tk.Button(self, text="Залогинься!", command=self.login_command)

        login_lb.pack()
        self.login_entry.pack()
        password_lb.pack()
        self.password_entry.pack()
        self.submit_button.pack()

    def login_command(self):
        if self.login_entry.get() == USER and self.password_entry.get() == PASSWORD:
            ms.showinfo(title="Успех", message="Вы успешно вошли!")
            self.forget()
            app = MainPage(self.master)
            app.pack()
        else:
            ms.showerror(title="Ошибка", message="Неверный логин или пароль!")

class MainPage(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)

        self.name_label = tk.Label(self, text="Название клуба:")
        self.name_entry = tk.Entry(self)

        self.home_arena_label = tk.Label(self, text="Домашняя арена:")
        self.home_arena_entry = tk.Entry(self)

        self.email_label = tk.Label(self, text="Почта:")
        self.email_entry = tk.Entry(self)

        self.club_value_label = tk.Label(self, text="Стоимость клуба:")
        self.club_value_entry = tk.Entry(self)

        # Кнопка для добавления клуба
        self.submit_button = tk.Button(self, text="Добавить клуб", command=self.add_club_command)

        self.name_label.pack()
        self.name_entry.pack()

        self.home_arena_label.pack()
        self.home_arena_entry.pack()

        self.email_label.pack()
        self.email_entry.pack()

        self.club_value_label.pack()
        self.club_value_entry.pack()

        self.submit_button.pack()

    def add_club_command(self):
        name = self.name_entry.get().strip()
        home_arena = self.home_arena_entry.get().strip()
        email = self.email_entry.get().strip()
        club_value = self.club_value_entry.get().strip()
        if name:
            try:
                add_club(name,home_arena,email,club_value)  # Вызов функции добавления клуба
                ms.showinfo(title="Успех", message=f"Клуб '{name}' успешно добавлен!")
                self.name_entry.delete(0, tk.END)  # Очистка поля ввода
            except Exception as e:
                ms.showerror(title="Ошибка", message=f"Не удалось добавить клуб: {e}")
        else:
            ms.showerror(title="Ошибка", message="Введите название клуба!")

class MyApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("400x200")
        self.window.title("Sports Clubs Manager")

        self.login_page = LoginPage(self.window)
        self.login_page.pack()

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    app = MyApp()
    app.run()

