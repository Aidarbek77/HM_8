from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql://user:password@host/database')
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Country(Base):
    __tablename__ = 'countries'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)

class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String, nullable=False)
    area = Column(Float, default=0.0)
    country_id = Column(Integer, ForeignKey('countries.id'))

class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    city_id = Column(Integer, ForeignKey('cities.id'))

Base.metadata.create_all(engine)

conn.execute(Country.__table__.insert(), [
    {'title': 'Россия'},
    {'title': 'США'},
    {'title': 'Китай'}
])

conn.execute(City.__table__.insert(), [
    {'title': 'Москва', 'country_id': 1, 'area': 2511},
    {'title': 'Нью-Йорк', 'country_id': 2, 'area': 783.8},
    {'title': 'Шанхай', 'country_id': 3, 'area': 6340.5},
    {'title': 'Екатеринбург', 'country_id': 4, 'area': 767.2},
    {'title':'Пхенян', 'country_id': 5, 'area': 767.2},
    {'title':'НОвосибирк', 'country_id': 6, 'area': 767.2},
])

conn.execute(Student.__table__.insert(), [
    {'first_name': 'Иван', 'last_name': 'Иванов', 'city_id': 1},
    {'first_name': 'Петр', 'last_name': 'Петров', 'city_id': 2},
    {'first_name': 'Bob', 'last_name': 'Johnson', 'city_id': 3},
    {'first_name': 'Charlie', 'last_name': 'Brown', 'city_id': 4},
    {'first_name': 'David', 'last_name': 'Lee', 'city_id': 5},
    {'first_name': 'Emily', 'last_name': 'Davis', 'city_id': 6},
    {'first_name': 'frt', 'last_name': 'Петров', 'city_id': 7},
    {'first_name': 'Grace', 'last_name': 'Петров', 'city_id': 8},
    {'first_name': 'тр', 'last_name': 'Петров', 'city_id': 9},
    {'first_name': 'Пff', 'last_name': 'Петров', 'city_id': 10},
    {'first_name': 'Frank', 'last_name': 'Петров', 'city_id': 11,
    {'first_name': 'Пер', 'last_name': 'Петров', 'city_id': 12},
    {'first_name': 'Henry', 'last_name': 'Петров', 'city_id': 13},
    {'first_name': 'Jack', 'last_name': 'Петров', 'city_id': 14},
    {'first_name': 'Isabella', 'last_name': 'Петров', 'city_id': 15},

])

conn.commit()

def print_cities():
    cities = session.query(City).all()
    for city in cities:
        print(city.title)

def print_students_by_city(city_id):
    students = session.query(Student, City, Country).join(City).join(Country).filter(City.id == city_id).all()
    for student, city, country in students:
        print(f"Имя: {student.first_name}, Фамилия: {student.last_name}, Страна: {country.title}, Город: {city.title}, Площадь: {city.area}")

def main():
    print("Список городов из базы данных:")
    print_cities()

    while True:
        print("Вы можете отобразить список учеников по выбранному id города из перечня городов ниже, для выхода из программы введите 0:")

        city_id = int(input("Введите ID города: "))

        if city_id == 0:
            break

        print_students_by_city(city_id)

if __name__ == "__main__":
    main()