from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Настройки подключения к базе данных
auth = {
    'user': 'user1',
    'password': '1234'  # Замените на ваш пароль
}

engine = create_engine(
    f'postgresql+psycopg2://{auth["user"]}:{auth["password"]}@127.0.0.1/sports_clubs',
    echo=True,
)

Base = declarative_base()

# Определение модели Clubs
class Club(Base):
    __tablename__ = 'clubs'

    id_club = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    home_arena = Column(String)  # Новое поле для домашней арены
    email = Column(String)     # Новое поле для почты
    club_value = Column(String) 

# Создание таблиц (если они еще не существуют)
Base.metadata.create_all(engine)

def add_club(name,home_arena,email,club_value):
    Session = sessionmaker(bind=engine)
    with Session() as session:
        new_club = Club(name=name, home_arena=home_arena, email=email, club_value=club_value)  # Обновите модель Club
        session.add(new_club)
        session.commit()

