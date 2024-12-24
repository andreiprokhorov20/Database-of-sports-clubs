import tkinter as tk
from tkinter import messagebox, ttk
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

# Настройки подключения к базе данных
auth = {
    'user': 'postgres',
    'password': '2012_Egor'
}

engine = create_engine(
    f'postgresql+psycopg2://{auth["user"]}:{auth["password"]}@localhost/sports_clubs',
    echo=True,
)

SessionLocal = sessionmaker(bind=engine)

# Функции для работы с базой данных
def add_club(name, home_arena, email, club_value):
    with SessionLocal() as session:
        try:
            session.execute(text("SELECT add_club(:name, :home_arena, :email, :club_value);"),
                           {'name': name, 'home_arena': home_arena, 'email': email, 'club_value': club_value})
            session.commit()
            messagebox.showinfo("Добавить клуб", "Клуб добавлен успешно.")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

def add_player(full_name, birth_date, position, player_value, id_coach):
    with SessionLocal() as session:
        try:
            session.execute(text("SELECT add_player(:full_name, :birth_date, :position, :player_value, :id_coach);"),
                           {'full_name': full_name, 'birth_date': birth_date, 'position': position,
                            'player_value': player_value, 'id_coach': id_coach})
            session.commit()
            messagebox.showinfo("Добавить игрока", "Игрок добавлен успешно.")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

def add_coach(full_name, experience, id_club):
    with SessionLocal() as session:
        try:
            session.execute(text("SELECT add_coach(:full_name, :experience, :id_club);"),
                           {'full_name': full_name, 'experience': experience, 'id_club': id_club})
            session.commit()
            messagebox.showinfo("Добавить тренера", "Тренер добавлен успешно.")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

def add_match(match_date, address, id_club):
    with SessionLocal() as session:
        try:
            session.execute(text("SELECT add_match(:match_date, :address, :id_club);"),
                           {'match_date': match_date, 'address': address, 'id_club': id_club})
            session.commit()
            messagebox.showinfo("Добавить матч", "Матч добавлен успешно.")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

def add_training(training_date, training_time, place, id_coach):
    with SessionLocal() as session:
        try:
            session.execute(text("SELECT add_training(:training_date, :training_time, :place, :id_coach);"),
                           {'training_date': training_date, 'training_time': training_time,
                            'place': place, 'id_coach': id_coach})
            session.commit()
            messagebox.showinfo("Добавить тренировку", "Тренировка добавлена успешно.")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

def add_contract(signing_date, expiration_date, id_player):
    with SessionLocal() as session:
        try:
            session.execute(text("SELECT add_contract(:signing_date, :expiration_date, :id_player);"),
                           {'signing_date': signing_date,
                            'expiration_date': expiration_date,
                            'id_player': id_player})
            session.commit()
            messagebox.showinfo("Добавить контракт", "Контракт добавлен успешно.")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))
            
def delete_specific_entry(table_name, entry_id):
    with SessionLocal() as session:
        try:
            session.execute(text("SELECT delete_specific_entry(:table_name,:entry_id);"),
                           {'table_name': table_name,
                            'entry_id': entry_id})
            session.commit()
            messagebox.showinfo("Удалить запись", "Запись удалена успешно.")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

def update_entry(table_name, entry_id, field_name, new_value):
    with SessionLocal() as session:
        try:
            session.execute(text("SELECT update_entry(:table_name,:entry_id,:field_name,:new_value);"),
                           {'table_name': table_name.strip(), 
                            'entry_id': entry_id,
                            'field_name': field_name.strip(),
                            'new_value': new_value.strip()})
            session.commit()
            messagebox.showinfo("Обновить запись", "Запись обновлена успешно.")
        except Exception as e:
            messagebox.showerror("Ошибка", str(e))

# GUI с Tkinter
class SportsClubsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sports Clubs Database")

        # Frame для ввода данных клуба
        frame = ttk.Frame(self.root)
        frame.pack(padx=10, pady=10)

        # Добавление клуба
        ttk.Label(frame, text="Название клуба:").grid(row=0, column=0)
        self.club_name_entry = ttk.Entry(frame)
        self.club_name_entry.grid(row=0, column=1)

        ttk.Label(frame, text="Домашняя арена:").grid(row=1, column=0)
        self.home_arena_entry = ttk.Entry(frame)
        self.home_arena_entry.grid(row=1,column=1)

        ttk.Label(frame,text="Почта:").grid(row=2,column=0)
        self.email_entry = ttk.Entry(frame)
        self.email_entry.grid(row=2,column=1)

        ttk.Label(frame,text="Стоимость клуба:").grid(row=3,column=0)
        self.club_value_entry = ttk.Entry(frame)
        self.club_value_entry.grid(row=3,column=1)

        ttk.Button(frame,text="Добавить клуб",command=self.add_club).grid(row=4,columnspan=2)
        
        # Добавление матча
        ttk.Label(frame,text="Дата матча (YYYY-MM-DD):").grid(row=5,column=0)
        self.match_date_entry = ttk.Entry(frame) 
        self.match_date_entry.grid(row=5,column=1)

        ttk.Label(frame,text="Адрес матча:").grid(row=6,column=0)
        self.match_address_entry = ttk.Entry(frame) 
        self.match_address_entry.grid(row=6,column=1)

        ttk.Label(frame,text="ID Клуба:").grid(row=7,column=0)
        self.match_id_club_entry = ttk.Entry(frame) 
        self.match_id_club_entry.grid(row=7,column=1)

        ttk.Button(frame,text="Добавить матч",command=self.add_match).grid(row=8,columnspan=2)
        
        
        # Добавление тренера
        ttk.Label(frame,text="ФИО тренера:").grid(row=9,column=0)
        self.coach_full_name_entry = ttk.Entry(frame)
        self.coach_full_name_entry.grid(row=9,column=1)

        ttk.Label(frame,text="Стаж (в годах):").grid(row=10,column=0)
        self.coach_experience_entry = ttk.Entry(frame)
        self.coach_experience_entry.grid(row=10,column=1)

        ttk.Label(frame,text="ID Клуба:").grid(row=11,column=0)
        self.coach_id_club_entry = ttk.Entry(frame)
        self.coach_id_club_entry.grid(row=11,column=1)

        ttk.Button(frame,text="Добавить тренера",command=self.add_coach).grid(row=12,columnspan=2)
        
        # Добавление игрока
        ttk.Label(frame,text="ФИО игрока:").grid(row=13,column=0)
        self.player_full_name_entry = ttk.Entry(frame)
        self.player_full_name_entry.grid(row=13,column=1)

        ttk.Label(frame,text="Дата рождения:").grid(row=14,column=0)
        self.player_birth_date_entry = ttk.Entry(frame)  # формат YYYY-MM-DD
        self.player_birth_date_entry.grid(row=14,column=1)

        ttk.Label(frame,text="Позиция:").grid(row=15,column=0)
        self.player_position_entry = ttk.Entry(frame)
        self.player_position_entry.grid(row=15,column=1)

        ttk.Label(frame,text="Стоимость игрока:").grid(row=16,column=0)
        self.player_value_entry = ttk.Entry(frame)
        self.player_value_entry.grid(row=16,column=1)

        ttk.Label(frame,text="ID Тренера:").grid(row=17,column=0)
        self.player_coach_id_entry = ttk.Entry(frame)
        self.player_coach_id_entry.grid(row=17,column=1)

        ttk.Button(frame,text="Добавить игрока",command=self.add_player).grid(row=18,columnspan=2)
        
        # Добавление контракта
        ttk.Label(frame,text="Дата подписания (YYYY-MM-DD):").grid(row=19,column=0)
        self.contract_signing_date_entry = ttk.Entry(frame) 
        self.contract_signing_date_entry.grid(row=19,column=1)

        ttk.Label(frame,text="Дата окончания (YYYY-MM-DD):").grid(row=20,column=0)
        self.contract_expiration_date_entry = ttk.Entry(frame) 
        self.contract_expiration_date_entry.grid(row=20,column=1)

        ttk.Label(frame,text="ID Игрока:").grid(row=21,column=0)
        self.contract_id_player_entry = ttk.Entry(frame) 
        self.contract_id_player_entry.grid(row=21,column=1)

        ttk.Button(frame,text="Добавить контракт",command=self.add_contract).grid(row=22,columnspan=2)
        
        # Добавление тренировки
        ttk.Label(frame,text="Дата тренировки (YYYY-MM-DD):").grid(row=23,column=0)
        self.training_date_entry = ttk.Entry(frame) 
        self.training_date_entry.grid(row=23,column=1)

        ttk.Label(frame,text="Время тренировки (HH:MM):").grid(row=24,column=0)
        self.training_time_entry = ttk.Entry(frame) 
        self.training_time_entry.grid(row=24,column=1)

        ttk.Label(frame,text="Место проведения:").grid(row=25,column=0)
        self.training_place_entry = ttk.Entry(frame) 
        self.training_place_entry.grid(row=25,column=1)

        ttk.Label(frame,text="ID Тренера:").grid(row=26,column=0)
        self.training_id_coach_entry = ttk.Entry(frame) 
        self.training_id_coach_entry.grid(row=26,column=1)

        ttk.Button(frame,text="Добавить тренировку",command=self.add_training).grid(row=(27),columnspan=(2))
        
        # Удаление записи по ID
        ttk.Label(frame,text="Имя таблицы:").grid(row=(0),column=(2))
        self.delete_table_name_entry = ttk.Entry(frame) 
        self.delete_table_name_entry.grid(row=(0),column=(3))

        ttk.Label(frame,text="ID записи:").grid(row=(1),column=(2))
        self.delete_record_id_entry = ttk.Entry(frame) 
        self.delete_record_id_entry.grid(row=(1),column=(3))

        ttk.Button(frame,text="Удалить запись",command=self.delete_specific_record).grid(row=(3),column=(3))
        
        # Обновление записи по ID
        ttk.Label(frame,text="Имя таблицы (для обновления):").grid(row=(4),column=(2))
        self.update_table_name_entry = ttk.Entry(frame) 
        self.update_table_name_entry.grid(row=(4),column=(3))

        ttk.Label(frame,text="ID записи (для обновления):").grid(row=(5),column=(2))
        self.update_record_id_entry = ttk.Entry(frame) 
        self.update_record_id_entry.grid(row=(5),column=(3))

        ttk.Label(frame,text="Имя поля (для обновления):").grid(row=(6),column=(2))
        self.update_field_name_entry = ttk.Entry(frame) 
        self.update_field_name_entry.grid(row=(6),column=(3))

        ttk.Label(frame,text="Новое значение (для обновления):").grid(row=(7),column=(2))
        self.update_new_value_entry = ttk.Entry(frame) 
        self.update_new_value_entry.grid(row=(7),column=(3))

        ttk.Button(frame,text="Обновить запись",command=self.update_record).grid(row=(8),column=(3))

    def add_club(self):
        name = self.club_name_entry.get()
        home_arena = self.home_arena_entry.get()
        email = self.email_entry.get()
        
        try:
            club_value = float(self.club_value_entry.get())
            add_club(name.strip(), home_arena.strip(), email.strip(), club_value)

            # Очистка полей после добавления
            self.club_name_entry.delete(0,'end')
            self.home_arena_entry.delete(0,'end')
            self.email_entry.delete(0,'end')
            self.club_value_entry.delete(0,'end')
            
        except ValueError:
            messagebox.showerror("Ошибка ввода", "Введите корректное значение стоимости клуба.")

    def add_player(self):
        full_name = self.player_full_name_entry.get()
        
        try:
            birth_date = self.player_birth_date_entry.get()  # Дата в формате YYYY-MM-DD
            position = self.player_position_entry.get()
            player_value = float(self.player_value_entry.get())
            id_coach = int(self.player_coach_id_entry.get())

            add_player(full_name.strip(), birth_date.strip(), position.strip(), player_value , id_coach)

            # Очистка полей после добавления
            self.player_full_name_entry.delete(0,'end')
            self.player_birth_date_entry.delete(0,'end')
            self.player_position_entry.delete(0,'end')
            self.player_value_entry.delete(0,'end')
            self.player_coach_id_entry.delete(0,'end')

            
        except ValueError:
            messagebox.showerror("Ошибка ввода", "Проверьте введенные данные.")

    def add_coach(self):
         full_name = self.coach_full_name_entry.get()
         
         try:
             experience = int(self.coach_experience_entry.get())
             id_club = int(self.coach_id_club_entry.get())

             add_coach(full_name.strip(), experience , id_club)

             # Очистка полей после добавления
             self.coach_full_name_entry.delete(0,'end')
             self.coach_experience_entry.delete(0,'end')
             self.coach_id_club_entry.delete(0,'end')

             
         except ValueError:
             messagebox.showerror("Ошибка ввода", "Проверьте введенные данные.")
             
    def add_match(self):
         match_date = self.match_date_entry.get()  # Дата в формате YYYY-MM-DD
         
         address = self.match_address_entry.get()
         
         try:
             id_club = int(self.match_id_club_entry.get())

             add_match(match_date.strip(), address.strip(), id_club)

             # Очистка полей после добавления
             self.match_date_entry.delete(0,'end')
             self.match_address_entry.delete(0,'end')
             self.match_id_club_entry.delete(0,'end')

             
         except ValueError:
             messagebox.showerror("Ошибка ввода", "Проверьте введенные данные.")
            
    def add_contract(self):
          signing_date = self.contract_signing_date_entry.get()  # Дата в формате YYYY-MM-DD

          expiration_date =  self.contract_expiration_date_entry.get()  # Дата в формате YYYY-MM-DD

          try:
              id_player = int(self.contract_id_player_entry.get())

              add_contract(signing_date.strip(), expiration_date.strip(), id_player)

              # Очистка полей после добавления
              self.contract_signing_date_entry.delete(0,'end')
              self.contract_expiration_date_entry.delete(0,'end')
              self.contract_id_player_entry.delete(0,'end')

          except ValueError:
              messagebox
              
    def add_training(self):
          training_date = 	self.training_date_entry.get()  # Дата в формате YYYY-MM-DD

          training_time = 	self.training_time_entry.get()  # Время в формате HH:MM

          place = 	self.training_place_entry.get()

          try:
              id_coach = int(self.training_id_coach_entry.get())

              add_training(training_date.strip(), training_time.strip(), place.strip(), id_coach)

              # Очистка полей после добавления
              training_place_entry.delete(0,'end')
              training_time_entry.delete(0,'end')
              training_id_coach_entry.delete(0,'end')

          except ValueError:
              messagebox.showerror("Ошибка ввода", "Проверьте введенные данные.")
    
    '''def delete_entry_command(self):
        table_name = self.table_name_entry.get().strip()
        entry_id = self.entry_id_entry.get().strip()

        if table_name and entry_id:
            try:
                with Session() as session:
                    # Вызов процедуры удаления записи по ID
                    session.execute(text("SELECT delete_specific_entry(:table_name, :entry_id);"),
                                     {'table_name': table_name,
                                      'entry_id': int(entry_id)})
                    session.commit()  # Сохраняем изменения в базе данных
                    ms.showinfo("Успех", f"Запись с ID {entry_id} успешно удалена из таблицы '{table_name}'!")
                    # Очистка полей ввода
                    self.table_name_entry.delete(0, tk.END)
                    self.entry_id_entry.delete(0, tk.END)
            except Exception as e:
                ms.showerror("Ошибка", f"Не удалось удалить запись: {e}")
        else:
            ms.showerror("Ошибка", "Пожалуйста, заполните все поля!")'''
            
    def delete_specific_record(self):
          table_name = 	self.delete_table_name_entry.get().strip()
          
          try:
               entry_id = int(self.delete_record_id_entry.get().strip())

               delete_specific_entry(table_name.strip(), entry_id)

               # Очистка полей после удаления записи 
               delete_table_NAME_entry.delete(0,'end')
               delete_record_ID_entry.delete(0,'end')

          except ValueError:
               messagebox.showerror("Ошибка ввода", "Проверьте введенные данные.")
               
    def update_record(self):
          table_name = 	self.update_table_name_entry.get().strip()
          
          try:
               entry_id = int(self.update_record_id_entry.get().strip())
               field_name = 	self.update_field_name_entry.get().strip()
               new_value = 	self.update_new_value_entry.get().strip()

               update_entry(table_name.strip(), entry_id , field_name , new_value )

               # Очистка полей после обновления записи 
               update_table_NAME.entry.delete(0,'end')
               update_record_ID.entry.delete(0,'end')
               update_field_NAME.entry.delete(0,'end')
               update_new_VALUE.entry.delete(0,'end')

          except ValueError:
               messagebox.showerror("Ошибка ввода", "Проверьте введенные данные.")
    


if __name__ == "__main__":
    root = tk.Tk()
    app = SportsClubsApp(root)
    root.mainloop()

